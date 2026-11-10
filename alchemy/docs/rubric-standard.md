# Rubric standard

How to write criteria a Grading Agent applies the same way every time. Read this before the
first criterion and again before pasting the final five into the form. Rule ids are in
`rules.md`; the training's own rubric rules are in `../training/project-guidelines.md`.

The grader sees only two things: the criterion, and the agent's final response with its output
files. It never sees your correct answer, your design notes or, reliably, the input files. Every
criterion has to stand on that.

## The shape

**Subject + verb + expected value or decision.**

| Weak | Why | Strong |
| --- | --- | --- |
| The response should identify the correct root cause. | "should", "correct", no value | The memo attributes the $48,210 variance to the freight rate change effective July 1. |
| The workbook calculates leverage accurately. | "accurately" names no figure | The workbook reports a Q3 2026 total leverage ratio of 3.42x. |
| The analysis handles the cancelled contract appropriately. | "appropriately" is a judgment, not a check | The revised run claws back $7,215 of commission from Dana Ruiz for the cancelled Pinecrest contract. |
| The model will miss the amendment. | A prediction, not a property of the deliverable | The memo applies the $250,000 add-back cap from the March 2026 amendment. |

The subject is the deliverable or a named part of it ("The memo", "The revised schedule", "The
workbook"), never "the response", "the agent" or "the model" [R6, R8].

## The five properties

1. **Atomic** [R2]. One check per criterion. A criterion that needs "and" to join two claims is
   two criteria. A list of values that one decision produces together can stay in one criterion
   when they pass or fail together ("credits the renewal to Bell only, not to both Bell and
   Ruiz").
2. **Self-contained** [R3, R12]. The value, name, date or decision is written into the
   criterion. "The correct rate per the context file" fails, because the grader has to go and
   find the rate.
3. **Clear** [R4, R7]. One reasonable reading. No vague grading words: correct, appropriate,
   adequate, reasonable, comprehensive, properly. Write the value instead.
4. **Generalizable** [R5]. Any correct response passes. Do not name a cell, tab, column, formula,
   section order or exact wording unless the prompt asked for it. A memo that reaches the right
   decision in a different layout passes.
5. **Comprehensive** [R10]. Across the set, every material point that could make the answer
   wrong is checked, and at least one criterion catches the targeted failure directly.

## Write the basis in

A figure with its source-side basis in the same sentence is both self-contained and hard to
pass by accident:

- "The statement credits Kestrel $273.85 for fees overcharged at 2.90% on the five batches from
  September 15 to 21, 2026."
- "The reconciliation assigns the $18,400 wire to October by value date, not by the September 30
  booking date."
- "The accrual includes the $6,215.40 vendor credit for September usage even though the credit
  note is dated October 7."

Judgment words get anchored to a definition: "the largest exposure" becomes "the borrower with
the highest outstanding balance at September 30, 2026". Any basis written in must re-derive to the figure exactly
[R15].

## Shapes that get a criterion returned

| Shape | Why it is returned | Fix |
| --- | --- | --- |
| Four figures, or a total and its parts, in one criterion | Not atomic | One figure per criterion; each figure in one criterion only [R13] |
| "on the Summary tab", then "or equivalent" | A mandated layout, then a hedge | Say what the deliverable shows; drop where |
| "roughly two more weeks of cover" | A hedge | The figure or a band in figures [R7] |
| "each of its 6 recommendations" | A count the prompt never fixed | Grade the content of the actions that matter [R5] |
| "credit here is for", "is not this defect" | Grader instructions | State the property of the deliverable [R14] |
| "the flagged items", "clean exposure" | Undefined: the grader cannot tell which | Name them, or define the term inline [R3] |
| A label or name that exists only in your worked answer | Not grounded in the files | Use the files' own terms [I15] |
| Two criteria that disagree on a class of item | Contradiction | One rule, with the carve-out written in |

## Pin what the files force; leave open what the prompt leaves open

The two failure modes of a rubric pull against each other:

| A criterion that... | lets through... | so it must... |
| --- | --- | --- |
| checks a total, a count or a sample | a wrong answer whose errors offset | pin the values the files uniquely determine |
| pins a figure that a valid choice moves | nothing wrong, but fails a correct answer reached another way | grade the decision, or band the figure |

The rule: **pin every value the files uniquely determine; where the prompt leaves a choice
open, grade the decision and the figure that choice produces, not one fixed number.**

- **Totals do not prove members.** A correct total can hide two offsetting errors. When the
  answer has one value per item (per rep, per loan, per account), the criterion that matters
  is the item the targeted failure moves, with its value.
- **Closed sets get an exact-membership criterion.** If the files define which items are in
  ("which of the six facilities breach"), check the exact set: "The memo identifies exactly
  Facilities B and E as in breach of the DSCR covenant."
- **Bands on convention-moved figures.** Where a legitimate rounding or day-count convention
  moves a figure slightly, write the band in words: "a fixed charge coverage ratio between
  1.17x and 1.19x". Where only one route reaches the figure, keep it exact.
- **Either-or decisions are bound on both branches.** "The memo either declines the waiver, or
  grants it conditioned on a cure of at least $162,600 of EBITDA."
- Run the variants in your correct-answer script before wording a criterion: other rounding
  orders, another defensible reading of an ambiguous clause. Pin only what holds under all of
  them.

## Test each criterion against a wrong answer

For every criterion, ask two questions:

1. **If the deliverable had this wrong, would the criterion fail it?** If a model that took the
   trap still passes, the criterion is too loose.
2. **If a different correct deliverable came in, would the criterion pass it?** If a correct
   answer in a different layout or by a different valid method fails, the criterion is too
   tight.

Then grade your own correct answer against all five. It must pass every one.

## Grade every part of the ask

Each thing the prompt asks for is graded by at least one criterion [R16]. If the prompt asks for
a statement and a memo, both are graded; if it says the deliverable must hold up to a challenge,
a criterion checks the point most likely to be challenged. With only five criteria, spend them
on the targeted failure and the figures it moves, then on each remaining part of the ask.

## What to leave out

- Cosmetic checks: fonts, colors, bold, layout, tone, spelling [R9].
- Restatements of the prompt ("The deliverable is a workbook") unless the file itself is the
  point, and even then attached to content ("The workbook reports...").
- Predictions about the agent [R8].
- References to your gold-standard answer, an "expert answer" or "the context file" [R12].
- Two criteria that score the same thing [R13].

## For the full task (Phase 2)

The full task needs at least 20 criteria. The same properties hold. A larger rubric also has to
reach the parts of a document a short one skips: the order the prompt asks for (the
recommendation before the support), the separations it names (received versus invoiced), the
arithmetic shown. Write these as checkable properties, never as quality adjectives. Check the
count with `--full`.

## Checks

```
python3 tools/alchemy_check.py tasks/NN-slug --only rubric
```

Fix every ERROR. Every WARN needs a read. A vague word inside a quoted figure label may stand;
note why in `task.md`. Then do the two-question test on each criterion by hand. No script can
do it.
