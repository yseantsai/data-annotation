# Shadow validator: authorship read

Reconstruction of the reviewer-side read for signs of LLM use, from
[the reviewer checklist](../reference/prose/reviewer-checklist.md)
and [the style guide](../reference/prose/style-guide-llm-tells.md).
Not the platform's implementation. See [README.md](README.md).

## What this is for, and what it is not for

This workspace's own policy is that LLM-generated and LLM-edited materials are
allowed and are the default. So this validator is not an authorship test and
not a confession hunt. It reads for the register the checklist names, because
that register reads as unedited output to a reviewer, whoever typed it.

The standard is worth restating, since it is the opposite of the
intuition: correct, ordinary punctuation reads **more** human. The flagged
register is the clipped, breathless one, "an LLM trying too hard to sound like
a real, rushed, busy person". Do not loosen punctuation to pass this read.

Four of the checklist's lines are already coded and need no judge:

| Line | Code |
| --- | --- |
| Repeated em dashes | A6 |
| Negative parallelism, "it's not X, it's Y", serves-as verbs, sycophancy | A10 |
| Highly polished grammar, run-ons and comma splices | A20 |
| Long, highly uniform bullet lists | A33 |

Run `python3 tools/evalcheck.py --codes A6,A10,A20,A33` first. This validator
reads the rest, which is the part that needs a reader: rule-of-three phrasing,
lexical variation, sentence-length uniformity, register fit.

## Prompt

> Read the attached text as a reviewer scanning for signs that it is unedited
> model output. It is a professional's written evaluation of two deliverables.
>
> Report only what you can quote. For each finding give the quote, the pattern
> it matches, and a rewrite in plain professional English that keeps every fact
> and figure unchanged.
>
> Read for:
>
> - **Rule of three.** Ideas repeatedly grouped in sets of three.
> - **Lexical variation.** Several different phrases for one concept where one
>   clear term should repeat. Name the concept and list the variants.
> - **Sentence uniformity.** Sentence length and structure consistent
>   throughout in a way sustained writing is not. Quote three consecutive
>   sentences if so.
> - **Parallel structure.** The same grammatical pattern repeated across
>   sentences or list items.
> - **Contrast framing.** Ideas repeatedly set against one another to make a
>   point.
> - **Register fit.** Does this read as a practitioner's evaluation note, or as
>   a formal report regardless of audience? Quote a sentence that would not
>   survive being read aloud.
> - **Hedging.** "It is worth noting", "this may suggest", "one could argue",
>   especially on established facts.
> - **Self-description.** Any sentence describing the document rather than
>   constituting it.
>
> Then answer one question directly: is there any passage here whose substance
> could have been produced without reading the source files? Quote it. That
> passage is the problem, whatever its register.
>
> Do not flag correct punctuation, a serial comma, or an absence of em dashes.
> Those are the house standard, not tells.

## Output contract

```json
{
  "validator": "authorship-read",
  "task": "NNN-name",
  "run": "YYYY-MM-DD",
  "artifact": "evaluation/rationale.md",
  "findings": [
    {"pattern": "rule-of-three|lexical-variation|sentence-uniformity|parallel-structure|contrast-framing|register|hedging|self-description|unsourced",
     "quote": "...", "rewrite": "..."}
  ],
  "unsourced_passages": ["..."],
  "verdict": "clean|advisory"
}
```

Save as `evaluation/checks/authorship-read-<date>.json`.

## Reading the result

Advisory. It never blocks, and a finding here is a prompt to reread the
sentence, not a required edit. The last question is the one that matters: a
passage that could have been written without opening the files is a problem the
register checks cannot see and the rating depends on.
