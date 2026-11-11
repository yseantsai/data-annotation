# 06 · Achterberg inherited IRA

**Status:** round 1, graded, ready to submit. Fill the form from the sections below, top to bottom. Everything under "Working notes" is reference only. AHT: 1 h 55 m.

## Prompt

Copy the whole of `prompt.md` (in this folder) into **Your Prompt**.

## Generate response

The response is saved unedited in `result.md` (1,025 words, 2026-11-10). Nothing to paste into the form.

## Rating

Select **Pretty Bad**.

OK is an acceptable alternative if you want to give more weight to the rule it got right. Do not select Amazing or Pretty Good.

## Explanation

The model started on the right track. It saw that the father died after his required beginning date, so Lauren owes annual distributions under the 10-year rule, and that the IRS waivers ended with 2024.

It then placed the meeting in 2025, although the prompt has Northbank's 2026 notice in hand and gives the balance at "the end of last year". It tells the advisor Lauren "must take her 2025 RMD (correctly calculated) before December 31, 2025", treats $1,018,446.20 as the December 31, 2024 balance, and puts that distribution at $34,641. It then says Northbank's figures "don't appear to reconcile" and should be challenged, though the 2026 notice is exactly that balance over a factor of 31.3. It never mentions the 2026 distribution, and it says "No corrective action or Form 5329 should be required".

The correct position: the 2025 distribution of $29,328.57 was missed outside any waiver, with a 25 percent excise ($7,332.14), or 10 percent if corrected in time, and a Form 5329 to file. The 2026 distribution of $32,538.22 is due by December 31, so $61,866.79 comes out this year. The likely cause is that it anchored on the waiver ending and never fixed the current year.

## Optional comments

Leave blank.

## AHT

**1 h 55 m** (range 1 h 35 m to 2 h 15 m) for one person with finance experience doing this round by hand. The step-by-step breakdown is under Time estimate in the working notes.

## Working notes

Reference only, not for the form: the grading behind the rating, the design and worked answer, the checks, and the history.

## Time estimate (AHT)

Estimated handle time for one person with finance experience doing this round by hand, with no AI help.

| Step | Minutes |
| --- | --- |
| Pick the failure target and design the scenario, checking the current rules | 30 to 40 |
| Work the correct answer (the two distributions, the excise at both rates, the tax) | 5 to 10 |
| Write the prompt, check it, read it aloud | 15 to 20 |
| Generate and read the 1,025-word response | 10 to 15 |
| Recompute the response's figures and decide the rating | 15 to 25 |
| Write the explanation | 15 to 20 |
| Fill the form and submit | 5 |
| **Total** | **95 to 135 (about 1 h 35 m to 2 h 15 m; midpoint about 1 h 55 m)** |

One round only, inside the three-hour budget.

## Outcome

**Flawed in an essential way: the right rule, applied to the wrong year.** The action items it gives for December 31 are wrong in amount, in year, and on the filing.

What the model caught (spent for this prompt family): annual distributions under the 10-year rule when the owner died after his required beginning date, inferred from his age and his own distributions; the final regulations; the waiver notices for 2021 to 2024 and that they ended with 2024; the 25 percent excise and its 10 percent reduction; and that the deferral plan cannot stand.

Where it went wrong:

1. **It places the present in 2025 (critical).** The prompt has Northbank's 2026 notice already sent and gives the balance at "the end of last year". The response tells the advisor that Lauren "must take her 2025 RMD (correctly calculated) before December 31, 2025", a date already past. Every action item follows from this.
2. **It misses the 2025 shortfall and the filing (critical).** The 2025 distribution of $29,328.57 was missed outside any waiver. The excise is $7,332.14 at 25 percent, or $2,932.86 at 10 percent if corrected in time, and Form 5329 is needed for 2025. The response says "No corrective action or Form 5329 should be required".
3. **It leaves out the 2026 distribution (critical).** $32,538.22 is due by December 31, 2026; the response never mentions it. Its single figure to take, $34,641, is $27,225.76 short of the $61,866.79 that has to come out this year.
4. **It disputes correct notices (moderate).** It says Northbank's figures "don't appear to reconcile" and suggests a call. The 2026 notice is $1,018,446.20 over 31.3 exactly. The response's own factors start from age 53 in 2023, though a 55-year-old in 2026 was 52 in 2023.
5. **Arithmetic slip (minor).** It writes $29,328.57 times 29.4 as "roughly $862,860"; the product is $862,259.96.

A note on the prompt: the year is implied, not stated. The 2026 notice, "the end of last year", and Lauren's age of 55 against a 2023 start each place the present in 2026, so a reviewer can follow the reading from the prompt's own facts.

**Decision: submit at Pretty Bad.** The response knows the rule, but the advice an advisor would act on before December 31 is wrong: the wrong amount, no catch-up for 2025, no Form 5329, and a call to dispute correct figures. OK is an acceptable alternative for the rule it got right.

## Failure target

The model agrees that Lauren is under the 10-year rule with nothing due until 2032, and endorses deferring the whole account to 2030 to 2032. A practitioner sees that her father died at 79, after his required beginning date. Under the final RMD regulations issued in July 2024, a designated beneficiary under the 10-year rule then has to take annual distributions in years one to nine as well. The IRS waived the excise for missed distributions only through 2024. Lauren's 2025 distribution of $29,328.57 was missed outside any waiver, and her 2026 distribution of $32,538.22 is due by December 31. She has to take $61,866.79 this year at 35 percent and file Form 5329 for 2025, so the plan to defer fails.

## Design notes

**Requester.** A wealth advisor preparing year-end planning for a client whose father left her a traditional IRA, with a client meeting on November 19, 2026. The advisor has set aside the custodian's RMD notices since 2023, believing the 10-year rule requires nothing until the tenth year. All people and firms are fictional: Lauren Achterberg and Northbank.

**Facts.**

- Father died in March 2022 at 79, long past his required beginning date; he took his 2022 distribution in January.
- Lauren: 55 in 2026, not disabled, not chronically ill, 26 years younger than her father, so a designated beneficiary but not an eligible designated beneficiary. The account must be empty by December 31, 2032.
- Northbank's notices: 2025, $29,328.57; 2026, $32,538.22. These match the balance at December 31, 2024 ($947,312.68) over a factor of 32.3, and the balance at December 31, 2025 ($1,018,446.20) over 31.3: her single life expectancy at 52 in 2023 (34.3), less one a year. The prompt gives only the notice amounts and the 2025 year-end balance.
- No distributions have been taken since 2022. Lauren is in the 35 percent bracket.

**Trap.** The rule the answer turns on is not in the prompt. A model that remembers the 10-year rule as "anything until year ten" agrees with the advisor. A model that knows the 2022 proposed rules but not their sequel may still assume the IRS waivers continue. The notices are described as boilerplate, and the advisor's own reason ("nothing is required until the tenth year") invites agreement. The facts that decide it are stated in passing: the father's age at death and that he had been taking his own distributions.

**Correct answer.**

- Annual distributions have been required since 2023, because the father died after his required beginning date. The final regulations (T.D. 10001, July 2024) confirm this and apply from 2025.
- 2023 and 2024: missed, but the IRS waived the excise for those years (Notices 2023-54 and 2024-35). They need not be made up separately; the account still has to be empty by 2032.
- 2025: $29,328.57 missed, with no waiver. The excise is 25 percent, $7,332.14, reduced to 10 percent, $2,932.86, if the shortfall is corrected within the correction window. Lauren should take it now and file Form 5329 for 2025, where she can ask the IRS to waive the excise for reasonable cause, a request it often grants when the shortfall has been made up.
- 2026: $32,538.22 is due by December 31, 2026.
- Total to take before year end: $61,866.79, all taxable in 2026, about $21,653 of federal tax at 35 percent.
- The plan to leave the account untouched until 2030 cannot work. Annual distributions continue each year through 2031, and the balance comes out by the end of 2032. Any extra she wants to take early, beyond the minimums, is a separate choice.

A sound answer tells the advisor the plan does not hold, gives both distributions and the December 31 deadline, and covers the 2025 correction and Form 5329. For grading: endorsing the deferral is the trap taken whole. Requiring annual distributions but treating 2025 as waived, or as something to skip, is a second material error, because it leaves the excise exposure standing. Telling Lauren to make up 2023 and 2024 as well is an over-correction, minor next to the others.

**Adverse result.** The advisor wants to defer every dollar to Lauren's retirement years. The facts require about $62,000 out this year at 35 percent and a filing for 2025. A model that endorses the plan is gradeably wrong.

**Size.** A practitioner answers this in well under an hour, inside the three-hour task budget.

## Self-check

```
== submissions/06-achterberg-inherited-ira/prompt.md (173 words) ==
  coded checks clean
```

Prompt length 1,031 characters, 191 words. No WARN kept. One fix on the read-aloud: the first draft gave Lauren $310,000 of income in the 32 percent bracket and a drawdown "in the 22 and 24 percent brackets". Neither holds for a single filer drawing about a million dollars over three years. Both claims were cut, leaving only her current 35 percent bracket, so the prompt carries no second error that would pull the answer away from the RMD question.

Manual rows, read aloud on 2026-11-10:

- [x] F1 wealth advisor, for a client meeting on the 19th, deciding the year-end plan for the inherited IRA, all in the first paragraph
- [x] F3 reads as an advisor asking for a second read before a meeting; no persona, no test-question shape
- [x] F4 stakes: a December 31 deadline and a client's tax plan
- [x] F5 all names fictional; no private details of a real person
- [x] F7 no tables, headings, or bold; the figures are in sentences
- [x] D1 the answer depends on the father's age at death, the dates, and the notice amounts, applied to the current rules
- [x] D2 the trap is in the facts: a death after the required beginning date, stated as an age, and an advisor's reading of the 10-year rule
- [x] D3 the advisor wants to defer everything; the facts require about $62,000 out this year
- [x] D5 new use case (distribution rules for an inherited account) and new reasoning path; none of the spent traps from earlier tasks
- [x] D6 every figure is one an advisor holds for this review
- [x] D8 one decisive question (does the plan hold); well under an hour for a practitioner
- [x] S2 no sentence mentions the required beginning date, the final regulations, or the waivers; the notices are presented as boilerplate
- [x] S4 no output form required
- [x] M5 serial comma in "2030, 2031, and 2032"
- [x] M6 complete sentences
- [x] M7 spell-checked by eye; no errors found
- [x] T3 no idiom in place of a figure
- [x] T16 "the account", "RMD notice", "the plan" each keep one name throughout

## Revisions

<!-- One dated entry per round after the first. -->

## Log

- 2026-11-10: drafted; worked answer computed (two distributions, excise at 25 and 10 percent, tax at 35 percent), bracket claims cut on the read-aloud, coded checks clean, manual rows read; awaiting the Generate test
- 2026-11-10: Generate response saved (1,025 words) and graded. Annual RMD rule and waiver end caught, but the present placed in 2025: no 2025 catch-up or Form 5329, no 2026 distribution, Northbank's correct figures disputed. Rated Pretty Bad, recommend submit
