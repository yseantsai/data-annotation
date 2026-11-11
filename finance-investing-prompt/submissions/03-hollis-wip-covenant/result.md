# WIP Schedule Review – Hollis Electric, September 30

---

## Step 1: Establish the Correct Contract Values

Before computing percent complete, I need to decide what belongs in "contract value" for each job.

**Westfield Middle School and Riverside Medical Office** – No change-order or claim issues mentioned; I'll use the stated contract amounts.

**Lakeview Distribution Center** – Two items to sort out:

| Item | Amount | Treatment |
|---|---|---|
| Approved change order (Morrow, August) | $96,000 | **Include.** It's executed and approved before the balance-sheet date. |
| Delay claim submitted by PM | $140,000 | **Exclude.** A claim is a variable consideration item under ASC 606-10-32-11 through 32-16. You include it only to the extent it is *probable* of not reversing – and Morrow's October 22 letter, written before your financials are finalized, is a *subsequent event* that confirms the claim was already in dispute at September 30. Including $140,000 would almost certainly overstate revenue and contract assets. Remove it if it's currently in your workbook. |

**Revised Lakeview contract value: $3,917,480 + $96,000 = $4,013,480**

---

## Step 2: Recompute Each Job – Cost-to-Cost Percent Complete

### Formula recap
- **% Complete** = Cost to Date ÷ (Cost to Date + Est. Cost to Complete)
- **Revenue Earned** = % Complete × Contract Value
- **Contract Asset (Underbilling)** = Revenue Earned − Billed to Date *(if positive)*
- **Contract Liability (Overbilling)** = Billed to Date − Revenue Earned *(if positive)*

---

### Job 1 – Westfield Middle School

| | |
|---|---|
| Contract Value | $2,483,650 |
| Cost to Date | $1,433,700 |
| Est. Cost to Complete | $612,300 |
| Total Est. Cost | $2,046,000 |
| **% Complete** | 1,433,700 ÷ 2,046,000 = **70.07%** |
| **Revenue Earned** | 70.07% × $2,483,650 = **$1,740,505** |
| Billed to Date | $1,612,000 |
| **Position** | $1,740,505 − $1,612,000 = **$128,505 Underbilled (Contract Asset)** |

> **Margin check:** Gross margin implied = ($2,483,650 − $2,046,000) ÷ $2,483,650 = **17.6%.** Reasonable for commercial electrical work; no red flag.

---

### Job 2 – Lakeview Distribution Center

| | |
|---|---|
| Contract Value | **$4,013,480** (base $3,917,480 + approved CO $96,000) |
| Cost to Date | $2,871,750 |
| Est. Cost to Complete | $1,230,750 |
| Total Est. Cost | $4,102,500 |
| **% Complete** | 2,871,750 ÷ 4,102,500 = **69.99%** |
| **Revenue Earned** | 69.99% × $4,013,480 = **$2,809,247** |
| Billed to Date | $2,950,000 |
| **Position** | $2,809,247 − $2,950,000 = **($140,753) Overbilled (Contract Liability)** |

> **Critical flag:** This job is showing an *overbill* even after adding the approved change order. That means your billings are running ahead of earned revenue. Watch this one carefully – if costs continue to run over, you could be recognizing a loss job.

> **Margin check:** Implied gross margin = ($4,013,480 − $4,102,500) ÷ $4,013,480 = **−2.2%.** **This job is currently projected to lose money.** You need to scrutinize whether the $1,230,750 cost-to-complete estimate is solid. If it's understated, the loss – and the contract liability – will grow.

---

### Job 3 – Riverside Medical Office

| | |
|---|---|
| Contract Value | $1,126,400 |
| Cost to Date | $206,500 |
| Est. Cost to Complete | $732,200 |
| Total Est. Cost | $938,700 |
| **% Complete** | 206,500 ÷ 938,700 = **22.00%** |
| **Revenue Earned** | 22.00% × $1,126,400 = **$247,796** |
| Billed to Date | $337,900 |
| **Position** | $247,796 − $337,900 = **($90,104) Overbilled (Contract Liability)** |

> **Margin check:** Implied gross margin = ($1,126,400 − $938,700) ÷ $1,126,400 = **16.7%.** Margin is fine, but this job is only 22% done and already overbilled by $90K. Keep an eye on the ETC as the job develops.

---

## Step 3: Consolidated WIP Summary

| Job | Revenue Earned | Contract Asset | Contract Liability |
|---|---|---|---|
| Westfield Middle School | $1,740,505 | **$128,505** | — |
| Lakeview Distribution Center | $2,809,247 | — | **$140,753** |
| Riverside Medical Office | $247,796 | — | **$90,104** |
| **Net** | | **$128,505** | **$230,857** |

- **Total Contract Assets (current asset):** $128,505
- **Total Contract Liabilities (current liability):** $230,857

---

## Step 4: Working Capital Calculation

### What you need to adjust vs. your draft

Your draft shows $1,281,437. I don't have your draft's WIP detail, but the most likely source of difference is **the $140,000 claim on Lakeview.** If your workbook included that claim in the contract value, it would have inflated revenue earned on Lakeview and produced a larger contract asset (or smaller contract liability), overstating working capital. Here's the corrected picture:

| | Amount |
|---|---|
| Current assets per draft (ex-WIP) | $3,412,600 |
| Contract Assets (corrected) | $128,505 |
| **Total Current Assets** | **$3,541,105** |
| | |
| Current liabilities per draft (ex-WIP) | $1,961,666 |
| Contract Liabilities (corrected) | $230,857 |
| **Total Current Liabilities** | **$2,192,523** |
| | |
| **Corrected Working Capital** | **$1,348,582** |
| Covenant Requirement | $1,250,000 |
| **Headroom** | **$98,582** |

---

## Step 5: Comparison to Your Draft

| | Your Draft | Corrected |
|---|---|---|
| Working Capital | $1,281,437 | $1,348,582 |
| Difference | | +$67,145 |

Your working capital actually **improves** on a corrected basis – which tells me your draft likely already excluded the $140,000 claim (good), but may have computed the WIP positions slightly differently. You still **pass the covenant**, but I want to flag everything that could change that conclusion before you sign.

---

## Step 6: Issues to Resolve Before Signing

### 🔴 Issue 1 – Lakeview Is a Loss Job
**This is the most urgent matter.** The job is currently projected at a **negative 2.2% gross margin**, meaning estimated total cost ($4,102,500) exceeds the contract value ($4,013,480) by **$89,020**. Under ASC 606 / ASC 340-40-35-17, when a contract is onerous, you must accrue the **entire anticipated loss immediately** – not spread it over remaining activity.

- Loss to accrue: $89,020
- Less: portion already embedded in revenue recognized to date...

Actually, let's be precise. At 70% complete, your cumulative revenue recognized is $2,809,247 against cumulative cost of $2,871,750 – that's already a **$62,503 gross loss recognized to date** on this job. The *remaining* loss to be recognized on future work is approximately $89,020 − $62,503 = **$26,517**, which should be accrued as a liability (a "provision for loss on contract") in the September 30 balance sheet if not already recorded.

> **Action:** Confirm with your PM whether the $1,230,750 ETC is current and complete. If there is any chance it is understated, the loss – and the required accrual – grows. If a loss accrual is needed and not yet booked, it will increase current liabilities and reduce working capital further.

> *Rough sensitivity: Every $10,000 of additional loss accrual reduces working capital by $10,000. With $98,582 of headroom, you have room for about $98K of adverse adjustments before breaching – but that's not a large cushion.*

### 🔴 Issue 2 – The $140,000 Delay Claim Must Be Excluded
If your workbook includes the claim anywhere – in contract value, as a receivable, or as a contract asset – it must come out. The October 22 rejection letter is a *Type I subsequent event* (it provides evidence of conditions that existed at September 30, since the dispute was clearly live before year-end). Including the claim would be a GAAP departure and likely a misrepresentation on the compliance certificate.

If you have already excluded it, document that decision in your workpapers with reference to the rejection letter. Your auditors or the bank's field examiner will ask.

### 🟡 Issue 3 – Riverside Overbilling at Early Stage
Being $90K overbilled at only 22% complete on a $1.1M job is not automatically a problem, but it warrants a check. Make sure the $732,200 ETC is realistic and that your billing schedule isn't front-loaded in a way that will compress future billings and cash flow. If the ETC later proves understated, the contract liability grows and working capital shrinks.

### 🟡 Issue 4 – Headroom Is Still Thin
Even on corrected numbers, $98,582 of headroom on a $1,250,000 covenant is roughly 7.9%. One bad ETC revision on Lakeview, one billing timing issue, or a loss accrual could move you to the edge. Consider whether a proactive conversation with your bank is appropriate – most lenders prefer early transparency to a surprise waiver request.

---

## Bottom Line

| Question | Answer |
|---|---|
| Do you meet the covenant at September 30? | **Yes, $1,348,582 vs. $1,250,000 minimum** |
| Is there anything to fix before signing? | **Yes – three things** |

**Before you sign the compliance certificate:**

1. **Confirm the $140,000 claim is completely excluded** from the WIP schedule and from any receivables. Document why.
2. **Get a fresh ETC from your PM on Lakeview** and determine whether a loss contract accrual is required. Book it if so.
3. **Review the Riverside ETC** to make sure the early-stage overbilling isn't masking a cost problem.

If the Lakeview ETC holds and no loss accrual is required beyond what's already embedded, you pass and can sign – but I'd recommend keeping those workpapers tight, because with sub-$100K headroom, your bank may scrutinize this one closely.

---

*This analysis is based solely on the figures you provided. I haven't reviewed the underlying job cost reports, the change-order documentation, the loan agreement definition of "working capital," or the full balance sheet. Have your CPA review the loss contract question on Lakeview before you finalize.*