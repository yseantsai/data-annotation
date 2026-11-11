---
name: revise-finance-investing-prompt
description: Revise an existing finance task's prompt in finance-investing-prompt/submissions/NN-*/ after platform feedback on a submitted task, or on the user's direction, keeping the task's history and re-running the coded checks. Use it whenever the user runs /revise-finance-investing-prompt NN [direction], or asks to harden, toughen, rework, fix, tighten, or change the prompt of a finance task by number, even without naming the command. For a brand-new task use create-finance-investing; for grading a response use review-finance-investing-result.
---

# Revise a finance task's prompt

`/revise-finance-investing-prompt NN [optional direction]`

The project is `finance-investing-prompt/` under the workspace root. Work from that folder.
`NN` is the task's sequence number. The direction, if given, says what to change or why ("the
model caught the add-backs", "platform says too easy", "make the requester a lender"). Without
it, the reason is whatever the task's Outcome section says.

A response that is too good is not a reason to revise: the review deletes that task and a new
one is created (`docs/workflow.md`, Stage 4). This skill is for a submitted task the platform
returns, or a change the user asks for by name.

A revision keeps the task's number and folder and keeps its history, so the series of prompts
and results stays readable. It does not start a new task; when the scenario has to change so
much that nothing carries over, say so and suggest `/create-finance-investing` instead.

## 1. Locate the task and read everything it holds

```
python3 tools/task_status.py NN
```

Read `task.md` in full, especially the Outcome: it lists what the model caught (now spent) and
what it missed (where the difficulty should move). Read `prompt.md` and, if present,
`result.md`, because the response shows exactly how the model reasons about this scenario and
where it was confident. Read any `history/` round the same way.

Then re-read `docs/workflow.md` Stage 1 and Stage 2, `docs/prompt-rules.md`, and
`docs/llm-prose-tells.md`. A revision is held to the same bar as a first draft.

## 2. Decide what moves

The question is not "how do I make the prompt harder" but "where does the model's reasoning
break on this scenario, and how do the facts put the question there". Moves that have worked,
roughly in order of preference:

- **Move the difficulty to what the model missed.** The Outcome names dimensions the response
  never raised (cash the buyer must bring, taxes, a convention, a conflicting document). Make
  one of them the thing the requester actually needs answered, so skipping it is the failure.
- **Take back the pre-solved facts.** Any figure the requester supplied that does the model's
  work (a replacement quote, a market comp, a note that a fee recurs) becomes a raw fact or a
  document line the model has to interpret, or is removed and left for the model to ask about.
- **Make the adverse answer the only right one.** If the facts leave room for a comfortable
  recommendation, tighten them so the honest answer is the one the requester does not want.
- **Add a conflict, not a constraint.** Two sources that disagree, where which one governs
  decides the answer, beats an extra rule the model must follow.
- **Change the vantage point.** The same facts asked by a lender, a seller or a minority partner
  pose a different question with different defaults to get wrong.

Keep what worked: the realism, the voice, the stakes, the facts that produced the model's
genuine errors. Do not add arbitrary constraints or trivia; rule D6 forbids it, and the
platform reads that as prompt-engineering.

Stay inside the size budget (rule D8): the whole task fits in about three hours of human work.
Hardening means moving the trap, not adding threads. When a revision starts stacking new
dimensions (taxes on top of financing on top of working capital), pick the one that decides the
answer and cut the rest.

Recompute the correct answer for the revised facts with a short Python snippet, and update the
Design notes (Facts, Trap, Correct answer, Adverse result) to match. A revised prompt with the
old worked answer cannot be reviewed.

## 3. Archive the round, then rewrite

Before changing anything, keep the previous round in `history/` inside the task folder:
`prompt-rN.md`, `result-rN.md` if it exists, and `task-rN.md`, a copy of the whole task file
with that round's graded Outcome and Explanation, so the round can still be submitted if the
human decides to. N is the round being closed (the status tool prints the current round). Then:

- Rewrite `prompt.md` in place.
- Empty `result.md`; the new response goes there after the next Generate.
- In `task.md`, update the Failure target and Design notes, clear the Generate response,
  Outcome, Rating and Explanation sections back to their one-line notes, and add a
  **Revisions** section (create it before the Log if absent) with a dated entry: the reason,
  what changed in the facts and the ask, and what was deliberately kept.
- Add a dated line to the Log.

## 4. Check, then read aloud

```
python3 tools/prompt_check.py submissions/NN-slug/prompt.md
python3 tools/prompt_check.py --task submissions/NN-slug/task.md
```

The first checks the new prompt, the second every prose section of the rewritten task file
(failure target, design notes, revisions, log). Fix every ERROR, read every WARN, redo the MANUAL rows in the Self-check section with the new
date, and read the prompt aloud once. Rule S2 again: a revision that explains the trap to the
model is a revision that failed.

## 5. Hand over

Report what the model caught last round, what the revision moved and why, the new character
count, and the human's next step: paste the new `prompt.md` into the platform, Generate, save
the response to `result.md`, then `/review-finance-investing-result NN`. Do not submit and do
not predict the outcome.
