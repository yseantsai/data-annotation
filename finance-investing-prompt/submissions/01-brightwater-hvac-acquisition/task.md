# 01 · Brightwater HVAC acquisition

**Status:** round 2, graded, ready to submit. Fill the form from the sections below, top to bottom. Everything under "Working notes" is reference only. AHT: 2 h 40 m for this round.

## Prompt

Copy the whole of `prompt.md` (in this folder) into **Your Prompt**.

## Generate response

The response is saved unedited in `result.md` (2,493 words, 2026-11-09). Nothing to paste into the form.

## Rating

Select **Pretty Bad**.

OK is an acceptable alternative if you want to give more weight to what the model got right. Do not select Amazing or Pretty Good.

## Explanation


The model started on the right track. It added the lease deposit the broker left out ($208,850 at closing), saw that the buyer starts with no receivables and no supplier credit, and found that coverage passes in year one and year three.

It then sized the working capital need from rules of thumb ("parts and materials at 20 to 25 percent of revenue") instead of the figures given. Revenue of $2,837,400 less EBITDA of $361,400 means about $206,000 a month of costs, but its cash bridge uses $148,000. That puts the cash trough at $148,000 when it is roughly $250,000 to $290,000. So it concludes that the $150,000 working capital loan "closes gap" and tells the buyer to "sign term sheet". The buyer is actually still about $110,000 short and should not sign as written. The bridge also carries "$6,200 in debt service", while its own coverage section computes $16,340 a month for the SBA loan.

The likely cause is a cost structure built from industry ratios rather than from the revenue and EBITDA in the prompt, never checked against its own debt figures.

## Optional comments

Leave blank.

## AHT

**2 h 40 m** (range 2 h 15 m to 3 h 5 m; 4 h 30 m to 5 h 30 m counting round 1) for one person with finance experience doing this round by hand. The step-by-step breakdown is under Time estimate in the working notes.

## Working notes

Reference only, not for the form: the grading behind the rating, the design and worked answer, the checks, and the history.

## Time estimate (AHT)

Estimated handle time for one person with finance experience doing this task by hand, with no AI help.

| Step | Minutes |
| --- | --- |
| Pick the failure target and design the scenario | 30 to 40 |
| Work the correct answer in a spreadsheet (loan payments, working capital, coverage) | 25 to 35 |
| Write the prompt, check it, read it aloud | 20 to 30 |
| Generate and read the 2,493-word response | 15 to 20 |
| Recompute the response's figures and decide the rating | 25 to 35 |
| Write the explanation | 15 to 20 |
| Fill the form and submit | 5 |
| **Round 2 as submitted** | **135 to 185 (about 2 h 15 m to 3 h 5 m; midpoint about 2 h 40 m)** |

Round 1 is not in that figure. It went through the same steps with a longer prompt and a 3,943-word response, about 2 h 15 m to 2 h 45 m, and came back too good. Counting both rounds, the task took about 4 h 30 m to 5 h 30 m of human-equivalent work. A task that lands on its first round fits the three-hour budget. One that needs a second round does not, so the design step is where to spend extra care.

## Outcome

**Flawed in an essential way: right mechanism, wrong size, and the trap taken at the decisive number.**

What the model caught (spent for this prompt family): the lease first month and deposit missing from the broker's $185,450, giving $208,850 at closing; the reason a working capital hole exists (the seller keeps the receivables, and the supplier is on COD); the seller note capitalizing to $172,480 and costing about $40,000 a year from year three; coverage passing in both years; and the seller-side fix of leaving current receivables in the deal.

Where it went wrong:

1. **The working capital need is sized at about half its real depth (critical).** The cash bridge uses $148,000 a month of outflows, built from an assumed 22 percent parts ratio and an estimated payroll, instead of the $206,333 a month that the prompt's revenue less EBITDA implies. That understates annual operating costs by $774,400, or 31 percent. The trough comes out at $148,000. On the response's own collection pattern with the correct costs, the trough is about $253,000. On the 40-day collection period the receivables imply, it is about $292,000.
2. **It concludes the $150,000 loan closes the gap (critical).** The summary table says "Working capital loan ($150,000): closes gap? Yes, with ~$150 margin; take it". The correct answer is that the buyer is still about $90,000 to $130,000 short after taking the loan, depending on the collection timing assumed ($109,850 in the design notes). Even on its own figures the sign is wrong: a $371,850 requirement against $371,000 of cash is $850 short, not $150 over.
3. **It tells the buyer to sign.** The summary says "Sign term sheet, but make asks to seller this week", and it never asks the lender for more than $150,000 of working capital, because it believes $150,000 is enough. The prompt asked what to request before signing. The right answer is not to sign as written.
4. **Its debt figures disagree with each other (moderate).** The month-by-month bridge carries "roughly $6,200 in debt service", while Part Four computes the SBA payment at $16,340 a month. The $150,000 working capital loan is costed at $1,550 a month, against a correct $1,941.
5. **Small slips.** The SBA payment is $16,340 against a correct $16,360 (an exponent of 2.5804 against 2.5761). Year-three coverage on its own assumptions is 1.31x, not 1.34x. A 0.11x drop in coverage is called "11 basis points". A $20,000 capex reserve is introduced from nowhere, which does not change the coverage conclusion.

**Decision: submit.** The response answers the central question, how much cash the buyer needs and whether the $150,000 covers it, with the wrong magnitude and the wrong conclusion. A buyer acting on it would sign the term sheet, take the $150,000, and could run out of cash for payroll in the second month if the seller declined the receivables ask. It was on the right track and faltered on the number that decides the answer, which is the platform's "flawed in some essential way".

## Failure target

The model checks the lender's coverage test, sees it pass comfortably, accepts the broker's $185,450 as the cash needed to close, and tells the buyer the $150,000 of working capital is a comfortable cushion. A practitioner sees that the buyer starts with no receivables and no supplier credit, so the business needs roughly 40 days of operating costs funded before collections arrive, and that even with the $150,000 the buyer is about $110,000 short on day one.

## Design notes

**Requester.** The same buyer as round 1, one stage later. The LOI is signed at a renegotiated price, and the buyer must accept or push back on the lender's term sheet by December 4. The output is for the buyer alone. All entities are fictional.

**Facts.**

- Price $1,540,000, asset purchase. Quality of earnings: adjusted EBITDA $361,400 on 2025 revenue of $2,837,400, already after market rent, the wife's replacement, and the buyer's $120,000 salary.
- SBA 7(a): 80 percent of price ($1,232,000) at 9.5 percent over ten years, with the $32,340 guaranty fee financed. Optional working capital up to $150,000 added on the same terms.
- Seller note: 10 percent ($154,000) at 6 percent, full standby 24 months, interest accrues and is capitalized, then five-year amortization.
- Buyer equity 10 percent ($154,000).
- Cash-free, debt-free. Seller keeps receivables of $312,000 at the last month-end and pays his own payables. Main parts supplier puts a new owner on COD for 90 days.
- New lease $7,800 a month, first month plus two-month deposit due at closing.
- Broker's closing figure $185,450 (equity $154,000, attorney $24,600, lender fees $6,850).
- Buyer liquidity $261,000, of which $40,000 is untouchable.

**Trap.** The coverage test passes easily, which invites the conclusion that the deal works. The broker's closing figure omits the lease payment, and nothing in the deal funds working capital. The buyer inherits no receivables and gets no supplier credit, so payroll and parts for the first five to six weeks are paid before customer cash comes in. The default a model reaches for is that coverage passes, the buyer needs about $185,000 to $209,000, and the $150,000 loan is a cushion.

**Correct answer.**

| Item | Figure |
| --- | --- |
| Cash at closing (broker's $185,450 plus $23,400 lease first month and deposit) | $208,850 |
| Cash available ($261,000 less $40,000 kept back) | $221,000 |
| Left after closing | $12,150 |
| Annual cash operating costs (revenue less EBITDA) | $2,476,000, about $206,300 a month |
| Receivable days ($312,000 on $2,837,400) | about 40 days |
| Working capital to fund before collections (40 days of cash costs; the $312,000 receivable balance is the upper bound) | about $272,000 (range $270,000 to $312,000) |
| Gap without the working capital loan | about $260,000 short |
| Gap with the $150,000 working capital loan | about $110,000 short (range $108,000 to $150,000) |

Debt service and coverage on $361,400 of EBITDA:

| Structure | Annual debt service | Year 1 | Year 3 |
| --- | --- | --- | --- |
| SBA $1,264,340 (fee financed), no working capital | $196,323 | 1.84x | 1.53x |
| SBA $1,414,340 with $150,000 working capital | $219,615 | 1.65x | 1.39x |

Year 3 adds the seller note: $154,000 plus 24 months of simple interest is $172,480, amortized over five years at 6 percent for $3,335 a month, $40,014 a year. Monthly compounding gives $173,583 and $40,270 a year; either is acceptable. Amortizing the original $154,000 ($35,727 a year) is a minor error.

A sound answer takes the $150,000 because coverage stays well above 1.25x with it. It still finds the buyer about $110,000 short and says not to sign the term sheet as it stands. The fixes, any of which is acceptable: have the seller leave or sell a normal level of receivables at closing, financed by a larger seller note on standby or a price reduction; ask the lender for more working capital than $150,000; or bring about $110,000 more equity. A larger working capital loan still clears coverage: at $260,000 of working capital, year 1 is 1.53x and year 3 is 1.31x.

**Adverse result.** The buyer wants to hear that the renegotiated deal closes on the term sheet as written. It does not. A model that confirms the deal works because coverage passes, or that treats the $150,000 as spare cushion, is gradeably wrong.

**Size.** A practitioner answers this in about an hour. The whole task, design through rating, fits the project's three-hour budget.

## Self-check

```
== submissions/01-brightwater-hvac-acquisition/prompt.md (368 words) ==
  coded checks clean
```

Prompt length 2,143 characters. No WARN kept.

Manual rows, read aloud on 2026-11-09 (round 2):

- [x] F1 buyer, for himself, deciding whether to sign the term sheet, all in the first paragraph
- [x] F3 reads as the buyer briefing an adviser; no persona, no test-question shape
- [x] F4 stakes: term sheet due December 4, the couple's savings, a $1,540,000 purchase
- [x] F5 all entities fictional; the only real things are Dayton, Ohio and the SBA 7(a) program
- [x] D1 the answer depends on the receivables, supplier terms, savings, and loan structure given
- [x] D2 the trap is in the facts: no inherited receivables, COD supplier terms, a closing figure that leaves out working capital
- [x] D3 the buyer wants to hear the deal closes; the facts say he is about $110,000 short
- [x] D5 round 2 of task 01; the round-1 traps are no longer what the question turns on
- [x] D6 every fact is one a buyer at this stage would hold; nothing exists only to trip the model
- [x] D8 one decisive question (can he fund closing and working capital); about an hour for a practitioner, inside the three-hour task budget
- [x] S2 no sentence draws the working capital inference; receivables, supplier terms and costs are stated as bare facts, and the EBITDA definition is stated only so the salary is not double-counted
- [x] S4 no output form required
- [x] M5 serial comma in the EBITDA list and the closing ask
- [x] M6 complete sentences throughout
- [x] M7 spell-checked by eye; no errors found
- [x] T3 no idiom in place of a figure
- [x] T16 "working capital", "coverage", "term sheet" each keep one name throughout

## Revisions

- 2026-11-09, round 2. **Reason:** round 1 came back right on the whole. The model caught every add-back and multiple trap, and the platform test sends such a prompt back to design. It missed working capital, closing cash, and taxes. **Changed:** the scenario moves one stage later, to the term sheet after a signed LOI at $1,540,000, with the quality of earnings settled, so the add-backs are no longer in play. The question now turns on what the buyer must fund: the cash at closing, the working capital needed because he inherits no receivables and gets no supplier credit, and whether the $150,000 working capital loan closes the gap. The pre-solved facts from round 1 (the replacement quote, the market rent comp, the prior-year legal fees) are gone. Customer concentration, vans, and taxes were cut to keep the task inside the three-hour budget. **Kept:** the company, the buyer's voice, the SBA structure, the seller note on standby (now with capitalized interest), and the December 4 deadline. Round 1 is in history/prompt-r1.md, history/result-r1.md, and history/task-r1.md.

## Log

- 2026-11-09: drafted; design notes and prompt complete, coded checks clean, manual rows read; awaiting the Generate test
- 2026-11-09: Generate response saved as result.md and graded; borderline Pretty Good / OK, recommendation is to harden; submit decision pending
- 2026-11-09: round 2. Round 1 archived to history/. Prompt rewritten around closing cash and working capital, 368 words, coded checks clean, manual rows read. Awaiting the Generate test
- 2026-11-09: round 2 Generate response saved and graded. Flawed in an essential way: working capital need sized at about half, $150,000 loan wrongly said to close the gap, told to sign. Proposed Pretty Bad, recommend submit
