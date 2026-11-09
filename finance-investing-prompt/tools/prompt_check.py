#!/usr/bin/env python3
"""prompt_check.py: the coded self-check for a finance prompt, run before Generate.

    python3 tools/prompt_check.py drafts/NN-slug/prompt.md [more files]
    python3 tools/prompt_check.py --section Explanation drafts/NN-slug/task.md
    python3 tools/prompt_check.py --selftest

--section NAME checks the text under "## NAME" in a task file as prose rather than as a
prompt: the mechanics (M), prose tells (T), persona (F2) and stacked adjectives (S3) run; the
prompt-only checks (F6 topics, D7 length, S1 procedure, S5 round figures) are skipped, because
an explanation legitimately quotes figures and names what a model did wrong.

Reads each file. A bare prompt.md is checked whole. If the file has a "## Prompt" heading
(an older single-file draft), only the text under that heading up to the next "## " heading
is checked. Prints ERROR and WARN findings with the rule id from docs/prompt-rules.md,
then the MANUAL rows no regex can read. Exit status 1 when any ERROR is present.

Severity:
  ERROR  a defect the rules state flatly (em dash, persona opener, tautology, sycophancy).
  WARN   a heuristic hit that needs a read; keep it only with a reason noted in the task file.

Checks, by rule id:
  F2   persona opener                        T1   tautology
  F6   banned-topic keyword                  T2   known slogan phrases
  D7   length band (60 to 650 words)         T4   not just / not only ... but
  S1   numbered procedure, requirement stack T5   it's not X, it's Y
  S3   stacked quality adjectives            T6   serves as / stands as / boasts
  S5   round currency figures                T7   sycophancy
  M1   em dash                               T8   pre-counted list
  M2   missing comma before clause join      T9   hedging filler
  M3   three or more clauses in a sentence   T10  clinical vocabulary
  M4   comma splice                          T11  repeated sentence openers
                                             T12  uniform bullet run
                                             T13  semicolon maxim
                                             T14  short fragment opener
                                             T15  rule-of-three density

The grammar checks (M2, M3, M4) are heuristics tuned for precision over recall: they look for a
conjunction or comma followed by a recognisable subject and a verb from a fixed list. A clean
run is the floor, not the proof. Read the prompt aloud.

Adding a check: write the regex, give it a rule id that exists in docs/prompt-rules.md, add a
line to SELFTEST that must fire it, and keep CLEAN_SAMPLE silent.
"""
import re
import statistics
import sys
from pathlib import Path

EM_DASH = "—"

# ---------------------------------------------------------------- sentence helpers

_SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z\"'(])")


def sentences(text):
    out = []
    for para in re.split(r"\n\s*\n", text):
        for line in para.split("\n"):
            line = line.strip()
            if not line or line.startswith("#") or "|" in line:
                continue
            out.extend(s.strip() for s in _SENT_SPLIT.split(line) if s.strip())
    return out


def paragraphs(text):
    return [p for p in re.split(r"\n\s*\n", text) if p.strip()]


def words(text):
    return re.findall(r"[A-Za-z][A-Za-z'\-]*", text)


# ---------------------------------------------------------------- F: frame

PERSONA_RE = re.compile(
    r"\bYou are (?:a|an|the)\b"
    r"|\bAs (?:a|an) [^,.\n]{0,50}, you\b"
    r"|\bYour task is to\b"
    r"|\bYou have been (?:asked|tasked|hired|engaged) to\b"
    r"|\b(?:utiliz|leverag)\w* your (?:expertise|experience|knowledge|skills)\b"
    r"|\bAct as (?:a|an)\b|\bAssume the role of\b", re.I)

BANNED_RE = re.compile(
    r"\b(?:election|ballot|candidate for president|war in|invasion|genocide|terroris\w*|conspiracy"
    r"|suicide|self-harm|eating disorder|anorexi\w*|sexual|rape|assault|abuse|shooting|murder"
    r"|cocaine|heroin|fentanyl|launder\w*|ponzi|embezzl\w*|insider trading|tax evasion|bribe\w*)\b",
    re.I)

# ---------------------------------------------------------------- S: specification

STEP_LINE_RE = re.compile(r"^\s*(?:\d+[.)]|\(\d+\))\s+\S", re.M)
INLINE_STEPS_RE = re.compile(r"\(1\)[^.\n]{1,120}\(2\)[^.\n]{1,120}\(3\)")
REQUIREMENT_RE = re.compile(
    r"\b(?:should (?:include|contain|cover|address|provide|list|show)|must (?:include|contain|cover|address|provide)"
    r"|make sure (?:to|that|it|you)|ensure (?:that|the|it|you)|be sure to|needs? to (?:include|contain|cover))\b", re.I)
REQUIREMENT_CAP = 3

QUALITY_ADJ = (r"(?:clear|concise|comprehensive|thorough|detailed|robust|rigorous|well-structured|well-reasoned"
               r"|well-organized|actionable|insightful|nuanced|in-depth|high-quality|holistic|structured|complete"
               r"|professional|polished|accurate|precise|balanced|objective|data-driven|evidence-based)")
STACKED_ADJ_RE = re.compile(rf"\b{QUALITY_ADJ},?\s+(?:and\s+|yet\s+|but\s+)?{QUALITY_ADJ}\b", re.I)
NEGATED_FAILURE_RE = re.compile(
    r",\s*(?:not|rather than|instead of)\s+(?:vague|generic|superficial|incomplete|shallow|rushed|boilerplate"
    r"|hand-wavy|high-level|simplistic|fluffy|wishy-washy)\b", re.I)

ROUND_MONEY_RE = re.compile(r"(?<![\d.])\$\s?\d{1,3}(?:,000){1,3}(?![\d,.])|\$\s?\d{1,3}\s?(?:million|billion|k|m|bn)\b(?!\.\d)", re.I)
ANY_MONEY_RE = re.compile(r"\$\s?\d[\d,]*(?:\.\d+)?\s?(?:million|billion|k|m|bn)?\b", re.I)
ROUND_MONEY_CAP = 3
ROUND_MONEY_MIN = 2       # fewer round figures than this is never flagged
ROUND_MONEY_SHARE = 0.75  # flagged only when round figures are most of the money figures

# ---------------------------------------------------------------- M: mechanics

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
        r"|pulls|pulled|built|writes|trades|lends|borrows|borrowed|owed|costs|steps|stepped|know|let|tell|send"
        r"|need|want|think|see|give|find|keep|make|get|take|put)")
SUBJECT = rf"(?:{PRON}|{DET} \w+(?:'s)?(?: \w+){{0,2}}|[A-Z][\w-]+(?: [A-Z][\w-]+)?)"

BARE_JOIN_RE = re.compile(
    rf"(?<![,;:])\s(and|but|so|yet)\s+(?!that\b|then\b|long as\b|far as\b|much as\b|on\b)"
    rf"({SUBJECT})\s+(?:\w+\s+)?{VERB}\b")
COMMA_JOIN_RE = re.compile(rf",\s+(and|but|so|or|yet)\s+(?!that\b)({SUBJECT})\s+(?:\w+\s+)?{VERB}\b")
SEMI_JOIN_RE = re.compile(rf";\s+({SUBJECT})\s+(?:\w+\s+)?{VERB}\b")
SPLICE_RE = re.compile(rf",\s+({PRON})\s+(?:\w+\s+)?{VERB}\b")
ANY_VERB_RE = re.compile(rf"\b{VERB}\b")
# true subordinators: inside such a clause a bare "and" joins no independent clauses
SUBORD_RE = re.compile(
    r"\b(?:when|whenever|if|because|where|while|unless|until|after|before|although|though|since|whether"
    r"|once|provided|which|who|whose|as long as|so that)\b", re.I)
# words that open an introductory phrase; a comma after such a phrase is not a splice
OPENER_WORDS = {
    "when", "whenever", "if", "because", "where", "while", "unless", "until", "after", "before", "although",
    "though", "since", "whether", "once", "provided", "given", "assuming", "considering", "based", "unlike",
    "like", "despite", "regardless", "according", "with", "without", "for", "to", "in", "on", "at", "by", "as",
    "from", "over", "under", "between", "during", "per", "absent", "barring", "yes", "no", "well", "also",
    "however", "otherwise", "meanwhile", "ideally", "frankly", "honestly", "first", "second", "third", "finally",
}
COMPOUND_SUBJ_RE = re.compile(r"(?:^|\s)(?:[A-Z][\w-]*|you|I|we|me|us|him|her|them)$")
CLAUSE_CAP = 6


def bare_join_hits(s):
    out = []
    for m in BARE_JOIN_RE.finditer(s):
        before = s[:m.start()].rstrip()
        if COMPOUND_SUBJ_RE.search(before) or m.group(2).isupper():
            continue
        segment = re.split(r"[,;:]", before)[-1]
        if not ANY_VERB_RE.search(segment):
            continue
        if SUBORD_RE.search(segment):
            continue
        out.append(m)
    return out


def splice_hits(s):
    out = []
    for m in SPLICE_RE.finditer(s):
        before = s[:m.start()]
        segment = re.split(r"[;:]", before)[-1].strip()
        if not segment:
            continue
        first = segment.split()[0].lower().strip('"\'(').rstrip(",")
        if first in OPENER_WORDS or first.endswith("ly"):
            continue
        if SUBORD_RE.search(segment):
            continue
        if not ANY_VERB_RE.search(segment):
            continue
        out.append(m)
    return out


# ---------------------------------------------------------------- T: prose tells

TAUTOLOGY_RES = [
    re.compile(r"\b(\w+(?:\s+\w+){0,2})\s+(?:is|are)\s+(?:still\s+|just\s+)?\1\b", re.I),
    re.compile(r"\b(?:is|are)\s+the\s+whole\s+story\b", re.I),
    re.compile(r"\b(\w{5,})\b(?:[\w.\-]|[^\S\n]){0,20}?[^\S\n]+(?:is|are)\s+(?:still\s+|just\s+|always\s+)?\1\b", re.I),
]
TAUTOLOGY_OK_RE = re.compile(r"\bwhich is which\b|\bwhat is what\b|\bwho is who\b|\bbusiness is business\b", re.I)

SLOGAN_RE = re.compile(
    r"\buse it or lose it\b|\bis where the (?:money|pain|trouble|problem)\s+(?:hurts?|is|lands?)\b"
    r"|\bat the end of the day\b|\bgame[- ]changer\b|\bmake or break\b|\bno-brainer\b|\bmov(?:e|ing) the needle\b"
    r"|\blow-hanging fruit\b|\bbleeding cash\b|\bwhere we are naked\b|\bnot quietly (?:dropped|buried|lost)\b"
    r"|\bskin in the game\b|\bthe elephant in the room\b|\bperfect storm\b", re.I)

NEG_PARALLEL_RE = re.compile(r"\bnot (?:just|only|simply|merely)\b[^.;?!\n]{1,80}\bbut(?: also| rather)?\b", re.I)
ITS_NOT_RE = re.compile(
    r"\b(?:it|this)(?:'s|’s| is) not (?:just |only |simply |merely |about )?[^,.;\n]{1,50},\s*(?:it|this)(?:'s|’s| is)\b", re.I)
SERVES_AS_RE = re.compile(r"\b(?:serves?|stands?) as\b|\bboasts?\b|\bshowcases?\b", re.I)
SYCOPHANCY_RE = re.compile(
    r"\bgreat question\b|\bexcellent (?:point|question)\b|\bhappy to help\b|\bI(?:'d|’d| would) be happy to\b"
    r"|\byou(?:'re|’re| are) absolutely right\b|\babsolutely!|\bcertainly!|\bgreat choice\b|\bthank you so much\b", re.I)
PRECOUNT_RE = re.compile(
    r"\bthere are (?:two|three|four|five|six|seven|\d+) (?:key |main |primary |major |critical )?"
    r"(?:considerations|factors|drivers|reasons|issues|points|takeaways|findings|steps|risks|questions)\b"
    r"|\b(?:two|three|four|five|six|seven|\d+) key (?:considerations|factors|drivers|reasons|issues|points|takeaways|findings|risks)\b", re.I)
HEDGE_RE = re.compile(
    r"\bit is worth noting\b|\bit(?:'s|’s| is) important to (?:note|consider|remember|understand)\b"
    r"|\bone could argue\b|\bthis may suggest\b|\bit should be noted\b|\bneedless to say\b", re.I)
CLINICAL_RE = re.compile(
    r"\butiliz\w+\b|\bleverag(?:e|ing) (?:the|our|your|existing|this|these|any)\b|\bcomprehensive\b|\brobust\b|\bholistic\b"
    r"|\bfacilitat\w+\b|\boptimi[sz]\w+\b|\bsynerg\w+\b|\bdelv(?:e|ing)\b|\bin order to\b|\bstakeholder alignment\b"
    r"|\bbest practices\b|\bactionable insights?\b|\bdeep dive\b", re.I)
CLINICAL_CAP = 5

SEMI_MAXIM_RE = re.compile(r"\bis (?:a|an) \w+;[^.;\n]{0,80}\bis (?:a|an) \w+\b", re.I)
SHORT_OPENER_RE = re.compile(r"^([A-Z][\w']*(?: [\w']+){0,2})[.!]\s+[A-Z]")
GREETING_RE = re.compile(r"^(?:hi|hello|hey|thanks|thank you|morning|afternoon|ok|okay|quick one|update|fyi)\b", re.I)
CONNECTIVE_RE = re.compile(r"^(?:finally|then|also|next|lastly|and|but|first|second|third|so),?\s+", re.I)
BULLET_RE = re.compile(r"^(?:[-*•]|\d+[.)])\s+\S")
BULLET_MIN_RUN = 6
BULLET_MAX_SD = 1.5
TRIPLE_RE = re.compile(r"\b[\w'-]+, [\w'-]+,? (?:and|or) [\w'-]+\b")
TRIPLE_PER_300 = 3

MIN_WORDS = 60
MAX_WORDS = 650

MANUAL_ROWS = [
    ("F1", "who is asking, for whom, and what decision it feeds are in the prompt, woven in"),
    ("F3", "reads as a person briefing a colleague or assistant; passed the read-aloud"),
    ("F4", "stakes are concrete: a decision, a deadline, an amount, a person waiting"),
    ("F5", "every person and company is fictional; no private facts about real people"),
    ("D1", "not answerable by recall; depends on the scenario's own facts"),
    ("D2", "the trap is in the facts: a conflicting figure, a wrong default, a convention confusion"),
    ("D3", "the facts can support the answer the requester does not want"),
    ("D5", "not a variation on an attempt already in drafts/"),
    ("D6", "complexity is the scenario's own; no constraints that exist only to trip the model"),
    ("D8", "one decisive question; whole task fits about three hours, prompt answerable in about an hour"),
    ("S2", "no pitfall warning and no derived parameter handed over as a given"),
    ("S4", "the output form, if it matters, is named once in plain words"),
    ("M5", "serial comma in every list of three or more"),
    ("M6", "complete sentences; no fragments as headings"),
    ("M7", "spelling and grammar clean"),
    ("T3", "no idiom standing in for a quantity"),
    ("T16", "the same quantity keeps the same noun"),
]


# ---------------------------------------------------------------- the run

PROMPT_ONLY = {"F6", "D7", "S1", "S5"}


def findings(text, prompt=True):
    out = []

    def err(code, msg):
        out.append(("ERROR", code, msg))

    def warn(code, msg):
        out.append(("WARN", code, msg))

    def clip(s, n=80):
        s = " ".join(s.split())
        return s if len(s) <= n else s[:n] + "..."

    sents = sentences(text)
    paras = paragraphs(text)
    n_words = len(words(text))

    # F2 persona
    m = PERSONA_RE.search(text)
    if m:
        err("F2", f'persona opener "{clip(m.group(0))}": open on the situation in the requester\'s voice')

    # F6 banned topics
    seen = set()
    for m in BANNED_RE.finditer(text):
        w = m.group(0).lower()
        if w not in seen:
            seen.add(w)
            warn("F6", f'"{w}" touches a topic the instructions ban or restrict; confirm it is not the subject')

    # D7 length
    if n_words < MIN_WORDS:
        warn("D7", f"{n_words} words: almost certainly a softball; the scenario needs facts to reason over")
    elif n_words > MAX_WORDS:
        warn("D7", f"{n_words} words: over the {MAX_WORDS}-word line; cut repetition and over-explanation")

    # S1 procedure
    steps = len(STEP_LINE_RE.findall(text))
    if steps >= 3 or INLINE_STEPS_RE.search(text):
        warn("S1", f"numbered procedure ({max(steps, 3)} steps): say what to produce, not how, unless these are scenario facts")
    reqs = REQUIREMENT_RE.findall(text)
    if len(reqs) >= REQUIREMENT_CAP:
        warn("S1", f'{len(reqs)} requirement phrases ("{clip(reqs[0], 30)}", ...): a requirement stack dictates the answer\'s shape')

    # S3 stacked adjectives
    m = STACKED_ADJ_RE.search(text)
    if m:
        warn("S3", f'quality-adjective pair "{clip(m.group(0))}": name the specific thing wanted instead')
    m = NEGATED_FAILURE_RE.search(text)
    if m:
        warn("S3", f'failures-avoided tail "{clip(m.group(0))}": the stacked-adjective pattern; delete it')

    # S5 round money
    hits = [m.group(0) for m in ROUND_MONEY_RE.finditer(text)]
    total = len(ANY_MONEY_RE.findall(text))
    if len(hits) >= ROUND_MONEY_MIN and total and len(hits) / total >= ROUND_MONEY_SHARE:
        shown = ", ".join(hits[:ROUND_MONEY_CAP])
        warn("S5", f"{len(hits)} of {total} money figures are round ({shown}): a person quotes one round number, working figures carry precision")

    # M1 em dash
    n_em = text.count(EM_DASH)
    if n_em:
        err("M1", f"{n_em} em dash(es): zero allowed; use a comma, colon, semicolon, parentheses or a new sentence")

    # M2, M3, M4 clause mechanics
    n_clause = 0
    for s in sents:
        if len(s.split()) < 8:
            continue
        bares = bare_join_hits(s)
        joins = len(COMMA_JOIN_RE.findall(s)) + len(SEMI_JOIN_RE.findall(s)) + len(bares)
        if bares and n_clause < CLAUSE_CAP:
            b = bares[0]
            warn("M2", f'no comma before "{b.group(1)}" where a new clause starts: "...{clip(s[max(0, b.start() - 30):b.end() + 20], 70)}..."')
            n_clause += 1
        elif joins >= 2 and n_clause < CLAUSE_CAP:
            warn("M3", f'{joins + 1} independent clauses in one sentence: "{clip(s)}"')
            n_clause += 1
        for sp in splice_hits(s)[:1]:
            if n_clause < CLAUSE_CAP:
                warn("M4", f'possible comma splice at ", {sp.group(1)} ...": "{clip(s)}"')
                n_clause += 1

    # T1 tautology
    for rx in TAUTOLOGY_RES:
        m = next((m for m in rx.finditer(text) if not TAUTOLOGY_OK_RE.search(m.group(0))), None)
        if m:
            err("T1", f'tautology "{clip(m.group(0), 60)}": state the rule and its consequence instead')
            break

    # T2 slogans
    for m in list(SLOGAN_RE.finditer(text))[:3]:
        warn("T2", f'slogan "{m.group(0)}": state the mechanism or the quantity')

    # T4, T5
    m = NEG_PARALLEL_RE.search(text)
    if m:
        warn("T4", f'negative parallelism "{clip(m.group(0))}": say the second half on its own')
    m = ITS_NOT_RE.search(text)
    if m:
        warn("T5", f'"it\'s not X, it\'s Y" contrast "{clip(m.group(0))}"')

    # T6
    m = SERVES_AS_RE.search(text)
    if m:
        warn("T6", f'"{m.group(0)}": use is, has or holds')

    # T7
    m = SYCOPHANCY_RE.search(text)
    if m:
        err("T7", f'sycophantic phrase "{m.group(0)}": a requester never writes this')

    # T8
    m = PRECOUNT_RE.search(text)
    if m:
        warn("T8", f'pre-counted list "{clip(m.group(0))}": make the points without counting them')

    # T9
    m = HEDGE_RE.search(text)
    if m:
        warn("T9", f'hedging filler "{m.group(0)}": delete the frame, keep the claim')

    # T10
    hits = []
    for m in CLINICAL_RE.finditer(text):
        w = m.group(0).lower()
        if w not in hits:
            hits.append(w)
    if hits:
        warn("T10", f"clinical vocabulary: {', '.join(hits[:CLINICAL_CAP])}; use the plain word")

    # T11 repeated openers
    for para in paras:
        ps = [s for s in _SENT_SPLIT.split(" ".join(para.split())) if s.strip()]
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

    # T12 uniform bullets
    run = []
    runs = []
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
                warn("T12", f"{len(r)} consecutive bullets of {min(lengths)} to {max(lengths)} words (sd {sd:.1f}): vary length and shape")
                break

    # T13 semicolon maxim
    m = SEMI_MAXIM_RE.search(text)
    if m:
        warn("T13", f'semicolon-balanced maxim "{clip(m.group(0))}": say the consequence once')

    # T14 short fragment openers
    for para in paras:
        first = " ".join(para.split())
        m = SHORT_OPENER_RE.match(first)
        if m and not GREETING_RE.match(m.group(1)):
            warn("T14", f'paragraph opens on a fragment "{m.group(1)}.": open on the subject, not the atmosphere')
            break

    # T15 rule-of-three density
    triples = TRIPLE_RE.findall(text)
    if n_words and len(triples) / max(n_words, 1) * 300 >= TRIPLE_PER_300 and len(triples) >= 3:
        warn("T15", f'{len(triples)} three-item lists in {n_words} words ("{clip(triples[0], 40)}", ...): keep lists of record, cut padding')

    if not prompt:
        out = [f for f in out if f[1] not in PROMPT_ONLY]
    return out


def extract_section(text, name):
    m = re.search(rf"^## {re.escape(name)}\s*$", text, re.M)
    if not m:
        return None
    rest = text[m.end():]
    nxt = re.search(r"^## ", rest, re.M)
    body = rest[:nxt.start()] if nxt else rest
    return re.sub(r"<!--.*?-->", "", body, flags=re.S).strip()


def extract_prompt(text):
    m = re.search(r"^## Prompt\s*$", text, re.M)
    if not m:
        return text
    rest = text[m.end():]
    nxt = re.search(r"^## ", rest, re.M)
    body = rest[:nxt.start()] if nxt else rest
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    return body.strip()


def run_file(path, section=None):
    raw = Path(path).read_text(encoding="utf-8", errors="ignore")
    if section:
        text = extract_section(raw, section)
        if text is None:
            print(f"== {path}: no '## {section}' section")
            return 1
        found = findings(text, prompt=False)
        print(f"== {path} [{section}] ({len(words(text))} words) ==")
    else:
        text = extract_prompt(raw)
        found = findings(text)
        print(f"== {path} ({len(words(text))} words) ==")
    errors = [f for f in found if f[0] == "ERROR"]
    warns = [f for f in found if f[0] == "WARN"]
    for level, code, msg in errors + warns:
        print(f"  {level:5s} [{code}] {msg}")
    if not found:
        print("  coded checks clean")
    if section:
        print("  MANUAL: read it aloud; every flaw named carries a figure or a quote; no hedging")
    else:
        print("  MANUAL (read, then tick in the task file):")
        for code, row in MANUAL_ROWS:
            print(f"    [{code}] {row}")
    return 1 if errors else 0


# ---------------------------------------------------------------- self-test

SELFTEST = {
    "F2": "You are a senior equity analyst with ten years of experience.",
    "F6": "The client was convicted of insider trading last year and wants a portfolio.",
    "D7": "Value this company please.",
    "S1": "Please do the following.\n1. Build a DCF.\n2. Run the trading comps.\n3. Write the memo.",
    "S3": "I need a clear, comprehensive analysis of the deal.",
    "S5": "Revenue was $1,000,000 last year and the raise is $5 million.",
    "M1": f"The model {EM_DASH} as expected {EM_DASH} shows growth.",
    "M2": "The founder sent the model last week and the board meets on Friday morning.",
    "M3": "The founder sent the model, so I read it on the plane, and the board meets on Friday.",
    "M4": "The note was signed in February, it accrues 6 percent simple interest.",
    "T1": "Committed capital is committed, whatever the LPs say now.",
    "T2": "At the end of the day the market decides what the company is worth.",
    "T4": "This is not just a valuation question but a governance question.",
    "T5": "It's not the price, it's the preference stack.",
    "T6": "The term sheet serves as the basis for the valuation.",
    "T7": "Great question, happy to help with the model.",
    "T8": "There are three key considerations before we sign.",
    "T9": "It is worth noting that the margin is thin.",
    "T10": "We should leverage the existing data for a comprehensive and robust view.",
    "T11": "It should show the IRR. It should list the fees. It should recommend a price. It should state the risks.",
    "T12": "- Check the IRR now\n- Read the fee table\n- List the top risks\n- Price the common stock\n- Call the lender back\n- Send the memo out",
    "T13": "A fee the client hears about is a policy; a fee they find on a statement is an insult.",
    "T14": "Word travels. The lender called twice this morning about the covenant.",
    "T15": "Risks, exposures, and vulnerabilities. Clear, concise, and actionable. Fast, cheap, and good.",
}

CLEAN_SAMPLE = """My partner wants to put another $385k into Haldane Precision before their Series A prices, and the founder sent over a model that shows them cash-flow positive by the third quarter of next year. Their last three quarters of actuals are pasted below. Revenue in the model grows 18 percent a quarter while headcount stays flat, and the gross margin steps from 41 percent to 58 percent in two quarters with no explanation in the notes.

The pre-money they are asking for is $22.6M on a post of $27.4M, and our existing note converts at a 20 percent discount with a $15M cap. The note was signed in February 2025 and accrues 6 percent simple interest.

Tell me what you make of the model, whether the pre-money holds up against the actuals, and what I should push back on before the call on Friday. If the honest answer is that we should not follow on, say so and tell me why."""


def selftest():
    bad = 0
    for code, sample in SELFTEST.items():
        got = {c for _, c, _ in findings(sample)}
        if code not in got:
            bad += 1
            print(f"  FAIL {code}: fixture did not fire (got {sorted(got) or 'nothing'})")
    clean = findings(CLEAN_SAMPLE)
    if clean:
        bad += 1
        print("  FAIL clean sample fired:")
        for level, code, msg in clean:
            print(f"    {level} [{code}] {msg}")
    if bad:
        print(f"selftest: {bad} failure(s)")
        return 1
    print(f"selftest: {len(SELFTEST)} fixtures fire, clean sample silent")
    return 0


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    if argv[1] == "--selftest":
        return selftest()
    args = argv[1:]
    section = None
    if "--section" in args:
        i = args.index("--section")
        if i + 1 >= len(args):
            print(__doc__)
            return 2
        section = args[i + 1]
        del args[i:i + 2]
    rc = 0
    for target in args:
        rc |= run_file(target, section)
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv))
