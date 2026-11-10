# 02 · Larchwood Fly Supply September FX correction

<!-- Copy templates/ to tasks/NN-slug/. The sections down to Step 14 are the form, numbered as the form numbers them; fill them as the workflow reaches each step. Everything under "Working notes" is for this folder only. -->

**Status:** run 1 graded 4 of 5 (criterion 4 failed as designed); Step 13 text final; Step 14 next

**Escape hatch:** no

## Step 1: Field and role


I'm a merchant settlement analyst on the finance operations team at Halvard Payments, a card processor in Missoula, Montana, so most of my work is accounting for merchant payments. On a normal day I reconcile each merchant's settlement batches to the ledger, check the fees we charged against their agreement and any amendments, and keep the rolling reserve balances up to date. I also work chargebacks and refunds with our disputes team. When a merchant leaves us, I put together the final settlement statement and a payout recommendation for my manager to approve.

<!-- Same Step 1 as task 01: the role already covers multi-currency settlement and fee checks, so the form's Step 1 and Step 2 can stay as they are. -->

## Step 2: Scenario ideas


Not rerun. The Step 1 role is unchanged from task 01, whose three ideas (MS-1, MS-2, MS-3) are recorded there. Task 02 is a new scenario designed after task 01 closed; it overlaps MS-2 only in being a fee and pricing check.

## Step 3: Scenario


One of our cross-border merchants, Larchwood Fly Supply, says its Swiss franc sales settled short in September, and Tessa, the account manager, has already told their controller we will credit the difference on the October 6 settlement. Larchwood sells in Canadian dollars, Swiss francs, euros, and pounds, and we pay them in US dollars at our reference rate less a 1.20% FX margin. I have the September multi-currency settlement detail for the account and an email thread between Tessa, our treasury and billing teams, legal, Larchwood's controller, and my manager. I need to rebuild the September conversions in an Excel workbook and write a one-page memo to Tessa that says exactly what we settle with Larchwood on October 6.

**Scenario source:** Developed a new scenario, with or without LLM assistance

## Step 4: Failure plan


What I expect the agent to miss is the Canadian dollar side. Our new reference-rate feed went live on September 1 and quotes USD/CAD and USD/CHF in market convention, as francs or Canadian dollars per US dollar, but billing kept multiplying every amount by the rate, the way the old feed worked. That is right for EUR/USD and GBP/USD. For the franc it pays Larchwood about 0.88 dollars per franc instead of about 1.14, which is the $8,420.03 shortfall they are complaining about. For the Canadian dollar it pays about 1.37 dollars per Canadian dollar instead of about 0.73, so September's CAD batches were overpaid by $69,801.70.

Larchwood has only raised the franc, and Tessa has only promised the franc credit. An agent that converts the way billing did will agree with the system on every CAD line and find nothing wrong there. An agent that answers the complaint will credit the $8,420.03 and stop.

The correct position is that the CHF shortfall and the CAD overpayment come from the same error and are settled together, which leaves Larchwood owing Halvard a net $61,381.67. The October 2 batch, which pays on October 6, carries the same error, and converted correctly it is $25,486.23, not the $33,729.66 billed. Under Sections 7.3 and 7.4, that batch and the CHF shortfall ($33,906.26 together) go against the CAD overpayment, so Larchwood receives nothing on October 6 and still owes $35,895.44, which comes out of later settlements. If the agent credits the franc shortfall alone, we pay out money we do not owe and leave $69,801.70 of overpayment uncollected, in writing, on an account that is up for renewal.

## Step 5: Plan review


Second run on 2026-11-09 (after Steps 3 and 4 were pasted): likely to trip the agent. Acted on its point about the October 6 funds: the export now runs to October 2, with that batch PENDING for October 6 and carrying the same error, and Section 7.3 says "shall recover" so the October 6 position is unique. Kept the CSV and no quote-pair column, as below.

First run on 2026-11-09: likely to trip the agent. The helper agreed that the CHF complaint and Tessa's promise give a plausible stopping point, and that reading the market-convention quotes is standard professional knowledge that can stay unstated.

- Acted on: Priya's email now also quotes Section 7.4 (set-off), so netting the CHF credit against the CAD overpayment rests on the agreement and Tessa's promise does not leave an open conflict.
- Acted on: Schedule C now states that each conversion and each margin is rounded to the cent, and the data description says the same. Other rounding orders move the totals by at most $0.03, so the rubric's money figures carry a five-cent band.
- Kept: a 36-row CSV rather than a 60 to 100 batch workbook (volume adds no judgment); no quote-pair column in the export, because the thread names the four pairs and says "market convention", which keeps the convention in the files without the export pointing at it.

## Step 6: Data-file description


A CSV export from the payments company's settlement system for merchant Larchwood Fly Supply LLC, MID 4410-3176, file name `larchwood_fx_settlements_2026-09.csv`. It opens with the system's four-line run header (export title; merchant name, MID, and agreement number; date range September 1 to October 2, 2026, run time, and user; rate source "Halvard Reference Rate" and FX margin 1.20%) and a blank line, then the column header row. One row per currency per settlement batch: ten batches (September 1, 4, 8, 11, 15, 18, 22, 25, and 29, and October 2, 2026), each with a CAD, CHF, EUR, and GBP row, so 40 rows. Columns: batch_date, currency, txn_count, gross_local, ref_rate, usd_converted, fx_margin, usd_settled, payout_date, payout_status, payout_ref. ref_rate is the reference rate exactly as the feed publishes it, in market convention, with four decimals: EUR/USD around 1.08 to 1.09, GBP/USD around 1.26 to 1.28, USD/CAD around 1.36 to 1.38, and USD/CHF around 0.87 to 0.89, moving slightly from batch to batch. For every row, usd_converted is gross_local multiplied by ref_rate and rounded to the cent, fx_margin is 1.20% of usd_converted, also rounded to the cent, and usd_settled is usd_converted less fx_margin. Gross amounts per batch: CAD 9,800 to 15,400, CHF 2,600 to 4,900, EUR 2,900 to 5,600, and GBP 1,700 to 3,600, with two decimals and no round figures. payout_date is the next business day after the batch (the Tuesday after a Friday batch). payout_status is PAID for every September batch and PENDING for the four October 2 rows, which pay on Tuesday, October 6. payout_ref looks like PO-0902-7311. Do not add a totals row, notes, a legend, or any column that names the quote convention.

## Step 6: Context-file description


A Word document named `RE Larchwood September CHF settlement.docx`, holding an email thread printed from Outlook, about 800 to 1,000 words. It opens with the print line "Printed from Outlook by Ines Calloway on Monday, October 5, 2026, most recent first." Each message carries From, Sent (weekday, date, and time), To, Cc where relevant, Subject, and Attachments where there are any. Halvard signatures carry name, title, "Halvard Payments, 220 West Front Street, Suite 400, Missoula, MT 59802", and a direct line in the 406 area code; email addresses use halvardpayments.com. Participants: Ines Calloway (Finance Operations Manager), Tessa Moreland (Account Manager, Larchwood's relationship owner), Owen Takahashi (Treasury Operations Analyst), Marisol Vega (Billing Operations Lead), Priya Raman (Senior Counsel, Commercial Contracts), and Callum Reyes (Controller, Larchwood Fly Supply LLC, Hamilton, Montana, larchwoodfly.com address). Messages, oldest to newest:

1. Friday, August 28, 2026, Owen to Marisol and Ines: the new reference-rate feed goes live on Tuesday, September 1, for all multi-currency merchants, and the old feed is retired on August 31. Mainly about cutover timing and the 4:00 PM Eastern publication time. In passing he says the new feed publishes the four pairs in market convention (EUR/USD, GBP/USD, USD/CAD, and USD/CHF), the same way the bank's trade confirmations show them.
2. Wednesday, September 2, 2026, Marisol to Owen and Ines: billing now reads the reference rates from the new feed, the September 1 batch ran on it, and nothing else in the settlement calculation changed.
3. Monday, October 5, 2026, 8:05 AM, Callum to Tessa: Larchwood's Swiss franc sales came in light all September. The franc was worth more than a dollar all month, but the settlements paid them about 88 cents per franc. He asks for the September CHF shortfall to be credited. He says the Canadian, euro, and pound settlements look fine to them. No figure.
4. Monday, October 5, 2026, 9:40 AM, Tessa to Ines, forwarding Callum's email: she has told Callum that Halvard will credit the CHF shortfall on the October 6 settlement and asks Ines for the number today. Larchwood is one of the larger cross-border accounts, and its agreement is up for renewal in January.
5. Monday, October 5, 2026, 11:20 AM, Priya to Ines: the sections Ines asked for, quoted from agreement MA-2023-0291:
   - "Schedule C, item 2. Currency conversion. Transactions presented in CAD, CHF, EUR, or GBP are converted to US dollars at the Halvard Reference Rate published for the batch date. Halvard deducts an FX margin of 1.20% of the converted amount. Each converted amount and each margin is rounded to the nearest cent."
   - "7.3 Settlement Adjustments. Halvard may correct any error in a settlement. Halvard shall recover any amount overpaid to Merchant by deducting it from subsequent settlement funds until it is repaid in full, and shall pay any amount underpaid to Merchant with the next settlement."
   - "7.4 Set-off. Halvard may set off any amount Merchant owes Halvard against any amount Halvard owes Merchant, including amounts due under Section 7.3."

Plain business email register: short paragraphs, one or two small typos, no headings inside messages, no bold notes, no summary of the thread, and no message that computes a corrected amount, mentions Canadian dollar overpayment, or says how the rates should be applied.

## Steps 7 and 8: Input files


File Builder run on 2026-11-09, downloaded as the whole archive. The two files were extracted into `inputs/` (names already matched the prompt); the archive and its `output.json` run record are in `design/filebuilder/`, with the thread's original copy.

The File Builder rebuilt the gross amounts but matched every target total: September CAD overpaid $69,801.70, CHF short $8,420.03, the October 2 batch $33,729.66 billed and $25,486.23 correct. The answer, rubric, and Step 4 stand unchanged.

Edited by hand, in the thread only:

- Serial commas in Owen's list of pairs and Callum's list of currencies [M5].
- Cleared the document properties' description field, which read "generated by python-docx" [I12]. Internal note only: kept out of the Step 14 feedback by the user's choice (2026-11-09).

Checks after the edits: `design/verify_inputs.py` passes (40 rows; every row multiplied as billing did; rates in their market-convention bands; September PAID, October 2 PENDING for October 6; thread facts present, nothing leaks); `alchemy_check.py --only inputs` is clean. ZIP built; fingerprint a512d6bb19acf948.

## Step 9: Final prompt

Copy the whole of `prompt.md` into **Your Final Prompt**.

## Step 10: Rubric


Copy the five criteria from `rubric.md`, in order, after comparing them with the Rubric Drafter's five. Paste these into the optional "which file or fact supports this criterion" column:

| # | Supporting file or fact |
| --- | --- |
| 1 | larchwood_fx_settlements_2026-09.csv: September CAD rows, usd_converted equal to gross_local times ref_rate (about 1.37). RE Larchwood September CHF settlement.docx: Owen's Aug 28 email, the four pairs publish in market convention, including USD/CAD; Marisol's Sept 2 email, nothing else in the calculation changed. |
| 2 | larchwood_fx_settlements_2026-09.csv: September CHF rows at ref_rate of about 0.88, multiplied. RE Larchwood September CHF settlement.docx: Callum's Oct 5 email (about 88 cents per franc); Schedule C item 2 in Priya's Oct 5 email (1.20% margin, rounding to the cent). |
| 3 | larchwood_fx_settlements_2026-09.csv: October 2 rows, PENDING, payout date Oct 6. RE Larchwood September CHF settlement.docx: Sections 7.3 and 7.4 in Priya's Oct 5 email; Tessa's Oct 5 email promising the CHF credit on Oct 6. |
| 4 | larchwood_fx_settlements_2026-09.csv: the September CAD and CHF rows and the October 2 batch. RE Larchwood September CHF settlement.docx: Section 7.3 in Priya's Oct 5 email (overpayments recovered from subsequent settlement funds until repaid in full). |
| 5 | larchwood_fx_settlements_2026-09.csv: EUR and GBP rows at ref_rate of about 1.08 and 1.27. RE Larchwood September CHF settlement.docx: Owen's Aug 28 email names EUR/USD and GBP/USD in market convention. |

## Steps 11 and 12: Attempting Agent run and grading

Each run is recorded in runs/run-N.md.

- Run 1, 2026-11-09, fingerprint a512d6bb19acf948: passed 4 of 5. Caught the quote convention, both September figures, and the $0.00 October 6 payout; failed criterion 4 by reporting $44,138.87 still owed instead of $35,895.44 (double-counted the pending October 2 batch). Verdict: a substantive calculation error that carries into the recovery; submittable.

## Step 13: Failure description

The agent found the conversion error and got the October 6 payout right at $0.00, but it overstated what Larchwood still owes by $8,243.43, which criterion 4 captures. Its memo tells Tessa that Larchwood owes $44,138.87 after the October 6 settlement. The correct figure is $35,895.44.

The error is a double count of the October 2 batch. In larchwood_fx_settlements_2026-09.csv that batch is PENDING and pays on October 6, so nothing has been paid on it yet. The agent took the $8,243.43 gap between the billed $33,729.66 and the corrected $25,486.23 as money Larchwood owed us, added it to the September net of $61,381.67 to get $69,625.10, and then also set the corrected $25,486.23 against that total. A billing error on an unpaid batch is corrected once, by paying the right amount. Under Sections 7.3 and 7.4 quoted in RE Larchwood September CHF settlement.docx, the corrected batch and the $8,420.03 September CHF shortfall, $33,906.26 together, go against the $69,801.70 CAD overpayment, which leaves $35,895.44.

The memo is the figure Tessa takes to Larchwood's controller and the basis for recovering from later settlements. Acting on it, we would deduct $8,243.43 that Larchwood does not owe from a large account that is up for renewal, and the controller would find the gap as soon as he reconciles the October settlements.

## Step 14: Time spent

<!-- The actual time spent, from the Log: Less than 2 hours / 2 to 4 hours / 4 to 6 hours. -->

## Step 14: Feedback and comments


The training was clear, and the plan-review helper gave useful comments each time I ran it. A few things in the tools needed fixing by hand. On my first scenario, the Rubric Drafter's first criterion named a merchant, Briarstone Marine Supply, that appears in neither input file, so I replaced all five criteria. The File Builder did not use the reference table I pasted into the data-file description and rebuilt the rows itself, although it kept the totals the description named. It also gave every email address a placeholder .example domain, which I corrected before uploading. It would help if the File Builder said when it set aside part of a description.

## Working notes

Reference only, not for the form.

## Correct answer



Computed by `design/answer.py` on the reference data. After the File Builder runs, `design/answer.py --inputs` recomputes from the shipped CSV, and the figures here and in the rubric are replaced with those.

September (PAID batches):

| Currency | Gross local | USD settled | USD correct (after 1.20% margin) | Difference |
| --- | --- | --- | --- | --- |
| CAD (USD/CAD, divide) | 110,507.38 | 149,524.95 | 79,723.25 | −69,801.70 overpaid |
| CHF (USD/CHF, divide) | 32,070.17 | 27,753.85 | 36,173.88 | +8,420.03 underpaid |
| EUR (EUR/USD, multiply) | 33,971.86 | 36,401.68 | 36,401.68 | 0.00 |
| GBP (GBP/USD, multiply) | 27,454.24 | 34,537.49 | 34,537.49 | 0.00 |
| **Net** | | | | **Larchwood owes Halvard $61,381.67** |

October 6 settlement (the PENDING October 2 batch):

| Item | USD |
| --- | --- |
| October 2 batch as billed (multiplied) | 33,729.66 |
| October 2 batch converted correctly | 25,486.23 |
| Plus the September CHF shortfall (7.3, paid with the next settlement) | +8,420.03 |
| Funds due on October 6 before recovery | 33,906.26 |
| Less the September CAD overpayment, up to the funds available (7.3 shall recover, 7.4 set-off) | −33,906.26 |
| **October 6 payout to Larchwood** | **0.00** |
| **Still owed by Larchwood after October 6** | **35,895.44**, deducted from later settlements |

Likely wrong answers: pay the October 2 batch as billed plus the CHF credit ($42,149.69); pay the corrected batch plus the CHF credit with no recovery ($33,906.26); credit the CHF shortfall only and leave $69,801.70 uncollected; convert every currency by multiplying, as billing did (no difference found anywhere); convert every currency by dividing (EUR and GBP also look wrong).

## Design


**Requester and decision.** Ines Calloway, Finance Operations Manager, hands the correction to the analyst. It decides what Tessa tells Larchwood's controller today and what the October 6 settlement carries.

**Judgment call.** The quote convention. Nothing in either file says to divide for USD/CAD and USD/CHF; the thread only says the new feed publishes "in market convention". A professional knows USD/CAD and USD/CHF are quoted as foreign units per US dollar.

**Dependency.** The convention decides the CAD and CHF corrections and the October 2 batch, and those decide the October 6 payout and the balance carried forward.

**Split.** The export carries every amount and rate. The thread carries the feed change, the fact that billing changed nothing else, the complaint, the promise, and the agreement clauses. The answer needs both.

**Planted issues.**
- usd_converted is gross_local times ref_rate for all 40 rows, which is right for EUR and GBP and wrong for CAD and CHF.
- The PENDING October 2 batch carries the same error, so the October 6 settlement itself must be rebuilt before the recovery is applied.
- The complaint and the promise cover CHF only; Callum says the CAD settlements "look fine".
- Section 7.3 has both directions (underpayments paid, overpayments recovered), so the correct October 6 position is the net.
- No total is wrong on purpose (I10 has nothing to note).

## Hardening queue

<!-- Ideas held back for Stage 7, one lever per round. -->

## Checks

WARN kept: T11 on the Step 6 context description. The numbered entries are a dated list of messages, three of them on Monday, October 5, which is a list of record. The second T11 (three sentences opening "Halvard may") is quoted agreement text, kept verbatim.

## Runs

<!-- One line per run: date, fingerprint, criteria failed, what the agent caught and missed. Traps it caught are spent. -->

## Revisions

<!-- One dated entry per round after the first: the reason, what changed, what was kept. Earlier rounds live in history/rN/. -->

## Log

- 2026-11-09: feedback no longer mentions the python-docx properties text; that stays an internal note under Steps 7 and 8.
- 2026-11-09: Step 14 feedback drafted (optional) and checked; Step 13 text hand-read clean.
- 2026-11-09: run 1 graded: 4 of 5, criterion 4 FAIL, the grader's reason matching ours. Failure description final.
- 2026-11-09: run 1 final message: conversion, September figures, and the $0.00 October 6 payout right; remaining receivable $44,138.87 instead of $35,895.44 (double-counted the pending October 2 batch). Failure description drafted.
- 2026-11-09: Steps 7 and 8: File Builder matched every target total; thread fixed (two serial commas, generator description cleared); verifier and input checks clean; ZIP built, fingerprint a512d6bb19acf948. Support notes drafted.
- 2026-11-09: Step 5 rerun: likely to trip the agent. Acted on "what funds would otherwise settle on October 6": the export now runs to October 2 with that batch PENDING for October 6, carrying the same error; Section 7.3 says "shall recover", so the October 6 position is unique ($0.00 paid, $35,895.44 still owed). Prompt now asks for the conversions in the export. Rubric criteria 3 and 4 replaced.
- 2026-11-09: Step 5 plan review: likely to trip the agent. Added Section 7.4 set-off and the rounding rule; rubric figures banded at five cents.
- 2026-11-09: hand read: rubric criterion 5 changed from a deduction method (7.3 says "may", so invoicing is also valid) to EUR and GBP left unchanged, which catches an agent that divides every rate.
- 2026-11-09: designed after task 01 closed (its stated-fact traps were all caught). New trap: an unstated quote convention that the system and a careless agent get wrong the same way. Correct answer computed (design/answer.py); form text for Steps 1 to 6 written in the first person; prompt and rubric drafted.
