"""E-codes: the rationale, confidence note and ratings, against the platform's own rules.

This workspace checks an evaluation an author wrote about two deliverables. Every
rule below is quoted from docs/reference/evaluation-instructions.md, the
transcribed platform instructions, and the quote is in the finding so a
disagreement can be taken up with the source rather than with the tool.

E50 is the one worth running first: every money figure the rationale states has
to be findable in the files, because the platform's standard is "counting only
errors you verified in the files".
"""
import re

from .common import prose_only, split_sentences, word_count
from .core import check
from .task import DIMENSIONS, OVERALL, SCALE

RATIONALE_MIN_WORDS = 150
RATINGS = "evaluation/ratings.md"

# E06 leak window. Six words is short enough to catch a partial lift ("the
# decision should be approve the petition") and long enough that ordinary
# shared phrasing does not collide. A prompt and a reference solution
# legitimately cite the same authority, so citation-bearing windows are
# dropped: that is the one overlap which proves nothing.
_LEAK_N = 6
def _blockquote(text):
    """The prompt as recorded: the blockquote templates/prompt.md asks for, or,
    where a task recorded the prompt without one, the whole file."""
    quoted = [l.lstrip(">").strip() for l in text.split("\n") if l.lstrip().startswith(">")]
    return "\n".join(quoted) if quoted else text


def _below_rule(text):
    """The reference solution itself: everything below the first horizontal rule,
    which is where the template puts it, or the whole file where there is none."""
    parts = re.split(r"(?m)^-{3,}\s*$", text, maxsplit=1)
    return parts[1] if len(parts) == 2 else text


_LEAK_STOP = set("""a an and are as at be been but by for from had has have he her his i if in into is it
its me my no not of on or our she so that the their them there these this those to too us was we were
what when where which who will with would you your de ms mr mrs dr u s""".split())


def _names(text):
    """Tokens that appear capitalized away from a sentence start: party names,
    places, document titles. A prompt and its reference solution necessarily
    share these, so an overlap made only of them proves nothing."""
    out = set()
    for sent in split_sentences(text):
        for tok in re.findall(r"(?<![.!?]\s)\b([A-Z][a-zA-Z]+)", sent)[1:]:
            out.add(tok.lower())
    return out


def _informative(gram, names):
    """A shared window counts only if it carries at least two content words that
    are neither stopwords nor names. "is the example of a battery" counts;
    "vernon lloyd lattimore a u s" does not."""
    content = [w for w in gram.split() if w not in _LEAK_STOP and w not in names]
    return len(content) >= 2


_CITATION_RE = re.compile(
    r"\b(?:policy manual|volume \d|chapter \d|part [a-z]\b|section \d|"
    r"\d+ cfr|u s c|usc \d|form i \d+)\b")

# "Do not critique the agent's process, speed or reasoning style; judge the deliverables."
_PROCESS_RE = re.compile(
    r"\b(?:reasoning|thought process|chain of thought|thinking|its process|the process it|"
    r"took longer|was faster|was slower|ran quickly|ran slowly|response time|latency|"
    r"number of steps|tool calls|iterations|self-corrected|backtracked)\b", re.I)

# "give the what (specific file and location) and the why"
# Found wanting on task 002 (2026-11-05): the old pattern ended in \b after a
# single \d, so "page 58" and "paragraph 14" never matched, and a Roman-numeral
# section ("Section III.7.C") was not a location at all.
_LOCATION_RE = re.compile(
    r"(?:\b(?:section|sections|§+|table|row|page|pages|paragraph|paragraphs|para|clinic|"
    r"part|item|footnote|line)\s*(?:\d+|[IVXLC]+\b)|¶\s*\d+|\bcell\s*[A-Z]+\d+|"
    r"\bcolumn\s*[A-Z]\b|\bsheet\b|\bappendix\b|\.docx\b|\.xlsx\b|\.pdf\b|\.md\b)", re.I)

_MONEY_RE = re.compile(r"£\s?(\d{1,3}(?:,\d{3})*(?:\.\d+)?|\d+(?:\.\d+)?)")


def _norm_money(s):
    return s.replace(",", "").rstrip("0").rstrip(".") if "." in s else s.replace(",", "")


def _money_in(text):
    return set(_norm_money(m.group(1)) for m in _MONEY_RE.finditer(text))


def _rationale(ctx):
    return ctx.one("rationale.md")


@check(codes=["E05"], rules=["EVAL-RECORD"], scope="authored")
def check_prompt_recorded(ctx, report):
    """The task records the prompt both harnesses were given, and it is not still the template."""
    text = ctx.prompt
    if text is None:
        report.error("E05", "prompt.md",
                     "The task records no prompt. Both harnesses have to receive identical text, "
                     "and this file is the only proof of that; copy templates/prompt.md and fill "
                     "it before the first run.")
        return
    report.fact("prompt_words", word_count(prose_only(text)))
    if "Paste the prompt here" in text:
        report.error("E05", "prompt.md",
                     "still carries the template placeholder. Replace it with the prompt text as "
                     "pasted into the harness.")


@check(codes=["E06"], rules=["EVAL-LEAK"], scope="authored")
def check_reference_solution_not_in_prompt(ctx, report):
    """No sentence of the reference solution description reappears in the prompt.

    The reference solution is the task author's own answer. A run whose prompt
    carried any of it is void, and the leak is silent: both harnesses would
    simply look unusually good.
    """
    ref = ctx.folder / "reference-solution.md"
    raw = ctx.prompt
    if raw is None or not ref.is_file():
        return
    from .common import read_text

    # Compare the recorded prompt against the recorded solution, not the
    # editorial framing around them: both files carry our own notes about this
    # very check, and comparing whole files makes E06 fire on itself.
    prompt = _blockquote(raw)
    reference = _below_rule(read_text(ref))

    def shingles(text):
        out = set()
        for s in split_sentences(prose_only(text)):
            words = re.findall(r"[a-z0-9]+", s.lower())
            for i in range(len(words) - _LEAK_N + 1):
                out.add(" ".join(words[i:i + _LEAK_N]))
        return out

    names = _names(reference) | _names(prompt)
    shared = set(g for g in shingles(reference) & shingles(prompt)
                 if not _CITATION_RE.search(g) and _informative(g, names))
    if shared:
        report.error("E06", "prompt.md",
                     "%d passage(s) of reference-solution.md reappear in the prompt, e.g. \"%s\". "
                     "The reference solution is the author's own answer and is never sent to a "
                     "model; a run whose prompt carried it is void."
                     % (len(shared), sorted(shared)[0]))


@check(codes=["E10"], rules=["EVAL-RATIONALE"], scope="authored")
def check_rationale_present_and_long_enough(ctx, report):
    """The rationale exists and reaches the platform's 150-word minimum."""
    a = _rationale(ctx)
    if a is None:
        report.error("E10", "evaluation/rationale.md",
                     "No rationale. Stage 5 requires one before Check Your Task can run.")
        return
    n = word_count(prose_only(a.text))
    report.fact("rationale_words", n)
    if n < RATIONALE_MIN_WORDS:
        report.error("E10", a.name,
                     "%d words, under the %d-word minimum: \"Write an expert-level comparison "
                     "(at least 150 words) that explains your preference.\"" % (n, RATIONALE_MIN_WORDS))


@check(codes=["E20"], rules=["EVAL-RATIONALE"], scope="authored")
def check_rationale_covers_each_result(ctx, report):
    """The rationale names both harnesses and analyses each on its own, not only comparatively."""
    a = _rationale(ctx)
    if a is None or not ctx.harnesses:
        return
    text = prose_only(a.text)
    labels = {}
    for h in ctx.harnesses:
        words = [w for w in re.split(r"[^A-Za-z]+", h) if len(w) > 2]
        if not words:
            continue
        labels[h] = re.compile(r"\b(?:%s)\b" % "|".join(re.escape(w) for w in words), re.I)
    missing = [h for h, rx in labels.items() if not rx.search(text)]
    if missing:
        report.error("E20", a.name,
                     "The rationale never names %s. Each result needs its own key strengths and "
                     "weaknesses." % ", ".join(sorted(missing)))
        return
    for h, rx in labels.items():
        others = [r for k, r in labels.items() if k != h]
        solo = [s for s in split_sentences(text)
                if rx.search(s) and not any(o.search(s) for o in others)]
        report.fact("solo_sentences:%s" % h, len(solo))
        if len(solo) < 2:
            report.error("E20", a.name,
                         "%s is discussed in %d sentence(s) that do not also name the other "
                         "harness. The Mediocre examples fail for exactly this: \"does not "
                         "analyze each model's output on its own\"." % (h, len(solo)))


@check(codes=["E30"], rules=["EVAL-RATIONALE"], scope="authored")
def check_rationale_judges_deliverables(ctx, report):
    """The rationale judges the deliverables, not the agent's process, speed or reasoning style."""
    a = _rationale(ctx)
    if a is None:
        return
    for m in _PROCESS_RE.finditer(a.text):
        report.error("E30", a.name,
                     'process critique "%s": "Do not critique the agent\'s process, speed or '
                     'reasoning style; judge the deliverables."' % m.group(0))


@check(codes=["E40"], rules=["EVAL-RATIONALE"], scope="authored")
def check_rationale_gives_locations(ctx, report):
    """The rationale points at specific locations, not only at conclusions."""
    a = _rationale(ctx)
    if a is None:
        return
    hits = _LOCATION_RE.findall(a.text)
    report.fact("location_references", len(hits))
    if len(hits) < 2:
        report.error("E40", a.name,
                     "%d location reference(s). \"For every issue, give the what (specific file "
                     "and location) and the why.\"" % len(hits))


@check(codes=["E50"], rules=["EVAL-TRACE"], scope="authored")
def check_rationale_figures_are_traceable(ctx, report):
    """Every money figure the rationale states is findable in an output or a source file."""
    a = _rationale(ctx)
    if a is None:
        return
    corpus = {}
    for art in ctx.artifacts:
        if art.kind in ("evidence", "source"):
            corpus[art.name] = _money_in(art.text)
    stated = _money_in(a.text)
    report.fact("rationale_figures", len(stated))
    for fig in sorted(stated):
        where = sorted(n for n, vals in corpus.items() if fig in vals)
        if not where:
            report.error("E50", a.name,
                         "£%s appears in no output or source file. Rate \"counting only "
                         "errors you verified in the files\"; check the figure or cite where it "
                         "comes from." % fig)
        else:
            report.fact("traced:£%s" % fig, where)


@check(codes=["E60"], rules=["EVAL-RATIONALE"], scope="authored")
def check_confidence_note(ctx, report):
    """The confidence note exists and names what could not be fully evaluated."""
    a = ctx.one("confidence.md")
    if a is None:
        report.error("E60", "evaluation/confidence.md",
                     "No confidence note. Stage 5: \"Rate your Confidence and note anything you "
                     "could not fully evaluate.\"")
        return
    report.fact("confidence_words", word_count(prose_only(a.text)))
    if not re.search(r"\b(?:could not|cannot|unable to|not confirm|unconfirmed|would need|"
                     r"no way to|not verifiable|uncertain)\b", a.text, re.I):
        report.error("E60", a.name,
                     "The note states no limit on what was checked. It has to \"note anything "
                     "you could not fully evaluate\".")


@check(codes=["E70"], rules=["EVAL-RATINGS"], scope="authored")
def check_ratings_complete(ctx, report):
    """Every harness carries the four dimensions on the five-point scale and an overall 1 to 7."""
    r = ctx.ratings
    if not r:
        report.error("E70", RATINGS,
                     "No ratings table. Copy templates/ratings.md; E80 cannot check the "
                     "preference against scores without it.")
        return
    for h in ctx.harnesses:
        if h not in r.harnesses:
            report.error("E70", RATINGS, "no column for harness %s." % h)
            continue
        for dim in DIMENSIONS:
            row = next((v for k, v in r.rows.items() if k.lower() == dim.lower()), None)
            if row is None:
                report.error("E70", RATINGS, "no row for %s." % dim)
                continue
            val = row.get(h, "")
            if val not in SCALE:
                report.error("E70", RATINGS,
                             "%s / %s is %r, not one of the five-point scale %s."
                             % (dim, h, val, ", ".join(SCALE)))
        overall = r.overall(h)
        report.fact("overall:%s" % h, overall)
        if overall is None:
            report.error("E70", RATINGS, "no overall quality score for %s." % h)
        elif not (1 <= overall <= 7):
            report.error("E70", RATINGS,
                         "overall quality for %s is %s, outside 1 to 7." % (h, overall))


@check(codes=["E80"], rules=["EVAL-RATINGS"], scope="authored")
def check_preference_matches_ratings(ctx, report):
    """The stated preference agrees with the recorded overall scores."""
    r = ctx.ratings
    a = _rationale(ctx)
    if not r or not r.preference:
        return
    scores = dict((h, r.overall(h)) for h in r.harnesses)
    if any(v is None for v in scores.values()) or len(scores) < 2:
        return
    best = max(scores, key=lambda h: scores[h])
    worst = min(scores, key=lambda h: scores[h])
    pref = r.preference
    unsure = re.search(r"\bunsure|negligib", pref, re.I)
    report.fact("preference", pref)
    if unsure:
        if scores[best] - scores[worst] > 1:
            report.error("E80", RATINGS,
                         "preference is %r while the overall scores differ by %g (%s %g, %s %g). "
                         "\"Use an Unsure or negligibly better option only when the two are almost "
                         "equal.\"" % (pref, scores[best] - scores[worst], best, scores[best],
                                       worst, scores[worst]))
        return
    named = [h for h in scores if h.lower() in pref.lower()
             or any(w.lower() in pref.lower() for w in h.split("-") if len(w) > 2)]
    if not named:
        report.error("E80", RATINGS,
                     "preference %r names no harness column (%s)." % (pref, ", ".join(r.harnesses)))
        return
    if scores[named[0]] < scores[best]:
        report.error("E80", RATINGS,
                     "preference is %s (overall %g) but %s scores higher (%g). Check Your Task "
                     "reviews \"whether it matches your ratings and preference\"."
                     % (named[0], scores[named[0]], best, scores[best]))
    if scores[best] == scores[worst] and not unsure:
        # The platform form refuses this outright (observed 2026-11-05, task 002):
        # "Your overall quality ratings are equal (...), so only an 'Unsure or ...
        # negligibly better' preference fits. Choose one of those, or revise a rating."
        report.error("E80", RATINGS,
                     "the two overall scores are equal (%g) while the preference names %s. The "
                     "platform form refuses this: with equal overall scores only an \"Unsure or "
                     "... negligibly better\" option fits. Revise a rating or the preference."
                     % (scores[best], named[0]))
