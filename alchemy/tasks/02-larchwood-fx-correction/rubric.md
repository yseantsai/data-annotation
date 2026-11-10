<!-- Draft by Claude, 2026-11-09, from design/answer.py (reference data). Recompute with `answer.py --inputs` after the File Builder runs; figures change if it rebuilds the rows. Compare with the Rubric Drafter's five before keeping either. -->

1. The memo or the workbook reports that Larchwood's September CAD batches were overpaid by $69,801.70 (within $0.05), because the USD/CAD rate was multiplied instead of divided.
2. The memo or the workbook reports a September CHF shortfall of $8,420.03 (within $0.05) owed to Larchwood, after the 1.20% FX margin.
3. The memo states that Larchwood receives $0.00 on the October 6 settlement.
4. The memo states that Larchwood still owes Halvard $35,895.44 (within $0.05) after the October 6 settlement.
5. The workbook shows no difference larger than $0.05 on the EUR and GBP batches, because EUR/USD and GBP/USD are quoted in US dollars per unit, so multiplying by the rate was right for them.

## Supporting notes

Paste each note into the form's optional "which file or fact supports this criterion" column, next to its criterion.

| # | Supporting file or fact |
| --- | --- |
| 1 | larchwood_fx_settlements_2026-09.csv: September CAD rows, usd_converted equal to gross_local times ref_rate (about 1.37). RE Larchwood September CHF settlement.docx: Owen's Aug 28 email, the four pairs publish in market convention, including USD/CAD; Marisol's Sept 2 email, nothing else in the calculation changed. |
| 2 | larchwood_fx_settlements_2026-09.csv: September CHF rows at ref_rate of about 0.88, multiplied. RE Larchwood September CHF settlement.docx: Callum's Oct 5 email (about 88 cents per franc); Schedule C item 2 in Priya's Oct 5 email (1.20% margin, rounding to the cent). |
| 3 | larchwood_fx_settlements_2026-09.csv: October 2 rows, PENDING, payout date Oct 6. RE Larchwood September CHF settlement.docx: Sections 7.3 and 7.4 in Priya's Oct 5 email; Tessa's Oct 5 email promising the CHF credit on Oct 6. |
| 4 | larchwood_fx_settlements_2026-09.csv: the September CAD and CHF rows and the October 2 batch. RE Larchwood September CHF settlement.docx: Section 7.3 in Priya's Oct 5 email (overpayments recovered from subsequent settlement funds until repaid in full). |
| 5 | larchwood_fx_settlements_2026-09.csv: EUR and GBP rows at ref_rate of about 1.08 and 1.27. RE Larchwood September CHF settlement.docx: Owen's Aug 28 email names EUR/USD and GBP/USD in market convention. |
