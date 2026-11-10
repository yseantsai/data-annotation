I'll build this out systematically so every number ties before we touch the commentary.

---

## Step 1: Establish the Budget and Actual P&L

**Budget**

| Line | Units | Avg Price | Revenue | Unit Cost | COGS | Gross Profit |
|---|---|---|---|---|---|---|
| Standard | 18,350 | $212.40 | $3,895,440 | $161.85 | $2,969,948 | $925,493 |
| Heavy-duty | 6,880 | $468.90 | $3,225,432 | $322.15 | $2,216,392 | $1,009,040 |
| **Total** | **25,230** | | **$7,120,872** | | **$5,186,340** | **$1,934,533** |

Budget gross margin: $1,934,533 / $7,120,872 = **27.2%** ✓

**Actual**

| Line | Units | Avg Price | Revenue | Unit Cost | COGS | Gross Profit |
|---|---|---|---|---|---|---|
| Standard | 23,640 | $203.10 | $4,801,284 | $166.95 | $3,946,698 | $854,586 |
| Heavy-duty | 5,135 | $472.30 | $2,425,261 | $331.20 | $1,700,772 | $724,489 |
| **Total** | **28,775** | | **$7,226,545** | | **$5,647,470** | **$1,579,075** |

Actual gross margin: $1,579,075 / $7,226,545 = **21.9%** ✓

**The miss: $1,579,075 − $1,934,533 = −$355,458 in gross profit dollars**

In percentage points: 21.9% − 27.2% = **−5.3 pp**

---

## Step 2: Build a Clean Margin Bridge

I'll use a classic volume / mix / price / cost bridge. The order matters: volume and mix use budget rates; price and cost variances use actual volumes.

### Bridge Components

---

### 2A. Volume Effect (holding budget mix and budget margins)

Actual total units were 28,775 vs. budget 25,230, an increase of 3,545 units.

At budget blended margin per unit:
- Budget blended margin per unit = $1,934,533 / 25,230 = **$76.68/unit**
- Pure volume effect = 3,545 × $76.68 = **+$271,831**

---

### 2B. Mix Effect

The volume increase was entirely in standard units (cheapest, lowest-margin line) while heavy-duty ran short. We need to isolate the margin impact of shipping a richer or poorer mix than budgeted.

Method: Hold each line at its budget margin per unit, compare actual mix to budget mix at actual total volume.

**Budget margin per unit:**
- Standard: $212.40 − $161.85 = **$50.55**
- Heavy-duty: $468.90 − $322.15 = **$146.75**

**Expected GP at actual volumes using budget margins:**

| Line | Actual Units | Budget Margin/Unit | Expected GP |
|---|---|---|---|
| Standard | 23,640 | $50.55 | $1,195,002 |
| Heavy-duty | 5,135 | $146.75 | $753,541 |
| **Total** | | | **$1,948,543** |

Mix + volume combined = $1,948,543.
Volume effect already calculated = +$271,831 (i.e., budget GP $1,934,533 + $271,831 = $2,206,364 at budget mix scaled to actual volume).

**Mix effect = $1,948,543 − $2,206,364 = −$257,821**

This is the largest single driver of the miss. The company shipped 3,545 more standard units and 1,745 fewer heavy-duty units than budgeted. Heavy-duty carries nearly three times the margin per unit ($146.75 vs. $50.55). Losing that heavy-duty volume and replacing it with standard is severely dilutive.

---

### 2C. Selling Price Effect (actual units × price change vs. budget)

**Standard:** ($203.10 − $212.40) × 23,640 = −$9.30 × 23,640 = **−$219,852**

**Heavy-duty:** ($472.30 − $468.90) × 5,135 = +$3.40 × 5,135 = **+$17,459**

**Net price effect = −$202,393**

The standard-line promotion cost $219,852 in revenue at actual volumes, partially offset by a small heavy-duty price gain.

---

### 2D. Unit Cost Effect (actual units × cost change vs. budget)

Higher unit cost = worse margin, so favorable/unfavorable is inverted from price.

**Standard:** ($166.95 − $161.85) × 23,640 = +$5.10 × 23,640 = **−$120,564**

**Heavy-duty:** ($331.20 − $322.15) × 5,135 = +$9.05 × 5,135 = **−$46,472**

**Net unit cost effect = −$167,036**

---

### 2E. Bridge Summary

| Driver | $ Impact | pp Impact* |
|---|---|---|
| Volume (more units shipped) | +$271,831 | +3.8 pp |
| Mix (shift toward standard, away from heavy-duty) | −$257,821 | −3.6 pp |
| Selling price (standard-line promotion) | −$202,393 | −2.8 pp |
| Unit cost increase | −$167,036 | −2.3 pp |
| **Total variance** | **−$355,419** | **−5.3 pp** |
| Rounding vs. exact | −$39 | — |

*pp impacts are approximate; they're converted by dividing the dollar impact by actual revenue of $7,226,545. The residual $39 is rounding throughout the unit cost and price calculations.

**The bridge ties to −$355,458 (within $39 of rounding).**

---

## Step 3: Decompose the Unit Cost Variance — Where Does the Surcharge Actually Land?

This is where Dale's number needs scrutiny.

### 3A. Steel Consumed in Q3 Under FIFO

You need to know how many tons were actually expensed in Q3 (i.e., consumed in production), not purchased.

**Steel content per unit:**
- Standard: 82 lbs = 82/2,000 = 0.041 tons
- Heavy-duty: 176 lbs = 176/2,000 = 0.088 tons

**Tons consumed in Q3 production:**
- Standard: 23,640 × 0.041 = 969.24 tons
- Heavy-duty: 5,135 × 0.088 = 451.88 tons
- **Total consumed: 1,421.12 tons**

### 3B. FIFO Layers

| Layer | Tons | Cost Basis |
|---|---|---|
| Opening inventory Aug 1 (pre-surcharge) | 690 | Budget/pre-surcharge rate |
| Purchased Aug–Sep (at surcharge) | 412 | Surcharge price |
| Ending inventory Sep 30 | 144 | — |
| **Total available** | **1,102 tons** | |

Wait — 690 + 412 = 1,102 tons available, but consumption was 1,421 tons. That means you had steel on hand before July too. Let me re-read your note.

You stated: "690 tons on hand on August 1 after purchasing bought ahead in July." The quarter runs July–September. So steel used in July came from pre-surcharge inventory purchased before or during July (pre-August 1 purchases), and the 690 tons is the position *entering* August.

Let me re-frame the FIFO analysis for the whole quarter:

**July production steel needs:**
Total consumed Q3 = 1,421.12 tons over three months. Without a monthly production split I'll work with what you've given me: the 690-ton pre-surcharge inventory was available to cover the first portion of consumption, and 412 surcharge-priced tons were purchased in August–September.

**The key FIFO question:** How many of the 1,421 tons consumed were at the surcharge price vs. the pre-surcharge price?

Under FIFO, pre-surcharge steel is used first.

- Pre-surcharge steel available to consume (all July inventory purchases + the 690 tons entering August): The 690 tons was the balance *after* July purchasing, so it was the pre-surcharge stock entering August. July production drew from whatever was on hand at July 1 plus July purchases. Since you've only given me the August 1 position, I'll treat the 690 tons as the pre-surcharge stock available at the start of the surcharge period.
- Under FIFO, the first 690 tons consumed in August and beyond are at the pre-surcharge rate. After that, the 412 tons purchased at surcharge price flow through.
- Ending inventory of 144 tons: Under FIFO this would be the last-purchased surcharge-price steel (412 tons bought, 144 remain, so 268 tons of surcharge steel were consumed).

**Surcharge-priced steel expensed in Q3 = 412 − 144 = 268 tons**

### 3C. Surcharge Dollar Impact

The surcharge is $95/ton. The incremental cost of the 268 tons that flowed through COGS at the surcharge price:

**268 tons × $95 = $25,460**

Dale's figure of $135,000 represents the surcharge on *all steel shipped in Q3* as if every unit bore the surcharge price. That is not what FIFO expensing produces. Under FIFO, 690 tons of pre-surcharge inventory flowed first, and only 268 tons of surcharge-priced steel hit COGS this quarter. The remaining 144 tons of surcharge-priced steel sits in ending inventory and will hit Q4.

**The surcharge explains $25,460 of the $167,036 unit cost variance — roughly 15%, not the leading story.**

---

## Step 4: What Else Is in the Unit Cost Variance?

Total unit cost variance = −$167,036. We've identified $25,460 to the steel surcharge (FIFO-based). What's the rest?

**Identified cost items:**
- Overtime premium: −$71,380
- Expedited inbound freight: −$28,940
- Steel surcharge (FIFO): −$25,460
- Subtotal identified: **−$125,780**
- Remaining unidentified cost variance: **−$41,256**

The $41,256 residual is likely a combination of normal input cost inflation on non-steel materials, overhead absorption changes on the mix shift, or other manufacturing variances the plant controller hasn't yet broken out. Flag this as "under review with plant controller" in the commentary — do not leave it unexplained for the CFO.

As a sanity check: the overtime and freight are plausible given the Saturday shifts across two months and the volume surge on a build-to-order model.

---

## Step 5: The Full Picture

Here is what actually happened to your margin:

| Driver | $ Impact | % of Revenue | Key Fact |
|---|---|---|---|
| **Volume** | +$271,831 | +3.8 pp | 14% more units than budget |
| **Mix** | −$257,821 | −3.6 pp | Heavy-duty 25% below budget; standard 29% above |
| **Standard-line promotion** | −$202,393 | −2.8 pp | $9.30/unit average price reduction |
| **Overtime & expedited freight** | −$100,320 | −1.4 pp | Saturday shifts July–Aug; surge freight |
| **Steel surcharge (FIFO)** | −$25,460 | −0.4 pp | 268 of 1,421 tons consumed at surcharge price |
| **Other cost variances** | −$41,256 | −0.6 pp | Under review with plant controller |
| **Net margin variance** | **−$355,419** | **−5.3 pp** | |

---

## Step 6: Commentary for the Board Deck

Here is draft language that is defensible, sequenced correctly by magnitude, and honest about what Q4 looks like.

---

**Q3 Gross Margin Commentary**

*Gross margin was 21.9% in Q3, 530 basis points below the 27.2% budget. Revenue of $7.2M exceeded budget by $106K on unit volume 14% above plan, but four cost and price factors offset the volume benefit.*

**Mix shift (−360 bps, −$258K).** Standard-line units came in 29% above budget while heavy-duty units ran 25% below. Because heavy-duty carries roughly $96 more margin per unit than standard, the shift in composition was the single largest driver of the margin miss. Sales and operations leadership are reviewing the pipeline to assess whether Q4 heavy-duty order intake reflects timing or a structural demand change.

**Standard-line promotion (−280 bps, −$202K).** A promotional price reduction averaging $9.30 per unit was run on the standard line for most of the quarter to support volume growth. The promotion drove the 29% volume outperformance on standard, but at the cost of $202K in gross margin. We are evaluating the net contribution including absorption benefit before determining whether to extend the program.

**Overtime and expedited freight (−140 bps, −$100K).** Saturday production shifts in July and August to meet standard-line demand generated $71K in overtime premium. Surge demand also required $29K in expedited inbound freight. These costs are expected to normalize in Q4 as the production schedule returns to a standard five-day week.

**Manufacturing cost variances (−100 bps, −$67K, partially identified).** Unit costs on both lines exceeded budget. Of the $167K total unit cost variance, $25K is attributable to the Brennick Steel surcharge of $95/ton. Under our FIFO inventory policy, 690 tons of pre-surcharge steel on hand August 1 were consumed before surcharge-priced material flowed through COGS; only 268 of the 1,421 tons consumed in Q3 carried the surcharge cost. An additional $101K in cost variance is attributable to overtime and freight as noted above, and $41K remains under review with the plant controller; we will provide a complete breakdown before the board meeting.

**Steel surcharge — Q4 outlook.** The 144 tons of surcharge-priced steel in ending inventory will flow through Q4 COGS under FIFO. Assuming the surcharge remains in place, all steel purchased in Q4 will also carry the $95/ton premium. At current run rates, this will represent a more material headwind in Q4 than in Q3, as the buffer of pre-surcharge inventory has been exhausted.

**Volume benefit (+380 bps, +$272K).** The 3,545-unit volume increase above budget contributed $272K in gross profit at budget margins, partially offsetting the factors above.

---

## A Note for Your CFO Conversation

A few things worth having ready:

**On Dale's $135,000 figure:** It is arithmetically correct as a calculation of what the surcharge *would cost* if applied to every unit shipped in Q3. The problem is it doesn't reflect FIFO accounting. The pre-surcharge inventory buffer absorbed the first 690 tons of August and September consumption. The right FIFO number for the income statement is $25,460. Dale's figure is better framed as a forward-looking run-rate exposure once pre-surcharge inventory is fully depleted — which as of October 1 it is.

**On the $41K residual:** Don't leave this blank in the deck. Either get the plant controller to break it out before Thursday or explicitly label it "additional manufacturing variances under review." A CFO will accept an open item that is labeled; they won't accept one that appears to be hidden.

**On mix:** This is the story the board actually needs to hear. The margin miss looks like a cost problem but it's primarily a revenue-mix problem. If heavy-duty demand is softening, that's a strategic discussion, not just a finance one.