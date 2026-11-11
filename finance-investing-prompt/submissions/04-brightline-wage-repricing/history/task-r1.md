# 04 · Brightline wage repricing

**Status:** round 1, graded: borderline. The recommendation is to harden, and OK is defensible if you submit. Fill the form from the sections below, top to bottom. AHT: 2 h 10 m.

## Prompt

Copy the whole of `prompt.md` (in this folder) into **Your Prompt**.

## Generate response

Already done. The response is saved unedited in `result.md` (1,311 words, 2026-11-10). Nothing to paste into the form.

## Rating

Select **OK** if you submit this round.

The recommendation is to harden instead, because the response gets the 2027 answer right. The reasoning is under Outcome. Do not select Pretty Bad, Terrible, Amazing, or Pretty Good.

## Explanation

The model caught the main point. It saw that the wage increase runs from January 1 while each contract reprices only at renewal, and it put the 2027 change at about -$232,600, close to the correct -$250,845 with renewals spread evenly. Its 10.3 percent to hold 2027 is near the correct 10.2 percent.

The decisive mistake is the figure it tells the CFO to present for the following year. It says the company recovers "to a full-year benefit of roughly +$320,000 in 2028" and closes on "a $320,000 improvement in 2028" as the number to stand behind. That is the full-year price increase less the wage increase with no attrition, which is the shortcut the CFO started from. On the response's own 4 percent attrition, the run rate once every contract has renewed is +$102,059, about a third of what the owners would be told. Every contract has also renewed by the end of 2027, not "sometime in 2028".

Smaller slips: it never removes the price increase on the accounts that leave, which overstates 2027 by about $18,500, and its 10.3 percent divides by an attrition haircut it had already counted.

The likely cause is that it worked attrition into the 2027 bridge but went back to the requester's figures for the run rate.

## Optional comments

Leave blank.

## AHT

**2 h 10 m** (range 1 h 45 m to 2 h 30 m) for one person with finance experience doing this round by hand. The step-by-step breakdown is under Time estimate in the working notes.

## Working notes

Reference only, not for the form: the grading behind the rating, the design and worked answer, the checks, and the history.

## Time estimate (AHT)

Estimated handle time for one person with finance experience doing this round by hand, with no AI help.

| Step | Minutes |
| --- | --- |
| Pick the failure target and design the scenario | 25 to 35 |
| Work the correct answer in a spreadsheet (renewal timing, attrition, labor and supplies) | 15 to 25 |
| Write the prompt, check it, read it aloud | 15 to 20 |
| Generate and read the 1,311-word response | 10 to 15 |
| Recompute the response's figures and decide the rating | 20 to 30 |
| Write the explanation | 15 to 20 |
| Fill the form and submit | 5 |
| **Total** | **105 to 150 (about 1 h 45 m to 2 h 30 m; midpoint about 2 h 10 m)** |

One round so far. A second round, if this one is hardened, adds roughly 1 h 30 m to 2 h and takes the task over the three-hour budget.

## Outcome

**Borderline: right on the 2027 answer, wrong on the run rate it tells the owners to expect.**

What the model caught (spent for this prompt family): that a price change on fixed-price annual contracts takes effect only at each renewal while a wage change hits the whole cost base on one date; the half-year convention for renewals spread across the calendar; attrition as lost gross profit with labor and supplies leaving with the account; the 2027 change of about -$232,600 against a correct -$221,436 to -$250,845; the price needed to hold 2027, 10.3 percent against a correct 10.2 percent; and the advice to tell the owners 2027 is a down year.

Where it went wrong:

1. **The run rate is the trap figure (material).** It tells the CFO to present "a full-year benefit of roughly +$320,000 in 2028" and closes on "a $320,000 improvement in 2028". That is $925,392 of price less $603,749 of wages, the full-year shortcut with no attrition ($321,643). On its own 4 percent attrition the run rate is +$102,059. The owners would be told to expect about three times the real payoff.
2. **It dates the full repricing to 2028 (minor).** Every one-year contract renews once during 2027, so the book is fully repriced by December 31, 2027, not "sometime in 2028".
3. **It keeps the price increase on lost accounts (minor).** The $462,696 uplift is on the whole book, and the $284,736 of lost revenue is at the old price. The uplift on the accounts that leave, $18,508, is never removed, so 2027 shows -$232,337 against -$250,845 on the same convention. It still lands inside the acceptable range.
4. **Its required rate double-counts attrition (minor).** It adds the $103,300 attrition drag and then divides by 0.95 for attrition again. Without the second haircut its method gives 9.8 percent. The 10.3 percent it reports is close to the correct 10.2 percent by offset.
5. **Unsupported and muddled lines (minor).** A table row on "cost increase from price increase on surviving accounts" carries no figure and no meaning, Option B's sentence on the mid-year review does not parse, and the claim that a Q1-heavy renewal schedule shifts the analysis by $80,000 to $120,000 is not worked.

**Decision: borderline, lean harden.** The decisive question was the 2027 effect, and the response answers it correctly with the right reasoning. Its answer to whether 6.5 percent is right is also correct in direction. On the platform's scale that reads as right on the whole, so the recommendation is to harden. OK is defensible: the closing "number you can stand behind" pairs the right 2027 figure with a run rate overstated by $219,584, and an owner acting on it would expect a recovery the facts do not support. The renewal-lag trap is now spent. A second round on this scenario would need a different trap, such as wage pass-through clauses on part of the book or a renewal schedule bunched in a way the half-year convention misstates. A new task in an unused use case is likely cheaper under the three-hour budget.

## Failure target

The model applies the 6.5 percent increase to a full year of revenue, as the sales budget and the CFO do, and confirms the company comes out about $320,000 ahead in 2027. A practitioner sees that the wage increase hits every crew on January 1, while each fixed-price contract reprices only at its own renewal date. Spread across the calendar, renewals put about half of 2027's revenue at the new price, so 2027 gross profit falls by about $220,000 to $250,000 against 2026, even though 6.5 percent is enough once every contract has renewed.

## Design notes

**Requester.** The CFO of a commercial janitorial company, presenting the 2027 budget to the owners on December 3 and about to tell them the price increase more than covers the wage increase. Dana, who runs sales, built the revenue side. All entities are fictional: Brightline Building Services and Dana.

**Facts.**

- 2026 run rate: contract revenue $14,236,800; direct labor including payroll taxes and workers' comp $8,228,870 (57.8 percent of revenue); cleaning supplies and equipment $839,971 (5.9 percent). Gross profit $5,167,959 (36.3 percent).
- Base wage from $18.40 to $19.75 on January 1, an increase of 7.337 percent. Payroll taxes and comp move with it.
- Price increase 6.5 percent. Almost all of 143 contracts are one-year terms with the price fixed for the year, renewing on start dates spread across the calendar.
- Dana expects to lose 4 percent of renewing revenue to the increase. Labor and supplies are scheduled job by job and go away with a lost account.
- Dana's budget: the increase adds about $925,000 (6.5 percent of $14,236,800). The CFO's check: the wage increase is about $604,000 (7.337 percent of $8,228,870), so about $320,000 ahead.

**Trap.** Both figures in the requester's check are full-year figures. The wage cost is full-year because it starts on January 1 for every crew. The price figure is not, because no contract reprices until it renews. With renewals spread evenly, the average contract spends half of 2027 at the old price. The sales budget and the CFO's own arithmetic invite the model to accept $925,000 against $604,000. The default a model reaches for is "you are about $320,000 ahead, net of a little attrition".

**Correct answer.** With renewals spread evenly, half of 2027 runs at the old price and half at the new price on 96 percent of the book.

| 2027 against 2026 | Renewals spread evenly | Renewals on the 1st of each month |
| --- | --- | --- |
| Revenue | +$159,452 | +$172,740 |
| Direct labor | +$427,096 | +$412,375 |
| Supplies | -$16,799 | -$18,199 |
| **Gross profit** | **-$250,845** | **-$221,436** |

Revenue for evenly spread renewals is $14,236,800 x (0.5 + 0.5 x 0.96 x 1.065). Labor is $8,228,870 x 1.07337 x (0.5 + 0.5 x 0.96), and supplies $839,971 x (0.5 + 0.5 x 0.96). Any reasonable renewal convention is acceptable if it lands the 2027 change somewhere around -$220,000 to -$250,000.

Is 6.5 percent the right number? It is enough for the run rate: once every contract has renewed, gross profit is $102,059 above 2026. It does not hold 2027, which would need about 10.2 percent at renewal, and that figure assumes attrition stays at 4 percent at a higher increase, which it likely would not. A sound answer tells the CFO 2027 gross profit falls by roughly a quarter of a million dollars, explains the renewal lag, and keeps 6.5 percent as the run-rate price. It then names the levers for 2027: wage pass-through or surcharge clauses where contracts allow, earlier repricing on renewals that fall early in the year, or telling the owners about the dip now.

For grading: ignoring the lag and applying attrition to the whole book gives +$102,059, the run-rate answer presented as 2027. Applying the lag but ignoring attrition gives -$141,053, which points the right way but misses the attrition. Accepting the requester's +$320,000 is the trap taken whole.

**Adverse result.** The CFO wants to tell the owners the company comes out ahead. The facts say 2027 gross profit falls by about $220,000 to $250,000. A model that confirms the gain is gradeably wrong.

**Size.** A practitioner answers this in under an hour, inside the three-hour task budget.

## Self-check

```
== submissions/04-brightline-wage-repricing/prompt.md (207 words) ==
  coded checks clean
```

Prompt length 1,269 characters, 226 words. No WARN kept. One clause removed on the read-aloud: "and the new wage applies to every crew from January 1" sat next to the renewal dates and set the two side by side for the model. The January 1 date is already in the first paragraph.

Manual rows, read aloud on 2026-11-10:

- [x] F1 CFO, for the owners, deciding what the 2027 budget says, all in the first paragraph
- [x] F3 reads as a CFO checking a budget line before a presentation; no persona, no test-question shape
- [x] F4 stakes: an owners' presentation on December 3 and a figure the CFO does not want to retract
- [x] F5 all names fictional; Spokane is the only real place
- [x] F7 no tables, headings, or bold; the figures are in sentences
- [x] D1 the answer depends on the contract terms, the cost base, and the attrition given
- [x] D2 the trap is in the facts: a cost that starts on one date for everyone, a price that starts at each renewal, two full-year figures set against each other
- [x] D3 the CFO wants a gain; the facts give a loss in 2027
- [x] D5 new use case (pricing) and new reasoning path; none of the spent traps from earlier tasks
- [x] D6 every figure is one a CFO holds for this budget
- [x] D8 one decisive question (the 2027 gross profit effect); under an hour for a practitioner
- [x] S2 the prompt never says the price lags; it gives the contract term and the renewal pattern as bare facts, and the January 1 wage date only once
- [x] S4 no output form required
- [x] M5 serial comma in the cost-base list
- [x] M6 complete sentences
- [x] M7 spell-checked by eye; no errors found
- [x] T3 one idiom ("take back"), within the limit of one per prompt
- [x] T16 "price increase", "wage increase", "gross profit" each keep one name throughout

## Revisions

<!-- One dated entry per round after the first. -->

## Log

- 2026-11-10: drafted; worked answer computed under two renewal conventions and the wrong paths, coded checks clean, manual rows read; awaiting the Generate test
- 2026-11-10: Generate response saved (1,311 words) and graded. Renewal lag caught, 2027 at -$232,600 against a correct -$250,845, but the 2028 run rate given as +$320,000 against +$102,059. Borderline: lean harden, OK defensible
