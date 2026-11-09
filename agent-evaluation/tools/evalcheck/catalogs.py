"""Regex catalogs for the A-code prose checks.

Each list below holds the patterns one check scans for, with the label a
finding carries. Patterns and labels live here so prose.py stays a set of
scorers and the catalog can be edited on its own. Each class is described in
docs/reference/prose/llm-prose-tells.md.

Docx paragraph text is read with zipfile (common.py), so nothing here needs
python-docx.
"""
import re

from .common import split_sentences

# A noun restated as itself. The adjacent-repeat form keeps it tight: it fires
# on restatement, not on ordinary predication.
_TAUTOLOGY_RES = [
    re.compile(r"\b(\w+(?:\s+\w+){0,2})\s+(?:is|are)\s+(?:still\s+|just\s+)?\1\b", re.I),
    re.compile(r"\b(?:is|are)\s+the\s+whole\s+story\b", re.I),
    re.compile(r"\b(\w+)\s+is\s+\1[.,]", re.I),
    # head noun restated as the predicate: "Committed work is committed",
    # "policy 6.3 is still policy" — the two the adjacent-repeat form misses.
    # gap stays on ONE line: crossing a paragraph break matches unrelated list
    # items ("...attached\\nCertificates are attached") rather than a restatement.
    re.compile(r"\b(\w{5,})\b(?:[\w.\-]|[^\S\n]){0,20}?[^\S\n]+(?:is|are)\s+"
               r"(?:still\s+|just\s+|always\s+)?\1\b", re.I),
]


# Ordinary English that the restatement patterns catch by accident.
_TAUTOLOGY_OK_RE = re.compile(r"\bwhich is which\b|\bwhat is what\b|\bwho is who\b", re.I)


_SLOGAN_RES = [
    (re.compile(r"\buse it or lose it\b", re.I), "slogan"),
    (re.compile(r"\bis where the (?:money|pain|trouble|problem)\s+(?:hurts?|is|lands?)\b", re.I), "slogan"),
    (re.compile(r"\bnobody (?:promises|tells|asks|wants)\b[^.]{0,40}\bnot (?:coming|there|going)\b", re.I), "slogan"),
    (re.compile(r"\bwhere we are naked\b|\bknowing where we (?:stand|are) naked\b", re.I), "idiom for a quantity"),
    (re.compile(r"\bnot quietly (?:dropped|buried|lost)\b", re.I), "idiom for a quantity"),
    (re.compile(r"\bleave (?:them|it) and (?:they|it) (?:are|is) gone\b", re.I), "slogan"),
    (re.compile(r"\bI pulled the rest\b|\bI went and pulled\b", re.I), "first-person filler"),
    (re.compile(r"\bthe rest of it has to follow\b", re.I), "first-person filler"),
    (re.compile(r"\bhas to show as short\b|\bgoes short has to show\b", re.I), "slogan"),
    (re.compile(r"\btrying too hard\b", re.I), "slogan"),
    (re.compile(r"\bthat is close enough for (?:this|now|me)\b", re.I), "slogan"),
    (re.compile(r"\bis not (?:supply|going to happen|coming back)\.", re.I), "slogan"),
    (re.compile(r"\bwhat (?:we|they) leave on the counter\b", re.I), "idiom for a quantity"),
    (re.compile(r"\bthe one people forget\b|\bthe one thing everybody forgets\b", re.I), "slogan"),
    (re.compile(r"\bI am not spending my (?:fall|spring|summer|winter|year)\b", re.I), "slogan"),
    (re.compile(r"\bwould be buying it twice\b|\bpaying for it twice\b", re.I), "slogan"),
    # Three further classes: the semicolon-balanced maxim, the scene-setting fragment
    # and urgency performed through an image. The reviewer standard behind them is
    # "nobody with a truly urgent issue speaks in less-than-clear language". Catalog:
    # docs/reference/prose/llm-prose-tells.md, classes 8-10.
    (re.compile(r"\bis (?:a|an) \w+;[^.;\n]{0,80}\bis (?:a|an) \w+\b", re.I),
     "aphoristic parallelism (semicolon-balanced maxim)"),
    (re.compile(r"\b(?:was|were) (?:old|new) when \w+ (?:was|were) (?:cheap|young|new|easy)\b", re.I),
     "idiom for a quantity"),
    (re.compile(r"\bbefore the pencil comes out\b|\bWord travels\.", re.I), "scene-setting fragment"),
    (re.compile(r"\bgoing to stay \w+ until\b", re.I), "idiom for a quantity"),
    (re.compile(r"\bstand at (?:a|the) counter and defend\b", re.I), "idiom for a quantity"),
    (re.compile(r"\bhonestly,? that is fine with me\b", re.I), "first-person filler"),
    (re.compile(r"\bmeets? (?:it |them )?cold on a\b|\bmeet cold on\b", re.I), "idiom for a quantity"),
    # Two classes under the reviewer heading "Remove unclear LLM slang": a physical
    # surface standing in for the deliverable ("that is what goes on the door", meaning
    # the posted list), and an adverb-led opener whose clause break is unpunctuated so
    # the sentence reads as a fragment ("Read quickly that is the clean end of the
    # account"). Catalog: docs/reference/prose/llm-prose-tells.md, class 11.
    (re.compile(r"\b(?:read|taken|seen|viewed|looked at|put) "
                r"(?:quickly|fast|alone|together|straight|in isolation|side by side) "
                r"that (?:is|was)\b", re.I),
     "unpunctuated clause break reading as a fragment"),
    # Three phrase shapes from the reviewer-side "signs of LLM use" checklist
    # (docs/reference/prose/reviewer-checklist.md). The looser "not X, but Y" form is
    # ordinary correspondence and stays a read. Catalog:
    # docs/reference/prose/llm-prose-tells.md, class 12.
    (re.compile(r"\bnot (?:just|only|simply|merely)\b[^.;?!\n]{1,80}\bbut(?: also| rather)?\b", re.I),
     "negative parallelism (not only X but Y)"),
    (re.compile(r"\b(?:it|this)(?:'s|’s| is) not (?:just |only |simply |merely |about )?[^,.;\n]{1,50},\s*"
                r"(?:it|this)(?:'s|’s| is)\b", re.I),
     "\"it's not X, it's Y\" contrast"),
    (re.compile(r"\b(?:serves?|stands?) as\b|\bboasts?\b|\bshowcases?\b", re.I),
     "a simple verb avoided (serves as / stands as / boasts)"),
]


# The platform's authorship read names three more classes: pre-counted lists, "the
# sections that follow" roadmaps, and self-describing titles. These are scanned over
# every string, not only prose-length passages, because a self-describing title is
# short.
_SELF_DESCRIBING_RES = [
    (re.compile(r"\bgolden[\s_-]*solution\b", re.I), "self-describing title"),
    (re.compile(r"\b(?:ai|llm|model)[\s-]*(?:generated|output|response|answer)\b", re.I), "self-describing title"),
    (re.compile(r"\bas requested,? (?:this|the) (?:workbook|document|memo|report|file|deliverable)\b", re.I),
     "self-describing sentence"),
    (re.compile(r"\bthis (?:workbook|document|memo|report|deliverable|analysis) (?:provides|presents|"
                r"summari[sz]es|outlines|contains|is organi[sz]ed|walks through)\b", re.I),
     "self-describing sentence"),
    (re.compile(r"\bthe (?:sections?|pages?|paragraphs?) (?:that follow|below)\b|\bthe following (?:sections?|pages?)\b"
                r"|\bthe remainder of this (?:document|memo|report|workbook)\b", re.I), "roadmap sentence"),
    (re.compile(r"\bthere are (?:two|three|four|five|six|seven|eight|nine|ten|\d+) (?:key |main |primary |major )?"
                r"(?:considerations|factors|drivers|reasons|issues|points|takeaways|findings|steps)\b", re.I),
     "pre-counted list"),
    (re.compile(r"\b(?:two|three|four|five|six|seven|eight|nine|ten|\d+) key (?:considerations|factors|drivers|"
                r"reasons|issues|points|takeaways|findings)\b", re.I), "pre-counted list"),
]


# Scanned over every string, like _SELF_DESCRIBING_RES and for the same reason: the
# metonymy can sit in a heading, far below the prose-length threshold the slogan list
# works over. The "what goes on the X" framing is required: it is the subjectless
# relative that makes the surface stand in for the document. A declarative with a real
# subject ("the notice goes on the noticeboard") is literal and stays silent.
_SHORT_IDIOM_RES = [
    (re.compile(r"\b(?:what|that is what|which is what|this is what) goes (?:up )?on the "
                r"(?:door|wall|board|fridge)\b", re.I),
     "place metonymy for the deliverable"),
]


# Reviewer checklist line "Sycophantic language - overly agreeable, validating, or
# enthusiastic wording". Scanned over every string because the phrase is short and sits
# where a model answers the requester (a memo opener, a cover note). "Thank you for your
# order" and "you are right" are ordinary correspondence and stay off the list.
_SYCOPHANTIC_RES = [
    (re.compile(r"\bgreat question\b|\bexcellent (?:point|question)\b|\bhappy to help\b"
                r"|\bI(?:'d|’d| would) be happy to\b|\byou(?:'re|’re| are) absolutely right\b"
                r"|\babsolutely!|\bcertainly!|\bgreat choice\b|\bthank you so much\b", re.I),
     "sycophantic phrasing"),
]


# ---- A20 constants and helpers ----
# The serial comma in lists is the third rule the reviewer named and is a read, not a check.
_A20_PRON = r"(?:I|we|they|he|she|it|you|there|nobody|neither|none|everyone|everybody|nothing)"
_A20_DET = r"(?:the|our|my|a|an|this|that|these|those|his|her|their|its|each|every|no|both|all|one)"
# auxiliaries, modals and verbs that are rarely nouns; noun-ambiguous forms (charge, order,
# record, list, plan, cost, run, sign, ...) are left out on purpose - precision over recall
_A20_VERB = (
    r"(?:is|are|was|were|has|have|had|will|can|cannot|could|would|should|may|might|must|does|do|did|"
    r"goes|comes|came|went|needs|gets|got|takes|took|becomes|became|stays|remains|seems|means|says|said|"
    r"tells|told|knows|knew|wants|expects|thinks|thought|agrees|agreed|belongs|owes|arrives|expires|lapses|"
    r"starts|begins|began|fell|rises|rose|crosses|passes|reaches|reached|fails|puts|ran|keeps|kept|makes|made|"
    r"wrote|bought|sold|owns|wore|broke|carries|pays|paid|sends|sent|sees|saw|left|"
    r"stood|asked|includes|excludes|allows|requires|applies|renews|"
    r"picked|crossed|failed|tripped|landed|moved|stayed|covered|"
    r"needed|wanted|asked|caught|lost|found|sat|held|ended|started|closed|opened)")
_A20_SUBJECT = (rf"(?:{_A20_PRON}|{_A20_DET} \w+(?:'s)?(?: \w+){{0,2}}|[A-Z][\w-]+(?: [A-Z][\w-]+)?)")
# a bare conjunction (no comma in front) that opens a new clause; "or" is left out because it
# joins alternatives far more often than clauses
_A20_BARE_RE = re.compile(rf"(?<![,;:])\s(and|but|so|yet)\s+(?!that\b|then\b|long as\b|far as\b|much as\b|on\b)"
                          rf"({_A20_SUBJECT})\s+(?:\w+\s+)?(?:{_A20_VERB})\b")
# a comma-and-conjunction join that opens a new clause (an Oxford-comma list item has no verb)
_A20_COMMA_RE = re.compile(rf",\s+(and|but|so|or|yet)\s+(?!that\b)({_A20_SUBJECT})\s+(?:\w+\s+)?(?:{_A20_VERB})\b")
# a semicolon that opens a new clause (a semicolon list item has no subject and verb)
_A20_SEMI_RE = re.compile(rf";\s+({_A20_SUBJECT})\s+(?:\w+\s+)?(?:{_A20_VERB})\b")
_A20_CAP = 6
# a compound subject ("Reggie and Curtis run", "you and Darrell can") or an all-caps list
# item ("FORKS or MAST_CHAINS takes") is not a clause join
_A20_COMPOUND_RE = re.compile(r"(?:^|\s)(?:[A-Z][\w-]*|you|I|we|me|us|him|her|them)$")


_A20_ANYVERB_RE = re.compile(rf"\b{_A20_VERB}\b")
_A20_SUBORD_RE = re.compile(r"\b(?:when|whenever|if|because|where|while|unless|until|after|before|although|though|since|"
                            r"whether|once|provided|which|who|whose|as long as|so that)\b", re.I)


def _a20_bare_hits(s):
    """Bare-conjunction clause joins, minus compound subjects: if the stretch back to the
    previous comma holds no verb yet ("Nine roof panels and a section of coping came off",
    "the covers and the tape are"), the conjunction is joining subjects, not clauses."""
    out = []
    for m in _A20_BARE_RE.finditer(s):
        before = s[:m.start()].rstrip()
        subj = m.group(2)
        if _A20_COMPOUND_RE.search(before) or subj.isupper():
            continue
        segment = re.split(r"[,;:]", before)[-1]
        if not _A20_ANYVERB_RE.search(segment):
            continue
        # "between the last passing test and this adjustment were" pairs objects, not clauses
        if re.search(r"\b(?:between|both|either|neither)\b", segment, re.I):
            continue
        # inside a subordinate clause ("when the vendors answer and the reconciliation has to
        # hold", "if the driver is willing to wait and a receiver is free") no comma is due
        if _A20_SUBORD_RE.search(segment):
            continue
        out.append(m)
    return out


def _a20_sentences(text):
    for line in text.split("\n"):
        line = line.strip()
        if not line or "|" in line or line.upper() == line:
            continue
        for s in split_sentences(line, capital=True):
            s = s.strip()
            if len(s.split()) >= 8:
                yield s


# ---- A21 constants ----
# A10 reads vocabulary sentence by sentence and never sees a document whose every sentence
# is the same status-report sentence. A21 measures that share.
_A21_TEMPLATE_RE = re.compile(
    r"\b(?:remain(?:s|ed)?|continues?|continued|(?:was|were|has been|have been) completed"
    r"|according to (?:established|standard|existing|approved)"
    r"|no [a-z -]+ (?:was|were|have been|has been|occurred|reported))\b", re.I)
_A21_MIN_SENTENCES = 20
_A21_SHARE = 0.5

# ---- A32 generic headings ----
# The reader keeps a list of the headings a model reaches for and reads two of them in one
# document as its outline. One alone is ordinary.
_A32_GENERIC = {"executive summary", "recommendations", "recommendation", "introduction", "overview", "background",
                "conclusion", "conclusions", "next steps", "key findings", "findings", "methodology", "summary",
                "analysis", "purpose", "objectives", "scope"}


# ---- A33 constants and the markdown bullet-run reader ----
# The reviewer checklist names "long, highly uniform bullet lists" beside the phrase tells.
# It is measurable: a run of six or more bullets whose word counts have a standard
# deviation of 1.5 or under.
_A33_MIN_RUN = 6
_A33_MAX_SD = 1.5
_A33_MD_BULLET_RE = re.compile(r"^(?:[-*•]|\d+[.)])\s+\S")

def _a33_md_runs(text):
    runs, run = [], []
    for line in text.split("\n"):
        s = line.strip()
        if _A33_MD_BULLET_RE.match(s):
            run.append(s)
        else:
            if run:
                runs.append(run)
            run = []
    if run:
        runs.append(run)
    return runs

