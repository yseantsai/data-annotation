# Workflow: one prompt attempt, start to finish

Each attempt lives in one folder, `drafts/NN-slug/`, copied from `templates/`. The number is
the next unused one. `prompt.md` holds the prompt alone, exactly as it will be pasted into the
form, so it can be found and copied without hunting. `result.md` holds the Generate response, pasted unedited. `task.md` holds the design
notes, the check output, the rating and the explanation, so an attempt can be
revisited or compared with later ones. Nothing is submitted from memory; the form fields are
copied out of these two files.

Rule ids in brackets are defined in `prompt-rules.md`.

## Stage 0: pick a failure target

Start from where models fail, not from a topic. Useful targets in this domain:

- A standard method applied where its assumptions do not hold (a DCF on a company with
  negative and volatile cash flows, a P/E comparison across firms with different fiscal
  year ends or one-off items, CAPM on an illiquid private asset).
- Facts in the scenario that conflict, where the model must notice and decide which governs
  (a term sheet that contradicts the email summarising it, a budget whose line items do not
  sum to the stated total).
- A number the model will compute confidently but with the wrong convention (day-count,
  compounding frequency, pre-money versus post-money, gross versus net of fees, nominal
  versus real, book versus market weights).
- A regulation or accounting rule the model will state from a stale or wrong jurisdiction
  (tax lots, wash-sale windows, lease classification, revenue recognition timing).
- A question whose honest answer is "you cannot decide this from these numbers" or "the
  answer you want is the wrong one", where a model playing along will produce a confident
  recommendation anyway.

Write the target as one sentence at the top of the task file: what the model is expected to
get wrong, and why a competent practitioner would not.

Discard the target if the question is common enough that the model has seen the answer
pattern thousands of times, if it is answerable by recall, or if it is a minor variation on an
attempt already in `drafts/` [D1, D5].

## Stage 1: design the scenario

Before writing a sentence of prompt, write the design notes:

1. **The requester.** Who is asking, who the output is for, and what decision it feeds
   [F1, F4]. All people and companies are fictional [F5].
2. **The facts.** The figures, dates and documents the scenario carries. Realistic values,
   not round ones. Enough detail that the question cannot be answered without them.
3. **The trap.** The one thing in the facts that changes the answer, and the default the
   model is expected to reach for instead [D2].
4. **The correct answer.** A sketch of what a competent practitioner would conclude, with
   the arithmetic where there is any. This is what the rating is judged against later.
5. **The adverse result.** What answer the requester does not want to hear, and whether the
   facts support it [D3]. A model that tells the requester what they want to hear is a
   gradeable failure only if the facts say otherwise.

If the trap is something the model can dodge by hedging ("it depends"), tighten the ask so
that a position has to be taken.

Keep the scope inside the size budget [D8]: the whole task, design through rating, fits in
about three hours of human work. Pick one decisive question and cut every thread that does not
change the answer. A prompt a practitioner answers in about an hour, with a trap in the facts,
is the target. Stacking taxes, depreciation, financing and concentration into one prompt makes
the task bigger without making it harder.

## Stage 2: write the prompt

Write it the way the requester would brief a colleague or type it to an assistant. The
instructions' own guidance applies: a party planner with many dietary restrictions writes a
long prompt, a person asking for a short email does not.

- Open on the situation, not on a persona [F2, F3]. Context is woven in, never announced.
- Say what is needed and why now. Stakes are a decision, a deadline or an amount at risk [F4].
- Give the facts the way a person would: a figure here, a quoted line from a document there,
  an aside about what the boss said. Not a numbered data sheet.
- Ask for what to produce, never how to produce it [S1, S2]. No step lists, no outlined
  sections, no dictated formulas, no warning about the pitfall.
- Keep the sentence mechanics clean [M1 to M7]. Zero em dashes, a comma before a conjunction
  that joins two clauses, never three clauses in one sentence, the serial comma.
- None of the shapes in `llm-prose-tells.md` [T1 to T14].

Complexity must be the scenario's own. A long prompt is fine when the situation is complex.
Arbitrary constraints that exist only to trip the model are not [D6].

## Stage 3: self-check

```
python3 tools/prompt_check.py drafts/NN-slug/prompt.md
```

The script checks the whole of `prompt.md`. Fix every ERROR. Read every WARN
and either fix it or note in the task file why it stands (a real finance term the vocabulary
scan dislikes, a legitimate list of three). Then walk the MANUAL rows it prints: those are the
rules no regex can read, and each one is a reason a prompt gets rejected or fails to produce a
model failure.

Read the prompt aloud once. If any sentence exists only to sound like a person, delete it.

## Stage 4: Generate

Paste the prompt into the platform and click Generate. Paste the full response, unedited, into
`result.md` in the task folder. Retry on error up to three times; report to the project chat after that or after
fifteen minutes without a response.

Read the response against the correct-answer sketch from Stage 1. Decide which of the three
outcomes applies:

| Outcome | What you saw | Next |
| --- | --- | --- |
| Major issues | Wrong conclusion, wrong method, invented facts, or the trap taken whole | Stage 5 |
| Flawed in an essential way | Parts right, but a crucial element wrong and the result only marginally useful | Stage 5 |
| Few or no issues | Conclusions and logic right on the whole, even with minor slips | Back to Stage 1 or Stage 0 |

A response that is right on the whole is not a submission, however long it took to build. Note
in the task file what the model handled correctly so the next attempt does not repeat it.

## Stage 5: rate and explain

Rate only from the response in the task file [R1]. Only OK, Pretty Bad or Terrible are
submittable [R3]:

- **Terrible.** The conclusion is wrong or misleading, and a reader acting on it would be harmed.
- **Pretty Bad.** The core reasoning has an essential flaw, even if some parts are right.
- **OK.** Right in places, wrong on something that matters, moderately useful at best.

Write the explanation as a few plain sentences [R2]. It names the specific mistakes, says how
severe each one is, says whether the model started on the right track before faltering or
missed the mark from the first line, and offers a theory of why (a default method, a missed
fact, a convention confusion). Quote the response where a quote makes the error concrete.
State what the correct answer is, so that a reader can verify the rating.

Optional comments hold anything else worth saying about the prompt or the response.

Check the explanation the same way as the prompt, then read it aloud:

```
python3 tools/prompt_check.py --section Explanation drafts/NN-slug/task.md
```

Record the time estimate (AHT) for the round in `task.md`: the minutes per step for one person
doing it by hand, and the total against the three-hour budget [D8].

## Stage 6: submit and log

Copy the prompt, rating, explanation and optional comments from the task file into the form.
After submitting, add a dated line to the task file's log: submitted, and any feedback received
later. If the platform returns the task, the fix is made in the task file first and the log
says what changed and why.

## Revising a task after a round

When Stage 4 sends a task back to design, or the platform returns it, the task keeps its number
and folder. The closing round's `prompt.md` and `result.md` are copied to `history/prompt-rN.md`
and `history/result-rN.md`, `prompt.md` is rewritten, `result.md` is emptied, the Design notes
are recomputed for the new facts, the Outcome, Rating and Explanation sections are cleared, and
a dated entry goes under Revisions in `task.md` saying why, what moved and what was kept. The
difficulty moves to what the model missed; the traps it caught are spent. `task_status.py NN`
prints the current round. `/revise-finance-investing-prompt NN` does all of this.

## When to stop

The instructions say to take a break rather than force submissions. When the next idea is a
variation on the last one, or the target is a topic rather than a failure, stop and come back
later. Quantity of submissions is not the measure here.
