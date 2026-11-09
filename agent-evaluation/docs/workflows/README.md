# Evaluation workflows

The five platform stages, one file each, written so a session can pick up at
any stage without re-reading the whole instruction transcript. The authority is
always [the transcribed instructions](../reference/evaluation-instructions.md);
where these files and that transcript disagree, the transcript wins and the
file is wrong.

| Stage | File | Gate before moving on |
| --- | --- | --- |
| 1, 3. Run the task in a harness | [01-run-a-harness.md](01-run-a-harness.md) | Outputs and the final message are saved under `outputs/<harness>/` |
| 2, 4. Rate the result | [02-rate-a-result.md](02-rate-a-result.md) | Every output file opened, `evaluation/ratings.md` column filled with evidence lines |
| 5. Preference and rationale | [03-rationale.md](03-rationale.md) | `python3 tools/evalcheck.py` clean of ERROR |
| 5. Check and finish | [04-check-and-submit.md](04-check-and-submit.md) | Check Your Task run, confidence recorded |

## The ordering rule that is easy to break

Rate the first harness **before** running the second. The instructions say so,
and the reason is that a rating written after seeing both results is a
comparison wearing a rating's clothes. `templates/ratings.md` keeps a Revisions
section for the case where a rating genuinely has to change later, so the
change is visible instead of silent.

## What the tooling does and does not do

`tools/evalcheck.py` checks the things a machine can settle: that the rationale
reaches 150 words, names both results, analyses each on its own, points at
locations, quotes only figures that exist in the files, and that the stated
preference matches the recorded scores. It also runs the prose tells over
what we wrote.

It cannot tell whether a rating is right. It cannot confirm a calculation in a
model's output. A clean run means nothing is mechanically wrong with the
submission, not that the evaluation is correct. The verification that matters
is the one in [02-rate-a-result.md](02-rate-a-result.md), done by hand against
the source files.
