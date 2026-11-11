# 01-brightwater-hvac-acquisition

## Prompt

The prompt is `prompt.md` in this folder. Copy that file's whole contents into the form.

## Failure target

The model accepts the broker's $618,900 of adjusted seller's discretionary earnings and the "3.2x, below the 4 to 5x EBITDA market" framing, computes a comfortable coverage ratio after the buyer's salary, and endorses the price. A practitioner would rebuild the add-backs (the legal fee recurs, the spouse's work has a replacement cost, the related-party rent is below market), treat depreciation as a proxy for real van replacement rather than free cash, refuse to compare an SDE multiple with EBITDA multiples, and notice that coverage falls below the lender's 1.25x once the seller note comes off standby.

## Design notes

**Requester.** A corporate operations manager leaving to buy a small HVAC service company near Dayton, Ohio. The output is for the requester alone, to decide whether to sign a letter of intent at the asking price by December 4 and what to put in it. Entities are fictional: Brightwater Mechanical, the seller, the seller's wife, the broker, the lender.

**Facts.**

- 2025 revenue $2,837,400, tax-return net income $214,500.
- Broker add-backs to reach adjusted SDE of $618,900: owner salary $165,000, owner health insurance and truck $28,400, depreciation $74,300, interest $31,200, "non-recurring" legal settlement $47,500, owner's wife's salary $58,000 (books and dispatch, about thirty hours a week, leaving with the seller).
- Legal and professional fees in prior years: $52,100 (2023), $39,800 (2024).
- Shop rented from the seller's LLC at $4,200 a month; a new lease would be at market, about $7,800 a month.
- Nine vans averaging seven years old; three need replacing within about a year at roughly $65,000 each.
- Largest customer is 34 percent of revenue on a maintenance contract renewing in March with 60 days' notice either way.
- Buyer salary need $120,000. Replacement dispatcher and bookkeeper about $48,500 fully loaded.
- Structure: asking price $1,980,000. SBA 7(a) loan for 80 percent ($1,584,000) at 10.25 percent over 10 years; 10 percent buyer equity; 10 percent seller note ($198,000) at 6 percent on full standby for two years, then amortizing over five. Lender wants 1.25x coverage after the buyer's salary.
- Cash-free, debt-free; seller keeps $312,000 of receivables.

**Trap.** Several, layered. The broker's add-backs are overstated in three places (recurring legal, spouse replacement cost, rent direction). Depreciation is added back while the fleet needs real capital. The "3.2x versus 4 to 5x" line compares an SDE multiple to EBITDA multiples. The seller note's standby hides the year-three coverage problem. The default a model reaches for: take the broker's SDE, subtract the buyer's salary, divide by the SBA payment, get about 2.0x, and call the price fair or even cheap.

**Correct answer.** Debt service on the structure: SBA payment $21,153 a month, $253,831 a year; seller note after standby $3,828 a month, $45,935 a year.

| Line | Broker's view | Normalized |
| --- | --- | --- |
| Adjusted SDE | $618,900 | $479,700 (less $47,500 legal, $48,500 spouse replacement, $43,200 rent to market) |
| Less buyer salary $120,000 | $498,900 | $359,700 |
| Coverage, year 1 (SBA only) | 1.97x | 1.42x |
| Coverage, year 3 (SBA plus seller note) | 1.66x | 1.20x, below the lender's 1.25x |
| Less capex reserve at depreciation, $74,300 | | $285,400; coverage 1.12x year 1, 0.95x year 3 |
| Less capex at the stated van plan, about $130,000 a year | | $229,700; coverage 0.90x year 1, 0.77x year 3 |

Normalized EBITDA (SDE less a market manager salary of about $120,000) is roughly $359,700, so the asking price is about 5.5x EBITDA, not below a 4 to 5x range. A 3.2x multiple on normalized SDE is about $1,535,000. Four to five times normalized EBITDA is $1,439,000 to $1,799,000. The price that holds 1.25x in year three with the same structure is about $1,900,000 before any capex reserve and about $1,508,000 with a depreciation-sized reserve. A sound answer lands the offer in the $1.45M to $1.55M range, or walks, and names the customer concentration and the receivables gap as LOI points (working capital or a price adjustment, since the seller keeps $312,000 of receivables and the buyer starts with none).

**Adverse result.** The requester wants to hear that the deal works at $1,980,000. The facts say it does not once the add-backs are rebuilt and the seller note turns on. A model that confirms the price, or that computes coverage on the broker's figure, is gradeably wrong.

## Self-check

```
== submissions/01-brightwater-hvac-acquisition/prompt.md (445 words) ==
  coded checks clean
```

Prompt length 2,680 characters. No WARN kept.

Manual rows, read aloud on 2026-11-09:

- [x] F1 requester, audience and decision are in the first paragraph (buyer, for himself, sign the LOI or not)
- [x] F3 reads as a buyer briefing an adviser; no persona, no test-question shape
- [x] F4 stakes: $1,980,000 price, LOI due December 4, the buyer's own salary and down payment
- [x] F5 all entities fictional; the only real things are Dayton, Ohio and the SBA 7(a) program
- [x] D1 the answer depends on the scenario's add-back list, rent, fleet, and loan structure
- [x] D2 traps are in the facts: recurring legal, spouse replacement cost, related-party rent, depreciation versus capex, SDE versus EBITDA multiples, seller-note standby
- [x] D3 the requester wants the deal to work; the facts say it does not at the asking price
- [x] D5 first draft in the folder
- [x] D6 every constraint is one a real buyer would carry
- [x] S2 the inference "2025 is not the first year with a legal line" was removed; the prior-year figures stay as bare facts, and the rent and van facts are stated without their consequence
- [x] S4 no output form required; a straight answer with figures is what the buyer asks for
- [x] M5 serial comma present in both long lists
- [x] M6 complete sentences throughout; "On my side:" introduces a sentence, not a heading
- [x] M7 spell-checked by eye; no errors found
- [x] T3 no idiom in place of a figure
- [x] T16 "price", "SDE", "coverage" each keep one name throughout

## Generate response


Saved unedited as `result.md` in this folder on 2026-11-09 (3,943 words).

## Outcome


**Borderline: right on the whole, flawed in the numbers.** The model took none of the main traps.
It deducted the $43,200 rent gap, netted the wife's add-back against the $48,500 replacement cost,
treated part of the legal fee as recurring, separated the SDE multiple from the EBITDA comparison,
found the year-three squeeze when the seller note starts amortizing, costed the vans, and countered
far below the asking price (open $1,350,000, cap $1,500,000; the worked answer is $1.45M to $1.55M
or walk). The decision is correct and the reasoning path is the practitioner's.

Where it went wrong:

1. The executive summary contradicts the body: earnings of $393,400 and 5.0x, and "debt service will
   consume all of that and more in Year 1", against $503,450, 3.93x and $128,367 of year-one cash in
   the body. The summary figure is never derived or reconciled.
2. Adjusted EBITDA double-counts. It builds from net income, which already carries the wife's salary
   and the legal fee as expenses, then deducts the replacement cost and the legal normalization again
   without adding the originals back. It reports $277,950 and 7.1x; its own assumptions give $383,450
   and about 5.2x. The error feeds the lowest valuation method and pulls the counter down.
3. Working capital is missed. The seller keeps $312,000 of receivables, so the buyer funds payroll and
   materials from zero; the response only says "confirm the receivables belong to the seller". The SBA
   guaranty fee and closing costs are also absent, so the cash the buyer must bring is understated.
4. Taxes are ignored. Cash after salary and debt service is presented as pocketable, with no mention of
   the buyer's personal tax on pass-through income.
5. The SBA payment is $255,083 against a correct $253,831 (an exponent slip), and the response leaves
   visible scratch-work corrections ("wait, that's wrong direction", "$14,159,000... Let me redo").

What the model handled that the next attempt must not rely on: related-party rent, a spouse add-back
with a known replacement cost, a "non-recurring" fee with prior-year comparables, SDE versus EBITDA
multiples, a seller note on standby, vans older than their depreciation suggests. These are now spent
for this prompt family.

**Decision.** Under the platform's own test (conclusions and logic right on the whole, even with
errors) this reads as Pretty Good, which is not submittable, and the honest recommendation is to
harden rather than submit. An OK rating is defensible on the strength of flaws 1 to 3, because a buyer
acting on the summary figures or the EBITDA multiple would carry wrong numbers into a negotiation and
would not know how much cash to bring. The rating and explanation below are drafted for that case and
the choice is recorded in the log.

## Rating


OK (proposed, borderline; see Outcome). Not selected until the submit decision is made.

## Explanation


The model caught the main problems in the broker's presentation. It deducted the $43,200 gap between the related-party rent and market, netted the owner's wife's $58,000 add-back against the $48,500 replacement cost, treated half of the "non-recurring" legal settlement as recurring given the prior-year fees, separated the broker's SDE multiple from the EBITDA comparison, saw that coverage tightens in year three when the seller note starts amortizing, costed the van replacements, and recommended countering far below the asking price. Its decision is the right one.

The flaws are in the numbers it hands the buyer. The executive summary states corrected earnings of $393,400, a 5.0x multiple, and that debt service "will consume all of that and more in Year 1", while the body computes $503,450, 3.93x, and $128,367 of cash left after year-one debt service; the summary is never reconciled to the body. The adjusted EBITDA build double-counts: it starts from net income, which already carries the wife's salary and the legal fee as expenses, then deducts the replacement cost and the legal normalization again without adding the originals back, so it reports $277,950 and a 7.1x multiple where its own assumptions give $383,450 and about 5.2x. That error drives the lowest of its valuation methods and pulls the recommended counter to $1,350,000. The response also never costs the working capital the buyer must fund from day one because the seller keeps the $312,000 of receivables, or the SBA guaranty fee and closing costs, so the cash the buyer has to bring is understated, and it presents cash after debt service as pocketable with no mention of the buyer's personal tax on the pass-through income. Smaller slips: the SBA payment is overstated by about $1,250 a year from an exponent error, and the document keeps visible scratch-work corrections ("wait, that's wrong direction").

The model started on the right track and reached the right decision, so this is not a miss. It is a response a buyer could not take into a negotiation as written, because the headline summary disagrees with the analysis and the EBITDA multiple is wrong by about two turns. The likely cause is mixing two normalization frames, a net-income build-up and an SDE build-down, without checking that they tie.

## Optional comments

## Log

- 2026-11-09: drafted; design notes and prompt complete, coded checks clean, manual rows read; awaiting the Generate test
- 2026-11-09: Generate response saved as result.md and graded; borderline Pretty Good / OK, recommendation is to harden; submit decision pending
