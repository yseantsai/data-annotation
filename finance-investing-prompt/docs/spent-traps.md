# Spent traps

Every trap a Generate response has handled correctly, and every trap that made the model fail.
A task whose response is not submittable is deleted (`docs/workflow.md`, Stage 4), so this file
is the only record of what it taught. `/review-finance-investing-result` adds a line here before
it deletes a task, and `/create-finance-investing` reads this file before designing a new one.
A new task must not rely on a trap listed under "Caught" (rule D5).

## Caught (do not reuse)

| Trap | Domain | What the model did |
| --- | --- | --- |
| Seller's discretionary earnings add-backs; SBA coverage test | small-business acquisition | handled both (submission 01, round 1) |
| FIFO layering of a commodity surcharge | margin variance | priced the surcharge correctly (submission 02) |
| IRR against a point-to-point index return; public market equivalent | fund performance | ran the PME on dated flows and found the $254,000 shortfall (deleted task, Calderwood) |
| Full loss provision on a loss contract; rejected claim kept out of contract value | construction WIP | handled both (submission 03) |
| Fixed-price contracts reprice only at renewal while a wage rise hits on January 1 | pricing | found the renewal lag (submission 04, round 1) |
| Post-money SAFE conversion base excludes the Series A pool top-up | venture financing | converted on the right base, 1.97x against a claimed 2x (deleted task, Pellwick) |
| IFRS 16 EBITDA against US-listed comps | trading comparables | spotted the mismatch, but then misstated the US rule (submission 05) |
| Wash sale triggered by a purchase in the taxpayer's own IRA | portfolio and tax | caught it and stopped the summary, though it gave no corrected figure (deleted task, Ferreira) |
| Soft call reset by an amendment's word swap ("the Closing Date" replaced) | corporate borrowing | read the swap into the quoted clause and priced the $1.86 million premium (deleted task, Rennick) |
| Borrowing base eligibility: cross-aging at 50 percent, contra, 25 percent concentration on the post-exclusion pool | asset-based lending | applied every quoted clause in order, exact to the cent (deleted task, Castell) |
| Annual distributions under the 10-year rule when the owner died after the required beginning date; waivers ended with 2024 | inherited IRA | knew the rule (submission 06), but misdated the present |

## What made the model fail

| Submission | Failure |
| --- | --- |
| 01 | Left out the working capital a buyer must fund when the seller keeps the receivables |
| 02 | Got the dollar-to-basis-point bridge wrong and named the wrong driver |
| 03 | Counted an approved change order twice, though the contract figure already included it |
| 04 | Took a wage pass-through clause at face value without checking that it applies only to legally required increases |
| 05 | Recalled the US lease rule wrongly ("identical in effect" to IFRS 16) and valued on the inconsistent basis |
| 06 | Placed the present a year early and missed both the 2025 catch-up and the 2026 distribution |

The pattern so far: the model handles any rule the prompt quotes in full, and any well-known
concept it can name. It fails on a figure misread mid-calculation, a condition it never checks,
a rule it has to recall and recalls wrongly, and a fact the prompt implies rather than states.
