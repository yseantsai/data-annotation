## Validating Your 2027 Gross Profit Estimate

Let me rebuild this from scratch so you can see every assumption and catch anything that doesn't match your records.

---

### Step 1: Establish the 2026 Baseline

| Item | Amount |
|---|---|
| Contract revenue | $14,236,800 |
| Direct labor (incl. taxes & comp) | $8,228,870 |
| Cleaning supplies & equipment | $839,971 |
| **Gross profit** | **$5,167,959** |

**Gross margin: 36.3%**

---

### Step 2: Characterize the Contract Portfolio

You have two populations:

**Pass-through accounts (61 contracts)**
- Revenue: $9,174,260
- Share of total: 64.4%

**Standard accounts (82 contracts)**
- Revenue: $14,236,800 − $9,174,260 = **$5,062,540**
- Share of total: 35.6%

---

### Step 3: Quantify the Wage Increase

The raise is $18.40 → $19.75, an increase of **$1.35/hour**, or **7.337% on the base wage rate**.

Your $8,228,870 direct labor figure already includes payroll taxes and comp. The wage component drives those burdens, so the full burdened cost scales with the wage rate.

**Burdened labor cost increase = $8,228,870 × 7.337% = $603,533**

This is what it costs you on a full-year basis to run every 2026 hour at the new rate. I'll allocate it between populations below.

*Proportional allocation by revenue (a reasonable proxy absent job-level data):*

| Population | Revenue share | Labor cost increase |
|---|---|---|
| Pass-through (64.4%) | 64.4% | $388,675 |
| Standard (35.6%) | 35.6% | $214,858 |

---

### Step 4: Pass-Through Accounts

These 61 accounts receive 30-day notice this week, so the wage increase bills to them starting **February 1** (conservative; if notices go out before December 2 you may capture all of January as well, but I'll use February to be safe with your owners).

**Pass-through revenue added:**
$388,675 × (11/12 months) = **$356,286**

They then renew onto 6.5% pricing on their individual anniversary dates. The pass-through mechanism replaces their pricing increase until renewal, at which point the 6.5% applies to the then-current contract price — but since you're modeling 2027 and they carry the wage recovery until renewal, there's no double-count issue within the year.

**Attrition:** You flagged 4% loss on *renewing* revenue. Pass-through accounts renew at their start-date anniversaries, so the same attrition logic applies to them. I'll work attrition into Step 6 uniformly.

---

### Step 5: Distributing Renewal Months — 6.5% Price Increase

Absent your actual contract start-date distribution, the standard assumption for a portfolio of annual contracts is uniform distribution — roughly 1/12 of revenue renewing each month. The 6.5% increase on a contract renewing in month *M* earns revenue for (13 − M) months in 2027.

**Expected revenue capture of 6.5% increase, full portfolio, before attrition:**

$$\text{Incremental revenue} = \text{Annual revenue} \times 6.5\% \times \frac{\sum_{M=1}^{12}(13-M)}{12 \times 12}$$

The weighted average months of capture = (12+11+10+...+1)/12 = **6.5 months**

$$= \$14,236,800 \times 6.5\% \times \frac{6.5}{12} = \$14,236,800 \times 6.5\% \times 0.5417 = \$501,081$$

This applies to **all 143 contracts** at renewal. Pass-through accounts get the wage recovery from February and then the 6.5% price increase at renewal — these are sequential, not simultaneous, so there's no overlap to net out within the year.

---

### Step 6: Attrition — 4% of Renewing Revenue

Dana's 4% loss assumption applies to revenue at the moment of renewal. With uniform distribution, every contract renews once during 2027.

**Revenue lost to attrition:**

The lost revenue is 4% of the base, but since it's lost at the renewal point, you lose the *post-increase* price for the remaining months. For a contract renewing in month M, you lose 6.5%-priced revenue for (13 − M) months.

Blended lost revenue:
- Lost base revenue (full year equivalent): $14,236,800 × 4% = $569,472
- Weighted average remaining months after renewal: 6.5/12 = 0.5417 of a year
- Lost base revenue actually billed in 2027: $569,472 × 0.5417 = **$308,428**
- Lost incremental (6.5%) revenue: $569,472 × 6.5% × 0.5417 = **$20,048**
- **Total revenue lost to attrition: $328,476**

**Labor and supplies saved on lost accounts** (variable costs go away with the account):
- Lost accounts represent 4% of portfolio labor and supplies
- Labor saved: $8,228,870 × 4% × 0.5417 = **$178,163**
- Supplies saved: $839,971 × 4% × 0.5417 = **$18,191**
- **Total variable cost saved: $196,354**

**Net gross profit impact of attrition: −$328,476 + $196,354 = −$132,122**

---

### Step 7: 2027 Labor Cost — Full Year at New Rate

The base labor cost at the new wage for the full portfolio (before attrition):

$$\$8,228,870 \times \frac{\$19.75}{\$18.40} = \$8,228,870 \times 1.07337 = \$8,832,403$$

**Incremental labor cost vs. 2026: $603,533**

After removing labor for lost accounts:
$8,832,403 − $178,163 = **$8,654,240**

---

### Step 8: 2027 Supplies Cost

Supplies scale with revenue retained. Lost accounts take 4% of supplies × 0.5417 year:

$839,971 − $18,191 = **$821,780**

---

### Step 9: 2027 Revenue Build

| Component | Amount |
|---|---|
| 2026 base revenue | $14,236,800 |
| Pass-through wage recovery (Feb–Dec) | +$356,286 |
| 6.5% price increase at renewal | +$501,081 |
| Attrition loss | −$328,476 |
| **2027 Total Revenue** | **$14,765,691** |

---

### Step 10: 2027 Gross Profit

| Item | 2026 | 2027 |
|---|---|---|
| Revenue | $14,236,800 | $14,765,691 |
| Direct labor | $8,228,870 | $8,654,240 |
| Supplies & equipment | $839,971 | $821,780 |
| **Gross profit** | **$5,167,959** | **$5,289,671** |
| **Gross margin** | **36.3%** | **35.8%** |

**Year-over-year change: +$121,712**

---

### Where the Difference With Your Number Comes From

Your figure showed gross profit **down ~$56,000**. This model shows it **up ~$122,000** — a gap of roughly $178,000. The most likely sources:

| Factor | Direction | Magnitude |
|---|---|---|
| Pass-through billing start (Jan vs. Feb) | Upward | ~$32,000 |
| Whether 6.5% applies to pass-through accounts at renewal *on top of* recovered base | Upward | Depends on contract count/renewal timing |
| Your internal labor burden rate may differ from the proportional allocation I used | Either direction | Could be significant |
| Attrition applied to gross revenue vs. net-of-increase revenue | Modest | ~$10,000–20,000 |

**The most important question for your March defensibility:** What labor burden rate (taxes + comp as a percentage of gross wages) are you carrying? If your burden rate is, say, 22%, the $1.35 raise generates a different total cost increase than the proportional method I used. I'd recommend running the wage increase as:

> **Total burdened hours × $1.35 × (1 + burden rate)**

If you have total hours worked in 2026, that's the cleaner path to the labor delta.

---

### What I'd Confirm Before December 3

1. **Notice dates:** If notices go out this week and 30 days puts you at January 1 or January 2, you recover the full 12 months on pass-through accounts — worth ~$32,000 to your number.
2. **Pass-through account renewal distribution:** If those 61 contracts are weighted toward early-year renewals, they flip to 6.5% pricing faster and you capture more of the increase.
3. **Actual labor burden rate** vs. my proportional proxy.
4. **Whether the 4% attrition is concentrated in pass-through or standard accounts** — losing a large pass-through account early in the year has an outsized labor cost impact since you stop absorbing the unrecovered portion of the wage increase.
5. **Dana's $925,000 figure** — back-check whether she was applying 6.5% to the full $14.2M for 12 months ($925,392 would be exactly that), which confirms she made no renewal-timing adjustment. Your rebuild of that number is the right approach.

The directional story for your owners is sound: the pass-through clause does its job, the 6.5% increase at renewal offsets most of the remaining labor cost increase, and attrition is a manageable drag. Whether gross profit is up $122K or down $56K turns on the labor arithmetic, and that's worth pinning down before the 3rd.