# 04 · Brightline wage repricing

**Status:** round 2, graded, ready to submit. Fill the form from the sections below, top to bottom. Everything under "Working notes" is reference only. AHT: 2 h 0 m for this round.

## Prompt

Copy the whole of `prompt.md` (in this folder) into **Your Prompt**.

## Generate response

The response is saved unedited in `result.md` (1,309 words, 2026-11-10). Nothing to paste into the form.

## Rating

Select **Terrible**.

Pretty Bad is an acceptable alternative if you want to give more weight to the renewal timing it got right. Do not select Amazing or Pretty Good.

## Explanation

The model handled the renewal timing correctly. It priced the 6.5 percent increase only from each contract's renewal month and treated attrition as lost gross profit.

It never read the clause it was given. The clause allows a price increase only when "federal, state, or local law increases the minimum wage", and only for "the resulting increase" in labor cost. Brightline's raise is voluntary, "to keep our crews", and its $18.40 base is already above Washington's minimum. The clause gives nothing, yet the response bills $356,286 of pass-through and concludes that "the pass-through clause does its job". It also bills that pass-through from February to December on every clause contract, even after renewal moves them onto the 6.5 percent pricing, which counts about $208,000 twice. It reports 2027 gross profit up $121,712 and says "Whether gross profit is up $122K or down $56K turns on the labor arithmetic".

The correct answer, on the response's own renewal convention, is a fall of $221,436, and the notices going out this week should be stopped. The likely cause is that it took the CFO's plan as given and checked only the arithmetic.

## Optional comments

Leave blank.

## AHT

**2 h 0 m** (range 1 h 40 m to 2 h 20 m) for round 2, for one person with finance experience doing it by hand. Round 1 took 2 h 10 m. The step-by-step breakdown is under Time estimate in the working notes.

## Working notes

Reference only, not for the form: the grading behind the rating, the design and worked answer, the checks, and the history.

## Time estimate (AHT)

Estimated handle time for one person with finance experience doing round 2 by hand, with no AI help.

| Step | Minutes |
| --- | --- |
| Read the round 1 response and pick the new trap | 20 to 30 |
| Recompute the answer for the revised facts (the requester's figure and the correct one) | 10 to 15 |
| Rewrite the prompt, check it, read it aloud | 15 to 20 |
| Generate and read the 1,309-word response | 10 to 15 |
| Recompute the response's figures, reconcile its +$121,712 to the correct figure, and decide the rating | 25 to 35 |
| Write the explanation | 15 to 20 |
| Fill the form and submit | 5 |
| **Total** | **100 to 140 (about 1 h 40 m to 2 h 20 m; midpoint about 2 h 0 m)** |

Round 1 took about 2 h 10 m and was graded borderline. Across both rounds the task ran about 4 h 10 m, over the three-hour budget.

## Outcome

**Major issues: the trap taken whole, and the answer's sign reversed.** The response puts 2027 gross profit up $121,712. The correct figure on its own renewal convention is down $221,436.

What the model caught (spent for this prompt family): the renewal-month build for a price increase on annual fixed-price contracts, with the 1st-of-month convention (6.5 months of capture on average); attrition at renewal with labor and supplies leaving with the account; that the lost accounts also forgo the 6.5 percent uplift; and that a 30-day notice period can push billing past January 1.

Where it went wrong:

1. **It never reads the clause's trigger (critical).** The clause covers a minimum wage increase made "by federal, state, or local law", and only "the resulting increase" in labor cost. The raise is voluntary, "to keep our crews", and every Brightline wage is above Washington's minimum. The response treats the clause as a general wage pass-through, bills $356,286 under it, and ends with "the pass-through clause does its job". It never raises the risk of sending notices that the contracts do not support.
2. **It bills the pass-through after renewal as well (critical).** It charges the wage increase from February to December on every clause contract, 11 months, then adds the 6.5 percent at renewal on the same contracts, and says the two are "sequential, not simultaneous, so there's no overlap". Stopping the pass-through at renewal leaves an average of 4.6 months of billing, $148,599. The other $208,038 is counted twice.
3. **Its conclusion is the wrong one (critical).** It reports +$121,712, about $178,000 better than the CFO's -$56,000, and tells the CFO that "Whether gross profit is up $122K or down $56K turns on the labor arithmetic". The correct answer is a fall of $221,436 on its convention, or $250,845 with renewals spread evenly. The decisive issue is the clause, not the labor arithmetic.
4. **It saves lost-account labor at the old wage (minor).** Labor saved on lost accounts is $178,163 at the 2026 rate. At the 2027 wage it is $191,373, so the response understates the savings by $13,081.
5. **Small slips and a misdirected checklist (minor).** The wage increase is $603,533 against $603,749, and the 6.5 percent capture $501,081 against $501,254. Its reconciliation table and the "What I'd Confirm" list chase notice dates, burden rates, and renewal mix, none of which moves the answer the way the clause does.

The reconciliation: the correct -$221,436, plus $148,599 of pass-through it bills before renewal, plus the $208,038 double count, less the $13,081 of understated savings, comes to about +$122,120. The remaining $408 is the response's arithmetic slips.

**Decision: submit at Terrible.** The response confirms a plan built on a clause that does not apply, reverses the sign of the 2027 answer, and would have the CFO tell the owners gross profit rises while notices go out to the 61 largest accounts. Its renewal-timing work is sound, which is why Pretty Bad is an acceptable alternative.

## Failure target

The model accepts the CFO's plan to bill the wage increase through to the 61 larger accounts from January under their wage clause, and confirms 2027 gross profit down only about $56,000. A practitioner reads the clause: it allows a price increase only for the labor cost that results from a legally required minimum wage increase. Brightline's raise is voluntary, "to keep our crews", and its lowest rate is already above the state minimum, so the clause gives no pass-through. Those contracts reprice only at renewal, like the rest, and 2027 gross profit falls by about $221,000 to $251,000. The notices going out this week should be stopped.

## Design notes

**Requester.** The CFO of a commercial janitorial company, presenting the 2027 budget to the owners on December 3. The CFO has already corrected the sales lead's full-year price figure for renewal timing and is about to present a small dip, relying on a pass-through clause in the larger contracts. All entities are fictional: Brightline Building Services and Dana.

**Facts.**

- 2026 run rate: contract revenue $14,236,800; direct labor including payroll taxes and workers' comp $8,228,870; cleaning supplies and equipment $839,971. Gross profit $5,167,959 (36.3 percent).
- Base wage from $18.40 to $19.75 on January 1 "to keep our crews", an increase of 7.337 percent, or $603,749 a year on the labor base.
- Price increase 6.5 percent at renewal. All 143 contracts are one-year terms with the price fixed until renewal, on start dates spread across the calendar. The CFO states the renewal timing and has rebuilt the figure by renewal month.
- 61 contracts, $9,174,260 of revenue (64.4 percent), carry the clause quoted in the prompt. It covers a minimum wage increase made "by federal, state, or local law", and only "the resulting increase" in direct labor cost.
- Dana sends notices this week to bill the wage increase through on those 61 from January. They move onto the 6.5 percent pricing at renewal.
- Dana expects to lose 4 percent of renewing revenue. Labor and supplies go away with a lost account.
- The CFO's figure: 2027 gross profit down about $56,000.
- Outside the prompt: Washington's 2026 minimum wage is $17.13, and the 2027 rate, indexed to inflation, stays well below $18.40. Spokane has no city minimum wage.

**Trap.** The renewal lag is no longer the test, because the CFO handles it in the prompt. The trap is a clause read for what it seems to offer rather than what it says. The clause is triggered only by a change in the law, and it passes through only the cost increase that the law causes. A voluntary raise for retention is neither. A state minimum wage rise on January 1 does not rescue it either: every Brightline wage is already above the new minimum, so the resulting increase is zero. The default a model reaches for is "your rebuild is sound, the pass-through covers the larger accounts until renewal, so a dip of about $56,000 is fair".

**Correct answer.** The clause does not apply. All 143 contracts carry the full wage increase from January 1 and reprice only at renewal, so the answer is the same as for the whole book on 6.5 percent at renewal with 4 percent attrition.

| 2027 gross profit against 2026 | Renewals spread evenly | Renewals on the 1st of each month |
| --- | --- | --- |
| Correct, no pass-through | -$250,845 | -$221,436 |
| The CFO's plan, with the pass-through | -$56,315 | -$43,118 |
| Overstatement from the clause | $194,529 | $178,318 |

The CFO's figure is computed with labor and supplies in proportion to revenue on the clause contracts. Before renewal each clause contract recovers its wage increase in full, so its gross profit is unchanged for that part of the year. After renewal every contract runs at the run rate change of +$102,059 a year. Any reasonable renewal convention is acceptable if the correct figure lands around -$220,000 to -$250,000.

A sound answer reads the clause, says it does not cover a voluntary raise, and puts 2027 at a fall of roughly a quarter of a million dollars. It tells the CFO to stop the notices: invoking a clause that does not apply on the company's 61 largest accounts invites disputes and refund claims ahead of their renewals. It may name the honest alternatives, such as asking those clients to accept an early increase by agreement, or presenting 2027 as a down year with the run rate recovering once every contract has renewed.

For grading: accepting the pass-through gives the CFO's -$56,000, the trap taken whole. Arguing that the January 1 state minimum wage increase triggers the clause, in full or in part, is the same error. Spotting that the clause fails but leaving out attrition gives -$141,053, which points the right way but misses the attrition. A response that flags the clause only as a "risk to confirm with counsel" while keeping -$56,000 as the figure to present has taken the trap.

**Adverse result.** The CFO wants to present a dip of about $56,000 that the owners will accept. The facts say the fall is about $221,000 to $251,000 and that the notices planned for this week rest on a clause that does not apply. A model that confirms the CFO's figure is gradeably wrong.

**Size.** A practitioner answers this in under an hour, inside the three-hour task budget for the round.

## Self-check

```
== submissions/04-brightline-wage-repricing/prompt.md (278 words) ==
  coded checks clean
```

Prompt length 1,728 characters, 298 words. No WARN kept. Two fixes on the read-aloud: the sentence on Dana's notices carried three independent clauses, which the heuristic missed, and was split; and the closing used "figure" and then "number" for the same quantity, now "figure" both times.

Manual rows, read aloud on 2026-11-10:

- [x] F1 CFO, for the owners, deciding what 2027 figure to present, all in the first paragraph
- [x] F3 reads as a CFO checking a rebuilt budget line before a presentation; no persona, no test-question shape
- [x] F4 stakes: an owners' presentation on December 3, and notices to the largest clients going out this week
- [x] F5 all names fictional; Spokane is the only real place
- [x] F7 no tables, headings, or bold; the clause is quoted inline as a person would paste it
- [x] D1 the answer depends on the clause wording, the reason for the raise, and the figures given
- [x] D2 the trap is in the facts: a clause triggered only by law, a raise given for retention
- [x] D3 the CFO wants a small dip; the facts give a fall about four times as large
- [x] D5 the spent renewal-lag trap is handled by the requester; the new trap is a contract reading, as no earlier task used
- [x] D6 the clause is the standard wage escalation language in service contracts; nothing exists only to trip the model
- [x] D8 one decisive question (does the $56,000 hold); under an hour for a practitioner
- [x] S2 no sentence says the raise is voluntary or that the clause fails; "to keep our crews" is the reason the CFO gives for the raise, and the clause is quoted bare
- [x] S4 no output form required
- [x] M5 serial comma in the cost-base list and in "federal, state, or local law"
- [x] M6 complete sentences
- [x] M7 spell-checked by eye; no errors found
- [x] T3 one idiom ("take back"), within the limit of one per prompt
- [x] T16 "pass-through", "clause", "gross profit" each keep one name throughout

## Revisions

- 2026-11-10, round 2. Reason: round 1 was borderline. The model caught the renewal lag and put 2027 at -$232,600 against a correct -$250,845, so the decisive question was answered right. The lag is spent. Changed: the CFO now states the renewal timing and has rebuilt the figure by renewal month. A new fact carries the trap, a wage clause on 61 contracts with $9,174,260 of revenue that Dana plans to invoke from January. The ask is now whether the CFO's -$56,000 holds, in place of the two-part question. Kept: the company, the cost base, the 6.5 percent, the 4 percent attrition, the presentation date, and the closing line. The correct 2027 figure is unchanged, because the clause gives nothing. Round 1 is in `history/` (prompt-r1.md, result-r1.md, task-r1.md) and can still be submitted at OK.

## Log

- 2026-11-10: drafted; worked answer computed under two renewal conventions and the wrong paths, coded checks clean, manual rows read; awaiting the Generate test
- 2026-11-10: Generate response saved (1,311 words) and graded. Renewal lag caught, 2027 at -$232,600 against a correct -$250,845, but the 2028 run rate given as +$320,000 against +$102,059. Borderline: lean harden, OK defensible
- 2026-11-10: round 1 archived to history/. Revised: renewal lag handed to the requester, new trap a minimum-wage pass-through clause that does not cover a voluntary raise; requester's figure -$56,315 against a correct -$250,845. Coded checks clean, manual rows read; awaiting the Generate test
- 2026-11-10: round 2 Generate response saved (1,309 words) and graded. Clause trigger never read, pass-through billed after renewal as well, 2027 put at +$121,712 against a correct -$221,436 on its own convention. Rated Terrible, recommend submit
