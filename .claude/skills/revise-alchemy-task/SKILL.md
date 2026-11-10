---
name: revise-alchemy-task
description: Revise or harden an existing Alchemy task in alchemy/tasks/NN-*/ after a run where the agent passed every criterion, after reviewer feedback, or on the user's direction: archive the round, move the difficulty to what the agent missed, update the file descriptions, input files, prompt and rubric, and rerun the coded checks. Use it whenever the user runs /revise-alchemy-task NN [direction], or asks to harden, toughen, rework, fix or change an Alchemy task by number, even without naming the command. For a new task use create-alchemy-task; for reading a run use review-alchemy-run.
---

# Revise an Alchemy task

`/revise-alchemy-task NN [optional direction]`

The project is `alchemy/` under the workspace root. Work from that folder. Read
`docs/workflow.md` (Stage 7 and "Revising a task"), `docs/rules.md` and
`docs/rubric-standard.md` first.

## 1. Know why the round closed

Read `task.md` in full, the latest run file, and its output files. Write down, from the evidence,
what the agent got right (those traps are spent) and where it was closest to going wrong. If the
direction is reviewer feedback, quote it into `task.md` under Revisions before acting on it.

## 2. Archive the round

Copy `prompt.md`, `rubric.md` and `inputs/` to `history/rN/`, where N is the round that just
closed. Never edit the archived copies.

## 3. Pick one lever

From Stage 7 of the workflow, pick the lever that targets what the agent nearly missed, not the
trap it already caught: another thread to weigh, more realistic mess, judgment instead of
lookup, a late fact that forces a revision, or a red flag an expert would notice. One lever per
round, so the next run shows which change mattered. Never bury a fact, and never declare an
answer the files do not support (D8, D3).

## 4. Recompute, then change

Update the Correct answer script and its result first. Then update, in order: the file
descriptions in `task.md`, the input files (by hand for small edits; a fresh File Builder run for
large ones, with the description changed to match), `prompt.md` if needed, and `rubric.md` so at
least one criterion catches the new targeted failure. Every figure comes from the recomputed
answer.

## 5. Check

```
python3 tools/alchemy_check.py tasks/NN-slug --zip
python3 tools/alchemy_check.py tasks/NN-slug
```

The earlier runs now report as stale (A3). That is expected: tell the user to delete them on the
platform, upload the new ZIP, and run again. Fix every other ERROR, read every WARN.

## 6. Record

Add a dated entry under Revisions in `task.md` (the reason, the lever, what changed and what was
kept), set Status to revising, and add a Log line. Report what changed and the user's next
platform step.
