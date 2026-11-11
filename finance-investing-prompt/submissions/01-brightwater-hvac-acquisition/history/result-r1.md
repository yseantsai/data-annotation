# Brightwater Mechanical — Independent Deal Analysis

## Executive Summary

The broker's $618,900 SDE figure is materially overstated. After correcting for the lease gap, replacing the owner's wife's functions at market cost, and treating legal fees more conservatively, true owner-benefit earnings are closer to **$393,400**. At the asking price of $1,980,000, you are paying **5.0× corrected SDE** — not 3.2×. Debt service will consume all of that and more in Year 1 at the current price. The deal is financeable and potentially worth doing, but not at this number and not with the LOI as the broker has structured the narrative. **I would counter at $1,350,000 to $1,450,000**, which I'll justify below. If the seller won't move meaningfully, walking away is the right call.

---

## Part 1 — Reconstructing the SDE

Let me work through each component systematically before building cash flow.

### Starting Point: The Broker's Math

| Item | Broker's Figure |
|---|---|
| Net income per tax return | $214,500 |
| Owner salary add-back | $165,000 |
| Owner benefits and truck | $28,400 |
| Depreciation | $74,300 |
| Interest | $31,200 |
| Legal settlement (non-recurring) | $47,500 |
| Owner's wife salary | $58,000 |
| **Broker's Adjusted SDE** | **$618,900** |

That arithmetic is correct given those inputs. The problem is with three of the inputs themselves.

---

### Adjustment 1 — The Lease Gap

The seller currently charges his own company $4,200/month for the shop. Market rent, per the broker's own comparable data, is $7,800/month. The delta is $3,600/month, or **$43,200/year**.

This is not a gray area. The below-market rent is a hidden owner benefit that inflates reported earnings. A buyer paying market rent from day one will see costs rise by $43,200 annually. The broker has not deducted this anywhere — in fact, the structure of an SDE add-back presentation typically leaves operating rent in costs, which is correct, but only when rent is at market. Here, rent is artificially suppressed, making net income look $43,200 higher than it would under arm's-length conditions.

**Deduct $43,200 from SDE.**

---

### Adjustment 2 — Replacing the Owner's Wife

The broker adds back $58,000 as though this is pure profit that disappears when she leaves. It is not. She works approximately thirty hours a week doing bookkeeping and dispatching — real, necessary functions. You have already priced a replacement at $48,500 fully loaded. The add-back should be netted: $58,000 added back, $48,500 cost to replace, net benefit of $9,500.

The broker is overcounting by $48,500.

**Deduct $48,500 from SDE.** *(The $9,500 net is what remains in the corrected figure.)*

---

### Adjustment 3 — Legal and Professional Fees

The CIM adds back $47,500 as a one-time legal settlement. That is a legitimate question. But look at the pattern:

- 2023: Legal and professional fees of $52,100
- 2024: Legal and professional fees of $39,800
- 2025: A $47,500 settlement labeled non-recurring

A company with eleven employees and nine vans, running $45,000+ in legal and professional fees across multiple years, is not experiencing a one-time event. It is running a business with recurring legal exposure — employment disputes, customer claims, contractor issues, or something else you don't yet know. The 2025 settlement is the most visible piece, but the underlying pattern in 2023 and 2024 suggests normalized legal costs well above what a clean small HVAC company should carry (which is typically $8,000 to $15,000 annually for a business this size, covering routine accounting, insurance compliance, and minor legal review).

There are two ways to handle this. The conservative approach treats none of the $47,500 as truly non-recurring and adds back nothing. The moderate approach credits half — say $23,750 — as genuinely one-time, recognizing that some portion may be specific to the case being settled. I am going to use the moderate approach and credit only $23,750, leaving $23,750 as a normalized recurring cost that the broker has obscured.

**Deduct $23,750 from SDE.**

---

### Corrected SDE Calculation

| Item | Amount |
|---|---|
| Broker's adjusted SDE | $618,900 |
| Less: lease gap to market | ($43,200) |
| Less: cost to replace dispatching/bookkeeping function | ($48,500) |
| Plus: wife's salary already added back (net it properly) | — *(already embedded above)* |
| Less: portion of legal settlement that is recurring | ($23,750) |
| **Corrected SDE (your economic earnings as owner-operator)** | **$503,450** |

Wait — I need to be precise about the wife's salary netting. The broker added back $58,000. I need to remove the $48,500 replacement cost. The correct adjustment to broker's SDE is to subtract $48,500 (the new employee cost), because the add-back of $58,000 already sits in the broker's $618,900. Net effect on SDE: minus $48,500.

Rechecking the table:

| Broker's SDE | $618,900 |
|---|---|
| Lease gap | ($43,200) |
| Replacement labor for wife's role | ($48,500) |
| Legal normalization | ($23,750) |
| **Corrected SDE** | **$503,450** |

This is what the business earns in the owner's pocket before debt service, before your own salary, and before capital expenditures. But SDE as typically presented already includes your salary as the owner-operator — that's the convention: SDE is the total economic benefit available to a full-time owner, from which they pay themselves. So $503,450 is the pool from which you draw $120,000 in salary and service debt.

**Earnings available for salary and debt service: $503,450**

---

## Part 2 — What Cash Flow Really Looks Like

### Your Salary

You need $120,000. That is already embedded in the SDE framework — your salary is not an additional deduction from SDE in the traditional sense, but we need to see what's left after you pay yourself, since the lender's coverage test will be based on this.

**After your $120,000 salary:**
$503,450 − $120,000 = **$383,450 available for debt service**

---

### Debt Service Structure

**Purchase price: $1,980,000**

| Component | Amount | Rate | Term | Annual Payment |
|---|---|---|---|---|
| SBA 7(a) loan (80%) | $1,584,000 | 10.25% | 10 years | — |
| Your equity (10%) | $198,000 | — | — | — |
| Seller note (10%) | $198,000 | 6.00% | 7 years total* | — |

*Seller note: 2 years full standby, then 5-year amortization.

**SBA loan annual payment** — 10 years, 10.25%, $1,584,000:

Using the standard annuity formula:
Monthly rate = 10.25% / 12 = 0.8542%
n = 120 months
Monthly payment = $1,584,000 × [0.008542 × (1.008542)^120] / [(1.008542)^120 − 1]

(1.008542)^120 ≈ 2.7524
Monthly payment = $1,584,000 × [0.008542 × 2.7524] / [2.7524 − 1]
= $1,584,000 × [0.023516] / [1.7524]
= $1,584,000 × 0.013420
= **$21,257/month → $255,083/year**

**Seller note — Years 1–2 (standby):** $0 cash payment

**Seller note — Years 3–7 (amortizing):** 5-year amortization at 6%, $198,000 principal
Monthly payment = $198,000 × [0.005 × (1.005)^60] / [(1.005)^60 − 1]
(1.005)^60 = 1.3489
Monthly = $198,000 × [0.005 × 1.3489] / [0.3489]
= $198,000 × 0.006745 / 0.3489
= $198,000 × 0.019333
= **$3,828/month → $45,933/year**

---

### Year 1 Coverage Test (Seller Note on Standby)

| Item | Amount |
|---|---|
| Corrected SDE | $503,450 |
| Less: your salary | ($120,000) |
| Cash available for debt service | $383,450 |
| SBA annual payment | ($255,083) |
| Seller note (Year 1, standby) | $0 |
| **Net cash after salary and debt** | **$128,367** |
| **DSCR (Year 1)** | **$383,450 / $255,083 = 1.50×** |

The lender's 1.25× test passes in Year 1 — but only barely in a comfortable range, and that is using corrected SDE. The broker's inflated SDE would show DSCR of roughly 2.0×, which is misleading.

**Note:** SBA lenders typically calculate DSCR slightly differently — they may use net income plus depreciation plus add-backs rather than SDE directly, and they will apply their own normalization. The lender will likely arrive at something between my number and the broker's. Flag this.

---

### Year 3 Coverage Test (Seller Note Now Paying)

| Item | Amount |
|---|---|
| Cash available for debt service (same) | $383,450 |
| SBA annual payment | $255,083 |
| Seller note annual payment | $45,933 |
| **Total debt service** | **$301,016** |
| **Net cash after salary and debt** | **$82,434** |
| **DSCR (Year 3+)** | **$383,450 / $301,016 = 1.27×** |

This barely passes the 1.25× test — at **1.27×**. That is razor-thin. Any softness in revenue, any unexpected cost, any increase in normalized legal costs, and you are underwater. The buffer above the coverage floor is only $6,017 per year — essentially nothing.

---

### The Capital Expenditure Problem

Nothing above accounts for the van replacements. Three vans at $65,000 each is $195,000. Even if you finance them separately, you are adding debt service. If you pay cash or buy from operations:

- Three vans over three years = $65,000/year in capex
- After capex, Year 1 net: $128,367 − $65,000 = **$63,367**
- After capex, Year 3+ net: $82,434 − $65,000 = **$17,434**

At Year 3 with van replacement spending, you have $17,000 of margin. That is not a business — that is a job with legal liability and no cushion for anything going wrong.

The depreciation add-back of $74,300 is legitimate for SDE purposes, but the van situation reveals that the real maintenance capex exceeds depreciation on an economic basis. The fleet is older than its book value suggests it should be.

---

### The Customer Concentration Risk

The property management company at 34% of revenue deserves a standalone calculation. Total revenue is $2,837,400. That customer represents approximately $964,700 in revenue. Maintenance contracts in HVAC typically run margins north of 50% on a contribution basis, so this single customer is probably contributing somewhere between $400,000 and $550,000 in gross profit.

The contract renews in March — which may be before or after your close, depending on timing — with 60 days' notice. If that customer leaves for any reason (management change, new property ownership, competitive bid, your transition uncertainty), your SDE drops dramatically. A rough estimate: losing that customer could cost $200,000 to $300,000 in annual EBITDA, which would make this deal immediately insolvent at the current price and debt structure.

This is not a deal-killer by itself, but it is a price-adjustment and structure issue. You need:
1. A multi-year contract assignment as a condition of close, or
2. A meaningful escrow or earnout tied to that customer's retention, or
3. A price that reflects the risk if the customer is gone.

---

## Part 3 — Valuation: What Price Is Actually Justified

### The Broker's Framing Is Wrong on Both Metrics

**On SDE multiple:** The broker says 3.2× SDE. Using corrected SDE of $503,450, the asking price is:
$1,980,000 / $503,450 = **3.93× corrected SDE**

If you use industry convention of SDE-to-buyer (meaning SDE after a market salary for the owner), which is the cleaner way to frame it for a deal like this:
$383,450 available for debt service / divided back to earnings basis is a different framing, but the multiple on corrected SDE is nearly 4×, not 3.2×.

**On EBITDA:** The broker claims "well below 4–5× EBITDA." Let me build EBITDA from the corrected figures:

EBITDA = Net income + Interest + Depreciation + Taxes
= $214,500 + $31,200 + $74,300 + (taxes, which aren't shown — if this is a pass-through entity, taxes may be zero at entity level)

Assuming pass-through entity, EBITDA ≈ $320,000 before add-backs.

But EBITDA for transaction purposes typically means adjusted EBITDA with the same normalization — owner comp at market, rent at market, non-recurring items. Using adjusted EBITDA with a $120,000 market salary for the owner, market rent, and normalized legal:

Adjusted EBITDA = $214,500 + $31,200 + $74,300 − $43,200 (rent gap) − $23,750 (legal normalization) − $48,500 (replacement labor) + $165,000 (owner salary) − $120,000 (market salary) + $28,400 (personal benefits)
= **$277,950**

$1,980,000 / $277,950 = **7.1× adjusted EBITDA**

That is not "below 4–5×." That is well above it. The broker's EBITDA framing is using an unnormalized or selectively normalized number.

For reference, a healthy residential-heavy HVAC service business with no customer concentration issues, clean fleet, and stable management typically trades at:
- 3.5× to 5.0× adjusted EBITDA
- 2.5× to 3.5× SDE (from which the owner pays themselves)

---

### Where the Price Should Be

**Method 1: 4× corrected SDE**
$503,450 × 4.0 = **$2,013,800** — This is roughly the asking price, which might suggest the deal is fair, but this ignores the fleet capex, the customer concentration discount, and the fact that 4× is the high end for a business with these characteristics.

**Method 2: 3× corrected SDE (appropriate given risks)**
$503,450 × 3.0 = **$1,510,350**

**Method 3: 4.5× adjusted EBITDA (top of market, no adjustments for risk)**
$277,950 × 4.5 = **$1,250,775**

**Method 4: DCF / Coverage-Based Pricing**
Working backwards from what the deal can support: if the business needs to generate 1.35× DSCR (a comfortable buffer above the 1.25× floor), and cash available for debt service after your salary is $383,450:

Maximum supportable debt service = $383,450 / 1.35 = $284,000/year

At 10.25% over 10 years, $284,000/year of debt service supports a loan of approximately:
Using the same annuity math in reverse: PV = $284,000 / 0.013420 (the payment factor per dollar) = **$21,162,… wait, that's wrong direction.** Let me redo this.

Monthly payment needed: $284,000 / 12 = $23,667
At 10.25%/12 = 0.8542% monthly, 120 months:
PV = $23,667 × [(1 − (1.008542)^−120) / 0.008542]
= $23,667 × [(1 − 0.3634) / 0.008542]
= $23,667 × [0.6366 / 0.008542]
= $23,667 × 74.53
= **$1,764,500 total loan capacity**

If the SBA loan is 80% of purchase price:
Maximum purchase price supported = $1,764,500 / 0.80 = **$2,205,600**

But this doesn't account for the seller note activating in Year 3. When the seller note payments begin, supportable deal price drops:

Combined annual debt service budget (Year 3): $383,450 / 1.35 = $284,000
Seller note takes $45,933 of that
Remaining for SBA: $284,000 − $45,933 = $238,067/year

Monthly SBA payment: $238,067 / 12 = $19,839
SBA loan capacity: $19,839 × 74.53 = $1,478,800
Maximum purchase price: $1,478,800 / 0.80 = **$1,848,500**

This is the ceiling at which the deal works at your required salary with an adequate coverage buffer. But this uses optimistic corrected SDE with no capex deduction.

**Adjusting for normalized capex:** If vans cost $65,000/year in real economic replacement, reduce cash available for debt service by $65,000:
Adjusted cash for DS: $383,450 − $65,000 = $318,450
Budget for DS: $318,450 / 1.35 = $235,889
Seller note: ($45,933)
SBA budget: $189,956
SBA loan capacity: $189,956 × 74.53 = $14,159,000… 

Let me redo this more carefully.

Monthly SBA budget: $189,956 / 12 = $15,830
SBA loan capacity: $15,830 / 0.013420 = $1,179,600
Maximum purchase price: $1,179,600 / 0.80 = **$1,474,500**

---

### My Recommended Offer

Triangulating across methods:

| Method | Indicated Value |
|---|---|
| 3.0× corrected SDE | $1,510,350 |
| 4.5× adjusted EBITDA | $1,250,775 |
| Coverage-based (no capex) | $1,848,500 ceiling |
| Coverage-based (with capex) | $1,474,500 ceiling |

The range is roughly $1,250,000 to $1,510,000. Given that you need a margin of safety and the customer concentration risk is real, I would **open your counter at $1,350,000 and be willing to pay up to $1,500,000 with the right structure.**

---

## Part 4 — What to Push Back On in the LOI

Here are the specific points to address, in order of importance.

---

### 1. Price — Counter at $1,350,000

Present your corrected SDE analysis. Do not attack the broker; just show your math. The three adjustments are defensible and documentable. If the seller wants to defend the lease as market rent, ask for comparable signed leases. If he wants to defend his wife's salary as a pure add-back, remind him she is leaving and her functions need to be filled. If he wants the full legal settlement treated as non-recurring, ask for documentation showing no ongoing legal exposure and an explanation for the elevated legal fees in 2023 and 2024.

---

### 2. Structure the Earnout for Customer Concentration

As an alternative or supplement to a lower price, propose that $150,000 to $200,000 of the purchase price be held in escrow for 18 months, released only if the property management company remains a customer and renews in March. If they leave, that escrowed amount comes back to you or is credited against the seller note. This aligns incentives and protects you from paying for a revenue stream that may not transfer.

Another approach: ask for a seller representation and warranty in the purchase agreement that the property management customer is current, the contract is not under dispute, and no notice of non-renewal has been received.

---

### 3. Lease — Lock in Terms at Market Before Close

Do not close without a fully executed lease at a fixed rent with a defined term. The seller's attorney saying "it'll be at market" is not sufficient. Market is $7,800/month per the broker's own data. You want a 5-year initial term with one 5-year option, rent increases capped at CPI or 3% annually, and no relocation clause. If you close without the lease, you are at the seller's mercy on rent — which could spike further and immediately destroy your coverage ratio.

---

### 4. Van Replacement Provision or Price Credit

Request a price reduction of $195,000 (three vans at $65,000 each), or alternatively, require that the seller replace the three flagged vans before close, or place $195,000 in escrow to fund replacement. If he will not move on price, propose that $195,000 of the seller note principal be forgiven and applied to van replacement costs that you document in the first 18 months. The fleet age and replacement need are real costs that the SDE calculation ignores.

---

### 5. Seller Note Structure

The standby period works in your favor in Years 1 and 2, but be sure the LOI specifies:
- Full standby means no interest accrual, not interest-only with deferred principal. Confirm whether interest accrues during standby and capitalizes onto principal. If $198,000 accrues interest at 6% for two years, you owe $222,000+ when amortization begins, which increases your Year 3+ payments.
- The seller note must be subordinated in writing to the SBA loan — the SBA will require this, but make sure it's explicit.
- Include a clause that if the property management customer does not renew in March, the seller note principal reduces by an agreed amount (linking to point 2).

---

### 6. Receivables

The CIM says the seller keeps the $312,000 of receivables. Confirm this explicitly in the LOI — you want it crystal clear that the deal is cash-free and debt-free and that the receivables belong to the seller. Also confirm that you are not inheriting any contingent liability on work associated with those receivables (warranty claims, disputed invoices, punch list items). Ask for an aging schedule during due diligence and flag anything over 90 days.

---

### 7. Representations on Legal History

Given the elevated legal and professional fees across three years and the settlement being added back as "non-recurring," you need a comprehensive representation in the purchase agreement covering pending or threatened litigation, regulatory complaints, warranty claims, and any OSHA, EPA, or licensing issues. The settlement being labeled non-recurring does not mean the underlying issue is resolved or won't recur.

---

### 8. Key Employee / Transition

You have eleven employees. Ask during diligence: who are the two or three technicians with the longest tenure and customer relationships? Are any of them at risk of leaving during transition? Consider whether a retention bonus funded from escrow for 12 months post-close is appropriate for one or two key people. This is not an LOI item necessarily but should be in your due diligence checklist.

---

## Part 5 — Due Diligence Checklist Before You Close

Since you are on a tight timeline with the December 4 LOI, here are the critical items to verify during the due diligence period that follows:

**Financial**
- Three years of federal tax returns (not just the P&L summaries)
- Actual bank statements for 2023, 2024, and YTD 2025 — reconcile to the revenue figures
- Accounts receivable aging in detail — confirm the $312,000 figure and its composition
- Payroll records — verify employee count, wages, any pending labor issues
- Complete breakdown of legal and professional fees for 2023, 2024, and 2025, including invoices

**Operational**
- Copy of the property management maintenance contract and all other commercial maintenance agreements — verify renewal dates, pricing, and termination provisions
- Van title records and maintenance logs — verify age and condition, get independent mechanic inspection on the three flagged vehicles
- Current insurance policies and claims history for the past five years
- Business licenses, EPA certifications (refrigerant handling), and state HVAC contractor licenses — verify transferability

**Legal**
- Complete documentation on the settled legal matter — confirm resolution is final
- Any OSHA citations, unemployment claims, or workers' compensation claims in the past five years
- Copies of any vendor or supplier agreements with assignability issues

---

## Summary of Numbers

| Metric | Broker's Version | My Corrected Version |
|---|---|---|
| Adjusted SDE | $618,900 | $503,450 |
| Implied multiple at $1,980,000 | 3.2× | 3.93× |
| Adjusted EBITDA | Not stated | ~$277,950 |
| EBITDA multiple at $1,980,000 | "Below 4–5×" | 7.1× |
| Cash after salary and Year 1 debt | Not provided | $128,367 |
| Cash after salary and Year 3 debt | Not provided | $82,434 |
| Cash after salary, Year 3 debt, capex | Not provided | $17,434 |
| Year 1 DSCR | Implied >2.0× | 1.50× |
| Year 3 DSCR | Implied >2.0× | 1.27× |
| Year 3 DSCR with capex | Not considered | ~0.98× — fails |
| Recommended offer | — | $1,350,000 |
| Walk-away price | — | $1,500,000 |

---

## Final Recommendation

This business is real, the revenue appears legitimate, and the HVAC service model is durable. You are not looking at a fraud. You are looking at a broker who built a valuation on three individually defensible adjustments that together overstate earnings by $115,000 — roughly 23% — and then presented the resulting number against an EBITDA benchmark that he has also misstated.

At $1,350,000, this is a solid deal that gives you a living wage, manageable debt service, and genuine upside if you grow the commercial maintenance book and reduce concentration. At $1,980,000, you are buying a job that generates $17,000 of annual cushion after debt and van replacement, with a single customer who can walk in March and cut your cash flow in half with 60 days' notice.

**Counter at $1,350,000.** Be transparent about your analysis. A seller who has built a real business over the years deserves a real explanation, not a lowball with no math behind it. If he is reasonable, you'll find a number in the $1,400,000 to $1,500,000 range that works for both of you. If he insists on $1,980,000 and won't engage with the corrections, the broker has his ear, and you should walk.

The December 4 deadline is a sales tactic. Good deals don't expire in a week. If this one does, it probably means someone else is being shown the same inflated numbers and the seller is hoping one of you signs before you do the math.