---
name: review-finance-investing-result
description: Grade the Generate response saved in finance-investing-prompt/drafts/NN-*/result.md against that task's worked correct answer, decide whether the response is a submittable failure (OK, Pretty Bad, Terrible) or too good (harden instead), and fill the task's Outcome, Rating and Explanation. Use it whenever the user runs /review-finance-investing-result NN, or asks to review, grade, rate, check or judge a model result, response or output for a finance task, including "please review result.md" or "how did the model do on 02". For writing or changing the prompt itself use create-finance-investing or revise-finance-investing-prompt.
---

# Review a finance task's Generate response

`/review-finance-investing-result NN`

The project is `finance-investing-prompt/` under the workspace root. Work from that folder.
`NN` is the task's sequence number; the task is `drafts/NN-slug/` with `prompt.md`,
`result.md` and `task.md`. The platform's own text in `instructions.md` and
`submission-form.md` defines the three outcomes and the ratings, and `docs/workflow.md`
Stage 4 and Stage 5 say how this project applies them. Read both before grading.

## 1. Locate the task and confirm there is something to review

```
python3 tools/task_status.py NN
```

If `result.md` is missing or empty, stop and say so: the human pastes the full Generate
response there first. If the Outcome section is already filled, this is a re-review; say so
and overwrite only with the human's agreement.

Read, in this order: `task.md` in full (the Failure target and the Design notes carry the
worked correct answer the response is judged against), `prompt.md`, then `result.md` in full.
A response can be several thousand words; read all of it, because the errors that matter are
often in a summary that disagrees with the body, or in a valuation method near the end.

## 2. Verify the response's own numbers

Where the response computes anything (loan payments, multiples, coverage ratios, present
values, tax lots, variances), recompute it with a short Python snippet on the response's own
assumptions, then on the design notes' assumptions. Three things come out of this: arithmetic
slips, methods that are wrong (a double-count, a mixed frame, a convention misapplied), and
places where the response's conclusion would change under the correct figures. Never grade
from impression; every flaw named in the explanation should carry a figure or a quote.

## 3. Decide the outcome

Compare against the Failure target and the Correct answer in `task.md`:

- Which of the planted traps did the model catch, and which did it take?
- Is the final conclusion or recommendation the correct one? Directionally, and in magnitude?
- Does the response contradict itself (summary versus body, table versus prose)?
- What did it miss that the prompt's facts required a practitioner to raise?

Then place it on the platform's scale:

| Outcome | Meaning | Rating |
| --- | --- | --- |
| Major issues | Wrong conclusion or method, invented facts, the trap taken whole | Terrible, or Pretty Bad |
| Flawed in an essential way | Parts right, but a crucial element wrong; moderately useful at best | Pretty Bad, or OK |
| Few or no issues | Conclusions and logic right on the whole, even with minor errors | Not submittable: harden |

Be honest in the borderline case. A response that reached the right decision through the
right reasoning is "right on the whole" even when it carries real numerical errors, and the
platform says such a prompt goes back to design. When the errors are serious enough that a
reader acting on the response would be materially misled (a headline figure that contradicts
the analysis, a method error that moves the recommendation), an OK rating is defensible; say
which reading you take and why, and let the human make the submit call. Never select Amazing
or Pretty Good, and never soften a verdict to make a task submittable.

## 4. Fill the task file

`task.md` opens with the form's fields in the form's order (Prompt, Generate response, Rating,
Explanation, Optional comments), then a "Working notes" divider, then the grading and design
sections. Keep that order, so the human can fill the platform form top to bottom without
scrolling past notes. Write the Rating and Explanation sections as text ready to copy, with
no proposal language or internal reasoning in them; the reasoning belongs in Outcome. Update
the Status line under the title. In `task.md`:

- **Generate response:** the date, and that the response is in `result.md` with its word count.
- **Outcome:** the verdict in one bold line, then what the model caught (these traps are now
  spent for this prompt family and the next task must not rely on them), then the flaws as a
  numbered list, each with the quote or figure and its severity, then the submit-or-harden
  recommendation.
- **Rating:** the rating, or "not submittable, harden" with the reason.
- **Explanation:** written for the platform form, following rule R2 in `docs/prompt-rules.md`:
  a few plain sentences that name the specific mistakes, their severity, whether the model
  started on the right track, a theory of why it went wrong, and what the correct answer is.
  Quote the response where a quote makes the error concrete. Keep it to about 150 to 200
  words in two or three paragraphs: what it got right in a sentence, the decisive mistake with
  its figures, the correct answer, and the likely cause. The full list of flaws stays in the
  Outcome. Written even when the recommendation is to harden, so the human can submit if they
  decide otherwise.
- **Time estimate (AHT):** the handle time for one person with finance experience doing this
  round by hand, as a table of steps in minutes, with the total and a line on earlier rounds.
  Base the reading and grading rows on the actual response length. Rule D8 sets the target at
  about three hours.
- **Log:** a dated line with the verdict and the recommendation.

Mechanics apply to this prose too: zero em dashes, clean commas, no hedging filler. Run the
check on the sections the human will copy, and on the Outcome, then fix every finding:

```
python3 tools/prompt_check.py --section Explanation drafts/NN-slug/task.md
python3 tools/prompt_check.py --section Outcome drafts/NN-slug/task.md
```

Then read the explanation aloud once. The form's reviewers read it as closely as the prompt.

## 5. Hand over

Lead with the verdict and the recommendation. Then what the model caught, the flaws with their
figures, and the human's next step: submit from `task.md`, or run
`/revise-finance-investing-prompt NN` to harden. Nothing is submitted by this skill, and no
rating is given to a response that was not actually read.
