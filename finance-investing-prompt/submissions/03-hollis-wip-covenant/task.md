# 03 · Hollis WIP covenant

**Status:** round 1, graded, ready to submit. Fill the form from the sections below, top to bottom. Everything under "Working notes" is reference only. AHT: 2 h 15 m.

## Prompt

Copy the whole of `prompt.md` (in this folder) into **Your Prompt**.

## Generate response


The response is saved unedited in `result.md` (1,621 words, 2026-11-10). Nothing to paste into the form.

## Rating


Select **Terrible**.

Pretty Bad is an acceptable alternative if you want to give more weight to the claim exclusion it got right. Do not select Amazing or Pretty Good.

## Explanation


The model started well on the claim. It excluded the $140,000 delay claim that the general contractor had rejected, and it named the right rule for a loss job: book the entire expected loss now.

It then got the decisive number wrong. The prompt says Lakeview's $3,917,480 contract already includes the $96,000 approved change order, but the response adds it again ("$3,917,480 + $96,000 = $4,013,480"). That cuts Lakeview's expected loss from $185,020 to $89,020 and understates the overbilling by $67,200. It also leaves its own $26,517 loss provision out of working capital. It reports $1,348,582, tells the controller the covenant passes with "$98,582" of headroom, and says working capital "actually improves" against the draft. The correct figure is $1,225,931: booking the remaining $55,506 of Lakeview's loss puts the company $24,069 below the $1,250,000 covenant, so the certificate cannot be signed as drafted.

The likely cause is a misread of the change-order sentence, followed by a provision it named but never carried into the total. A controller acting on this would sign a false compliance certificate.

## Optional comments


Leave blank.

## AHT


**2 h 15 m** (range 1 h 50 m to 2 h 35 m) for one person with finance experience doing this round by hand. The step-by-step breakdown is under Time estimate in the working notes.

## Working notes

Reference only, not for the form: the grading behind the rating, the design and worked answer, the checks, and the history.

## Time estimate (AHT)


Estimated handle time for one person with finance experience doing this round by hand, with no AI help.

| Step | Minutes |
| --- | --- |
| Pick the failure target and design the scenario | 25 to 35 |
| Work the correct answer in a spreadsheet (WIP schedule, loss provision, covenant test) | 20 to 30 |
| Write the prompt, check it, read it aloud | 15 to 20 |
| Generate and read the 1,621-word response | 10 to 15 |
| Recompute the response's figures and decide the rating | 20 to 30 |
| Write the explanation | 15 to 20 |
| Fill the form and submit | 5 |
| **Total** | **110 to 155 (about 1 h 50 m to 2 h 35 m; midpoint about 2 h 15 m)** |

One round only, inside the three-hour budget.

## Outcome


**Major issues: the decisive answer is inverted.** The response says the covenant passes with $98,582 of headroom. The company is $24,069 short.

What the model caught (spent for this prompt family): the exclusion of a claim the counterparty has rejected in writing, under the constraint on variable consideration, with the rejection letter treated as evidence of conditions at the balance sheet date; the rule that a loss contract books its entire expected loss now; per-job underbilling and overbilling mechanics.

Where it went wrong:

1. **It counts the approved change order twice (critical).** The prompt says Lakeview's $3,917,480 contract includes the $96,000 change order. The response writes "$3,917,480 + $96,000 = $4,013,480". That cuts the expected loss from $185,020 to $89,020, the overbilling from $207,764 to $140,753, and the remaining loss to provide from $55,506 to $26,517.
2. **It names the loss provision but leaves it out of working capital (critical).** It computes "$26,517, which should be accrued as a liability", then reports working capital of $1,348,582 without it. Its bottom line says that if "no loss accrual is required beyond what's already embedded, you pass and can sign", which contradicts its own Issue 1. Even with its $26,517 booked, its figures give $1,322,065, still a pass.
3. **Its conclusion is the wrong one (critical).** It answers "Yes, $1,348,582 vs. $1,250,000 minimum" and says working capital "actually improves" against the draft by $67,145. The correct working capital is $1,225,931, which is $55,506 below the draft and $24,069 below the covenant. The controller should not sign the certificate as drafted and should go to the bank before the 20th.
4. **A mis-cited standard (minor).** It cites ASC 340-40, which covers contract costs, for the loss provision. The guidance on provisions for losses on construction contracts sits in ASC 605-35.
5. **Small slips.** Percent complete is rounded to 70.07, 69.99, and 22.00 percent, which moves earned revenue by a few hundred dollars per job, and a false start is left in the answer before the loss figure.

**Decision: submit at Terrible.** The response gives the wrong answer to the question asked, and a controller acting on it would sign a compliance certificate that misstates the covenant to the bank. It got the claim right and named the loss rule, which is why Pretty Bad is an acceptable alternative.

## Failure target

The model runs every job on cost-to-cost percent complete, as the controller does, so the losing Lakeview job books only the 70 percent of its loss earned to date. Or it counts the project manager's $140,000 delay claim as contract value, which shrinks the loss. Either way it confirms the covenant passes. A practitioner books the whole expected loss on Lakeview now and leaves out a claim the general contractor has rejected in writing. On that basis working capital is $1,225,931, so the covenant fails by $24,069 and the certificate cannot be signed as drafted.

## Design notes

**Requester.** The controller of a commercial electrical contractor, preparing the quarterly covenant package and compliance certificate for the bank, due on the 20th. The controller has a draft showing a pass and plans to sign it. All entities are fictional: Hollis Electric, Morrow Construction, and the jobs.

**Facts.**

| Job | Contract | Cost to date | Est. cost to complete | Billed to date |
| --- | --- | --- | --- | --- |
| Westfield Middle School | 2,483,650 | 1,433,700 | 612,300 | 1,612,000 |
| Lakeview Distribution Center | 3,917,480 | 2,871,750 | 1,230,750 | 2,950,000 |
| Riverside Medical Office | 1,126,400 | 206,500 | 732,200 | 337,900 |

- Lakeview's contract includes a $96,000 change order approved in August (original contract $3,821,480).
- Lakeview delay claim of $140,000, submitted by the project manager and rejected in full by the general contractor's letter of October 22. Nothing further filed.
- Covenant: working capital of at least $1,250,000 at September 30, with contract assets and liabilities from the WIP schedule.
- Outside the WIP: current assets $3,412,600, current liabilities $1,961,666.
- The controller's draft: $1,281,437, which is percent complete on every job and no loss provision.

**Trap.** Two, and each one alone flips the answer to a pass. First, percent complete applied to a loss job recognizes only the share of the loss earned to date. The rule for a loss contract is to recognize the entire expected loss when it becomes evident. The controller's "for every job, which is how our CPA set us up" invites the model to keep the method. Second, the $140,000 claim would cut Lakeview's loss and add revenue, and the project manager is "confident". The general contractor has rejected it in writing. Nothing has been filed since, so including it fails the constraint on variable consideration. The default a model reaches for is "your WIP ties, you pass by about $31,000, maybe more if the claim comes through".

**Correct answer.**

| Job | Percent complete | Earned revenue | Billed | Over or under billed | Gross profit to date |
| --- | --- | --- | --- | --- | --- |
| Westfield | 70.0733% | $1,740,375.86 | $1,612,000 | underbilled $128,375.86 | +$306,675.86 |
| Lakeview | 70.0000% | $2,742,236.00 | $2,950,000 | overbilled $207,764.00 | -$129,514.00 |
| Riverside | 21.9985% | $247,791.20 | $337,900 | overbilled $90,108.80 | +$41,291.20 |

Lakeview's estimated total cost is $4,102,500 against a contract of $3,917,480, an expected loss of $185,020. Percent complete has recognized $129,514 of it. The remaining $55,506 is booked now as a provision for loss on the contract, a current liability.

| Working capital at September 30 | Draft | Correct |
| --- | --- | --- |
| Current assets outside the WIP | $3,412,600.00 | $3,412,600.00 |
| Underbillings (contract asset) | $128,375.86 | $128,375.86 |
| Current liabilities outside the WIP | -$1,961,666.00 | -$1,961,666.00 |
| Overbillings (contract liability) | -$297,872.80 | -$297,872.80 |
| Provision for loss on Lakeview | 0 | -$55,506.00 |
| **Working capital** | **$1,281,437.06, passes by $31,437** | **$1,225,931.06, fails by $24,069** |

The two wrong paths, for grading: with the claim included and the full loss booked, working capital is $1,365,931, a pass by $115,931. With the claim included on percent complete, it is $1,379,437, a pass by $129,437.

A sound answer finds the breach, says not to sign the certificate as drafted, and recommends going to the bank before the 20th for a waiver or an amendment. The underbillings and overbillings can be shown per job or netted, as long as working capital comes out at $1,225,931. Presenting the loss provision as a reduction of a contract asset rather than a separate liability is acceptable, since the working capital effect is the same.

**Adverse result.** The controller wants to sign a passing certificate. The facts say the company is in breach, and that only an unsupported claim or an incorrect method makes it pass. A model that confirms the pass is gradeably wrong. Endorsing a certificate that relies on the rejected claim would be more serious still.

**Size.** A practitioner answers this in about an hour, inside the three-hour task budget.

## Self-check

```
== submissions/03-hollis-wip-covenant/prompt.md (209 words) ==
  coded checks clean
```

Prompt length 1,453 characters, 231 words including the pasted rows. No WARN kept.

Manual rows, read aloud on 2026-11-10:

- [x] F1 controller, for the bank's covenant package, deciding whether to sign the compliance certificate, all in the first paragraph
- [x] F3 reads as a controller asking for a review before signing; no persona, no test-question shape
- [x] F4 stakes: a signed certificate to the bank by the 20th, with $31,437 of headroom on the draft
- [x] F5 all names fictional; Indianapolis is the only real place
- [x] F7 the WIP rows are tab-separated, as pasted from the workbook; no markdown
- [x] D1 the answer depends on the job figures, the claim history, and the balances given
- [x] D2 the trap is in the facts: a job whose estimated cost exceeds its contract, a uniform method the controller is proud of, a confident project manager against a written rejection
- [x] D3 the controller wants to sign; the facts say breach
- [x] D5 new use case (bookkeeping compliance) and new reasoning path; none of the spent traps from earlier tasks
- [x] D6 every figure is one a controller holds for this package
- [x] D8 one decisive question (do we meet the covenant); about an hour for a practitioner
- [x] S2 no sentence says Lakeview loses money or that the claim fails; the estimated cost and the rejection letter are bare facts
- [x] S4 no output form required
- [x] M5 no list of three in running prose
- [x] M6 complete sentences
- [x] M7 spell-checked by eye; no errors found
- [x] T3 one idiom ("a second set of eyes"), within the limit of one per prompt
- [x] T16 "covenant", "claim", "certificate" each keep one name throughout

## Revisions

<!-- One dated entry per round after the first. -->

## Log

- 2026-11-10: drafted; worked answer computed for the correct path and both wrong paths, coded checks clean, manual rows read; awaiting the Generate test
- 2026-11-10: Generate response saved (1,621 words) and graded. Change order counted twice, loss provision left out of working capital, covenant called a pass at $1,348,582 against a correct breach at $1,225,931. Rated Terrible, recommend submit
