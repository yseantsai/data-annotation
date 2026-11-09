# Stage 5: check and finish

Three passes, cheapest first. Each one catches a class the next cannot see.

## 1. Mechanical

```bash
python3 tools/evalcheck.py tasks/NNN-name
```

Exit 0 means no ERROR. Fix every ERROR or record why it stands. NOTE findings
are about the harness outputs and never block.

## 2. Shadow validators

The platform runs model-driven checks we cannot call. The specs in
[docs/validators/](../validators/) reproduce what they ask for, so the finding
arrives before the platform's does rather than after:

- [check-your-task.md](../validators/check-your-task.md) reviews the rationale
  against the ratings and the preference, which is what the platform's own
  Check Your Task does.
- [authorship-read.md](../validators/authorship-read.md) reads the rationale
  the way the reviewer-side "signs of LLM use" checklist reads a submission.

Run them as a separate pass, on the finished text, against the spec. Do not run
them while still drafting: a judge applied to a draft grades the draft.

## 3. The platform's own Check Your Task

Run it. It reviews the rationale and whether it matches the ratings and the
preference.

Fix what you agree with and rerun it. Where you disagree, explain rather than
edit: the instructions ask for the explanation, and a rationale rewritten to
satisfy a checker you think is wrong is worse than the one you had.

## Confidence

Rate confidence and write `evaluation/confidence.md`, naming anything you could
not fully evaluate. E60 requires that the note state at least one limit,
because a note that claims everything was checked is almost always a note
written without checking what could not be.

Good content for it: a figure that could not be recomputed from the files, a
question only the client or seller could settle, anything judged from a render
rather than the original, anything the Markdown conversion could have hidden.

## Record what actually happened

In the task README, distinguish:

- what you observed (files opened, figures recomputed, checks run)
- what the platform reported (checker results, with the date)
- what you were told or assumed

Specifically, distinguish user-reported completion from an observed
submission. The two look identical a month later, and only one of them is
evidence.

## Save the check results

```bash
python3 tools/evalcheck.py tasks/NNN-name --save
```

Writes `evaluation/checks/evalcheck-<date>.json`. These are historical results
for the text as saved at that moment, not live checks and not a submission
record. If the text later changes in the platform and not here, the JSON is
about the old text, and the task README should say so.
