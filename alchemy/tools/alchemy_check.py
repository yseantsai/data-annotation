#!/usr/bin/env python3
"""alchemy_check.py: the coded checks for an Alchemy task folder.

    python3 tools/alchemy_check.py tasks/NN-slug                 every check on the folder
    python3 tools/alchemy_check.py tasks/NN-slug --only prompt   one family: prompt, inputs, zip,
                                                                 rubric, failure, runs
    python3 tools/alchemy_check.py tasks/NN-slug --zip           build inputs.zip the way the form
                                                                 wants it, then check it
    python3 tools/alchemy_check.py tasks/NN-slug --fingerprint   print the fingerprint to record
                                                                 in a run file
    python3 tools/alchemy_check.py tasks/NN-slug --full          full-task rubric band (20 or more)
    python3 tools/alchemy_check.py path/to/prompt.md             prompt checks on a loose file
    python3 tools/alchemy_check.py --prose path/to/file.md       mechanics and prose tells only
    python3 tools/alchemy_check.py --list | --next               where each task stands; next number
    python3 tools/alchemy_check.py --selftest

Run from the alchemy/ folder. Standard library only. Rule ids are defined in docs/rules.md.

The task folder (copied from templates/):

    tasks/NN-slug/
      task.md        the form fields, the design notes, the failure description, the log
      prompt.md      the final prompt alone, exactly as pasted into the form
      rubric.md      the criteria as a numbered list, one criterion per item
      inputs/        exactly the two input files, as uploaded
      inputs.zip     built by --zip; its only top-level folder is inputs/
      runs/          run-N.md per Attempting Agent run, with its fingerprint and grading lines,
                     and run-N/ holding the agent's output files

Severity:
  ERROR  a rule the training states flatly, or a defect that blocks submission. Exit status 1.
  WARN   a pattern that needs a read. Fix it, or note in task.md why it stands.
  NOTE   information only (a PDF that cannot be scanned, a generator stamp on a file).

Checks, by family and rule id:
  prompt   P1 sentences 2-6, P2 words 10-180, P3 deliverable file named, P4 role-play,
           P5 email formatting, P6 long background, P7 procedure, P8 answer hints,
           P9 invites questions, P10 web lookup, P12 project vocabulary, P13 file glosses or no input
           named, plus M and T
  inputs   I1 two files, I3 generic names, I5 project vocabulary and signposting, I8 PII,
           placeholders and real firm names, I10 total rows that do not tie, I11 fabrication
           tells (555 numbers, false weekdays, no-variance columns, float residue, em dashes,
           prose tells), I12 hidden content, I13 empty or thin files, T18 annotation voice,
           T19 self-describing text
  zip      I14 one top-level inputs/ folder, two files, no system files, matches inputs/
  rubric   R1 count, R2 atomic, R3 carries a value, R5 mandated method or location, R6 shape,
           R7 vague words and hedges, R8 predictions, R9 cosmetic, R12 unseen material, R13 duplicates,
           R14 grader instructions, M1
  failure  A2 non-severe failure words, A4 50 to 350 words, A5 criterion numbers, A6 file and figure
           evidence, plus M and T
  runs     A1 a current run fails a criterion, A3 stale runs by fingerprint

Run file conventions (runs/run-N.md):
  Fingerprint: <hex>             from --fingerprint at the time of the run
  Criterion 1: PASS              one line per criterion from the Grading Agent
  Criterion 2: FAIL
The escape hatch counts when task.md carries the line "**Escape hatch:** yes".

The grammar checks (M2, M3, M4) are heuristics tuned for precision over recall. A clean run is
the floor, not the proof. Read everything aloud.

Adding a check: write the pattern, give it a rule id that exists in docs/rules.md, add a fixture
to SELFTEST that must fire it, and keep the clean samples silent.
"""
import csv
import datetime
import hashlib
import io
import re
import statistics
import sys
import tempfile
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
TASKS = ROOT / "tasks"
EM_DASH = "\u2014"

STARTER_CRITERIA = 5
FULL_MIN_CRITERIA = 20


# ================================================================ text helpers

_ABBREV = re.compile(
    r"\b(?:Mr|Mrs|Ms|Dr|Inc|Co|Corp|Ltd|LLC|LP|No|vs|etc|approx|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept"
    r"|Oct|Nov|Dec|St|Ave|Rd|U\.S|e\.g|i\.e|a\.m|p\.m)\.", re.I)
_SENT_SPLIT = re.compile(r"(?<=[.!?])[\"')\]]*\s+(?=[A-Z0-9\"'(\[$])")


def strip_comments(text):
    return re.sub(r"<!--.*?-->", "", text, flags=re.S)


def sentence_list(text):
    """Sentences in prose: headings and table rows are skipped, abbreviations protected."""
    out = []
    for para in re.split(r"\n\s*\n", text):
        lines = [ln.strip() for ln in para.split("\n")]
        lines = [ln for ln in lines if ln and not ln.startswith("#") and not ln.startswith("|")]
        if not lines:
            continue
        joined = " ".join(lines)
        protected = _ABBREV.sub(lambda m: m.group(0).replace(".", "\x00"), joined)
        protected = re.sub(r"(\d)\.(\d)", "\\1\x00\\2", protected)
        for s in _SENT_SPLIT.split(protected):
            s = s.replace("\x00", ".").strip()
            if s:
                out.append(s)
    return out


def paragraphs(text):
    return [p for p in re.split(r"\n\s*\n", text) if p.strip()]


def words(text):
    return re.findall(r"[A-Za-z0-9$][A-Za-z0-9'%$.,\-]*", text)


def clip(s, n=80):
    s = " ".join(s.split())
    return s if len(s) <= n else s[:n] + "..."


class Report:
    def __init__(self):
        self.items = []

    def add(self, level, code, where, msg):
        self.items.append((level, code, where, msg))

    def error(self, code, where, msg):
        self.add("ERROR", code, where, msg)

    def warn(self, code, where, msg):
        self.add("WARN", code, where, msg)

    def note(self, code, where, msg):
        self.add("NOTE", code, where, msg)

    def codes(self):
        return {c for _, c, _, _ in self.items}

    def has_error(self):
        return any(lv == "ERROR" for lv, _, _, _ in self.items)


# ================================================================ M and T: shared prose checks

PRON = r"(?:I|we|they|he|she|it|you|there|nobody|neither|none|everyone|everybody|nothing)"
DET = r"(?:the|our|my|a|an|this|that|these|those|his|her|their|its|each|every|no|both|all|one)"
VERB = (r"(?:is|are|was|were|has|have|had|will|can|cannot|could|would|should|may|might|must|does|do|did"
        r"|goes|comes|came|went|needs|gets|got|takes|took|becomes|became|stays|remains|seems|means|says|said"
        r"|tells|told|knows|knew|wants|expects|thinks|thought|agrees|agreed|owes|arrives|expires|lapses"
        r"|starts|begins|began|fell|rises|rose|crosses|passes|reaches|reached|fails|puts|ran|keeps|kept|makes|made"
        r"|wrote|bought|sold|owns|carries|pays|paid|sends|sent|sees|saw|left|stood|asked|includes|excludes"
        r"|allows|requires|applies|renews|picked|crossed|failed|landed|moved|stayed|covered|needed|wanted|caught"
        r"|lost|found|sat|held|ended|started|closed|opened|dropped|changed|gave|grew|shrank|missed|hit|shows|showed"
        r"|looks|looked|signed|priced|raised|booked|posted|reported|projects|assumes"
        r"|meets|met|read|reads|calls|called|runs|works|worked|asks|buys|sells|charges|converts|accrues|matures"
        r"|pulls|pulled|built|writes|trades|lends|borrows|borrowed|owed|costs|steps|stepped)")
SUBJECT = rf"(?:{PRON}|{DET} \w+(?:'s)?(?: \w+){{0,2}}|[A-Z][\w-]+(?: [A-Z][\w-]+)?)"

BARE_JOIN_RE = re.compile(
    rf"(?<![,;:])\s(and|but|so|yet)\s+(?!that\b|then\b|long as\b|far as\b|much as\b|on\b)"
    rf"({SUBJECT})\s+(?:\w+\s+)?{VERB}\b")
COMMA_JOIN_RE = re.compile(rf",\s+(and|but|so|or|yet)\s+(?!that\b)({SUBJECT})\s+(?:\w+\s+)?{VERB}\b")
SEMI_JOIN_RE = re.compile(rf";\s+({SUBJECT})\s+(?:\w+\s+)?{VERB}\b")
SPLICE_RE = re.compile(rf",\s+({PRON})\s+(?:\w+\s+)?{VERB}\b")
ANY_VERB_RE = re.compile(rf"\b{VERB}\b")
SUBORD_RE = re.compile(
    r"\b(?:when|whenever|if|because|where|while|unless|until|after|before|although|though|since|whether"
    r"|once|provided|which|who|whose|as long as|so that)\b", re.I)
OPENER_WORDS = {
    "when", "whenever", "if", "because", "where", "while", "unless", "until", "after", "before", "although",
    "though", "since", "whether", "once", "provided", "given", "assuming", "considering", "based", "unlike",
    "like", "despite", "regardless", "according", "with", "without", "for", "to", "in", "on", "at", "by", "as",
    "from", "over", "under", "between", "during", "per", "absent", "barring", "yes", "no", "well", "also",
    "however", "otherwise", "meanwhile", "ideally", "frankly", "honestly", "first", "second", "third", "finally",
}
COMPOUND_SUBJ_RE = re.compile(r"(?:^|\s)(?:[A-Z][\w-]*|you|I|we|me|us|him|her|them)$")
CLAUSE_CAP = 6

TAUTOLOGY_RES = [
    re.compile(r"\b(\w+(?:\s+\w+){0,2})\s+(?:is|are)\s+(?:still\s+|just\s+)?\1\b", re.I),
    re.compile(r"\b(?:is|are)\s+the\s+whole\s+story\b", re.I),
    re.compile(r"\b(\w{5,})\b(?:[\w.\-]|[^\S\n]){0,20}?[^\S\n]+(?:is|are)\s+(?:still\s+|just\s+|always\s+)?\1\b", re.I),
]
TAUTOLOGY_OK_RE = re.compile(r"\bwhich is which\b|\bwhat is what\b|\bwho is who\b", re.I)
SLOGAN_RE = re.compile(
    r"\buse it or lose it\b|\bis where the (?:money|pain|trouble|problem)\s+(?:hurts?|is|lands?)\b"
    r"|\bat the end of the day\b|\bgame[- ]changer\b|\bmake or break\b|\bno-brainer\b|\bmov(?:e|ing) the needle\b"
    r"|\blow-hanging fruit\b|\bbleeding cash\b|\bwhere we are naked\b|\bnot quietly (?:dropped|buried|lost)\b"
    r"|\bskin in the game\b|\bthe elephant in the room\b|\bperfect storm\b|\bthe numbers don't lie\b"
    r"|\bmoney talks\b|\bcash is king\b", re.I)
NEG_PARALLEL_RE = re.compile(r"\bnot (?:just|only|simply|merely)\b[^.;?!\n]{1,80}\bbut(?: also| rather)?\b", re.I)
ITS_NOT_RE = re.compile(
    r"\b(?:it|this)(?:'s|\u2019s| is) not (?:just |only |simply |merely |about )?[^,.;\n]{1,50},\s*(?:it|this)"
    r"(?:'s|\u2019s| is)\b", re.I)
SERVES_AS_RE = re.compile(r"\b(?:serves?|stands?) as\b|\bboasts?\b|\bshowcases?\b", re.I)
SYCOPHANCY_RE = re.compile(
    r"\bgreat question\b|\bexcellent (?:point|question)\b|\bhappy to help\b|\bI(?:'d|\u2019d| would) be happy to\b"
    r"|\byou(?:'re|\u2019re| are) absolutely right\b|\babsolutely!|\bcertainly!|\bgreat choice\b"
    r"|\bthank you so much\b", re.I)
PRECOUNT_RE = re.compile(
    r"\bthere are (?:two|three|four|five|six|seven|\d+) (?:key |main |primary |major |critical )?"
    r"(?:considerations|factors|drivers|reasons|issues|points|takeaways|findings|steps|risks|questions)\b"
    r"|\b(?:two|three|four|five|six|seven|\d+) key (?:considerations|factors|drivers|reasons|issues|points"
    r"|takeaways|findings|risks)\b", re.I)
HEDGE_RE = re.compile(
    r"\bit is worth noting\b|\bit(?:'s|\u2019s| is) important to (?:note|consider|remember|understand)\b"
    r"|\bone could argue\b|\bthis may suggest\b|\bit should be noted\b|\bneedless to say\b", re.I)
CLINICAL_RE = re.compile(
    r"\butiliz\w+\b|\bleverag(?:e|ing) (?:the|our|your|existing|this|these|any)\b|\bcomprehensive\b|\brobust\b"
    r"|\bholistic\b|\bfacilitat\w+\b|\boptimi[sz]\w+\b|\bsynerg\w+\b|\bdelv(?:e|ing)\b|\bin order to\b"
    r"|\bstakeholder alignment\b|\bbest practices\b|\bactionable insights?\b|\bdeep dive\b|\bseamless\w*\b", re.I)
CLINICAL_CAP = 5
SEMI_MAXIM_RE = re.compile(r"\bis (?:a|an) \w+;[^.;\n]{0,80}\bis (?:a|an) \w+\b", re.I)
SHORT_OPENER_RE = re.compile(r"^([A-Z][\w']*(?: [\w']+){0,2})[.!]\s+[A-Z]")
GREETING_WORDS_RE = re.compile(
    r"^(?:hi|hello|hey|dear|thanks|thank you|morning|afternoon|ok|okay|update|fyi|subject|re|fw|from|to|cc"
    r"|date|sent)\b", re.I)
CONNECTIVE_RE = re.compile(r"^(?:finally|then|also|next|lastly|and|but|first|second|third|so),?\s+", re.I)
BULLET_RE = re.compile(r"^(?:[-*\u2022]|\d+[.)])\s+\S")
BULLET_MIN_RUN = 6
BULLET_MAX_SD = 1.5
TRIPLE_RE = re.compile(r"\b[A-Za-z][\w'-]*, [A-Za-z][\w'-]*,? (?:and|or) [A-Za-z][\w'-]*\b")  # words, not dates
TRIPLE_PER_300 = 3
METONYMY_RE = re.compile(r"\bwhat goes (?:on|in|into|out on|up on) the \w+", re.I)
PERSONA_RE = re.compile(
    r"\bYou are (?:a|an|the)\b"
    r"|\bAs (?:a|an) [^,.\n]{0,50}, you\b"
    r"|\bYour (?:task|job|role) is to\b"
    r"|\bYou have been (?:asked|tasked|hired|engaged) to\b"
    r"|\b(?:utiliz|leverag)\w* your (?:expertise|experience|knowledge|skills)\b"
    r"|\bAct as (?:a|an)\b|\bAssume the role of\b|\bImagine you are\b", re.I)


def bare_join_hits(s):
    out = []
    for m in BARE_JOIN_RE.finditer(s):
        before = s[:m.start()].rstrip()
        if COMPOUND_SUBJ_RE.search(before) or m.group(2).isupper():
            continue
        segment = re.split(r"[,;:]", before)[-1]
        if not ANY_VERB_RE.search(segment) or SUBORD_RE.search(segment):
            continue
        out.append(m)
    return out


def splice_hits(s):
    out = []
    for m in SPLICE_RE.finditer(s):
        segment = re.split(r"[;:]", s[:m.start()])[-1].strip()
        if not segment:
            continue
        first = segment.split()[0].lower().strip("\"'(").rstrip(",")
        if first in OPENER_WORDS or first.endswith("ly"):
            continue
        if SUBORD_RE.search(segment) or not ANY_VERB_RE.search(segment):
            continue
        out.append(m)
    return out


def prose_checks(text, rep, where, soft=False, skip=()):
    """M1-M4 and T1-T17 on a block of prose. soft=True turns every ERROR into a WARN (input files)."""

    def err(code, msg):
        if code in skip:
            return
        (rep.warn if soft else rep.error)(code, where, msg)

    def warn(code, msg):
        if code not in skip:
            rep.warn(code, where, msg)

    sents = sentence_list(text)
    paras = paragraphs(text)
    n_words = len(words(text))

    m = PERSONA_RE.search(text)
    if m and not soft:
        err("P4", f'role-play opener "{clip(m.group(0))}": open on the work, in the requester\'s voice')

    n_em = text.count(EM_DASH)
    if n_em:
        err("M1", f"{n_em} em dash(es): use a comma, colon, semicolon, parentheses or a new sentence")

    n_clause = 0
    for s in sents:
        if len(s.split()) < 8:
            continue
        bares = bare_join_hits(s)
        joins = len(COMMA_JOIN_RE.findall(s)) + len(SEMI_JOIN_RE.findall(s)) + len(bares)
        if bares and n_clause < CLAUSE_CAP:
            b = bares[0]
            warn("M2", f'no comma before "{b.group(1)}" where a new clause starts: '
                       f'"...{clip(s[max(0, b.start() - 30):b.end() + 20], 70)}..."')
            n_clause += 1
        elif joins >= 2 and n_clause < CLAUSE_CAP:
            warn("M3", f'{joins + 1} independent clauses in one sentence: "{clip(s)}"')
            n_clause += 1
        for sp in splice_hits(s)[:1]:
            if n_clause < CLAUSE_CAP:
                warn("M4", f'possible comma splice at ", {sp.group(1)} ...": "{clip(s)}"')
                n_clause += 1

    for rx in TAUTOLOGY_RES:
        m = next((m for m in rx.finditer(text) if not TAUTOLOGY_OK_RE.search(m.group(0))), None)
        if m:
            err("T1", f'tautology "{clip(m.group(0), 60)}": state the rule and its consequence')
            break
    for m in list(SLOGAN_RE.finditer(text))[:3]:
        warn("T2", f'slogan "{m.group(0)}": state the mechanism or the quantity')
    m = NEG_PARALLEL_RE.search(text)
    if m:
        warn("T4", f'negative parallelism "{clip(m.group(0))}": say the second half on its own')
    m = ITS_NOT_RE.search(text)
    if m:
        warn("T5", f'"it\'s not X, it\'s Y" contrast "{clip(m.group(0))}"')
    m = SERVES_AS_RE.search(text)
    if m:
        warn("T6", f'"{m.group(0)}": use is, has or holds')
    m = SYCOPHANCY_RE.search(text)
    if m:
        err("T7", f'sycophantic phrase "{m.group(0)}"')
    m = PRECOUNT_RE.search(text)
    if m:
        warn("T8", f'pre-counted list "{clip(m.group(0))}": make the points without counting them')
    m = HEDGE_RE.search(text)
    if m:
        warn("T9", f'hedging filler "{m.group(0)}": delete the frame, keep the claim')
    hits = []
    for m in CLINICAL_RE.finditer(text):
        w = m.group(0).lower()
        if w not in hits:
            hits.append(w)
    if hits:
        warn("T10", f"clinical vocabulary: {', '.join(hits[:CLINICAL_CAP])}; use the plain word")

    for para in paras:
        ps = sentence_list(para)
        if len(ps) < 3:
            continue
        stems = {}
        for s in ps:
            w = re.findall(r"[A-Za-z']+", CONNECTIVE_RE.sub("", s))[:2]
            if len(w) == 2:
                k = " ".join(x.lower() for x in w)
                stems[k] = stems.get(k, 0) + 1
        for k, n in stems.items():
            if n >= 3:
                warn("T11", f'{n} sentences in one paragraph open on "{k} ...": vary the shape')

    run, runs = [], []
    for line in text.split("\n"):
        s = line.strip()
        if BULLET_RE.match(s):
            run.append(s)
        else:
            if run:
                runs.append(run)
            run = []
    if run:
        runs.append(run)
    for r in runs:
        if len(r) >= BULLET_MIN_RUN:
            lengths = [len(b.split()) for b in r]
            sd = statistics.pstdev(lengths)
            if sd <= BULLET_MAX_SD:
                warn("T12", f"{len(r)} consecutive bullets of {min(lengths)} to {max(lengths)} words "
                            f"(sd {sd:.1f}): vary length and shape")
                break

    m = SEMI_MAXIM_RE.search(text)
    if m:
        warn("T13", f'semicolon-balanced maxim "{clip(m.group(0))}": say the consequence once')
    for para in paras:
        first = " ".join(para.split())
        m = SHORT_OPENER_RE.match(first)
        if m and not GREETING_WORDS_RE.match(m.group(1)) and not first.startswith("#"):
            warn("T14", f'paragraph opens on a fragment "{m.group(1)}.": open on the subject')
            break
    triples = TRIPLE_RE.findall(text)
    if len(triples) >= 3 and len(triples) / max(n_words, 1) * 300 >= TRIPLE_PER_300:
        warn("T15", f'{len(triples)} three-item lists in {n_words} words ("{clip(triples[0], 40)}", ...): '
                    f"keep lists of record, cut padding")
    m = METONYMY_RE.search(text)
    if m:
        warn("T17", f'"{m.group(0)}": name the document or list itself')


# ================================================================ P: prompt

DELIVERABLE_RE = re.compile(
    r"\b[\w-]+\.(?:xlsx|xls|docx|doc|csv|pdf|pptx|md|txt)\b"
    r"|\b(?:spreadsheet|workbook|excel|memo|memorandum|word document|document|deck|slides|powerpoint"
    r"|pdf|file|files|letter|template|tracker|csv)\b", re.I)
CHAT_ONLY_RE = re.compile(
    r"\b(?:just )?(?:reply|answer|respond|tell me|let me know) (?:here|in (?:the )?chat|in your reply)\b", re.I)
GREETING_LINE_RE = re.compile(r"^\s*(?:hi|hello|hey|dear|good (?:morning|afternoon|evening))\b[^\n]{0,40}$", re.I)
SIGNOFF_RE = re.compile(
    r"(?:^|\n)\s*(?:thanks|thank you|best|regards|cheers|kind regards|best regards|many thanks|sincerely"
    r"|warmly|talk soon)[,!.]?\s*(?:\n[^\n]{0,40})?\s*$", re.I)
SUBJECT_LINE_RE = re.compile(r"^\s*(?:subject|re|fw|to|from|cc)\s*:", re.I | re.M)
STEP_LINE_RE = re.compile(r"^\s*(?:\d+[.)]|\(\d+\)|[-*\u2022])\s+\S", re.M)
INLINE_STEPS_RE = re.compile(r"\(1\)[^.\n]{1,120}\(2\)")
SEQUENCE_RE = re.compile(r"\bfirst\b[^.?!]{0,200}[.?!]?[^.?!]{0,200}\b(?:then|next|finally|after that)\b", re.I)
REQUIREMENT_RE = re.compile(
    r"\b(?:should (?:include|contain|cover|address|provide|list|show)|must (?:include|contain|cover|address|provide)"
    r"|make sure (?:to|that|it|you)|ensure (?:that|the|it|you)|be sure to|needs? to (?:include|contain|cover))\b",
    re.I)
HINT_RE = re.compile(
    r"\b(?:be careful|careful with|watch out|watch for|keep in mind|don'?t forget|do not forget|beware"
    r"|pay (?:close )?attention|double-check|note that|heads up"
    r"|make sure (?:you|to) (?:check|catch|notice|spot|flag|look)"
    r"|there (?:may|might|could) be (?:an? |some )?(?:errors?|mistakes?|inconsistenc\w*|discrepanc\w*|issues?)"
    r"|(?:is|are|was|were|may be|might be) (?:outdated|superseded|stale|out of date|wrong|incorrect)"
    r"|trap|gotcha|tricky)\b", re.I)
WEB_RE = re.compile(
    r"\b(?:look (?:it |them |this )?up|search (?:the web|online|for)|google|browse|on the internet|online"
    r"|(?:current|latest|today'?s) (?:market )?(?:rates?|prices?|yields?|index|guidance|figures?))\b", re.I)
INVITE_RE = re.compile(
    r"\b(?:let me know if you have (?:any )?questions|ask (?:me )?if (?:anything|you)|if anything is unclear"
    r"|feel free to ask|any questions)\b", re.I)
PROJECT_VOCAB_RE = re.compile(
    r"\bAlchemy\b|\brubric\b|\bgrader\b|\bgrading agent\b|\battempting agent\b|\bFile Builder\b"
    r"|\bRubric Drafter\b|\bLLMs?\b|\bAI[- ]generated\b|\blanguage model\b|\bgold(?:en)?[- ]standard\b"
    r"|\banswer key\b|\bstarter project\b|\bsevere failure\b|\breinforcement learning\b"
    r"|\bthe (?:model|agent|AI|assistant) (?:should|must|will)\b", re.I)
AI_WORD_RE = re.compile(r"\b(?:AI|chatbot|ChatGPT|Claude|GPT-?\d*)\b")

FILENAME = r"[\w.()\- ]{2,60}?\.(?:csv|xlsx|xls|docx|doc|pdf|pptx|md|txt|eml)"
GLOSS_RE = re.compile(
    rf"\b{FILENAME}\s+(?:has|holds|contains|shows|lists|covers|is (?:the|our|their)|gives)\b"
    rf"|\b(?:the|our|their) [\w ]{{2,30}}? (?:is|are) (?:in )?{FILENAME}", re.I)
INPUT_REF_RE = re.compile(rf"{FILENAME}|\b(?:attached|export|thread|files?|spreadsheet|workbook|ledger|statement"
                          rf"|register|report|memo|email|policy|agreement)\b", re.I)
PROMPT_MIN_WORDS, PROMPT_MAX_WORDS, PROMPT_NEAR_CAP = 10, 180, 150
PROMPT_MIN_SENT, PROMPT_MAX_SENT = 2, 6
LONG_SENTENCE = 45


def check_prompt(text, rep, where="prompt.md"):
    text = strip_comments(text).strip()
    if not text:
        rep.error("P1", where, "prompt.md is empty")
        return
    sents = sentence_list(text)
    n_sent = len(sents)
    n_words = len(words(text))
    if not PROMPT_MIN_SENT <= n_sent <= PROMPT_MAX_SENT:
        rep.error("P1", where, f"{n_sent} sentence(s): the form wants 2 to 6")
    if n_words < PROMPT_MIN_WORDS or n_words > PROMPT_MAX_WORDS:
        rep.error("P2", where, f"{n_words} words: the form accepts 10 to 180")
    elif n_words > PROMPT_NEAR_CAP:
        rep.warn("P2", where, f"{n_words} words: near the 180-word cap; move background into the files")
    if not DELIVERABLE_RE.search(text):
        rep.warn("P3", where, "no output file is named (memo, workbook, deck, .xlsx ...): a chat answer is not a "
                              "deliverable")
    m = CHAT_ONLY_RE.search(text)
    if m:
        rep.warn("P3", where, f'"{m.group(0)}" asks for a chat answer; ask for a file')
    lines = [ln for ln in text.split("\n") if ln.strip()]
    if lines and GREETING_LINE_RE.match(lines[0]):
        rep.error("P5", where, f'greeting line "{clip(lines[0], 40)}": no email formatting')
    if SIGNOFF_RE.search(text):
        rep.error("P5", where, "sign-off at the end: no email formatting")
    if SUBJECT_LINE_RE.search(text):
        rep.error("P5", where, "header line (Subject:, To:, From:): no email formatting")
    paras = paragraphs(text)
    if len(paras) > 2:
        rep.warn("P6", where, f"{len(paras)} paragraphs: a handoff is one or two; move background into the files")
    for s in sents:
        if len(s.split()) > LONG_SENTENCE:
            rep.warn("P6", where, f'{len(s.split())}-word sentence: "{clip(s, 60)}"; split it or move the detail '
                                  f"into a file")
            break
    steps = len(STEP_LINE_RE.findall(text))
    if steps >= 2 or INLINE_STEPS_RE.search(text):
        rep.warn("P7", where, "a list or numbered procedure: say what to produce, not how")
    if SEQUENCE_RE.search(text):
        rep.warn("P7", where, '"first ... then" sequencing: the order of the work is the colleague\'s call')
    reqs = REQUIREMENT_RE.findall(text)
    if len(reqs) >= 2:
        rep.warn("P7", where, f'{len(reqs)} requirement phrases ("{reqs[0]}", ...): a requirement stack dictates '
                              f"the answer's shape")
    for m in list(HINT_RE.finditer(text))[:3]:
        rep.warn("P8", where, f'"{m.group(0)}" may hand over what the agent should notice: keep the facts in the '
                              f"files and let the work find them")
    m = INVITE_RE.search(text)
    if m:
        rep.warn("P9", where, f'"{m.group(0)}" invites a clarifying question, which is not a failure')
    m = WEB_RE.search(text)
    if m:
        rep.warn("P10", where, f'"{m.group(0)}": the agent has no web access; put the figure in a file')
    for m in list(PROJECT_VOCAB_RE.finditer(text))[:3]:
        rep.error("P12", where, f'project or evaluation vocabulary "{m.group(0)}"')
    m = AI_WORD_RE.search(text)
    if m:
        rep.warn("P12", where, f'"{m.group(0)}": a handoff to a colleague does not mention AI')
    glosses = GLOSS_RE.findall(text)
    if glosses:
        rep.warn("P13", where, f'{len(glosses)} file name(s) paired with what the file holds ("{clip(glosses[0], 50)}"): '
                               f"name the files in the story and let the work find what is in them")
    if not INPUT_REF_RE.search(text):
        rep.warn("P13", where, "no input is referred to: name the files or say what is attached")
    prose_checks(text, rep, where)


# ================================================================ I: input files

GENERIC_NAME_RE = re.compile(
    r"^(?:data|context|input|inputs|file|document|doc|sample|test|example|untitled|new|draft|output)"
    r"(?:[_\- ]?(?:file|doc|data|\d+))*\.", re.I)
SSN_RE = re.compile(r"\b(?!000|666|9\d\d)\d{3}-(?!00)\d{2}-(?!0000)\d{4}\b")
CARD_RE = re.compile(r"\b(?:\d[ -]?){13,19}\b")
PHONE_555_RE = re.compile(r"\(?\b\d{3}\)?[-.\s]?555[-.\s]\d{4}\b")
PERSONAL_EMAIL_RE = re.compile(r"\b[\w.+-]+@(?:gmail|yahoo|hotmail|outlook|icloud|aol|proton(?:mail)?|live)\.\w+\b",
                               re.I)
PLACEHOLDER_HARD_RE = re.compile(
    r"\blorem ipsum\b|\[(?:name|company|client|date|insert|amount|address|firm|bank|your)[^\]]{0,30}\]"
    r"|<(?:insert|name|company|client)[^>]{0,30}>|\{\{[^}]{1,30}\}\}|\bJohn Doe\b|\bJane Doe\b|\bAcme\b"
    r"|\bexample\.(?:com|org|net)\b|@[\w.-]+\.(?:example|invalid|test|localhost)\b|\bsample data\b|\bplaceholder\b"
    r"|\bdummy (?:text|data)\b"
    r"|\b(?:Company|Client|Person|Customer|Vendor|Borrower|Bank) [A-C]\b", re.I)
PLACEHOLDER_SOFT_RE = re.compile(r"\bTB[DC]\b|\bX{3,}\b")
REAL_FIRM_RE = re.compile(
    r"\b(?:Goldman Sachs|JP ?Morgan|J\.P\. Morgan|Morgan Stanley|Citi(?:group|bank)?|Wells Fargo|Bank of America"
    r"|BofA|HSBC|Barclays|UBS|Credit Suisse|Deutsche Bank|BNP Paribas|Santander|Deloitte|PwC"
    r"|PricewaterhouseCoopers|KPMG|Ernst & Young|BlackRock|Vanguard|Blackstone|KKR|Carlyle|Apollo Global"
    r"|Fidelity|Charles Schwab|Berkshire Hathaway|State Street|Lazard|Evercore|Jefferies|Moody'?s|S&P Global"
    r"|Fitch|Bloomberg|Airwallex|Stripe|PayPal|Visa|Mastercard|American Express|Apple|Microsoft|Amazon"
    r"|Alphabet|Google|Meta|Tesla|Nvidia|Walmart|Prudential|MetLife|AIG|Allianz|AXA|Lloyd'?s)\b")
INPUT_SIGNPOST_RES = [
    re.compile(r"\b(?:intentional|deliberate|planted|seeded)\s+(?:error|mistake|discrepanc\w*|inconsistenc\w*)\b", re.I),
    re.compile(r"\bthe correct (?:figure|amount|rate|number|treatment|answer|value|total|balance) (?:is|should be|"
               r"would be)\b", re.I),
    re.compile(r"\b(?:note|nb|important|reminder)\s*:\s*[^.\n]{0,80}\b(?:wrong|incorrect|error|outdated|superseded|"
               r"stale|do not use|ignore)\b", re.I),
    re.compile(r"\b(?:the analyst|the reviewer|the reader|whoever (?:picks|reads|works) (?:this|on this))\s+"
               r"(?:should|must|will need to|needs to)\b", re.I),
    re.compile(r"\bthis (?:figure|number|row|entry|line|amount|rate|balance) is (?:wrong|incorrect|outdated|a typo|"
               r"an error|superseded)\b", re.I),
    re.compile(r"\b(?:hint|spoiler|answer)\s*:", re.I),
]
ANNOTATION_RE = re.compile(r"^\s*(?:\*\*)?(?:note|important|key takeaways?|reminder|tip|nb)(?:\*\*)?\s*:", re.I | re.M)
SELF_DESC_RE = re.compile(
    r"\bthe sections? (?:that )?follow(?:s|ing)?\b|\bas (?:outlined|detailed|summari[sz]ed|set out) below\b"
    r"|\bbelow (?:you will find|is a summary|are the key)\b|\bthis (?:document|memo|thread|file|email|workbook|sheet"
    r"|export|report) (?:contains|describes|summari[sz]es|outlines|provides|sets out|is intended)\b"
    r"|\b(?:yellow|green|blue|grey|gray|shaded) cells (?:are|show|hold)\b|\bfor (?:your|the reader's) reference\b", re.I)
FLOAT_DUST_RE = re.compile(r"\b\d+\.\d*?(?:0{6,}[1-9]\d*|9{6,}\d*)\b")
WEEKDAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
MONTHS = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
          "november", "december"]
WD = r"(Mon|Tue|Tues|Wed|Thu|Thur|Thurs|Fri|Sat|Sun)(?:day|sday|nesday|rsday|urday)?\.?"
MO = r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\.?"
DATE_RES = [
    (re.compile(rf"\b{WD},?\s+{MO}\s+(\d{{1,2}})(?:st|nd|rd|th)?,?\s+(\d{{4}})\b", re.I), "wmdy"),
    (re.compile(rf"\b{WD},?\s+(\d{{1,2}})(?:st|nd|rd|th)?\s+{MO},?\s+(\d{{4}})\b", re.I), "wdmy"),
    (re.compile(rf"\b{WD},?\s+(\d{{1,2}})/(\d{{1,2}})/(\d{{4}})\b", re.I), "wnum"),
]
GENERATOR_RE = re.compile(r"python-docx|openpyxl|xlsxwriter|pandas|python|reportlab|docx\.js|exceljs|sheetjs|"
                          r"Apache POI|docx4j", re.I)
NON_ADDITIVE_HEADER_RE = re.compile(
    r"rate|%|pct|percent|price|avg|average|ratio|margin|yield|date|year|\bid\b|\bno\b|number|#|days|term|months"
    r"|score|grade|rank|age|bps|multiple|factor|coupon|apr|ltv|dscr|fico|zip|phone|code", re.I)
ROUND_OK_HEADER_RE = re.compile(r"limit|principal|commitment|facility|line|budget|target|plan|quota|cap|face|par"
                                r"|notional|authori[sz]ed|approved|requested|loan amount|deposit", re.I)
THIN_WORDS = 60
PROSE_DOC_WORDS = 200
THIN_CELLS = 12
TEXT_EXT = {".md", ".txt", ".eml", ".json", ".xml", ".html", ".htm", ".rtf"}
TABLE_EXT = {".csv", ".tsv"}


def _xml(z, name):
    try:
        return ET.fromstring(z.read(name))
    except (KeyError, ET.ParseError):
        return None


def _doc_props(z, rep, where):
    for part in ("docProps/core.xml", "docProps/app.xml"):
        root = _xml(z, part)
        if root is None:
            continue
        for el in root.iter():
            if el.text and GENERATOR_RE.search(el.text):
                tag = el.tag.split("}")[-1]
                rep.note("I12", where, f'{part} {tag} is "{clip(el.text, 40)}": a generator stamp; expected if '
                                       f"File Builder made the file, otherwise re-save it in Office")
                return


def read_docx(path, rep, where):
    W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
    with zipfile.ZipFile(path) as z:
        names = set(z.namelist())
        root = _xml(z, "word/document.xml")
        if root is None:
            rep.error("I13", where, "cannot read word/document.xml")
            return "", []
        paras = ["".join(t.text or "" for t in p.iter(W + "t")) for p in root.iter(W + "p")]
        tables = []
        for tbl in root.iter(W + "tbl"):
            rows = [["".join(t.text or "" for t in tc.iter(W + "t")) for tc in tr.iter(W + "tc")]
                    for tr in tbl.iter(W + "tr")]
            tables.append(rows)
        if any(True for _ in root.iter(W + "ins")) or any(True for _ in root.iter(W + "del")):
            rep.warn("I12", where, "tracked changes present: accept or reject them before upload")
        if "word/comments.xml" in names:
            rep.warn("I12", where, "comments present: remove them, or make sure none points at the answer")
        _doc_props(z, rep, where)
    return "\n\n".join(p for p in paras if p.strip()), tables


def _col_index(ref):
    letters = re.match(r"[A-Z]+", ref or "A")
    n = 0
    for ch in letters.group(0) if letters else "A":
        n = n * 26 + ord(ch) - 64
    return n - 1


def read_xlsx(path, rep, where):
    M = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
    RID = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"
    tables, texts = [], []
    with zipfile.ZipFile(path) as z:
        names = set(z.namelist())
        shared = []
        sroot = _xml(z, "xl/sharedStrings.xml")
        if sroot is not None:
            for si in sroot.iter(M + "si"):
                shared.append("".join(t.text or "" for t in si.iter(M + "t")))
        wb = _xml(z, "xl/workbook.xml")
        rels = _xml(z, "xl/_rels/workbook.xml.rels")
        if wb is None or rels is None:
            rep.error("I13", where, "cannot read the workbook structure")
            return "", []
        relmap = {r.get("Id"): r.get("Target") for r in rels}
        for sh in wb.iter(M + "sheet"):
            name, state = sh.get("name"), sh.get("state")
            if state in ("hidden", "veryHidden"):
                rep.warn("I12", where, f'sheet "{name}" is {state}: unhide or delete it')
            target = relmap.get(sh.get(RID), "")
            part = target.lstrip("/") if target.startswith("/") else "xl/" + target
            sroot = _xml(z, part)
            if sroot is None:
                continue
            for col in sroot.iter(M + "col"):
                if col.get("hidden") in ("1", "true"):
                    rep.warn("I12", where, f'sheet "{name}" has hidden columns')
                    break
            rows = []
            hidden_rows = 0
            for row in sroot.iter(M + "row"):
                if row.get("hidden") in ("1", "true"):
                    hidden_rows += 1
                cells = {}
                for c in row.iter(M + "c"):
                    t = c.get("t")
                    v = c.find(M + "v")
                    if t == "s" and v is not None and v.text is not None:
                        val = shared[int(v.text)] if int(v.text) < len(shared) else ""
                    elif t == "inlineStr":
                        val = "".join(x.text or "" for x in c.iter(M + "t"))
                    else:
                        val = v.text if v is not None and v.text is not None else ""
                    cells[_col_index(c.get("r"))] = val
                if cells:
                    rows.append([cells.get(i, "") for i in range(max(cells) + 1)])
            if hidden_rows:
                rep.warn("I12", where, f'sheet "{name}" has {hidden_rows} hidden row(s)')
            tables.append(rows)
            texts.extend(cell for r in rows for cell in r if cell)
        if any(n.startswith("xl/comments") or n.startswith("xl/threadedComments") for n in names):
            rep.warn("I12", where, "cell comments present: remove them, or make sure none points at the answer")
        _doc_props(z, rep, where)
    return "\n".join(texts), tables


def read_pptx(path, rep, where):
    A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
    texts = []
    with zipfile.ZipFile(path) as z:
        for n in sorted(z.namelist()):
            if re.match(r"ppt/slides/slide\d+\.xml$", n):
                root = _xml(z, n)
                if root is not None:
                    texts.extend(p for p in ("".join(t.text or "" for t in para.iter(A + "t"))
                                             for para in root.iter(A + "p")) if p.strip())
            if n.startswith("ppt/notesSlides/"):
                rep.warn("I12", where, "speaker notes present: remove them, or make sure none points at the answer")
                break
        _doc_props(z, rep, where)
    return "\n\n".join(texts), []


def read_input(path, rep, where):
    """Returns (prose_text, all_text, tables)."""
    ext = path.suffix.lower()
    if ext in TABLE_EXT:
        raw = path.read_text(encoding="utf-8-sig", errors="replace")
        delim = "\t" if ext == ".tsv" else ","
        rows = list(csv.reader(io.StringIO(raw), delimiter=delim))
        cells = [c for r in rows for c in r]
        prose = "\n\n".join(c for c in cells if len(c.split()) >= 10)
        return prose, raw, [rows]
    if ext in TEXT_EXT:
        raw = path.read_text(encoding="utf-8", errors="replace")
        if ext in (".html", ".htm"):
            raw = re.sub(r"<[^>]+>", " ", raw)
        return raw, raw, []
    if ext == ".docx":
        text, tables = read_docx(path, rep, where)
        return text, text, tables
    if ext == ".xlsx":
        text, tables = read_xlsx(path, rep, where)
        prose = "\n\n".join(c for t in tables for r in t for c in r if len(c.split()) >= 10)
        return prose, text, tables
    if ext == ".pptx":
        text, tables = read_pptx(path, rep, where)
        return text, text, tables
    if ext == ".pdf":
        rep.note("I11", where, "PDF text is not scanned by this script: read it for every I rule by hand")
        return "", "", []
    rep.warn("I3", where, f"unusual file type {ext}: confirm the platform and the agent can open it")
    return "", "", []


def parse_number(s):
    s = (s or "").strip()
    if not s:
        return None
    neg = s.startswith("(") and s.endswith(")")
    s = s.strip("()").replace("$", "").replace(",", "").replace("\u00a3", "").replace("\u20ac", "").strip()
    if s.endswith("%"):
        return None
    if s.startswith("-"):
        neg, s = True, s[1:]
    if not re.fullmatch(r"\d+(?:\.\d+)?", s):
        return None
    v = float(s)
    return -v if neg else v


def check_tables(tables, rep, where):
    for rows in tables:
        # skip a report preamble (run header lines) down to the first row that looks like a header
        start = next((i for i, r in enumerate(rows) if sum(1 for c in r if (c or "").strip()) >= 3), 0)
        rows = rows[start:]
        if len(rows) < 3:
            continue
        header = rows[0]
        width = max(len(r) for r in rows)
        total_rows = [i for i, r in enumerate(rows)
                      if any(re.match(r"^\s*(?:grand |sub-?)?total\b|^\s*sum\b", (c or ""), re.I) for c in r[:2])]
        for col in range(width):
            head = header[col] if col < len(header) else ""
            if NON_ADDITIVE_HEADER_RE.search(head or ""):
                continue
            start = 1
            for ti in total_rows:
                row = rows[ti]
                tot = parse_number(row[col]) if col < len(row) else None
                parts = [parse_number(r[col]) for r in rows[start:ti] if col < len(r)]
                parts = [p for p in parts if p is not None]
                is_sub = re.match(r"^\s*sub", " ".join(row[:2]), re.I)
                if tot is not None and len(parts) >= 2:
                    s = sum(parts)
                    if abs(s - tot) > max(0.011, abs(tot) * 0.0005):
                        rep.warn("I10", where, f'"{clip(" ".join(row[:2]).strip(), 30)}" row, column '
                                               f'"{clip(head, 25)}": {tot:,.2f} stated, {s:,.2f} by sum. Planted? '
                                               f"Note it in task.md; otherwise fix it")
                if not is_sub:
                    start = ti + 1
            # no-variance column
            vals = [parse_number(r[col]) for r in rows[1:] if col < len(r) and r not in [rows[i] for i in total_rows]]
            vals = [v for v in vals if v is not None]
            if len(vals) >= 8 and not ROUND_OK_HEADER_RE.search(head or "") and \
                    all(abs(v) >= 100 and v % 100 == 0 for v in vals):
                rep.warn("I11", where, f'column "{clip(head, 25)}": all {len(vals)} values are multiples of 100; '
                                       f"real working figures carry variance")


def calendar_false(text):
    out = []
    for rx, shape in DATE_RES:
        for m in rx.finditer(text):
            try:
                wd = m.group(1).lower()[:3]
                if shape == "wmdy":
                    mo = [x[:3] for x in MONTHS].index(m.group(2).lower()[:3]) + 1
                    d, y = int(m.group(3)), int(m.group(4))
                elif shape == "wdmy":
                    d = int(m.group(2))
                    mo = [x[:3] for x in MONTHS].index(m.group(3).lower()[:3]) + 1
                    y = int(m.group(4))
                else:
                    mo, d, y = int(m.group(2)), int(m.group(3)), int(m.group(4))
                actual = datetime.date(y, mo, d).weekday()
            except (ValueError, IndexError):
                out.append((m.group(0), "not a real date"))
                continue
            if WEEKDAYS[actual][:3] != wd:
                out.append((m.group(0), f"that date is a {WEEKDAYS[actual].capitalize()}"))
    return out


def luhn(digits):
    total, alt = 0, False
    for ch in reversed(digits):
        d = int(ch)
        if alt:
            d *= 2
            if d > 9:
                d -= 9
        total += d
        alt = not alt
    return total % 10 == 0


def check_input_text(name, prose, alltext, tables, rep):
    where = f"inputs/{name}"
    n = len(words(alltext))
    if n == 0:
        rep.error("I13", where, "no readable content")
        return
    n_cells = sum(1 for t in tables for r in t for c in r if c.strip())
    if tables and n_cells >= THIN_CELLS:
        pass
    elif tables and n_cells < THIN_CELLS and n < THIN_WORDS:
        rep.warn("I13", where, f"{n_cells} filled cells: too thin to carry the scenario")
    elif n < THIN_WORDS:
        rep.warn("I13", where, f"{n} words: too thin to carry the scenario")
    elif not tables and n < PROSE_DOC_WORDS:
        rep.warn("I13", where, f"{n} words: short for a real thread, memo or policy; extend it in the writer's own voice, "
                               f"with no new rules")
    for m in list(PROJECT_VOCAB_RE.finditer(alltext))[:3]:
        rep.error("I5", where, f'project or evaluation vocabulary "{m.group(0)}"')
    for rx in INPUT_SIGNPOST_RES:
        m = rx.search(alltext)
        if m:
            rep.warn("I5", where, f'"{clip(m.group(0), 60)}" points at the answer; state the fact and let the '
                                  f"work find it")
    for m in list(SSN_RE.finditer(alltext))[:2]:
        rep.error("I8", where, f'"{m.group(0)}" has the shape of a US Social Security number; change the shape')
    for m in CARD_RE.finditer(alltext):
        digits = re.sub(r"\D", "", m.group(0))
        if 13 <= len(digits) <= 19 and luhn(digits) and len(set(digits)) > 2:
            rep.warn("I8", where, f'"{m.group(0).strip()}" passes the card-number checksum; use an internal '
                                  f"reference shape")
            break
    m = PERSONAL_EMAIL_RE.search(alltext)
    if m:
        rep.warn("I8", where, f'"{m.group(0)}" is a personal email domain; use the fictional firm\'s domain')
    for m in list(PLACEHOLDER_HARD_RE.finditer(alltext))[:3]:
        rep.error("I8", where, f'placeholder "{m.group(0)}": use a realistic fictional value')
    m = PLACEHOLDER_SOFT_RE.search(alltext)
    if m:
        rep.warn("I8", where, f'"{m.group(0)}": a placeholder, unless the document really leaves it open')
    firms = sorted({m.group(0) for m in REAL_FIRM_RE.finditer(alltext)})
    if firms:
        rep.warn("I8", where, f"real company name(s): {', '.join(firms[:5])}; the training says avoid real client or "
                              f"company names")
    for m in list(PHONE_555_RE.finditer(alltext))[:1]:
        rep.warn("I11", where, f'"{m.group(0)}": 555 numbers read as invented')
    for s, why in calendar_false(alltext)[:3]:
        rep.warn("I11", where, f'"{s}": {why}')
    m = FLOAT_DUST_RE.search(alltext)
    if m:
        rep.warn("I11", where, f'"{m.group(0)}": floating-point residue; round to the precision a person keys')
    for m in list(SELF_DESC_RE.finditer(alltext))[:2]:
        rep.warn("T19", where, f'"{m.group(0)}": the document describes itself; real documents just say the thing')
    n_ann = len(ANNOTATION_RE.findall(alltext))
    if n_ann >= 2:
        rep.warn("T18", where, f"{n_ann} Note:/Important:/Key takeaway lines: annotation voice addressed to the next "
                               f"reader; keep only what the real document would carry")
    check_tables(tables, rep, where)
    if prose:
        prose_checks(prose, rep, where, soft=True, skip=("T8", "T15", "M2", "M3", "M4"))


def check_inputs(folder, rep):
    inp = folder / "inputs"
    if not inp.is_dir():
        rep.error("I1", "inputs/", "no inputs/ folder")
        return []
    files = sorted(p for p in inp.iterdir() if p.is_file() and not p.name.startswith("."))
    junk = [p.name for p in inp.iterdir() if (p.name.startswith(".") or p.is_dir()) and p.name != ".gitkeep"]
    if junk:
        rep.note("I14", "inputs/", f"ignored: {', '.join(junk)} (kept out of the ZIP by --zip)")
    if len(files) != 2:
        rep.error("I1", "inputs/", f"{len(files)} file(s): the Starter Project wants exactly two (data and context)")
    for p in files:
        where = f"inputs/{p.name}"
        if GENERIC_NAME_RE.match(p.name):
            rep.warn("I3", where, "generic file name: name it the way the real document would be saved")
        if p.stat().st_size == 0:
            rep.error("I13", where, "empty file")
            continue
        try:
            prose, alltext, tables = read_input(p, rep, where)
        except (zipfile.BadZipFile, OSError, UnicodeError) as e:
            rep.error("I13", where, f"cannot open: {e}")
            continue
        if alltext or p.suffix.lower() != ".pdf":
            check_input_text(p.name, prose, alltext, tables, rep)
    return files


# ================================================================ I14: the ZIP

SYSTEM_FILE_RE = re.compile(r"(?:^|/)(?:__MACOSX|\.DS_Store|Thumbs\.db|desktop\.ini|\._)", re.I)


def build_zip(folder):
    inp = folder / "inputs"
    files = sorted(p for p in inp.iterdir() if p.is_file() and not p.name.startswith("."))
    out = folder / "inputs.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(zipfile.ZipInfo("inputs/"), "")
        for p in files:
            z.write(p, f"inputs/{p.name}")
    return out


def check_zip(folder, rep):
    zp = folder / "inputs.zip"
    if not zp.exists():
        rep.warn("I14", "inputs.zip", "not built yet: run with --zip once the two files are final")
        return
    try:
        z = zipfile.ZipFile(zp)
    except zipfile.BadZipFile:
        rep.error("I14", "inputs.zip", "not a valid ZIP")
        return
    with z:
        names = z.namelist()
        tops = {n.split("/")[0] for n in names}
        if tops != {"inputs"}:
            rep.error("I14", "inputs.zip", f"top level holds {sorted(tops)}: the only top-level entry must be inputs/")
        junk = [n for n in names if SYSTEM_FILE_RE.search(n)]
        if junk:
            rep.error("I14", "inputs.zip", f"system files inside: {', '.join(junk[:3])}")
        members = [n for n in names if not n.endswith("/") and not SYSTEM_FILE_RE.search(n)]
        nested = [n for n in members if n.count("/") != 1]
        if nested:
            rep.error("I14", "inputs.zip", f"files outside inputs/ or nested deeper: {', '.join(nested[:3])}")
        flat = [n for n in members if n.count("/") == 1 and n.startswith("inputs/")]
        if len(flat) != 2:
            rep.error("I14", "inputs.zip", f"{len(flat)} file(s) under inputs/: exactly two")
        inp = folder / "inputs"
        for n in flat:
            local = inp / n.split("/", 1)[1]
            if not local.exists():
                rep.error("I14", "inputs.zip", f"{n} has no match in inputs/: rebuild with --zip")
            elif z.read(n) != local.read_bytes():
                rep.error("I14", "inputs.zip", f"{n} differs from inputs/: the ZIP is stale, rebuild with --zip")
        if inp.is_dir():
            for p in inp.iterdir():
                if p.is_file() and not p.name.startswith(".") and f"inputs/{p.name}" not in flat:
                    rep.error("I14", "inputs.zip", f"inputs/{p.name} is missing from the ZIP: rebuild with --zip")


# ================================================================ R: rubric

CRIT_START_RE = re.compile(r"^\s*(\d+)[.)]\s+(.*\S)")
VAGUE_RE = re.compile(
    r"\b(?:correct(?:ly)?|appropriate(?:ly)?|adequate(?:ly)?|accurate(?:ly)?|proper(?:ly)?|reasonabl[ey]"
    r"|sufficient(?:ly)?|comprehensive(?:ly)?|thorough(?:ly)?|suitabl[ey]|good|clearly|relevant|meaningful(?:ly)?"
    r"|sensible|acceptable|satisfactor(?:y|ily))\b", re.I)
PREDICTION_RE = re.compile(
    r"\b(?:the )?(?:model|agent|AI|LLM|assistant)s? (?:will|would|is likely to|may|might|tends? to|often|usually)\b"
    r"|\bwill (?:likely|probably) (?:fail|miss)\b|\blikely to (?:fail|miss)\b", re.I)
SHAPE_RE = re.compile(r"\bthe (?:response|answer|output|submission) should\b|\bshould\b|\bmust\b|\bneeds? to\b", re.I)
AGENT_SUBJECT_RE = re.compile(r"\bthe (?:agent|AI|LLM|assistant|attempting agent)\b", re.I)
COSMETIC_RE = re.compile(
    r"\b(?:font|bold(?:ed)?|italic\w*|colou?r(?:ed|s)?|highlight\w*|formatting|formatted|layout|spelling|grammar"
    r"|typo\w*|tone|neat\w*|professional[- ]looking|visually|aesthetic\w*|title page|logo|bullet points?)\b", re.I)
HEDGE_CRIT_RE = re.compile(
    r"\b(?:roughly|approximately|approx\.|or equivalent|or similar|or so|etc\.|and so on|some of|most of"
    r"|generally|largely|mostly|broadly|in substance)\b", re.I)
GRADER_INSTR_RE = re.compile(
    r"\b(?:award|give|grant)s? (?:full |partial )?(?:credit|points?)\b|\bcredit (?:here )?is (?:given )?for\b"
    r"|\bis not this defect\b|\bthe grader\b|\bmark(?:ed)? (?:as )?(?:pass|fail|correct)\b|\bpartial credit\b"
    r"|\bdo not penali[sz]e\b|\bignore (?:minor|small|rounding)\b", re.I)
COUNT_RE = re.compile(
    r"\b(?:at least|exactly|no more than|no fewer than|each of (?:its|the|their)) (?:\d+|two|three|four|five|six|seven"
    r"|eight|nine|ten) (?:actions|bullets|figures|sections|paragraphs|tabs|sheets|recommendations|steps|points"
    r"|columns|rows|pages|charts|tables)\b", re.I)
METHOD_RE = re.compile(
    r"\b(?:in|on) (?:cell|column|row|tab|sheet|worksheet)\b|\bcell [A-Z]{1,3}\d+\b"
    r"|\b(?:using|via|by using|with) (?:the |a |an )?(?:formula|function|method|approach|VLOOKUP|XLOOKUP|SUMIFS?"
    r"|INDEX|MATCH|pivot(?: table)?)\b|\bin (?:that|this|the following|the same) order\b"
    r"|\bexact (?:wording|phrase|phrasing)\b|\bverbatim\b|\b(?:first|second|last) (?:tab|sheet|section|paragraph)\b",
    re.I)
UNSEEN_HARD_RE = re.compile(
    r"\bgold(?:en)?[- ]?(?:standard|answer|solution)\b|\b(?:reference|expert|model|sample) (?:answer|solution)\b"
    r"|\banswer key\b|\bmy (?:answer|solution|deliverable)\b", re.I)
UNSEEN_SOFT_RE = re.compile(
    r"\b(?:the|an?) (?:input|data|context|source|attached) (?:file|document|spreadsheet|workbook|email|memo)\b"
    r"|\bper the (?:files?|inputs?|attachments?)\b|\bas (?:stated|described|shown|given|listed) in the\b", re.I)
DECISION_RE = re.compile(
    r"\b(?:approv\w+|reject\w*|declin\w+|recommend\w*|exclud\w+|includ\w+|classif\w+|flag\w*|treat\w*|record\w*"
    r"|defer\w*|accru\w+|capitali[sz]\w+|expens\w+|write[sd]?[- ]off|written off|revers\w+|withh[eo]ld\w*"
    r"|escalat\w+|breach\w*|waiv\w+|eligible|ineligible|identif\w+|names?|states?|reports?|lists?)\b", re.I)
QUOTE_RE = re.compile(r"\"[^\"]{2,}\"|\u201c[^\u201d]{2,}\u201d|'[^']{3,}'")
SECOND_CLAIM_RE = re.compile(
    r",? and (?:it |also |then |the \w+ )?(?:states|reports|shows|lists|identifies|recommends|flags|includes"
    r"|excludes|classifies|calculates|gives|names|notes|explains|treats|uses|applies|concludes|records)\b"
    r"|\bas well as\b|\bin addition to\b|\band also\b|\balong with\b", re.I)
STOP = set("the a an of to in on for and or is are be by with as at from that this it its which their".split())


def parse_rubric(text):
    text = strip_comments(text)
    crits = []
    cur = None
    for line in text.split("\n"):
        if re.match(r"^\s*\d+[.)]\s*$", line):
            if cur:
                crits.append(cur)
            cur = None
            continue
        m = CRIT_START_RE.match(line)
        if m:
            if cur:
                crits.append(cur)
            cur = [int(m.group(1)), m.group(2).strip()]
        elif cur and line.strip() and not line.lstrip().startswith(("#", ">", "|")):
            cur[1] += " " + line.strip()
        elif cur and not line.strip():
            crits.append(cur)
            cur = None
    if cur:
        crits.append(cur)
    return [(n, " ".join(t.split())) for n, t in crits]


def check_rubric(text, rep, full=False, where="rubric.md"):
    crits = parse_rubric(text)
    n = len(crits)
    if full and n < FULL_MIN_CRITERIA:
        rep.error("R1", where, f"{n} criteria: a full task needs at least {FULL_MIN_CRITERIA}")
    elif not full and n != STARTER_CRITERIA:
        rep.error("R1", where, f"{n} criteria: the Starter Project uses exactly {STARTER_CRITERIA}")
    nums = [c[0] for c in crits]
    if nums != list(range(1, n + 1)):
        rep.warn("R1", where, f"numbering {nums}: number the criteria 1 to {n} so the failure description can cite them")
    for num, c in crits:
        w = f"{where} #{num}"
        nw = len(c.split())
        if len(sentence_list(c)) > 1:
            rep.warn("R2", w, "more than one sentence: one criterion, one check")
        if ";" in c:
            rep.warn("R2", w, "semicolon joins two checks: split them")
        m = SECOND_CLAIM_RE.search(c)
        if m:
            rep.warn("R2", w, f'"{m.group(0).strip()}" adds a second claim: split it')
        if nw > 60:
            rep.warn("R2", w, f"{nw} words: probably a bundle")
        has_value = bool(re.search(r"\d", c) or QUOTE_RE.search(c) or DECISION_RE.search(c)
                         or re.search(r"(?<!^)(?<![.:]\s)\b[A-Z][a-z]+\b", c[1:]))
        if not has_value:
            rep.warn("R3", w, "no value, name, quote or decision: the grader cannot check it without one")
        if nw < 6:
            rep.warn("R3", w, f"{nw} words: too short to carry its expected value")
        m = METHOD_RE.search(c)
        if m:
            rep.warn("R5", w, f'"{m.group(0)}" mandates a location or method: any correct response must pass')
        m = PREDICTION_RE.search(c)
        if m:
            rep.error("R8", w, f'prediction "{m.group(0)}": a criterion states what a correct deliverable contains')
        else:
            m = SHAPE_RE.search(c)
            if m:
                rep.warn("R6", w, f'"{m.group(0)}": write subject + verb + expected value ("The memo reports ...")')
            m = AGENT_SUBJECT_RE.search(c)
            if m:
                rep.warn("R6", w, f'"{m.group(0)}" as subject: name the deliverable or its part instead')
        m = HEDGE_CRIT_RE.search(c)
        if m:
            rep.warn("R7", w, f'hedge "{m.group(0)}": state the band in figures ("between $X and $Y") or drop it')
        m = GRADER_INSTR_RE.search(c)
        if m:
            rep.error("R14", w, f'grader instruction "{m.group(0)}": a criterion states a property of the deliverable')
        m = COUNT_RE.search(c)
        if m:
            rep.warn("R5", w, f'"{m.group(0)}": a count the prompt did not fix; grade the content instead')
        vague = sorted({m.group(0).lower() for m in VAGUE_RE.finditer(c)})
        if vague:
            rep.warn("R7", w, f"vague word(s) {', '.join(vague)}: state the value or decision itself")
        m = COSMETIC_RE.search(c)
        if m:
            rep.warn("R9", w, f'"{m.group(0)}": cosmetic criteria are omitted')
        m = UNSEEN_HARD_RE.search(c)
        if m:
            rep.error("R12", w, f'"{m.group(0)}": the grader never sees it; state the value')
        m = UNSEEN_SOFT_RE.search(c)
        if m:
            rep.warn("R12", w, f'"{m.group(0)}": the grader sees only the response and output files; state the value')
        if EM_DASH in c:
            rep.error("M1", w, "em dash")
    bags = [(num, {x for x in re.findall(r"[a-z0-9$.,%]+", c.lower()) if x not in STOP}) for num, c in crits]
    for i in range(len(bags)):
        for j in range(i + 1, len(bags)):
            a, b = bags[i][1], bags[j][1]
            if a and b and len(a & b) / len(a | b) >= 0.7:
                rep.warn("R13", where, f"#{bags[i][0]} and #{bags[j][0]} are near-duplicates: one thing, scored once")
    return n


# ================================================================ A: failure description and runs

def extract_section(text, name):
    m = re.search(rf"^## (?:Steps? \d+(?:(?: and | to |-)\d+)?: )?{re.escape(name)}\s*$", text, re.M)
    if not m:
        return None
    rest = text[m.end():]
    nxt = re.search(r"^## ", rest, re.M)
    body = rest[:nxt.start()] if nxt else rest
    body = strip_comments(body)
    body = re.sub(r"^\s*>\s?", "", body, flags=re.M)
    return body.strip()


FAILURE_MIN_WORDS, FAILURE_MAX_WORDS = 50, 350
NON_SEVERE_RE = re.compile(
    r"\b(?:refus\w+|clarif\w+|asked (?:a |for )?(?:question|clarification)|formatting|typo\w*|font"
    r"|misunderst\w+ the (?:prompt|ask)|unclear prompt|cosmetic)\b", re.I)
CRIT_CITE_RE = re.compile(r"\bcriteri(?:on|a)\b\s*((?:(?:#?\s*\d+)\s*(?:,|and|&|or|to|-)?\s*)+)", re.I)


def check_failure(text, rep, n_crit=None, input_names=(), where="task.md Failure description"):
    if not text:
        rep.warn("A4", where, "empty: written after the Grading Agent runs")
        return
    n = len(words(text))
    if n < FAILURE_MIN_WORDS or n > FAILURE_MAX_WORDS:
        rep.error("A4", where, f"{n} words: the form wants {FAILURE_MIN_WORDS} to {FAILURE_MAX_WORDS}")
    cited = []
    for m in CRIT_CITE_RE.finditer(text):
        cited.extend(int(x) for x in re.findall(r"\d+", m.group(1)))
    cited.extend(int(x) for x in re.findall(r"(?<![\w$])#(\d+)\b", text))
    if not cited:
        rep.warn("A5", where, 'no criterion number cited ("criterion 3"): name the ones that capture the failure')
    elif n_crit:
        bad = sorted({c for c in cited if c < 1 or c > n_crit})
        if bad:
            rep.error("A5", where, f"cites criterion {bad}, but the rubric has {n_crit}")
    if input_names:
        stems = set()
        for nm in input_names:
            stem = Path(nm).stem.lower()
            stems.update({nm.lower(), stem, stem.replace("_", " "), stem.replace("-", " ")})
        if not any(s and s in text.lower() for s in stems):
            rep.warn("A6", where, "no input file is named: cite where the evidence sits")
    if not re.search(r"\d", text.replace("criterion", "")):
        rep.warn("A6", where, "no figure: give the expected value and what the agent produced")
    m = NON_SEVERE_RE.search(text)
    if m:
        rep.warn("A2", where, f'"{m.group(0)}": refusals, questions and formatting are not the target failure')
    prose_checks(text, rep, where)


FP_RE = re.compile(r"^\s*(?:\*\*)?Fingerprint:?(?:\*\*)?:?\s*`?([0-9a-f]{8,64})`?", re.I | re.M)
GRADE_RE = re.compile(r"^\s*[-*]?\s*(?:\*\*)?(?:criterion|#)\s*#?(\d+)(?:\*\*)?\s*[:|\-]\s*(?:\*\*)?(PASS|FAIL)\b",
                      re.I | re.M)
ESCAPE_RE = re.compile(r"^\s*(?:\*\*)?Escape hatch:?(?:\*\*)?:?\s*yes\b", re.I | re.M)


def fingerprint(folder):
    h = hashlib.sha256()
    prompt = folder / "prompt.md"
    text = strip_comments(prompt.read_text(encoding="utf-8")) if prompt.exists() else ""
    h.update(" ".join(text.split()).encode())
    inp = folder / "inputs"
    if inp.is_dir():
        for p in sorted(inp.iterdir()):
            if p.is_file() and not p.name.startswith("."):
                h.update(b"\0" + p.name.encode() + b"\0")
                h.update(p.read_bytes())
    return h.hexdigest()[:16]


def run_files(folder):
    rd = folder / "runs"
    if not rd.is_dir():
        return []
    return sorted((p for p in rd.glob("run-*.md")), key=lambda p: [int(x) for x in re.findall(r"\d+", p.stem)] or [0])


def read_run(p):
    t = p.read_text(encoding="utf-8")
    fp = FP_RE.search(t)
    grades = {int(n): v.upper() for n, v in GRADE_RE.findall(t)}
    return (fp.group(1) if fp else None), grades


def check_runs(folder, rep):
    runs = run_files(folder)
    current = fingerprint(folder)
    task = folder / "task.md"
    escape = bool(task.exists() and ESCAPE_RE.search(task.read_text(encoding="utf-8")))
    if not runs:
        rep.warn("A1", "runs/", "no Attempting Agent run recorded yet")
        return
    fails_on_current = False
    graded_any = False
    pending_current = False
    for p in runs:
        fp, grades = read_run(p)
        where = f"runs/{p.name}"
        if grades:
            graded_any = True  # any graded run, current or stale, means grading has started
        if not fp:
            rep.warn("A3", where, "no Fingerprint line: record the --fingerprint value when the run is made")
        elif fp != current[:len(fp)]:
            rep.error("A3", where, f"stale: fingerprint {fp} but prompt and inputs now give {current}. Delete the run "
                                   f"on the platform and run again")
            continue
        if not grades:
            rep.warn("A1", where, "no grading lines yet (Criterion N: PASS/FAIL)")
            pending_current = True
        if any(v == "FAIL" for v in grades.values()):
            fails_on_current = True
    if graded_any and not fails_on_current and not pending_current and not escape:
        rep.error("A1", "runs/", "no current run fails a criterion: harden the task (workflow, Stage 7) or record "
                                 "the escape hatch")


# ================================================================ the run

MANUAL_ROWS = [
    ("D2-D9", "a colleague could do it unaided; one defensible answer; a judgment call no file states; both files "
              "needed; a decision that carries downstream; severe if wrong"),
    ("I2", "every fact needed is in the files; nothing depends on a lookup"),
    ("I4", "each planted issue is one the correct answer resolves"),
    ("I6, I7", "files state facts, not conclusions; cross-references only where a real document has them"),
    ("I9", "names, dates, amounts and reference numbers agree across both files, except the planted issue"),
    ("P9, P11", "reads as a handoff to a trusted colleague; nothing an agent would ask about"),
    ("M5-M7", "serial comma; complete sentences; spelling and grammar"),
    ("T3, T16", "no idiom standing in for a quantity; the same quantity keeps the same noun"),
    ("R4, R10, R11", "each criterion has one reading; every material point covered; every value checked twice"),
    ("A7", "the failure description says why the deliverable is unusable"),
]


def print_report(rep, title):
    print(f"== {title} ==")
    order = {"ERROR": 0, "WARN": 1, "NOTE": 2}
    items = sorted(rep.items, key=lambda x: order[x[0]])
    if not items:
        print("  coded checks clean")
    for level, code, where, msg in items:
        print(f"  {level:5s} [{code}] {where}: {msg}")


def check_folder(folder, only=None, full=False):
    rep = Report()
    fams = {only} if only else {"prompt", "inputs", "zip", "rubric", "failure", "runs"}
    p = folder / "prompt.md"
    if "prompt" in fams:
        if p.exists():
            check_prompt(p.read_text(encoding="utf-8"), rep)
        else:
            rep.error("P1", "prompt.md", "missing")
    names = []
    if "inputs" in fams:
        names = [f.name for f in check_inputs(folder, rep)]
    elif (folder / "inputs").is_dir():
        names = [f.name for f in (folder / "inputs").iterdir() if f.is_file() and not f.name.startswith(".")]
    if "zip" in fams:
        check_zip(folder, rep)
    n_crit = None
    r = folder / "rubric.md"
    if "rubric" in fams:
        if r.exists():
            n_crit = check_rubric(r.read_text(encoding="utf-8"), rep, full=full)
        else:
            rep.warn("R1", "rubric.md", "missing")
    elif r.exists():
        n_crit = len(parse_rubric(r.read_text(encoding="utf-8")))
    if "failure" in fams:
        t = folder / "task.md"
        body = extract_section(t.read_text(encoding="utf-8"), "Failure description") if t.exists() else None
        check_failure(body or "", rep, n_crit, names)
    if "runs" in fams:
        check_runs(folder, rep)
    return rep


def task_dirs():
    if not TASKS.is_dir():
        return []
    return sorted(d for d in TASKS.iterdir() if d.is_dir() and re.match(r"\d{2}-", d.name))


def list_tasks():
    rows = task_dirs()
    if not rows:
        print("no tasks yet; next is 01")
        return 0
    print(f"{'task':34s} {'status':26s} prompt  inputs  rubric  runs  latest")
    for d in rows:
        t = d / "task.md"
        status = ""
        if t.exists():
            m = re.search(r"^\*\*Status:\*\*\s*(.*)$", t.read_text(encoding="utf-8"), re.M)
            status = strip_comments(m.group(1)).strip() if m else ""
        p = d / "prompt.md"
        pw = len(words(strip_comments(p.read_text(encoding="utf-8")))) if p.exists() else 0
        ni = len([f for f in (d / "inputs").iterdir() if f.is_file() and not f.name.startswith(".")]) \
            if (d / "inputs").is_dir() else 0
        r = d / "rubric.md"
        nc = len(parse_rubric(r.read_text(encoding="utf-8"))) if r.exists() else 0
        runs = run_files(d)
        latest = ""
        if runs:
            fp, g = read_run(runs[-1])
            stale = " stale" if fp and fp != fingerprint(d)[:len(fp)] else ""
            latest = f"{sum(v == 'FAIL' for v in g.values())} fail / {len(g)}{stale}"
        print(f"{d.name:34s} {clip(status, 26):26s} {pw:5d}w  {ni:6d}  {nc:6d}  {len(runs):4d}  {latest}")
    return 0


def next_number():
    nums = [int(d.name[:2]) for d in task_dirs()]
    return f"{(max(nums) + 1 if nums else 1):02d}"


# ================================================================ self-test

SELFTEST_PROMPT = {
    "P1": "Build the covenant test workbook for Harlow Fabrication from the attached files.",
    "P2": "Build it. Send it.",
    "P3": "The Q3 covenant numbers for Harlow came in this morning. Tell me whether they breach the facility.",
    "P4": "You are a credit analyst at a regional bank. Build the covenant workbook for Harlow from these files.",
    "P5": "Hi Dana,\nThe Q3 numbers for Harlow are in the files. Please build the covenant workbook from them.\nThanks,",
    "P6": ("Harlow sent Q3 numbers. They look fine to me. The lender wants a workbook.\n\nThe credit agreement is "
           "attached. It has the definitions.\n\nBuild the covenant workbook from both files."),
    "P7": "Build the covenant workbook for Harlow. First compute EBITDA, then the leverage ratio, then the coverage.",
    "P8": ("Build the covenant workbook for Harlow from the two files. Be careful, the March amendment may be "
           "outdated."),
    "P9": "Build the covenant workbook for Harlow from the two files. Let me know if you have any questions.",
    "P10": "Build the covenant workbook for Harlow. Look up the current SOFR rate and apply it to the term loan.",
    "P12": "Build the covenant workbook for Harlow. The rubric checks the leverage figure.",
    "M1": f"Build the covenant workbook for Harlow {EM_DASH} the Q3 file is attached. Send it by Friday.",
    "T1": "Build the covenant workbook for Harlow. A breach is a breach, whatever the CFO says on the call.",
    "P13": ("Harlow's package is attached. covenant_q3.xlsx has the quarterly EBITDA build and lender_thread.docx "
            "holds the amendment. Build the covenant workbook and a memo for the committee."),
}
SELFTEST_PROSE = {
    "M2": "The borrower sent the package last week and the lender meets on Friday morning.",
    "M3": "The borrower sent the package, so I read it on the train, and the lender meets on Friday.",
    "M4": "The note was signed in February, it accrues 6 percent simple interest.",
    "T2": "At the end of the day the lender decides what the covenant means.",
    "T4": "This is not just a pricing question but a governance question.",
    "T5": "It's not the margin, it's the add-back schedule.",
    "T6": "The amendment serves as the basis for the new definition.",
    "T7": "Great question, happy to help with the covenant.",
    "T8": "There are three key considerations before we sign.",
    "T9": "It is worth noting that the margin is thin.",
    "T10": "We should leverage the existing data for a robust view.",
    "T11": "It should show the ratio. It should list the add-backs. It should recommend a waiver. It should state the risk.",
    "T12": ("- Check the ratio now\n- Read the fee table\n- List the top risks\n- Price the term loan\n"
            "- Call the lender back\n- Send the memo out"),
    "T13": "A fee the client hears about is a policy; a fee they find on a statement is an insult.",
    "T14": "Word travels. The lender called twice this morning about the covenant.",
    "T15": "Risks, exposures, and vulnerabilities. Clear, concise, and actionable. Fast, cheap, and good.",
    "T17": "Send me what goes on the board before the meeting starts on Thursday.",
}
SELFTEST_RUBRIC = {
    "R1": "1. The workbook reports a Q3 leverage ratio of 3.42x.",
    "R2": ("1. The workbook reports a Q3 leverage ratio of 3.42x; it flags the covenant as breached.\n"
           "2. The memo names Harlow Fabrication as the borrower and recommends a waiver request.\n"
           "3. The memo excludes the $412,600 legal settlement from EBITDA add-backs.\n"
           "4. The workbook uses total funded debt of $18,940,000 at September 30, 2026.\n"
           "5. The memo states that the March 2026 amendment governs the add-back cap."),
    "R3": ("1. The workbook is complete and done.\n2. The memo reports leverage of 3.42x.\n"
           "3. The memo excludes the $412,600 settlement.\n4. The workbook uses debt of $18,940,000.\n"
           "5. The memo states the March 2026 amendment governs."),
    "R5": ("1. The workbook reports leverage of 3.42x in cell C14 of the summary.\n2. The memo reports leverage of "
           "3.42x.\n3. The memo excludes the $412,600 settlement.\n4. The workbook uses debt of $18,940,000.\n"
           "5. The memo states the March 2026 amendment governs."),
    "R6": ("1. The response should report leverage of 3.42x for Q3 2026.\n2. The memo reports coverage of 1.18x.\n"
           "3. The memo excludes the $412,600 settlement.\n4. The workbook uses debt of $18,940,000.\n"
           "5. The memo states the March 2026 amendment governs."),
    "R7": ("1. The memo uses the appropriate leverage definition for Q3 2026.\n2. The memo reports coverage of 1.18x.\n"
           "3. The memo excludes the $412,600 settlement.\n4. The workbook uses debt of $18,940,000.\n"
           "5. The memo states the March 2026 amendment governs."),
    "R8": ("1. The model will fail to exclude the $412,600 settlement.\n2. The memo reports coverage of 1.18x.\n"
           "3. The memo reports leverage of 3.42x.\n4. The workbook uses debt of $18,940,000.\n"
           "5. The memo states the March 2026 amendment governs."),
    "R9": ("1. The memo uses bold headings and a consistent font for Q3 2026.\n2. The memo reports coverage of 1.18x.\n"
           "3. The memo excludes the $412,600 settlement.\n4. The workbook uses debt of $18,940,000.\n"
           "5. The memo states the March 2026 amendment governs."),
    "R12": ("1. The memo reports the leverage ratio shown in the gold standard answer.\n2. The memo reports coverage "
            "of 1.18x.\n3. The memo excludes the $412,600 settlement.\n4. The workbook uses debt of $18,940,000.\n"
            "5. The memo states the March 2026 amendment governs."),
    "R14": ("1. The memo reports leverage of 3.42x; award partial credit for 3.4x.\n2. The memo reports coverage of "
            "1.18x.\n3. The memo excludes the $412,600 settlement.\n4. The workbook uses debt of $18,940,000.\n"
            "5. The memo states the March 2026 amendment governs."),
    "R13": ("1. The memo reports a Q3 2026 leverage ratio of 3.42x.\n2. The memo reports the Q3 2026 leverage ratio "
            "of 3.42x.\n3. The memo excludes the $412,600 settlement.\n4. The workbook uses debt of $18,940,000.\n"
            "5. The memo states the March 2026 amendment governs."),
}
SELFTEST_FAILURE = {
    "A2": ("The agent refused the task and asked a clarifying question about criterion 2 instead of building the "
           "workbook from covenant_package_q3.xlsx, so nothing was produced for the lender by the deadline that "
           "Friday, and the 3.42x figure never appeared anywhere in the response or its files."),
    "A4": "The agent missed the add-back cap in criterion 3, using $412,600.",
    "A5": ("The agent added back the full legal settlement from covenant_package_q3.xlsx and reported leverage of "
           "2.97x. The March amendment in the lender email caps one-time add-backs at $250,000, which gives 3.42x "
           "and a breach of the 3.25x maximum. The memo told the lender the borrower was in compliance."),
    "A6": ("The agent added back the full legal settlement and reported leverage below the maximum. The amendment "
           "caps one-time add-backs, which gives a breach. Criterion 3 and criterion 1 capture it. The memo told the "
           "lender the borrower was in compliance, which is the opposite of the right call."),
}

CLEAN_PROMPT = ("Harlow Fabrication's Q3 compliance package came in this morning, and the bank's credit committee "
                "meets Thursday to decide whether to grant the waiver it asked for in August. Using the package and "
                "the lender email thread, build me a covenant test workbook for Q3 2026 and a one-page memo to the "
                "committee saying whether Harlow is in breach and what we should do about the waiver.")
CLEAN_RUBRIC = """1. The memo reports a Q3 2026 total leverage ratio of 3.42x for Harlow Fabrication.
2. The workbook excludes $162,600 of the $412,600 legal settlement from the EBITDA add-backs.
3. The memo concludes that Harlow is in breach of the 3.25x maximum leverage covenant.
4. The memo recommends that the committee decline the waiver as requested in August.
5. The workbook reports a Q3 2026 fixed charge coverage ratio of 1.18x.
"""
CLEAN_FAILURE = ("The agent added back the whole $412,600 legal settlement from covenant_package_q3.csv and reported "
                 "total leverage of 2.97x, so the memo told the committee that Harlow was in compliance. The March "
                 "2026 amendment in the lender email thread caps one-time add-backs at $250,000, which gives 3.42x "
                 "against the 3.25x maximum and a breach. Criteria 1 and 3 capture the error. A committee acting on "
                 "the memo would grant a waiver for a borrower that is already in default.")
CLEAN_CSV = """Line item,Q1 2026,Q2 2026,Q3 2026
Net income,"1,214,380","1,187,925","1,096,412"
Interest expense,"402,118","409,770","417,305"
Income tax,"318,642","301,207","276,931"
Depreciation and amortization,"611,904","618,233","624,517"
Total EBITDA before add-backs,"2,547,044","2,517,135","2,415,165"
Legal settlement (one-time),0,0,"412,600"
"""
CLEAN_EMAIL = """From: Renata Okafor
Sent: Tuesday, October 6, 2026 9:14 AM
Subject: Harlow Fabrication: Q3 package and the March amendment

Dana, the Q3 package from Harlow is attached. Their controller added back the full legal settlement from the
supplier dispute in calculating EBITDA for the quarter.

For reference, the March 2026 amendment to the credit agreement caps one-time add-backs at $250,000 in any
fiscal quarter, and the maximum total leverage ratio stays at 3.25x through the end of 2026. The fixed charge
coverage minimum remains 1.15x. Total funded debt at September 30 was $18,940,000 according to the borrowing
base certificate they sent with the package.

Harlow asked in August for a waiver of the leverage covenant for Q3 and Q4. Their CFO has already called twice
about where the request stands, and I told him we would have an answer after the committee meets Thursday. I
have not promised him anything beyond that. If you need the August covenant certificate or the borrowing base
detail behind the debt figure, Marcus in loan servicing has both and can send them over this afternoon. The
package came in two days after the date the agreement requires, which I would like noted in the file.

Renata Okafor
Vice President, Commercial Banking
Westfield Valley Bank
"""


def _docx_bytes(body_xml, comments=False):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        z.writestr("[Content_Types].xml", "<Types/>")
        z.writestr("word/document.xml",
                   '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body>'
                   + body_xml + "</w:body></w:document>")
        if comments:
            z.writestr("word/comments.xml", "<w:comments/>")
        z.writestr("docProps/app.xml", "<Properties><Application>python-docx</Application></Properties>")
    return buf.getvalue()


def _xlsx_bytes(rows, hidden=False):
    def cell(r, c, v):
        ref = chr(65 + c) + str(r + 1)
        if isinstance(v, (int, float)):
            return f'<c r="{ref}"><v>{v}</v></c>'
        return f'<c r="{ref}" t="inlineStr"><is><t>{v}</t></is></c>'
    sheet = "".join(f'<row r="{i + 1}">' + "".join(cell(i, j, v) for j, v in enumerate(r)) + "</row>"
                    for i, r in enumerate(rows))
    ns = 'xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" ' \
         'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"'
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        z.writestr("xl/workbook.xml",
                   f'<workbook {ns}><sheets><sheet name="Q3" sheetId="1" r:id="rId1"/>'
                   + ('<sheet name="Old" sheetId="2" state="hidden" r:id="rId2"/>' if hidden else "")
                   + "</sheets></workbook>")
        z.writestr("xl/_rels/workbook.xml.rels",
                   '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                   '<Relationship Id="rId1" Target="worksheets/sheet1.xml"/>'
                   '<Relationship Id="rId2" Target="worksheets/sheet2.xml"/></Relationships>')
        z.writestr("xl/worksheets/sheet1.xml", f"<worksheet {ns}><sheetData>{sheet}</sheetData></worksheet>")
        z.writestr("xl/worksheets/sheet2.xml", f"<worksheet {ns}><sheetData></sheetData></worksheet>")
    return buf.getvalue()


def _make_task(root, csv_text=CLEAN_CSV, email=CLEAN_EMAIL, extra=None, prompt=CLEAN_PROMPT, rubric=CLEAN_RUBRIC,
               failure=CLEAN_FAILURE, run_grades=("PASS", "PASS", "FAIL", "PASS", "PASS"), fp=None, zip_it=True):
    d = Path(root)
    (d / "inputs").mkdir(parents=True)
    (d / "inputs" / "covenant_package_q3.csv").write_text(csv_text, encoding="utf-8")
    if email is not None:
        (d / "inputs" / "RE Harlow Q3 package.md").write_text(email, encoding="utf-8")
    for name, data in (extra or {}).items():
        (d / "inputs" / name).write_bytes(data if isinstance(data, bytes) else data.encode())
    (d / "prompt.md").write_text(prompt, encoding="utf-8")
    (d / "rubric.md").write_text(rubric, encoding="utf-8")
    (d / "task.md").write_text(f"# test\n\n## Step 13: Failure description\n\n{failure}\n\n## Log\n", encoding="utf-8")
    if zip_it:
        build_zip(d)
    if run_grades is not None:
        (d / "runs").mkdir()
        lines = "\n".join(f"Criterion {i + 1}: {g}" for i, g in enumerate(run_grades))
        (d / "runs" / "run-1.md").write_text(f"# Run 1\n\nFingerprint: {fp or fingerprint(d)}\n\n{lines}\n",
                                             encoding="utf-8")
    return d


def selftest():
    bad = 0

    def expect(code, rep, label):
        nonlocal bad
        if code not in rep.codes():
            bad += 1
            got = sorted(rep.codes()) or "nothing"
            print(f"  FAIL {label}: {code} did not fire (got {got})")

    def silent(rep, label):
        nonlocal bad
        noisy = [i for i in rep.items if i[0] != "NOTE"]
        if noisy:
            bad += 1
            print(f"  FAIL {label} is not silent:")
            for level, code, where, msg in noisy:
                print(f"    {level} [{code}] {where}: {msg}")

    for code, s in SELFTEST_PROMPT.items():
        rep = Report()
        check_prompt(s, rep)
        expect(code, rep, f"prompt fixture {code}")
    for code, s in SELFTEST_PROSE.items():
        rep = Report()
        prose_checks(s, rep, "fixture")
        expect(code, rep, f"prose fixture {code}")
    for code, s in SELFTEST_RUBRIC.items():
        rep = Report()
        check_rubric(s, rep)
        expect(code, rep, f"rubric fixture {code}")
    names = ["covenant_package_q3.csv", "RE Harlow Q3 package.md"]
    for code, s in SELFTEST_FAILURE.items():
        rep = Report()
        check_failure(s, rep, n_crit=2 if code == "A5" else 5, input_names=names)
        expect(code, rep, f"failure fixture {code}")
    rep = Report()
    check_failure(SELFTEST_FAILURE["A5"].replace("The memo", "Criterion 7 captures it. The memo"), rep, 5, names)
    expect("A5", rep, "failure fixture A5 out of range")
    rep = Report()
    check_failure((CLEAN_FAILURE + " ") * 5, rep, 5, names)
    expect("A4", rep, "failure fixture A4 over 350 words")

    rep = Report()
    check_prompt(CLEAN_PROMPT, rep)
    silent(rep, "clean prompt")
    rep = Report()
    check_rubric(CLEAN_RUBRIC, rep)
    silent(rep, "clean rubric")
    rep = Report()
    check_failure(CLEAN_FAILURE, rep, 5, names)
    silent(rep, "clean failure description")

    with tempfile.TemporaryDirectory() as tmp:
        d = _make_task(Path(tmp) / "01-clean")
        silent(check_folder(d), "clean task folder")

        dirty_email = (CLEAN_EMAIL.replace("Tuesday, October 6", "Monday, October 6")
                       .replace("Valley Bank\n", "Valley Bank\n(312) 555-0147\nNote: the Q2 figure is outdated, do not use.\n"
                                            "Important: the correct figure is $250,000.\n"
                                            "Prepared for the rubric by Jane Doe at renata.okafor@gmail.com, "
                                            "cc dana@westfieldbank.example, "
                                            "ref 123-45-6789, rate 0.30000000000000004.\n"))
        dirty_csv = CLEAN_CSV.replace('"2,415,165"', '"2,515,165"')
        d = _make_task(Path(tmp) / "02-dirty", csv_text=dirty_csv, email=dirty_email, zip_it=False)
        rep = check_folder(d)
        for code in ("I5", "I8", "I10", "I11", "T18", "I14"):
            expect(code, rep, f"dirty inputs {code}")

        d = _make_task(Path(tmp) / "03-three", extra={"data_file.csv": "a,b\n1,2\n"})
        rep = check_folder(d, only="inputs")
        expect("I1", rep, "three inputs I1")
        expect("I3", rep, "generic name I3")
        expect("I13", rep, "thin file I13")

        d = _make_task(Path(tmp) / "04-office", email=None, extra={
            "Harlow memo.docx": _docx_bytes('<w:p><w:ins><w:r><w:t>' + " ".join(["word"] * 70)
                                            + "</w:t></w:r></w:ins></w:p>", comments=True),
            "cov.xlsx": _xlsx_bytes([["Item", "Amount"]] + [[f"Line {i}", 1000 * (i + 1)] for i in range(9)],
                                    hidden=True)})
        rep = check_folder(d, only="inputs")
        expect("I12", rep, "office hidden content I12")
        expect("I11", rep, "no-variance column I11")
        expect("I1", rep, "office three files I1")

        d = _make_task(Path(tmp) / "05-stale", fp="0123456789abcdef")
        rep = check_folder(d, only="runs")
        expect("A3", rep, "stale run A3")
        expect("A1", rep, "stale run leaves A1")

        d = _make_task(Path(tmp) / "06-allpass", run_grades=("PASS",) * 5)
        rep = check_folder(d, only="runs")
        expect("A1", rep, "all-pass run A1")

        d = _make_task(Path(tmp) / "07-zip")
        with zipfile.ZipFile(d / "inputs.zip", "a") as z:
            z.writestr("__MACOSX/._x", "")
            z.writestr("extra.txt", "x")
        rep = check_folder(d, only="zip")
        expect("I14", rep, "bad zip I14")

    total = (len(SELFTEST_PROMPT) + len(SELFTEST_PROSE) + len(SELFTEST_RUBRIC) + len(SELFTEST_FAILURE))
    if bad:
        print(f"selftest: {bad} failure(s)")
        return 1
    print(f"selftest: {total} text fixtures and 7 folder fixtures fire; clean samples silent")
    return 0


# ================================================================ main

def main(argv):
    args = argv[1:]
    if not args:
        print(__doc__)
        return 2
    if args[0] == "--selftest":
        return selftest()
    if args[0] == "--list":
        return list_tasks()
    if args[0] == "--next":
        print(next_number())
        return 0
    if args[0] == "--prose":
        rc = 0
        for f in args[1:]:
            rep = Report()
            prose_checks(Path(f).read_text(encoding="utf-8"), rep, f)
            print_report(rep, f)
            rc |= rep.has_error()
        return rc
    full = "--full" in args
    only = None
    if "--only" in args:
        i = args.index("--only")
        if i + 1 >= len(args):
            print(__doc__)
            return 2
        only = args[i + 1]
        if only not in {"prompt", "inputs", "zip", "rubric", "failure", "runs"}:
            print(f"unknown family {only}")
            return 2
    target = Path(next(a for a in args if not a.startswith("--") and a != only))
    if target.is_file():
        rep = Report()
        check_prompt(target.read_text(encoding="utf-8"), rep, str(target))
        print_report(rep, str(target))
        return 1 if rep.has_error() else 0
    if not target.is_dir():
        print(f"no such task folder: {target}")
        return 2
    if "--fingerprint" in args:
        print(fingerprint(target))
        return 0
    if "--zip" in args:
        out = build_zip(target)
        print(f"built {out}")
        only = only or "zip"
    rep = check_folder(target, only=only, full=full)
    print_report(rep, f"{target}{' [' + only + ']' if only else ''}")
    if not only:
        print(f"  fingerprint {fingerprint(target)}")
        print("  MANUAL (read, then tick in task.md):")
        for code, row in MANUAL_ROWS:
            print(f"    [{code}] {row}")
    return 1 if rep.has_error() else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
