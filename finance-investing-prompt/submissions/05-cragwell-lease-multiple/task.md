# 05 · Cragwell lease multiple

**Status:** round 1, graded, ready to submit. Fill the form from the sections below, top to bottom. Everything under "Working notes" is reference only. AHT: 2 h 5 m.

## Prompt

Copy the whole of `prompt.md` (in this folder) into **Your Prompt**.

## Generate response

The response is saved unedited in `result.md` (1,195 words, 2026-11-10). Nothing to paste into the form.

## Rating

Select **Pretty Bad**.

OK is an acceptable alternative if you want to give more weight to its rejection of the £140 million. Do not select Amazing or Pretty Good.

## Explanation

The model started on the right track. It saw that Cragwell's IFRS EBITDA and the US comps' EBITDA are on different bases, and it computed £9.11 million of EBITDA after the £4.84 million of lease payments, noting the gap is worth "over £50m" of enterprise value.

It then dropped that figure and recommended the inconsistent method. It says IFRS 16 is "identical in effect to US ASC 842", which is wrong: under US GAAP an operating lease's cost stays in operating expenses, so the comps' EBITDA is after rent. On that basis it calls 11.2 times IFRS EBITDA with the leases added to net debt "the cleaner approach", values the equity at about £121 million, and advises opening at £105 to £110 million with a walk-away of £125 to £130 million. Its EBITDAR of £18.79 million also adds the lease payments back to an EBITDA that already excludes them.

The correct value at the comps' multiple is 11.2 times £9.11 million, less £7.75 million of net debt: about £94.3 million. Its opening bid is £11 to £16 million above that. The likely cause is a misremembered rule on how US GAAP treats operating leases.

## Optional comments

Leave blank.

## AHT

**2 h 5 m** (range 1 h 40 m to 2 h 25 m) for one person with finance experience doing this round by hand. The step-by-step breakdown is under Time estimate in the working notes.

## Working notes

Reference only, not for the form: the grading behind the rating, the design and worked answer, the checks, and the history.

## Time estimate (AHT)

Estimated handle time for one person with finance experience doing this round by hand, with no AI help.

| Step | Minutes |
| --- | --- |
| Pick the failure target and design the scenario | 25 to 35 |
| Work the correct answer in a spreadsheet (lease-adjusted EBITDA, enterprise value, equity, wrong paths) | 10 to 20 |
| Write the prompt, check it, read it aloud | 15 to 20 |
| Generate and read the 1,195-word response | 10 to 15 |
| Recompute the response's figures and decide the rating | 20 to 30 |
| Write the explanation | 15 to 20 |
| Fill the form and submit | 5 |
| **Total** | **100 to 145 (about 1 h 40 m to 2 h 25 m; midpoint about 2 h 5 m)** |

One round only, inside the three-hour budget.

## Outcome

**Flawed in an essential way: it finds the mismatch, then values on the wrong basis.** It rejects the £140 million, but recommends an opening bid of £105 to £110 million against a correct value of about £94.3 million.

What the model caught (spent for this prompt family): that IFRS EBITDA and US-listed comps' EBITDA may not be on the same basis; the IFRS 16 split of lease cost into depreciation and interest; the £9.11 million of EBITDA after lease payments and the "over £50m" of enterprise value it moves; that net debt and EBITDA must be on the same lease convention; and that £140 million should not be defended as it stands.

Where it went wrong:

1. **It misstates the US rule (critical).** It says IFRS 16 is "identical in effect to US ASC 842" and that US comps "present EBITDA in a way that excludes lease costs". Under ASC 842 an operating lease is a single straight-line cost in operating expenses, so the comps' EBITDA is after rent. This is the root of every later error.
2. **It recommends the inconsistent method (critical).** It calls 11.2 times IFRS EBITDA with the £27.4 million of leases in net debt "the cleaner approach" and values the equity at £121.1 million. The multiple is still from post-rent EBITDA, so this overvalues by £26.8 million. Its 10.5 times sensitivity, £111.3 million, has the same flaw.
3. **Its opening and walk-away are too high (critical).** It advises opening at £105 to £110 million, £10.7 million to £15.7 million above the comps value of £94.3 million, and a walk-away of £125 to £130 million, up to £35.7 million above it. A board acting on this would approve a bid range anchored above what the comps support.
4. **Its EBITDAR double-counts the leases (moderate).** It computes EBITDAR as £13.95 million plus £4.84 million, £18.79 million. Cragwell's IFRS EBITDA already excludes lease cost, so it is close to EBITDAR as it stands.
5. **It misreads the margin (minor).** It calls the 36 percent EBITDA margin "high for a climbing gym operator" and suggests normalisation items, without seeing that IFRS 16 is the reason. After lease payments the margin is 23.6 percent.
6. **Small slips (minor).** It writes "£11.6m bank loans + £3.85m cash = £7.75m net", with the sign of the cash wrong in the text, and "EBIT**A**" where it means EBITDA.

**Decision: submit at Pretty Bad.** The response identifies the issue and even computes the right adjusted EBITDA, which is why OK is an acceptable alternative. It then misstates the US rule, picks the inconsistent valuation, and gives the board an opening bid and a walk-away above the value the comps support. A reader acting on it would be materially misled on the number the question asked for.

## Failure target

The model applies the US comps' 11.2 times to Cragwell's IFRS EBITDA of £13.95 million, as the requester does, and supports an opening offer of about £140 million. A practitioner sees that IFRS 16 keeps lease costs out of EBITDA while US-listed operators under ASC 842 carry operating lease cost inside it, so the two are not on the same basis. Taking the £4.84 million of lease payments out of Cragwell's EBITDA gives £9.11 million, an enterprise value of about £102.0 million, and an equity value of about £94.3 million. An opening bid of £140 million is about 17.2 times like-for-like EBITDA and overpays by about £46 million.

## Design notes

**Requester.** The head of corporate development at a US climbing-gym operator, putting a non-binding offer to the founders of a UK chain, with the board signing off on the number on Thursday. All entities are fictional: Summitline Climbing, Cragwell Climbing, and the banker. The comps are described only as six US-listed fitness and leisure operators, so no real company's figures are stated.

**Facts.**

- Comps: six US-listed operators, median 11.2 times trailing EBITDA. Under US GAAP (ASC 842), operating lease cost is a single straight-line expense inside operating costs, so their EBITDA is after rent, and their enterprise value as usually quoted leaves out operating lease liabilities.
- Cragwell, UK IFRS, year to December 2025, £000: revenue 38,620; EBITDA 13,950; operating profit 6,110; bank loans 11,600; lease liabilities 27,400; cash 3,850; lease payments, principal and interest, 4,840.
- Under IFRS 16, lease cost falls into depreciation of right-of-use assets and interest on lease liabilities, both below EBITDA. Cragwell's EBITDA margin is 36.1 percent as reported and 23.6 percent after lease payments.
- The requester's figure: 11.2 times £13.95 million is £156.2 million of enterprise value; less net debt of £7.75 million (bank loans less cash), £148.5 million of equity; open at £140 million.

**Trap.** A routine multiple-times-EBITDA step across two accounting frames. The comps' multiple is on EBITDA after rent, and Cragwell's EBITDA is before it, so the requester's step overstates value by the multiple times the lease cost. Gyms are among the most lease-heavy businesses, so the gap is large. The prompt states "UK IFRS" and "US-listed" as bare facts and gives the lease lines without comment. The default a model reaches for is "your math is right, £148 million, and £140 million leaves room", perhaps with a note on cost savings from the combination or on currency.

**Correct answer.**

| £000 | Requester | Correct |
| --- | --- | --- |
| EBITDA used | 13,950 (IFRS 16) | 9,110 (after lease payments of 4,840) |
| Multiple | 11.2 | 11.2 |
| Enterprise value | 156,240 | 102,032 |
| Net debt (bank loans less cash) | 7,750 | 7,750 |
| Equity value | 148,490 | 94,282 |

The correct route keeps the comps as they are and puts Cragwell on their basis: EBITDA after lease costs, and net debt without the lease liabilities, since the comps' enterprise values leave theirs out. Using the cash lease payments of £4.84 million as the proxy for the rent a US GAAP set of accounts would show is standard. A response that uses a slightly different rent proxy, or puts both sides on an IFRS 16 basis with the comps' lease figures gathered, is acceptable if the equity value lands at roughly £90 million to £98 million.

A sound answer tells the requester that £140 million cannot be defended as 11.2 times, that it is about 17.2 times like-for-like EBITDA, and that an opening bid on the comps belongs well under £94 million. It may suggest opening in the mid-£80 millions to leave room to move. Cost savings from the combination, a UK control premium, or currency are fine to raise as reasons to pay more, as long as they are named as such and not used to rescue the 11.2 times on IFRS EBITDA.

For grading: the requester's £148.5 million, the trap taken whole. Adding the £27.4 million of lease liabilities to net debt while keeping 11.2 times on IFRS EBITDA gives £121.1 million, which points the right way but still overvalues by about £27 million, because the multiple and the EBITDA remain on different bases. A response that flags IFRS 16 as a "point to check" but keeps £140 million as defensible has taken the trap.

**Adverse result.** The requester wants board approval to open at £140 million. The facts support about £94 million at the comps' multiple. A model that endorses the £140 million is gradeably wrong.

**Size.** A practitioner answers this in well under an hour, inside the three-hour task budget.

## Self-check

```
== submissions/05-cragwell-lease-multiple/prompt.md (160 words) ==
  coded checks clean
```

Prompt length 1,000 characters, 178 words including the pasted rows. No WARN kept.

Manual rows, read aloud on 2026-11-10:

- [x] F1 head of corporate development, for the board, deciding the opening offer, all in the first paragraph
- [x] F3 reads as a corp dev lead checking a number before a board call; no persona, no test-question shape
- [x] F4 stakes: a board sign-off on Thursday and an opening bid of £140 million
- [x] F5 all names fictional; the comps are unnamed, so no real company's figures appear; England is the only real place
- [x] F7 the accounts are tab-separated rows as pulled from the data room; no markdown
- [x] D1 the answer depends on the accounting frames and the lease lines given
- [x] D2 the trap is in the facts: IFRS EBITDA set against a multiple from US GAAP comps, in a lease-heavy business
- [x] D3 the requester wants to open at £140 million; the facts support about £94 million
- [x] D5 new use case (trading comparables for an acquisition) and new reasoning path; none of the spent traps from earlier tasks
- [x] D6 every figure is one corp dev holds from the data room and the banker's book
- [x] D8 one decisive question (can we defend £140 million); well under an hour for a practitioner
- [x] S2 the prompt never mentions IFRS 16, ASC 842, or lease-adjusted EBITDA; "UK IFRS" and "US-listed" are bare facts
- [x] S4 no output form required
- [x] M5 no list of three in running prose
- [x] M6 complete sentences; the accounts are pasted rows
- [x] M7 spell-checked by eye; no errors found
- [x] T3 one idiom ("push back"), within the limit of one per prompt
- [x] T16 "EBITDA", "net debt", "enterprise value" each keep one name throughout

## Revisions

<!-- One dated entry per round after the first. -->

## Log

- 2026-11-10: drafted; worked answer computed for the correct path and both wrong paths, coded checks clean, manual rows read; awaiting the Generate test
- 2026-11-10: Generate response saved (1,195 words) and graded. Found the IFRS 16 mismatch and the £9.11 million, then valued at 11.2 times IFRS EBITDA with leases in net debt (£121.1 million) and advised opening at £105 to £110 million against a correct £94.3 million. Rated Pretty Bad, recommend submit
