# 01 · Kestrel Ridge final merchant settlement

<!-- Copy templates/ to tasks/NN-slug/. The first sections are the form, in the form's order; fill them as the workflow reaches each step. Everything under "Working notes" is for this folder only. -->

**Status:** closed 2026-11-09 after run 2 passed 5 of 5; replaced by task 02 (new scenario); prompt and rubric drafted; waiting on File Builder

**Escape hatch:** no

## Step 1: Field and role

I'm a merchant settlement analyst on the finance operations team at Halvard Payments, a card processor in Missoula, Montana, so most of my work is accounting for merchant payments. On a normal day I reconcile each merchant's settlement batches to the ledger, check the fees we charged against their agreement and any amendments, and keep the rolling reserve balances up to date. I also work chargebacks and refunds with our disputes team. When a merchant leaves us, I put together the final settlement statement and a payout recommendation for my manager to approve.

## Step 2: Scenario ideas

The scenario helper returned three ideas on 2026-11-09, after Kestrel was designed, all in settlement and fees (which confirms the Step 1 text lands):

- MS-1: settlement reconciliation after a funding cutoff change (double-posted batch, returned payout marked completed).
- MS-2: fee adjustment with a midmonth pricing amendment.
- MS-3: final settlement with unresolved disputes and reserve exposure.

Kestrel was not taken from them. It overlaps MS-3 and MS-2 because Step 1 already described this job. Unused ideas are in the Hardening queue under Working notes.

## Step 3: Scenario

One of our merchants, Kestrel Ridge Outfitters, ended its processing agreement with us on September 30, 2026, and I have to close out the account. Darren, the account manager, has already told their CFO she will have the final settlement figure by Friday, October 9. I have the settlement export for September and the first two days of October, plus an email thread between Darren, our billing team, legal, and my manager. The thread quotes the reserve, termination, and set-off sections of the merchant agreement, and it also has the date billing loaded the fee amendment Kestrel signed in August. I need to produce the final settlement statement as an Excel workbook and a one-page memo to Darren that says what we pay Kestrel now and what happens to their reserve.

**Scenario source:** Developed a new scenario, with or without LLM assistance

## Step 4: Failure plan

What I expect the agent to miss is the payout that came back. The export still shows the September 28 payout, PO-0929-5628, as PAID, but treasury's October 2 email lists it on the ACH returns file with return code R02, which means the account it went to is closed. That $22,238.43 is back in our clearing account and is owed to Kestrel again, so the final payout is $41,316.27, not $19,077.84.

The reserve is the other judgment. The export shows a $1,371.86 release scheduled for October 1, and Darren has told Kestrel's CFO that the rest of the reserve will keep coming back on the normal 90-day schedule. Section 11.4 of the merchant agreement holds everything in the reserve at termination, including releases scheduled after that date, for 180 days, so the whole $73,890.91 stays held until March 29, 2027.

The smaller items have to be right too. Only the five batches from September 15 to 21 were billed at the old 2.90% rate, so the fee credit is $273.85. The October 2 chargeback comes out of the unpaid settlement funds first. The $25 chargeback fee is not refundable, so nothing is credited back for the dispute Kestrel won.

If the agent trusts the PAID status, Darren gives Kestrel's CFO a figure in writing that is $22,238.43 short, and the returned money sits with us with no plan to send it back.

## Step 5: Plan review

Verdict on 2026-11-09: likely to trip the agent. The helper confirmed all three traps (the scheduled release and Darren's promise against Section 11.4, the fee load date, the chargeback set-off order).

- Acted on: the export now states the opening reserve balance in its run header, so the reserve reconciles from the file alone.
- Already covered: scheduled versus executed releases (payout_status), the billing load date kept as an aside, mispriced batches mixed among correct ones.
- Kept: CSV with 23 rows rather than a 30 to 45 record workbook (volume adds no judgment, and the prompt names the CSV); newest-first thread, the way Outlook prints it, with the manager on every message.

## Step 6: Data-file description

A CSV export from the payments company's merchant settlement system for merchant Kestrel Ridge Outfitters LLC, MID 4410-2287, file name `settlement_export_MID44102287_20260901_20261002.csv`. It opens with the system's four-line run header (export title; merchant name, MID, and agreement number; date range, run time, and user; the opening reserve balance of 78904.17 at September 1, the reserve rate of 10.00%, and the release lag of 90 days) and a blank line, then the column header row. One row per settlement batch: the 21 business-day batches from September 1 to September 30, 2026 (no batch on Labor Day, September 7; Monday batches carry the weekend), then a row dated October 1, 2026 for an automatic reserve release and a row dated October 2, 2026 for a chargeback. Columns: batch_date, txn_count, gross_sales, refunds, chargebacks, chargeback_fees, processing_fees, reserve_hold, reserve_release, net_settlement, reserve_balance, payout_status, payout_ref, memo. Amounts in US dollars with two decimals and no currency symbol. net_settlement equals gross_sales less refunds, chargebacks, chargeback_fees, processing_fees, and reserve_hold, plus reserve_release. reserve_balance is the running reserve after each row, starting from 78,904.17 at September 1. payout_status is PAID through the September 28 batch (each with a payout_ref such as PO-0902-4471), HELD-TERM for the September 29 and 30 batches, SCHEDULED for the October 1 release (memo "auto rsv release batch 2026-07-03"), and PENDING for the October 2 chargeback (memo "cb dsp-208813 orig txn 2026-08-18"). The memo column is terse and lowercase, the way the system writes it, for example "rfnd x2" and "cb dsp-206904". The September 24 chargeback of 1,214.00 is reversed on the September 28 batch as a negative chargeback (memo "cb reversal dsp-207561 rep won, cb fee not refunded"). processing_fees are the amounts actually charged: 2.90% of gross plus $0.30 per transaction for every batch through September 21, and 2.40% plus $0.30 from September 22. Use exactly the rows in the reference table below; do not add a totals row, notes, or a legend.

<!-- When pasting into the form, paste the paragraph above followed by the full contents of design/kestrel_settlements_reference.csv. -->

## Step 6: Context-file description

A Word document named `RE Kestrel Ridge final settlement.docx`, holding an email thread printed from Outlook, about 1,000 words. It opens with the print line "Printed from Outlook by Ines Calloway on Monday, October 5, 2026, most recent first." Each message carries From, Sent (weekday, date, and time), To, Cc where relevant, Subject, and Attachments where there are any. Signatures carry name, title, "Halvard Payments, 220 West Front Street, Suite 400, Missoula, MT 59802", and a direct line in the 406 area code. Participants at Halvard Payments: Ines Calloway (Finance Operations Manager), Darren Pike (Account Manager, Kestrel's relationship owner), Marisol Vega (Billing Operations Lead), Priya Raman (Senior Counsel, Commercial Contracts), and Owen Takahashi (Treasury Operations Analyst). Messages, oldest to newest:

1. Friday, August 14, 2026, Darren to Ines and Marisol, attachment `Kestrel_MA-2022-0417_Amendment2_signed.pdf`: Kestrel signed Amendment No. 2 to merchant agreement MA-2022-0417 after the pricing review. He pastes its operative paragraph: "1. Schedule A, item 1 is deleted and replaced with the following: Processing fee: 2.40% of the gross amount of each Transaction plus $0.30 per Transaction, for Transactions processed on or after September 15, 2026." He then quotes Schedule A item 2, which stays unchanged: "Chargeback fee: $25.00 per Chargeback, not refundable whatever the outcome of the dispute." He asks Marisol to load it.
2. Monday, August 31, 2026, Darren to Ines, cc merchant risk: Kestrel has given 30 days' written notice of termination under Section 11.1 despite the new pricing, so the Termination Date is September 30, 2026. They are moving card processing to their bank.
3. Wednesday, September 23, 2026, Marisol to Ines and Darren, mainly about closing the Kestrel MID in billing after September 30 and stopping the monthly statement fee. In passing she says the Amendment 2 rate card went live in billing yesterday, Tuesday the 22nd, and apologizes that it reached her team late.
4. Friday, October 2, 2026, 9:12 AM, Owen Takahashi (Treasury Operations Analyst) to Ines, cc Marisol, mainly about keeping Kestrel's bank instructions on file. In passing he says yesterday's ACH returns file had one Kestrel item, PO-0929-5628, return code R02, now sitting in merchant clearing, and that Kestrel must send new account details on company letterhead before treasury releases anything further.
5. Friday, October 2, 2026, 3:27 PM, Priya to Ines: the sections Ines asked for, quoted from the agreement as amended:
   - "6.2 Rolling Reserve. Halvard shall hold ten percent (10%) of the gross sales amount of each settlement batch as a reserve (the "Reserve"). Each amount held shall be released to Merchant ninety (90) days after the batch date, net of any amounts applied under Section 11.6."
   - "11.4 Reserve on Termination. Upon termination of this Agreement for any reason, all Reserve funds then held, including amounts that would otherwise be released under Section 6.2 after the Termination Date, shall be retained by Halvard until one hundred eighty (180) days after the Termination Date, after which the remaining balance, net of amounts applied under Section 11.6, shall be paid to Merchant."
   - "11.5 Final Settlement. Settlement funds not yet paid to Merchant on the Termination Date, together with any other amounts owed to Merchant under this Agreement, shall be paid within ten (10) business days after the Termination Date, net of amounts applied under Section 11.6."
   - "11.6 Set-off. Any chargeback, refund, fee or other amount owed by Merchant on or after the Termination Date shall be deducted first from settlement funds not yet paid to Merchant and then from the Reserve."
6. Monday, October 5, 2026, Darren to Ines: Gail Brennan, Kestrel's CFO, called this morning. He told her she would get the final payout along with the reserve release the system already has scheduled for October 1, and the rest of the reserve on the normal 90-day schedule. He has promised her the figure by Friday, October 9, and asks Ines to confirm the number before then.

Plain business email register: short paragraphs, replies that mention calls and the attachment, one or two small typos, no headings inside messages, no bold notes, no summary of the thread, and no message that states the final payout, the fee credit, the returned amount, or whether the reserve should be held.

## Steps 7 and 8: Input files

File Builder run on 2026-11-09. It was downloaded as the whole archive; the two files were extracted into `inputs/` (their names already matched the prompt) and the archive, with its `output.json` run record, was moved to `design/filebuilder/`.

The reference table did not reach the File Builder, so it rebuilt the 23 rows itself. It kept every amount the description named (the opening reserve, the $73,890.91 close, the $1,371.86 scheduled release, the five old-rate batches, the $273.85 overcharge) and invented the rest, including a $25.00 chargeback fee and an October 2 chargeback of $892.47. The file is internally consistent, so it was kept and the answer was recomputed from it (`design/answer_inputs.py`).

Edited by hand, in the thread only (original kept in `design/filebuilder/`):

- Every email address used the placeholder domain `halvardpayments.example` (13 times); changed to `halvardpayments.com` [I8].
- Removed "Please include the batch reconciliation and the agreement pricing check in the workbook." from Darren's October 5 email, because it pointed at the fee trap [P8, I5].

Round 2 edits to the thread (2026-11-09, round 1 copy in `history/r1/inputs/`):

- Added Owen Takahashi's treasury email (Friday, October 2, 9:12 AM): PO-0929-5628 on the ACH returns file with code R02, held in merchant clearing, new account details needed. The export is unchanged and still shows that payout as PAID.
- Added Schedule A item 2 to Darren's August 14 email: the $25.00 chargeback fee is not refundable whatever the outcome of the dispute. This settles the point run 1 failed on.

Checks after the edits: `design/verify_inputs.py` passes (arithmetic, fee rates by batch, statuses, thread facts, no leaks); `alchemy_check.py --only inputs` shows one NOTE (the File Builder's python-docx stamp on the thread).

## Step 9: Final prompt

Copy the whole of `prompt.md` into **Your Final Prompt**.

## Step 10: Rubric

Copy the five criteria from `rubric.md`, in order, replacing all five rows (round 2 changed criteria 1 and 5). Paste these into the optional "which file or fact supports this criterion" column:

| # | Supporting file or fact |
| --- | --- |
| 1 | settlement_export_MID44102287_20260901_20261002.csv: HELD-TERM batches Sept 29 ($9,705.03) and Sept 30 ($10,016.43). RE Kestrel Ridge final settlement.docx: Sections 11.5 and 11.6 in Priya's Oct 2 email. The returned payout and the fee credit are supported as in criteria 5 and 4; the Oct 2 chargeback of $892.47 and its $25.00 fee are on the export's PENDING row. |
| 2 | settlement_export_MID44102287_20260901_20261002.csv: reserve_balance of $73,890.91 at the Sept 30 close. RE Kestrel Ridge final settlement.docx: Section 11.4 in Priya's Oct 2 email retains all reserve funds, including releases scheduled after termination. |
| 3 | RE Kestrel Ridge final settlement.docx: Section 11.4 (180 days after the Termination Date) and Darren's Aug 31 email (Termination Date September 30, 2026). |
| 4 | settlement_export_MID44102287_20260901_20261002.csv: processing_fees on the Sept 15, 16, 17, 18, and 21 batches at 2.90% plus $0.30. RE Kestrel Ridge final settlement.docx: Amendment No. 2 (2.40% from Sept 15) in Darren's Aug 14 email; Marisol's Sept 23 email (rate card live Sept 22). |
| 5 | settlement_export_MID44102287_20260901_20261002.csv: Sept 28 batch, net_settlement $22,238.43, payout_ref PO-0929-5628, status PAID. RE Kestrel Ridge final settlement.docx: Owen Takahashi's Oct 2 email lists PO-0929-5628 on the ACH returns file with code R02, held in merchant clearing. |

Rubric Drafter output (2026-11-09), not used: (1) "The memo identifies Briarstone Marine Supply as the merchant whose processing agreement terminated." (a merchant name in neither file); (2) chargeback from unpaid settlement funds, no amount; (3) reserve retained until March 29, 2027, two checks in one, no amount; (4) fee credit of $273.85; (5) net payout of $19,077.84. Its figures in 4 and 5 match ours.

## Steps 11 and 12: Attempting Agent run and grading

Each run is recorded in runs/run-N.md with its output files in runs/run-N/.

- Run 1 (record in history/r1/runs/; stale after round 2, delete on the platform), 2026-11-09, fingerprint db053ecffdf3c3f7: passed 4 of 5. The agent caught every planted trap (reserve held under 11.4 including the Oct 1 release, the Sept 15 to 21 fee window, the 11.6 set-off, the already-netted Sept 30 chargeback). Criterion 1 failed only on a $25 credit for the unrefunded dsp-207561 chargeback fee, which the files leave arguable. Verdict: not a severe failure; harden.
- Run 2, 2026-11-09, fingerprint b0d2d9655f082fbe: passed 5 of 5. The agent caught the R02 returned payout and got $41,316.27 exactly, plus every earlier trap. Spent: returned payout, reserve retention, fee window, set-off order, netted Sept 30 chargeback, non-refundable fee. Verdict: harden again or use the escape hatch.

## Step 13: Failure description

<!-- Step 13. At least 50 words: what the agent did, with its figure; the file evidence and the correct expected result; the criterion numbers; why the deliverable is unusable. -->

## Step 14: Time spent

<!-- Less than 2 hours / 2 to 4 hours / 4 to 6 hours, from the Log. -->

## Step 14: Feedback and comments

<!-- Optional. Text to copy, or "Leave blank." -->

## Working notes

Reference only, not for the form.

## Correct answer

Computed by `design/answer_inputs.py` from the shipped files (round 2). Round 1's answer was $19,077.84; it is in the Revisions entry.

| Item | Amount | Basis |
| --- | --- | --- |
| Unpaid settlement at termination | $19,721.46 | HELD-TERM batches: Sept 29 $9,705.03 + Sept 30 $10,016.43 (11.5). The Sept 30 batch already nets its own $642.18 chargeback and $25.00 fee |
| Returned payout owed again | +$22,238.43 | Sept 28 batch, PO-0929-5628, still PAID in the export but on the Oct 1 ACH returns file with code R02 (Owen's Oct 2 email); "other amounts owed to Merchant" under 11.5 |
| Fee overcharge owed to Kestrel | +$273.85 | Five batches Sept 15, 16, 17, 18, and 21 charged at 2.90% instead of 2.40% (amendment effective Sept 15; billing live Sept 22). Per batch: $52.41, $43.98, $46.23, $38.41, $92.82 |
| October 2 chargeback and fee | −$917.47 | $892.47 + $25.00, deducted from unpaid settlement first (11.6) |
| dsp-207561 chargeback fee | $0.00 | Not refundable whatever the outcome of the dispute (Schedule A item 2) |
| **Final payout** | **$41,316.27** | Due within 10 business days of Sept 30: October 14, 2026, or October 15 if Columbus Day (Oct 12) is a bank holiday. Payable once Kestrel sends new account details. The rubric does not grade the date. |
| **Reserve retained** | **$73,890.91** | Balance at the Sept 30 close; the Oct 1 scheduled release of $1,371.86 is not paid (11.4) |
| **Reserve payable from** | **March 29, 2027** | 180 days after September 30, 2026, net of later set-offs |

Rounding: per-batch rounding and applying 0.50% once both give $273.85.

Likely wrong answers, from the same script: missing the returned payout gives $19,077.84 (run 1 gave $19,102.84 by also crediting the $25 fee back); crediting the dsp-207561 fee gives $41,341.27; a fee credit over every batch from Sept 15 to 30 gives $673.60; paying the Oct 1 release gives $42,688.13; deducting the Sept 30 chargeback again gives $40,649.09.


## Design

**Requester and decision.** Ines Calloway, Finance Operations Manager, hands the close-out to an analyst. The output decides the figure Darren gives the merchant's CFO on October 9 and what Halvard pays on or before October 14.

**Judgment call.** The export says PO-0929-5628 was PAID; treasury's returns note says it came back R02, so the money is owed again. Separately, the settlement system has scheduled the October 1 reserve release, and the account manager has promised it and the 90-day schedule. Section 11.4 overrides both. Nobody in the thread says so.

**Dependency.** The fee window (Sept 15 to 21 only) sets the credit; the set-off order sets where the October 2 chargeback lands; both move the final payout. The reserve decision moves the payout by $1,371.86 or $73,890.91.

**Split.** The data file carries every amount, the SCHEDULED row and the fees as charged. The context file carries the rate and its effective date, the billing load date, the contract sections and the promise to the CFO. The payout needs both.

**Planted issues.**
- The SCHEDULED reserve release on October 1 in the export, which 11.4 cancels.
- processing_fees for the Sept 15 to 21 batches at the old rate. They tie to 2.90%, so the export looks internally consistent; only the thread shows they are wrong.
- The October 2 chargeback, posted after termination, with a PENDING status that invites netting it against the reserve.
- The returned Sept 28 payout (round 2): PAID in the export, R02 on the treasury returns file, mentioned in an email about bank instructions.
- A $642.18 chargeback inside the HELD-TERM September 30 batch, already netted in that batch's net_settlement. Deducting it again is a double deduction (added by the File Builder).
- No total in the export is wrong on purpose (I10 has nothing to note).
- Realistic noise that does not change the answer: the run header, terse memos, and the September 24 chargeback reversed on September 28 (both inside PAID batches).
- The billing load date sits in an email about something else, as an aside.

## Hardening queue

Levers to use one at a time if a run passes every criterion (workflow, Stage 7):

1. Double deduction (from MS-3): a refund already netted in a September batch that the thread also lists as pending.
2. Conditional release (from MS-3): an early-release side letter whose condition is not met.
3. Category exclusion (from MS-2): the amendment's lower rate excludes one transaction category (for example, keyed transactions) that the export carries.
4. Minimum fee (from MS-2): the amendment replaces a monthly minimum-fee provision that billing still charged.
5. Returned payout (from MS-1): a September payout marked PAID that came back, so its funds are still owed.
6. Routine amendment terms (File Builder suggestion): quote Amendment 2's non-pricing terms beside the rate paragraph, so the effective date sits among ordinary clauses.

## Checks

<!-- Paste the latest alchemy_check.py output. One line for each WARN kept, saying why. Tick the MANUAL rows. -->

## Runs

<!-- One line per run: date, fingerprint, criteria failed, what the agent caught and missed. Traps it caught are spent. -->

## Revisions

- 2026-11-09, round 2. Reason: run 1 caught every planted trap (reserve, fee window, set-off, the netted Sept 30 chargeback) and failed only on a $25 chargeback-fee credit the files left arguable. Lever: a returned payout, from the hardening queue (item 5). Changed: a treasury email reporting PO-0929-5628 returned R02 while the export still shows PAID; Schedule A item 2 quoted to settle the $25 point; Step 4 and the Step 6 context description rewritten to match; rubric criteria 1 (payout $41,316.27) and 5 (returned payout) replaced, the old criterion 5 (set-off) folded into criterion 1's basis. Kept: the export, the prompt, the reserve, date, and fee criteria. Round 1 files are in history/r1/.

## Log

- 2026-11-09: support notes name the two input files instead of the shorthand Export and Thread.
- 2026-11-09: support notes checked (coded and read): one verbless fragment, two figure formats matched to the criteria, one serial comma.
- 2026-11-09: closed. The user chose a new scenario over a third round (notice-period lever, settlement-date convention, or escape hatch). Spent on this agent: contract retention over a system schedule, effective date versus billing load date, set-off order, a netted decoy chargeback, a non-refundable fee, a returned ACH payout. Lesson: traps carried as stated facts were all caught; the next task targets an unstated convention.
- 2026-11-09: run 2: 5 of 5, agent caught the returned payout and every earlier trap.
- 2026-11-09: round 2 built: treasury email with the R02 returned payout, Schedule A item 2 quoted; answer $41,316.27; Steps 4, 6, and 10 updated and checked; ZIP rebuilt (fingerprint b0d2d9655f082fbe).
- 2026-11-09: run 1: agent caught all traps; 4 of 5, failing only on a $25 chargeback-fee credit the files leave open. Not severe; hardening.
- 2026-11-09: Rubric Drafter run: its criterion 1 named a merchant in neither file (Briarstone Marine Supply); its payout ($19,077.84) and fee credit ($273.85) match ours. Kept our five, with support notes.
- 2026-11-09: Steps 9 and 10 hand read: prompt names the thread plainly; rubric dates take the comma after the year; criterion 2 loosened to the held balance alone (two-question test); criterion 1 accepts the memo or the statement (R16).
- 2026-11-09: Steps 7 and 8: File Builder rebuilt the export rows (no reference table reached it); kept its consistent file and recomputed the answer (payout $19,077.84, reserve $73,890.91 to 2027-03-29). Fixed the thread's placeholder domain and removed a sentence that pointed at the fee check. Rubric criteria 1, 4 and 5 updated.
- 2026-11-09: numbered the form sections Step 1 to Step 14, added sections for Steps 2, 5, 7 and 8, and 11 and 12; the hardening queue moved under Working notes.
- 2026-11-09: Step 5 plan review: "likely to trip the agent". Acted on one comment: the export's run header now states the opening reserve balance, rate, and release lag. Kept the CSV format, the 23 rows, and the newest-first thread (reasons in the chat record).
- 2026-11-09: Step 4 rewritten in the first person; clean on the coded checks and the read.
- 2026-11-09: Step 1 and Step 3 rewritten in the first person, in the analyst's voice; both clean on the coded checks and the read. Fixed a T15 false positive in the checker (dates were counted as three-item lists).
- 2026-11-09: manual prose-tell read of every form section, the prompt and the rubric: serial commas (M5), one memo text for the October 1 row (I16), a dangling modifier in Field and role, one name for the agreement and a three-clause sentence split in the Failure plan (T16, M3), and "figure" used throughout the prompt (T16).
- 2026-11-09: starter form updated from the platform (fictional Step 1 role, LLM drafting allowed, failure description 50 to 350 words). Wrote the Step 1 fictional role and set the scenario source wording.
- 2026-11-09: applied the lessons from accepted tasks: prompt names inputs and outputs in the story with no gloss, says what the figure must survive and that credits in Kestrel's favor count; export gets a run header, terse memos and a chargeback reversal; thread gets a print line, full headers, signatures, the amendment's operative paragraph, and the billing date as an aside. Answer unchanged.
- 2026-11-09: designed; correct answer computed (design/answer.py); prompt and rubric drafted. The rubric is my draft, to compare with the Rubric Drafter's five once the ZIP is uploaded. Field and role left for the user to write (superseded the same day by the form update).
