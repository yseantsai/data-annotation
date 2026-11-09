"""A6 A10 A20 A21 A32 A33: prose tells, run over this workspace's artifacts.

The patterns live in catalogs.py. What differs by artifact is only what they
are pointed at and how a hit is scored:

  authored prose (rationale.md, confidence.md)  ERROR. This is text we type into
      the platform, so the rule for platform-entered text applies: zero em
      dashes, and none of the flagged shapes.
  evidence (a harness's output document)  NOTE. We cannot edit a model's
      deliverable. A tell there is a Format & Presentation observation, logged
      with its quote so a rating can cite it, and it is never a defect to fix.

Source files are skipped: they are the client's documents, and neither we nor
the evaluated models wrote them.
"""
from . import catalogs as cat
from .common import (docx_emdash_stats, prose_only, split_sentences, word_count)
from .core import check
from .task import AUTHORED, EVIDENCE

import re
import statistics


def _scored(ctx):
    """(artifact, level) for every artifact a prose check judges."""
    for a in ctx.artifacts:
        if a.kind == AUTHORED and a.name.endswith("ratings.md"):
            continue            # a table of scores, not prose
        if a.kind == AUTHORED:
            yield a, "ERROR"
        elif a.kind == EVIDENCE:
            yield a, "NOTE"


def _quote(s, n=60):
    return s.strip()[:n]


@check(codes=["A6"], rules=["REV-PROSE"], scope="both")
def check_em_dashes(ctx, report):
    """Authored prose carries no em dash; an output document is read at docx density."""
    for a, level in _scored(ctx):
        if level == "ERROR":
            n = a.text.count("—")
            if n:
                report.error("A6", a.name,
                             "%d em dash(es). The house rule is zero em dashes in platform-entered "
                             "text; use a comma, colon, semicolon or parentheses instead." % n)
            report.fact("em_dash_count:%s" % a.name, n)
            continue
        if a.path.suffix.lower() != ".docx":
            continue
        stats = docx_emdash_stats(a.path)
        if not stats:
            continue
        em, words = stats
        per_k = 1000.0 * em / max(words, 1)
        if (em >= 4 and per_k >= 12) or (em >= 3 and per_k >= 8):
            report.note("A6", a.name,
                        "%d em dashes in %d words (%.0f/1000). Repeated 'clause - clause' "
                        "punctuation is the reviewer-flagged density; weigh it under Format & "
                        "Presentation." % (em, words, per_k))


@check(codes=["A10"], rules=["REV-PROSE"], scope="both")
def check_llm_prose(ctx, report):
    """No artifact carries a tautology, slogan, self-describing sentence, short idiom or sycophancy."""
    for a, level in _scored(ctx):
        text = a.text
        emit = report.error if level == "ERROR" else report.note
        for rx in cat._TAUTOLOGY_RES:
            m = next((m for m in rx.finditer(text)
                      if not cat._TAUTOLOGY_OK_RE.search(m.group(0))), None)
            if m:
                emit("A10", a.name,
                     'tautology "%s". The highest-confidence LLM prose tell; state the rule and '
                     'its consequence instead (docs/reference/prose/llm-prose-tells.md).'
                     % _quote(m.group(0)))
                break
        for rx, kind in cat._SLOGAN_RES:
            m = rx.search(text)
            if m:
                emit("A10", a.name,
                     '%s "%s". Reviewers read these as an LLM trying to sound real and busy; state '
                     'the mechanism or the quantity instead.' % (kind, _quote(m.group(0))))
                break
        seen = set()
        for rxs, note in ((cat._SHORT_IDIOM_RES, "name the artifact instead"),
                          (cat._SELF_DESCRIBING_RES,
                           "delete the sentence or give the thing its real title"),
                          (cat._SYCOPHANTIC_RES,
                           "a practitioner states the fact and moves on")):
            for rx, kind in rxs:
                m = rx.search(text)
                if m and kind not in seen:
                    seen.add(kind)
                    emit("A10", a.name,
                         '%s "%s". %s.' % (kind, _quote(m.group(0)), note))


@check(codes=["A20"], rules=["REV-REGISTER"], scope="both")
def check_run_on_sentences(ctx, report):
    """A sentence puts a comma before a clause-joining conjunction and joins no more than two clauses."""
    for a, level in _scored(ctx):
        emit = report.error if level == "ERROR" else report.note
        msgs = []
        for s in cat._a20_sentences(prose_only(a.text)):
            bares = cat._a20_bare_hits(s)
            bare = bares[0] if bares else None
            joins = (len(cat._A20_COMMA_RE.findall(s))
                     + len(cat._A20_SEMI_RE.findall(s)) + len(bares))
            if bare:
                window = s[max(0, bare.start() - 30):bare.end() + 20].strip()
                msgs.append('no comma before "%s" where a new clause starts ("...%s...")'
                            % (bare.group(1), window))
            elif joins >= 2:
                msgs.append('%d independent clauses in one sentence ("%s...")'
                            % (joins + 1, s[:100]))
        for msg in msgs[:cat._A20_CAP]:
            emit("A20", a.name,
                 msg + ". Comma before and/but/so/or between clauses, never more than two "
                       "clauses in a sentence, serial comma in lists.")
        if len(msgs) > cat._A20_CAP:
            emit("A20", a.name, "%d more sentences of the same shapes."
                 % (len(msgs) - cat._A20_CAP))


@check(codes=["A21"], rules=["REV-PROSE"], scope="both")
def check_status_template_register(ctx, report):
    """No document runs the status-report sentence skeleton on half or more of its sentences."""
    for a, level in _scored(ctx):
        emit = report.error if level == "ERROR" else report.note
        text = prose_only(a.text)
        sents = [s.strip() for para in text.split("\n")
                 for s in re.split(r"(?<=[.!?])\s+", para) if len(s.split()) >= 6]
        if len(sents) < cat._A21_MIN_SENTENCES:
            continue
        hits = [s for s in sents if cat._A21_TEMPLATE_RE.search(s)]
        share = len(hits) / float(len(sents))
        if share >= cat._A21_SHARE:
            emit("A21", a.name,
                 '%d of %d sentences (%.0f%%) are the status-report skeleton: "%s". The '
                 "platform's authorship reader calls this template-generated content; vary the "
                 "sentence shape section by section."
                 % (len(hits), len(sents), share * 100,
                    "; ".join(h[:70] for h in hits[:3])))


@check(codes=["A32"], rules=["REV-PROSE"], scope="evidence")
def check_generic_heading_pair(ctx, report):
    """An output document carries fewer than two headings from the generic report outline."""
    for a, level in _scored(ctx):
        if level != "NOTE":
            continue
        generic = [h for h in a.headings if h.lower().rstrip(":") in cat._A32_GENERIC]
        if len(generic) >= 2:
            report.note("A32", a.name,
                        "%d headings from the generic report outline (%s). The platform's "
                        "LLM-authorship check reads the pair as a model's outline; weigh it "
                        "under Format & Presentation." % (len(generic), ", ".join(generic)))


@check(codes=["A33"], rules=["REV-PROSE"], scope="both")
def check_uniform_bullet_run(ctx, report):
    """No artifact carries six or more consecutive bullets of near-identical length."""
    for a, level in _scored(ctx):
        emit = report.error if level == "ERROR" else report.note
        for run in cat._a33_md_runs(a.text):
            if len(run) < cat._A33_MIN_RUN:
                continue
            lengths = [len(b.split()) for b in run]
            sd = statistics.pstdev(lengths)
            if sd <= cat._A33_MAX_SD:
                emit("A33", a.name,
                     "%d consecutive bullets of %d to %d words (sd %.1f). The reviewer checklist "
                     "reads a long run of same-length bullets as a sign of LLM use; vary the "
                     "length, or fold the short ones into a sentence."
                     % (len(run), min(lengths), max(lengths), sd))
                break


@check(codes=["A40"], rules=["REV-PROSE"], scope="authored")
def check_word_counts(ctx, report):
    """Record the word count of each authored prose file, as the saved check JSON does."""
    for a, level in _scored(ctx):
        if level == "ERROR":
            report.fact("word_count:%s" % a.name, word_count(prose_only(a.text)))
