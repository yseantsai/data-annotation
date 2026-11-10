# 02 · Harrow Q3 margin variance

**Status:** round 1, graded, ready to submit. Fill the form from the sections below, top to bottom. Everything under "Working notes" is reference only. AHT: 2 h 25 m.

## Prompt

Copy the whole of `prompt.md` (in this folder) into **Your Prompt**.

## Generate response


Already done. The response is saved unedited in `result.md` (2,159 words, 2026-11-09). Nothing to paste into the form.

## Rating


Select **OK**.

Pretty Bad is not supported: the steel answer, the question the prompt led with, is right. Do not select Amazing or Pretty Good.

## Explanation


The model handled the steel question well. It rolled the inventory forward on FIFO, found that only 268 surcharge tons reached Q3 cost of goods ($25,460), and read Dale's $135,000 as a forward run rate.

The bridge and the board commentary it drafted are not defensible. Its budget figures carry multiplication errors (budget gross profit $1,934,533 against a correct $1,937,232.50), so it reports a $355,458 miss instead of $358,098. Its basis-point bridge divides each dollar effect by actual revenue. That gives volume "+380 bps", although more units at budget mix cannot change the margin rate, and its own lines add to 500 bps against the "530 basis points" it reports. A correct rate bridge gives volume 0, mix about 97 bps, price 207 and cost 231. It then tells the board that mix "was the single largest driver" and that the miss is "primarily a revenue-mix problem". In fact volume and mix net to only +$11,331, and the promotion's price cut, overtime and freight explain about 89 percent of the miss.

The likely cause is a shortcut from a dollar bridge to basis points instead of a rate bridge, with nothing checked against the total.

## Optional comments


Leave blank.

## AHT

**2 h 25 m** (range 2 h to 2 h 50 m) for one person with finance experience doing this round by hand. The step-by-step breakdown is under Time estimate in the working notes.

## Working notes

Reference only, not for the form: the grading behind the rating, the design and worked answer, the checks, and the history.

## Time estimate (AHT)


Estimated handle time for one person with finance experience doing this round by hand, with no AI help.

| Step | Minutes |
| --- | --- |
| Pick the failure target and design the scenario | 25 to 35 |
| Work the correct answer in a spreadsheet (variance bridge, FIFO steel layers) | 20 to 30 |
| Write the prompt, check it, read it aloud | 15 to 25 |
| Generate and read the 2,159-word response | 10 to 15 |
| Recompute the response's tables and build the rate bridge, then decide the rating | 30 to 40 |
| Write the explanation | 15 to 20 |
| Fill the form and submit | 5 |
| **Total** | **120 to 170 (about 2 h to 2 h 50 m; midpoint about 2 h 25 m)** |

One round only, inside the three-hour budget.

## Outcome


**Flawed in an essential way: the planted steel trap was caught, and the deliverable built around it is wrong.**

What the model caught (spent for this prompt family): the FIFO layering behind a pre-buy, giving $25,460 of surcharge in Q3 against the VP's $135,000; the VP's figure read as a forward run rate; the 144 tons carried into Q4; the dollar price and cost variances ($202,393 and $167,036); the cost variance split into steel, overtime, freight and a $41,256 residual flagged for the plant controller.

Where it went wrong:

1. **The basis-point bridge is wrong in method and does not tie (critical for the deliverable).** It converts each dollar effect to points by dividing by actual revenue, so volume shows "+380 bps" in the board commentary. Volume at budget mix cannot move the margin rate. The commentary lines add to 500 bps against the "530 basis points" it states. A sequential rate bridge gives volume 0, mix about 97 bps, price 207 bps and cost 231 bps.
2. **It points the board at the wrong driver (critical).** It calls mix "the single largest driver of the margin miss" and tells the requester "it's primarily a revenue-mix problem" and "if heavy-duty demand is softening, that's a strategic discussion". In dollars, quantity and mix net to +$11,331. In rate terms, mix is the smallest of the three. The promotion's price cut, overtime and freight explain about $320,000, or 89 percent of the miss, and the response never puts them together.
3. **Its budget P&L has multiplication errors, marked as checked (moderate).** Budget standard revenue is shown as $3,895,440 (correct $3,897,540), and heavy-duty as $3,225,432 (correct $3,226,032). Budget gross profit is $1,934,533 against $1,937,232.50, so the miss is reported as $355,458 instead of $358,098 and the revenue beat as "$106K" instead of $103K. The bridge is said to tie "within $39" to the wrong total. An FP&A lead asked for "numbers I can defend line by line" could not defend these against the budget book.
4. **Small slips.** The commentary's "manufacturing cost variances (-100 bps, -$67K)" is 92 bps on its own method. Scratch work is left in the answer, where it finds 1,102 tons available against 1,421 consumed and stops to "re-read your note".

**Decision: submit at OK.** The answer to the steel question is right, so the response is not a miss. The bridge and the commentary, which the requester will put in front of the board, are wrong in method and in headline. That is the platform's "flawed in some essential way", and OK is the honest rating. If a stronger failure is wanted, the alternative is to harden with `/revise-finance-investing-prompt 02`, moving the trap away from the steel layering, which is now spent.

## Failure target

The model takes the sales VP's $135,000 surcharge estimate (every unit shipped in Q3 times its steel weight times $95 a ton), or the surcharge on all 412 tons bought, and calls steel a large share of the margin miss. A practitioner rolls the steel inventory forward on FIFO, sees that the July pre-buy covered most of August and September, finds that only 268 surcharge tons reached Q3 cost of goods ($25,460, about 7 percent of the $358,098 miss), and builds a bridge that ties, showing the standard-line promotion behind most of the miss.

## Design notes

**Requester.** The FP&A lead at a steel shelving manufacturer, drafting the gross margin commentary for the Q3 board deck due to the CFO on Thursday. The VP of sales wants the commentary to lead with a supplier's steel surcharge, and the requester is inclined to agree. All entities are fictional: Harrow Rack & Shelving, Dale Okafor, Brennick Steel.

**Facts.**

| Line | Budget units | Budget price | Budget unit cost | Actual units | Actual price | Actual unit cost |
| --- | --- | --- | --- | --- | --- | --- |
| Standard | 18,350 | $212.40 | $161.85 | 23,640 | $203.10 | $166.95 |
| Heavy-duty | 6,880 | $468.90 | $322.15 | 5,135 | $472.30 | $331.20 |

- Surcharge $95 a ton from August 1. Steel content: 82 lb a standard unit, 176 lb a heavy-duty unit.
- Steel on hand August 1: 690 tons, after a July pre-buy at the old price. Bought at the surcharge price in August and September: 412 tons. On hand September 30: 144 tons. FIFO.
- Build to order, so steel issued to production in the quarter is in Q3 cost of goods.
- Promotion on the standard line for most of the quarter. Overtime premium $71,380; expedited inbound freight $28,940.

**Trap.** The VP's arithmetic is right, and his premise is wrong: he applies the surcharge to every unit shipped in the quarter, including July, and ignores the pre-bought steel that FIFO consumed first. The requester's "I redid his math and got the same figure" invites the model to accept it. A second wrong answer is the surcharge on all 412 tons bought ($39,140), which counts the 144 tons still in inventory. Underneath, the bridge has to tie: volume looks like a big positive until the mix shift toward the low-margin standard line takes nearly all of it back.

**Correct answer.**

Revenue $7,226,544.50 against budget $7,123,572.00, a beat of $102,972.50. Gross margin $1,579,134.50 (21.85 percent) against budget $1,937,232.50 (27.19 percent), a miss of $358,098.00.

| Bridge item | Amount |
| --- | --- |
| Price: standard $9.30 lower on 23,640 units | -$219,852.00 |
| Price: heavy-duty $3.40 higher on 5,135 units | +$17,459.00 |
| Cost: standard $5.10 higher on 23,640 units | -$120,564.00 |
| Cost: heavy-duty $9.05 higher on 5,135 units | -$46,471.75 |
| Sales quantity: 3,545 more units at the budget average margin of $76.78 | +$272,195.37 |
| Sales mix: shift toward the standard line ($50.55 budget margin against $146.75) | -$260,864.62 |
| **Total** | **-$358,098.00** |

Quantity and mix net to +$11,330.75, so the extra units added almost nothing. Any mix and quantity convention is acceptable if the bridge ties to -$358,098.

Steel: August and September usage is 690 + 412 - 144 = 958 tons. FIFO uses the 690 pre-bought tons first, so 268 surcharge tons reached cost of goods: 268 x $95 = $25,460, about 7.1 percent of the miss. The other 144 surcharge tons ($13,680) sit in inventory and hit Q4.

Cost variance of $167,035.75 splits into the surcharge $25,460, overtime $71,380, expedited freight $28,940, and $41,255.75 the given figures do not explain, which the commentary should flag for the plant controller rather than assign to steel.

The promotion links to the standard price cut ($219,852), the overtime, and the expedited freight, $320,172 together or about 89 percent of the miss, and it drove the mix shift that cancelled the volume gain. The VP's $135,006 is close to the full-quarter run rate of the surcharge at Q3 volumes and mix (1,421.12 tons x $95), so it describes Q4 exposure, not Q3's cost. A sound commentary says steel cost about $25,000 in Q3 and will cost about $135,000 a quarter from Q4 unless prices move. It attributes the Q3 miss mainly to the promotion's price cut and its operating costs, with the mix shift cancelling the volume gain.

**Adverse result.** The requester is inclined to lead with steel, and the VP wants it. The facts say steel explains about 7 percent of the Q3 miss and the VP's own promotion explains most of it. A model that leads with the surcharge, or that puts $135,000 or $39,140 against Q3, is gradeably wrong.

**Size.** A practitioner answers this in about an hour, inside the three-hour task budget.

## Self-check

```
== drafts/02-harrow-q3-margin-variance/prompt.md (273 words) ==
  coded checks clean
```

Prompt length 1,637 characters. No WARN kept.

Manual rows, read aloud on 2026-11-09:

- [x] F1 FP&A lead, for the CFO and board, deciding what the Q3 commentary says, all in the first paragraph
- [x] F3 reads as an analyst asking for a second pair of eyes; no persona, no test-question shape
- [x] F4 stakes: board deck to the CFO on Thursday, a VP's narrative, a $358,000 margin miss
- [x] F5 all people and companies fictional
- [x] D1 the answer depends on the unit table, the steel inventory roll, and the plant figures given
- [x] D2 the trap is in the facts: a VP's estimate whose arithmetic is right and premise wrong, a pre-buy hidden in an inventory roll, FIFO
- [x] D3 the requester and the VP want the steel story; the facts give steel about 7 percent
- [x] D5 new use case (budget variance) and new reasoning path; none of task 01's spent traps
- [x] D6 every figure is one an FP&A lead would hold for this commentary
- [x] D8 one decisive question (how much is steel); about an hour for a practitioner
- [x] S2 the prompt gives the inventory roll, not the issued tons, and never says the pre-buy shields Q3; the overtime and promotion are stated without a causal link
- [x] S4 no output form required beyond what the commentary should say
- [x] M5 serial comma not needed; no list of three in running prose
- [x] M6 complete sentences; the two bullets are labelled data lines, which a person pasting from a report would use
- [x] M7 spell-checked by eye; no errors found
- [x] T3 no idiom in place of a figure
- [x] T16 "surcharge", "margin miss", "commentary" each keep one name throughout

## Revisions

<!-- One dated entry per round after the first. -->

## Log

- 2026-11-09: drafted; worked answer computed, coded checks clean, manual rows read; awaiting the Generate test
- 2026-11-09: Generate response saved (2,159 words) and graded. Steel trap caught; bps bridge wrong in method and does not tie, mix named as the main driver, budget arithmetic errors. Rated OK, recommend submit
