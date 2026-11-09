# Task 001 — ALC Physio investment request

Category: Finance / Accounting. Harness order: Antigravity, then Gemini Native.

Status: User reported the first task completed. The platform checker reported that the rationale passed all checks. Final submission was not independently observed.

Authorship: LLM-generated and LLM-edited workspace materials.

## Prompt

[The prompt both harnesses were given](prompt.md), extracted verbatim from the
instruction transcript on 2026-11-05. It was not recorded at run time; task 002
onward records it before the first run.

## Markdown context

Read the [historical instructions and original task/reference solution](../../docs/reference/evaluation-instructions.md), then the source materials:

- [Investor request requirements](evaluation/converted/inputs/investment-request-requirements.md)
- [Email correspondence](evaluation/converted/inputs/email-correspondence.md)
- [Unadjusted profit and loss](evaluation/converted/inputs/unadjusted-profit-and-loss.md)

The workbook Markdown is a legacy conversion: it includes formula expressions but omits blank rows and cell coordinates. Use the original workbook for cell-level verification. All Markdown conversions omit some original formatting and are not suitable for judging pagination.

## Model deliverables

- [Antigravity form](evaluation/converted/antigravity/investment-request-form.md)
- [Gemini Native form](evaluation/converted/gemini-native/investment-request-form.md)

These are outputs to evaluate, not authoritative source facts. Each harness folder also contains its original DOCX and visual renders. Final chat messages are not stored in this task folder.

## Evaluation

- [Rationale draft](evaluation/rationale.md)
- [Confidence explanation draft](evaluation/confidence.md)
- [evalcheck baseline](evaluation/checks/evalcheck-2026-11-05.json)

The confidence file is the saved LLM-generated draft; later chat revisions may differ.

## Known check findings

`python3 tools/evalcheck.py tasks/001-alc-physio` reports one ERROR and one NOTE.

- **E70, no `evaluation/ratings.md`.** The per-dimension ratings and the overall
  scores were entered on the platform and never captured in this workspace, so
  there is nothing here for E80 to read the preference against. The scores are
  not reconstructed from the drafts, because a rating inferred from a rationale
  is not a record of what was submitted. The finding stands until the platform
  values can be recovered, or it is closed as unrecoverable.
- **A6 NOTE, 6 em dashes in 735 words in the Antigravity DOCX.** An observation
  about a harness output, which is not ours to edit. It belongs to Format &
  Presentation if those ratings are ever reconstructed.

The saved baseline above also records that all six money figures in the
rationale resolve to the files, each to the harness the rationale attributes it
to.

## Original artifacts

The input ZIP and its unpacked documents sit together in `inputs/`; the Antigravity output ZIP sits beside its unpacked DOCX in `outputs/antigravity/`. Markdown conversions and page renders are in `evaluation/converted/`. Folder flattened 2026-11-06; nothing was re-extracted.

## Shared editorial references

See [prose references](../../docs/reference/prose/README.md). Use one canonical copy of every draft; link to it from this page instead of duplicating it.
