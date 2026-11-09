# Stage 5: preference and rationale

Compare the two results side by side, say which you would rather receive from a
colleague, and write the rationale. Use *Unsure or negligibly better* only when
the two are almost equal; `evalcheck` E80 objects when that option sits beside
overall scores more than a point apart.

## What the rationale has to carry

At least 150 words, and four things:

1. Each result's key strengths and weaknesses, **on its own**.
2. What separated the two.
3. For every issue, the what (specific file and location) and the why.
4. Why the preferred result matters more in a professional context.

Judge the deliverables. Do not critique the agent's process, speed or reasoning
style. E30 scans for that vocabulary, because it is the easiest rule to break
when the run was visible.

## The failure mode the examples are built around

Read the Bad, Mediocre and Good examples in
[the instructions](../reference/evaluation-instructions.md). The Mediocre ones
are the instructive set: each identifies one real difference, then stops. Two
of the three fail for the same reason, written out in the feedback as "does not
analyze each model's output on its own".

That is what E20 measures. It counts, for each harness, the sentences that name
that harness and not the other one. Fewer than two, and the rationale is a
comparison with no per-result analysis in it, whatever its length.

Length is not the target. The terse Good example is shorter than the mediocre
ones and passes on substance.

## Shape that tends to work

Not a required format. The instructions say to use whatever feels natural.

- A paragraph per result: what it got right, what it got wrong, each with the
  location and the consequence.
- A paragraph on what separated them, naming the difference that decided it.
- A sentence on what the preference means in practice: usable as-is, usable
  after a named fix, or needing rework before anyone sees it.

Tie findings to consequence. "Gemini Native deducts £18,629.56 from EBITDA on a
staffing assumption the files do not establish, which moves the offer by
£26,081.38" is a finding. "Gemini Native made an assumption" is not.

## Prose standard

Plain, correctly punctuated sentences. Zero em dashes: this is text typed into
the platform, and the house rule for platform-entered text is zero. Comma
before a conjunction joining two clauses, never three clauses in one sentence,
serial comma in lists. A6, A10 and A20 enforce the mechanical part of this
against the rationale and the confidence note.

The reason is not pedantry about commas. The reviewer-side checklist reads
polished uniformity as a sign of generated text, and the prose standard's
answer is that correct ordinary punctuation reads more human than the clipped,
breathless register a model reaches for. See
[the prose references](../reference/prose/README.md).

## Before Check Your Task

```bash
python3 tools/evalcheck.py tasks/NNN-name
```

Clean of ERROR, then go to [04-check-and-submit.md](04-check-and-submit.md).
