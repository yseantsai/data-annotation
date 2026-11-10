---
name: review-alchemy-run
description: Read the latest Attempting Agent run saved in alchemy/tasks/NN-*/runs/ (final response, output files and Grading Agent results) against the task's worked correct answer and rubric, decide whether it shows a severe, valid failure or the task needs hardening, check the Grading Agent's verdicts, and write the failure description. Use it whenever the user runs /review-alchemy-run NN, or asks to review, grade, check or judge an Alchemy run, the agent's output, or the grading for a task, including "how did the agent do on 01". For writing a task use create-alchemy-task; for hardening one use revise-alchemy-task.
---

# Review an Alchemy run

`/review-alchemy-run NN`

The project is `alchemy/` under the workspace root. Work from that folder. The task is
`tasks/NN-slug/`. Read `docs/workflow.md` Stages 5 to 8 and `docs/rules.md` (A series) first.

## 1. Locate the run and check it is current

```
python3 tools/alchemy_check.py tasks/NN-slug --only runs
```

If there is no run file, or the latest one has no final response, stop and say what to save:
the response in `runs/run-N.md` and every output file in `runs/run-N/`. If the run is stale
(A3), stop: a stale run cannot support the submission, and the user deletes and reruns it.

Read, in this order: `task.md` in full (the Failure plan and Correct answer are the standard),
`prompt.md`, `rubric.md`, both input files, the run file, then every output file in
`runs/run-N/`. Read the workbook cells and the document text, not only the chat reply. The
error that matters is often in a tab the summary does not mention.

## 2. Verify the numbers

Recompute every figure the agent produced with a short Python script: once on the agent's own
assumptions, once on the Correct answer's. This separates arithmetic slips from method errors
and shows whether the conclusion changes. Every flaw named later carries a figure or a quote.

## 3. Decide

| What the run shows | Verdict |
| --- | --- |
| Refused, asked a question, or misread the deliverable | Prompt defect (P9). Fix the prompt and rerun; not a failure |
| A substantive error a professional would not accept (cascade, missed edge case, failed synthesis, misclassification, wrong source) | Severe failure: go on to step 4 |
| Right on the whole, minor slips only | Too good: recommend `/revise-alchemy-task NN` with the levers that fit |

Be honest in the borderline case. A run that reached the right decision through the right
reasoning is not a failure because of a rounding difference.

## 4. Check the Grading Agent

Compare each `Criterion N: PASS/FAIL` line with your own reading of the output files. Where they
disagree, name the criterion and say whether the criterion is unclear or not self-contained
(R3, R4), and propose the rewrite. A failure the grader did not catch does not count until the
criterion is fixed and the run is graded again.

## 5. Write it up

In the run file, fill Grader check and Output files. In `task.md`, add a line under Runs: the
date, the fingerprint, the criteria failed, what the agent caught (now spent) and what it missed.

If the failure is severe and graded, write the Failure description (50 to 350 words) to Stage 8
of the workflow, from the actual run and files only:
what the agent did with its figure, the file evidence and the correct value with the file named,
the criterion numbers, and why the deliverable is unusable. Then:

```
python3 tools/alchemy_check.py tasks/NN-slug --only failure
```

Fix every ERROR and read every WARN. Add a dated line to the Log, and report the verdict and
the next step. Do not submit anything.
