# Holodeck Guide to Building a Challenging Task (Phase 2)

In-project instructions are the final word on requirements. If this guide and your project template disagree, follow the template.

## The Holodeck Project Pipeline

| Phase | What Happens |
| --- | --- |
| Phase 1 - Propose | Describe a realistic task from your professional experience: scenario, draft prompt, planned context files, and how you'd verify a correct solution. |
| Phase 2 - Build & Test | Create the context files, write the prompt, create the rubric. Test against the agents until the task produces meaningful failures, then submit 6 final runs. |
| Phase 3 - QC & Review | Your task goes through automated QC and is reviewed by another domain expert who will apply any necessary fixes and confirm the task is correct, fair, and genuinely difficult. |

Your Phase 2 submission is the foundation everything else builds on. The more polished and internally consistent your work is, the less likely your task will be rejected in Phase 3. These tasks are very valuable to us, so please take your time here!

## Section 1: How Holodeck Works

You're a domain expert building a realistic professional task that today's strongest AI agents get meaningfully wrong. A human expert in your domain could do the task correctly, but the agent, given the same prompt and documents, produces work that a professional would be embarrassed to submit. That's exactly what we want. These failures will show us exactly where the models fall short, and your rubric is what measures them.

The pipeline is simple from your side (see the pipeline above).

- Phase 1 had you propose a task.

- In Phase 2, you build it. You'll create the context files, write and finalize the prompt, create the rubric, and test against agents to determine that your task is meaningfully difficult.

- Phase 3 is where your task goes through an automated QC process and is reviewed by other experts in your field. A clean, internally consistent submission holds up well through this review.

### What you're building

1. Context files: 10-20+ realistic documents. The "pile of documents" the agent receives.

2. Prompt: 1-4 sentences. A realistic work handoff, like you're assigning this to a trusted, competent colleague.

3. Rubric: 15+ pass/fail criteria. This is the grading instrument, and a key output of your task.

After you complete the above, you will complete six final agent runs, two each on Fable 5, Opus 5.0, and GPT 5.6, with meaningful failures across the runs of at least one of the final models.

### Hard constraints - check these before you build anything

- US-based workflows only. You can be located anywhere, but the scenario, frameworks, and currency must be US-based.

- Not fresh. The correct answer cannot change over time. If someone re-did your task a year from now, they should reach the same conclusions. Pin any dates that matter.

- No real PII or PHI. Every name, address, SSN, MRN, and company you create must be fictional. Use realistic fictional names that you invent yourself. Avoid placeholder names like "John Doe", "ABC Corporation", "123 Main Street".

- The agent gets only your prompt and your context files. Don't design a task that depends on the agent looking anything up - everything it needs must be in your files.

### Time

Expect this task to take about 25 hours of active work to complete. If you think you'll need more than 30, reach out to an Admin (via DM or Slack). The task time is 21 days, and you will need to log into the platform at least once a week. Please save your progress often.

## Section 2: What Makes a Task Hard (and What Doesn't)

This is a very important section of this guide. Get the difficulty right, and everything else is mechanics.

### The bar: meaningful failure

Your goal is a task that you can solve correctly but the agent gets meaningfully wrong. Meaningful means the output is unusable: errors that would take real time to fix and would be embarrassing to submit at work.

### Failures that count

- Incorrect calculations or formulas that flow into downstream numbers.

- Missing an edge case that changes the outcome.

- Failing to connect information across documents.

- Misclassifying a key item (capitalizing what should be expensed, assigning the wrong DRG, miscalculating a covenant, etc.).

- Pulling from the wrong document when sources conflict.

- Errors that would get you in trouble with a regulator, a client, or your boss.

### Failures that don't count

- Formatting or stylistic issues.

- A single small mistake a quick follow-up would fix.

- An output that's mostly right with cosmetic differences from your solution.

A task that scores in the "hard" range, but only loses points on presentation, citations, or nice-to-have criteria isn't actually hard. The failures have to be content failures. If the agent's output only has minor issues, your task isn't hard enough yet.

### Good and bad sources of difficulty

### Good sources of difficulty

- Branchiness. The agent must investigate several threads at the same time and hold off on conclusions until it can synthesize them. Models handle sequential work quite well; parallel investigations strain them.

- Updating working hypotheses. Models anchor on their first read. Tasks where mid-stream evidence should change the approach are reliably hard.

- Real-world causal reasoning. Models weight evidence by how relevant it sounds. Tasks where the narrative points one way and the facts point another way separate pattern-matching from understanding.

- Reasoning from different perspectives. The same transaction treated differently for each party, or the same facts assessed under different roles.

- Opportunity and red-flag recognition. Models are worse at noticing when incidental context creates an opportunity or a risk nobody explicitly asked about.

### OK sources of difficulty

- Sheer context volume, conflicting sources of information (as long as the conflict is realistic and resolvable from the files), and deviating from a standard approach.

### Bad sources of difficulty

- Deliberately burying information in hard-to-find locations. Hiding a number in a footnote isn't professional difficulty, it's a scavenger hunt.

- Manufactured ambiguities and contradictions. If your files genuinely support more than one answer but your rubric only accepts yours, the task is unfair, not hard. A good edge case has file evidence that rules out the tempting wrong answer.

### What seems difficult but the models are actually good at

- Following known procedures, long sequential workflows, cross-referencing, and long verifiable calculations. If your task's difficulty rests on one of these, the models will likely pass it.

### Stack your difficulty

A single trick on its own usually isn't enough to trip up the newest models. A single decoy, one buried edge case, or one required computation is likely to get caught.

Strong tasks stack several pressures: a value that must be computed rather than found, plus a plausible-but-wrong answer sitting in a polished document, plus a correction that has to cascade through everything downstream.

### Where models actually break

Across thousands of graded runs, agent failures cluster into a few patterns. When you design your task, you're welcome to keep these failure points in mind, but do not consistently attempt the same failure mode over and over again:

- Wrong scope or basis. The agent analyzes the wrong population, entity, period, or ownership share. Give the materials several plausible bases and make the right one depend on the professional objective.

- Knows the rule, doesn't apply it. The agent can recite the standard rule, then calculates as if a generic rule is applied. Make your governing rule visible so the failure is application, not ignorance.

- Trusts the wrong source. When documents conflict, models defer to the most polished, most recent, or most authoritative-looking one. Give your sources a real hierarchy (an executed contract beats an unsigned draft).

- Computes nothing. Models pick an answer-shaped number instead of deriving the real one. Make the correct answer appear nowhere in the files.

- Stops at the first plausible answer. Provide a tempting, easier-to-derive answer early, while the true answer takes more work and is inarguably correct.

- Doesn't carry corrections through. The agent fixes something locally, and leaves every dependent fixture stale. Require updating multiple dependent artifacts after a discovery.

- Won't commit. The agent notices the risk and leaves it as a comment instead of acting on it. Grade the committed conclusion, not the mention.

## Section 3: Building Your Context Files

### Core requirements

Every file set must meet all of these:

- 10-20+ files. Keep it under 50 unless the task genuinely needs more (a complex patient chart, for example). Fewer complex files > many one-page files. Padding the file count is not a source of difficulty.

- Realistic formats. Use what a profession would actually encounter: PDFs for forms, letters, and statements; Excel with working formulas for ledgers and models; email-style files for correspondence. Don't flatten a structured document into plain text.

- Authentic feel. Files should read like real working documents, not training materials. No explanatory headers, no files that announce what to do with them, no cross-references by filename unless that would happen naturally.

- Internal consistency. Every shared date, name, identifier, dose, and dollar amount agrees across every file that mentions it, unless a conflict is intentional and resolvable from the files. This is the single most common failure point we're seeing with AI-generated files, and unintentional inconsistencies will fail QC.

- Sufficient to solve. The files must contain everything needed to reach the correct answer; the agent gets only your prompt and these files, so don't rely on it looking anything up. If the files genuinely support more than one defensible answer, your rubric must account for that (Section 5).

- No real PII, PHI, or real entities. All names, addresses, SSNs, MRNs, and companies are fictional - and realistic! Invent them yourself. Don't use placeholders like "John Doe" or "ABC Corporation", and try to avoid obviously LLM-generated names, such as "Meridian Inc" or "Acme Medical Center".

- Personally verified. Every file created with AI assistance is checked by you for accuracy, consistency, and realism before it goes in the zip.

- Packaged correctly. Everything in a folder named inputs, and zipped. No answer keys, design notes, manifests, or rubric content in the zip - and no file names that telegraph the answers!

- Images as inputs only. A photo of handwritten notes or a diagram is fine as inputs, if legible, but don't build tasks that ask the agent to produce images.

### Build in layers - and test early!

Don't create 50 perfect files before your first test. Build 5-15 core files, write a draft prompt, and run it. Then expand.

1. **Layer 1 - The Core Spine:** The minimum documents needed to reach the correct answer. Solve the task yourself with just these. This is your anchor.
2. **Layer 2 - Complexity:** Documents that force cross-file synthesis and carry your edge cases: the lease that changes the depreciation life, the executed order form that supersedes the draft amendment, the consult note the attending never confirmed.
3. **Layer 3 - Distractors and Messiness:** Plausible files that aren't needed for the answer: prior drafts, superseded policies, unrelated correspondence. These can be lower-effort files. They make the agent exercise judgment about what matters.

### Use the plugin

Create your synthetic files in Claude Cowork with the Holodeck-File-Generation-Plugin (setup instructions can be found in your project instructions - please message an admin if you can't use it). The plugin plans a manifest with per-file provenance, generates files with built-in quality checks, and reviews the package for cross-file problems.

### Realism details

Real documents have quirks! A slightly informal email, an abbreviation one provider uses and another doesn't, a blank cell. A little messiness makes your files more convincing. And real documents state facts without drawing the conclusions - make sure you leave the implications to the agent.

### Common synthetic-file tells to avoid

- Perfect organization with always-helpful headers

- Files that cite each other by filename

- Placeholder data (John Smith, $10,000.00 exactly, sequential dates, 555 phone numbers, etc.)

- Template residue, like [INSERT NAME]

- Identical paragraphs recycled across files

- Emails that explain how to solve the task

- Telegraphic file names that describe the traps

- One Cowork-quirk worth remembering: it likes to reuse the same generated names. If your task has named people or companies, name them yourself.

### Audit before you test

Run the Synthetic-Data Audit Agent after uploading. It grades each file on seven criteria: authenticity, hidden hints, placeholders, value realism, overlapping text, template residue, and domain-specific realism. Fix what's real, rebut what isn't (with specifics), and move on. Run it once, at most twice - it will never be fully happy, and that's expected.

## Section 4: Writing Your Prompt

Your prompt should sound like a real work handoff to a trusted colleague. Someone you wouldn't over-explain to, because you trust them to know what they're doing and provide a fantastic output.

### Prompt rules

1. 1-4 sentences. If it's longer, the extra context belongs in a context file, not the prompt.

2. 100% human-written. This needs to be something you would ask for.

3. It must produce a deliverable. One or more output files. If the prompt can be satisfied by a written chat response alone, you need to rework it.

4. Don't spell out steps or flag the hard parts. If your prompt tells the agent what to look for and in what order, the reasoning lives in the prompt instead of the task. The edge cases should be discoverable from the files. If they aren't, you need to improve the files.

5. No artificial constraints. "Present exactly 12 items in a table sorted by amount" exists to make grading easier, not because it reflects real work. Real constraints (GAAP, payer policy, covenant definitions) belong in the context files.

### Good prompts

- Close the books for October 2024 and prepare the ownership reporting package, including location-level P&Ls with commissary allocations.

- "Review the Bytewave contract file and the incident record and prepare a breach-and-remedies memo: tell me whether Bytewave is in breach, what our maximum recoverable exposure is, and whether we can terminate for cause now."

- "Build a full investment committee memo for initiating a long position in Axiom Instruments, including a DCF and trading-comps valuation. Determine the recommended position size that satisfies all of Northshore's mandate constraints, and flag the binding constraint and any limit the PM's requested 5% size would breach."

### Bad prompt (answer key in disguise)

First, check the H&P for sepsis criteria, then cross-reference cultures, then verify CC/MCC status, then recalculate the DRG, then draft exactly two CDI queries...

Remember: the agent receives only your prompt and your context files. It never sees your Phase 1 scenario, so any background it needs must exist as a context file.

## Section 5: Writing Your Rubric

This project grades with rubrics: structured pass/fail criteria instead of the freeform Grading Guidance previously used. The rubric is a key output of your task. Model runs are scored against it, criterion by criterion, and those results are what your task ultimately produces. An inaccurate rubric makes the whole task unusable, no matter how good the files are.

### Rubric-writing methods

- Option 1 - Write an Answer Key first. Write out what a correct solution looks like in whatever form suits you: the correct solution and key values, how to get there, which documents are authoritative, how errors cascade, the 2-3 wrong-but-plausible answers you've planted, how distractors should be handled, and what separates a strong response from a mediocre one. Then let the in-template conversion agents draft rubric criteria from it, merge the drafts, and edit the result. If you write an Answer Key, write it yourself - don't have an LLM generate it.

- Option 2 - Draft criteria directly. Skip the narrative and write the pass/fail statements yourself.

Both paths are fine. Either way, you review, edit, and own every criterion. The conversion agents produce a starting point, not a finished rubric.

### The Golden Rule

A grader should not need domain expertise to score a criterion. Every criterion must be self-contained, with the expected result stated explicitly:

- **Bad:** "Correctly computes the self-employment tax" - this requires the grader to perform the calculation.
- **Good:** "The adjusted cash balance in the reconciliation equals $67,431.22."
- **Good:** "The memo concludes that Amendment No. 2 does not govern because it was never executed."

### What good criteria look like

- Atomic. One testable claim per criterion. If it contains "and", consider splitting it up.

- Pass/fail decidable. A criterion fails when the agent gets that element wrong, and passes when the agent gets it right. If the agent does everything correctly, every criterion passes.

- Aim for 15+ criteria. Cover the correct values and conclusions, the key treatment decisions, completeness of the deliverable, internal consistency, and edge-case handling.

- Aimed at real failures. After testing, make sure the ways the models actually failed are graded. If a real failure isn't captured by any criterion, add one. The in-project "Check Rubric Comprehensiveness" tool will help you spot gaps.

### Multiple defensible answers

One scenario can have more than one defensible answer. This is the most common way rubrics go wrong. If your prompt and files genuinely support more than one well-supported answer, your rubric must do so too. Before finalizing, ask yourself: could a professional in my field, seeing only these materials, reasonably reach a different but well-supported answer? If yes, do one of these:

- Make the prompt clearer, so only one interpretation fits.

- Add or revise source files, so the evidence rules the alternative out.

- Credit the alternative - accept it in the relevant criteria, or grade it as weaker-but-defensible with the file evidence that makes yours stronger.

Two traps to avoid: requiring an answer the files argue against, and calling something a judgment call but grading only one judgment as correct. If a QC step flags another valid answer, make the rubric fairer rather than hardening your original pick. This doesn't mean making the task easier - get your difficulty from the sources in Section 2 instead.

### Solve end-to-end

Solve the task yourself first, completely. Every expected value in your rubric must be reproducible from the context files alone. If you can't trace a criterion's expected result back through the files, fix the files or drop the criterion.

And if any criterion fails on every single final run, you'll be asked to justify it - an always failing criterion is sometimes a real, valuable failure, and sometimes it's a sign the criterion is unfair. Know which yours is.

## Section 6: Testing and Iterating

### The cycle

Test early and often. The last thing you want to do is build everything fully before testing anything.

1. Build ~5-15 files, write a draft prompt, run it. Use the WorldBench Testing Agent in the project.

2. Read the runs. Did the agent attempt the right deliverable? Did it fail meaningfully? Did the auto-grader catch the failures using your rubric?

3. Adjust all three pieces together. Prompt, files, and rubric drift out of sync when edited separately. If you add an edge case to the files, the rubric needs a criterion for it.

4. Repeat until the runs fail substantially for at least one final model.

### Model iterations

Iterate on the fast models, finalize on the slow ones. The testing agent offers Models A-E, this is the low-down:

- Models A and B are the ones whose performance matters most - both are slow, especially Model A.

- Model E is also slow - if Model A isn't working, focus on making Model E fail.

- Models C and D are fast and great for iteration. Only switch to the slow models once your prompt, files, and rubric are tentatively final.

### Reading scores

If the fast models perform well on your task, it's too simple and needs to be harder. Models scoring above 85% while still having meaningful failures is rare - a high score usually means the failures aren't there or the rubric isn't catching them.

### The agents in your template

| Agent | What It Does |
| --- | --- |
| Synthetic-Data Audit Agent | Grades each context file on 7 realism criteria. Run once or twice after files are up. |
| WorldBench Testing Agent | Runs your prompt against your files, multiple runs in parallel. Your iteration workhorse. |
| Rubric Evaluation | Auto-grades each run against your rubric on a 0-100 scale. Edit the rubric before starting the runs - the score uses the rubric as it exists at run time. |
| Rubric QC Agent | Final check across your prompt, files, rubric, and runs. For each criterion it proposes a revision you can accept, edit in place, or keep as-is. |

Agents can take 30+ minutes. Run them in parallel with other work: audit files while building the next batch, draft rubric criteria while the testing agent runs, etc. If a trajectory shows no progress for 5+ minutes, refresh and retry.

### Final runs

1. Make sure you're running your final, realistic prompt (not a draft prompt).

2. Delete your earlier test runs, then run exactly six final attempts via the WorldBench Final Agent Runs. The template will show which models the Final Agent Runs are using; it might be two runs on Fable 5, two runs on Opus 4.8, and two runs on GPT 5.6.

3. The bar: at least one of the final models shows clear, meaningful failures across its runs. All of them failing is ideal. If only one model fails, you can still submit.

4. If Fable 5 safety-flags your prompt (this happens most often in healthcare): run two on Fable 5 plus three each on Opus 4.8 and GPT 5.6, delete the two flagged Fable runs before clicking View Rubric Matrix or Merge Trajectories, and mention the flag in the comments field at the end.

5. Document each run's failures individually - what the model got wrong and why it matters, up to six sentences per run. No copy-pasting the same description across runs.

6. If you've made a genuine effort and can't get meaningful failures, you may still submit. Check the "no failures" option and say so honestly.

- Any substantive change after your final runs means re-running them! If you edit the files, prompt, or a load-bearing rubric criterion after the six runs, the runs no longer reflect your task. Re-run, and re-merge your trajectories so the QC bundle is fresh. (Typos and formatting do not require a re-run).

### Final QC

Run the Rubric QC Agent once after your final runs (Merge Final Trajectories first - this is required even if you're submitting without meaningful failures). It reviews your prompt, files, rubric, and the six graded runs, with special attention to criteria that fail on every run: are those valid model failures, or signs of a bad criterion?

Then click "Generate revision review" and go through its proposals with judgment. It's intentionally strict and will over-fire, so don't chase a clean report: accept only changes that make the task fairer, more realistic, and easier to grade correctly. Sometimes it suggests changing the task when the right fix is making the rubric less prescriptive - that call is yours!

You are not required to keep iterating with it. If you do make substantial changes and choose to re-run, delete the existing QC run and click Merge Trajectories again first so it sees your current task.

## Section 7: Pre-Submission Checklist and Top Pitfalls

### Checklist

#### Context files

- At least 10 files, in a folder named "inputs", zipped

- All shared dates, names, identifiers, and amounts consistent across files

- No real PII/PHI; realistic fictional names throughout

- Real-world formats; no hints, over-explaining, template residue, or giveaway file names

- No answer keys, design notes, or meta files in the zip

- Every AI-generated file personally verified

- Audit agent run; findings fixed or rebutted

#### Prompt

- 100% human-written

- Short and realistic; no step-by-step instructions, no artificial constraints

- Asks for a concrete deliverable (output files)

#### Rubric

- 15+ atomic, self-contained, pass/fail criteria with explicit expected values

- Passes the Golden Rule: gradable without domain expertise or the context files

- Captures the real failures you observed in testing

- No criterion that false-fails a correct response

- Checked for defensible alternative answer; alternatives credited or ruled out with file evidence

- Any always-failing criterion justified

#### Final Runs

- Six runs: e.g. two each on Fable 5, Opus 4.8, and GPT 5.6, all with the final prompt and final files

- Meaningful failures across the runs of at least one final model

- Per-run failure descriptions, specific to each run

- No substantive edits after the final runs (or runs were redone)

- Trajectories merged after the final runs

- Rubric QC Agent run once and its output carefully reviewed; accepted revisions applied

### Top pitfalls

1. Cross-file inconsistencies. The most common issue. A name spelled two ways, a figure that doesn't tie, etc. Do a dedicated consistency pass at the end: pull every shared data point and compare.

2. The rubric locks onto one answer when the files support two. See Section 5.

3. Criteria that aren't self-contained. "Correctly calculates X" is a problematic criterion; it forces the grader to solve your task, which we don't want. State any expected values.

4. Rubric values not traceable to the files. If you can't reproduce a criterion's expected result from the inputs alone, it can't be graded fairly.

5. The prompt does the work. Steps, warnings, and formatting demands in the prompt drain the difficulty out of the task.

6. The models fail because the prompt is unclear. Difficulty must come from the files and scenario, not from prompt vagueness or prompt guidance.

7. Low-value failures. Runs lose points only on presentation, citations, or nice-to-haves. Those aren't meaningful failures - make the task harder or rethink the trap.

8. Stale final runs. Files or rubrics edited after the fix runs, with no re-run. QC will catch the mismatch.

9. Single-trick difficulty. One decoy or one buried number doesn't stop current models. Stack your pressures (Section 2).

10. Placeholder-flavored synthetic data. "John Smith", $10,000.00 exactly, 555 phone numbers, [INSERT NAME]. The audit agent flags these, and so do reviewers.

## Appendix: Full Worked Examples by Domain

### Human Resources, Talent & People Operations: Merit Cycle Modeling with Pay-Equity Constraints

#### Scenario

Ridgeline Software, a 640-employee B2B software company, is running its 2025 merit cycle for the 128-person Engineering organization. Leadership has approved a 4% merit budget plus a 0.5% equity-adjustment pool. Salary increases are determined by a merit matrix that combines performance rating with position-in-band, and the annual pay-equity review has flagged five potential outliers, though two have documented business justifications.

The compensation data is far from clean. The HRIS export still maps employees hired before March to the old job-leveling framework, leaving nine engineers incorrectly leveled after a title-mapping migration. Two versions of the 2025 salary bands are circulating: the approved version and an outdated draft with higher midpoints that recruiters have been using. Three engineers changed roles mid-year, requiring prorated merit increases based on the effective date of the promotion and the new salary band. To complicate matters further, a VP promised one engineer an off-cycle 6% retention increase by email. Under company policy, that increase must be funded from the equity-adjustment pool with an offset elsewhere, not from the merit budget.

#### Prompt

Run the 2025 merit cycle for the Engineering organization and prepare the final compensation recommendations for HR review.

#### Context files

1. HRIS employee export: Current Engineering employee roster with salary, job level, performance rating, hire date, and job family. Pre-March hires still use the legacy job-level scheme, creating inconsistencies that must be reconciled.

2. 2025 compensation planning workbook: Approved salary bands by job family and level, the 2025 merit matrix, and budget assumptions, including the approved 4.0% merit pool and 0.5% equity adjustment pool.

3. Job level migration guide: Maps legacy job levels to the new framework introduced in March. Required to correctly classify nine engineers whose HRIS records still use the old levels.

4. Compensation policy: Policy covering merit eligibility, proration for mid-year role changes, off-cycle increases, and budget calculation rules.

5. 2025 calibrated performance ratings: Final performance ratings from the year-end calibration process used to determine merit increases.

6. Personnel action records: Mid-year promotion records for three engineers and a VP-approved retention increase granting one engineer a separate 6% off-cycle adjustment.

7. Pay equity review: Regression-based pay equity analysis identifying five statistical outliers, including methodology notes and documented business justifications for two of them.

8. Engineering organization reference: Current organization chart showing reporting relationships and job families used to identify appropriate peer groups.

9. Payroll register: Current payroll extract with base salaries used to reconcile and validate the final compensation recommendations.

10. Historical compensation files (distractors): Includes the draft 2025 salary band file with higher midpoints, the recruiter's email quoting those draft bands, and the 2024 merit matrix with different increase percentages.

#### Solution and where agents fail

Correct solution: Produce a final compensation file where every employee's increase follows the merit matrix based on their performance rating and corrected position-in-band. Total merit spend should reconcile to the 4% merit budget, retention and equity adjustments should be funded from the separate 0.5% pool, and the pay equity summary should document how the three unexplained outliers were resolved.

Most critical check (primary failure point): Determine whether the agent corrects the nine mis-leveled engineers using the title-mapping memo before calculating position-in-band. Using the HRIS job levels as-is places these employees in the wrong salary bands, applies the wrong merit matrix values, and cascades into incorrect increases, misallocated budget, and inaccurate pay equity conclusions.

Second failure point: Determine whether the VP-approved 6% retention increase is funded from the equity adjustment pool, with the required offset specified in the compensation policy, rather than being added to the merit budget. A weak response charges the increase to the merit budget and exceeds the 4% allocation.

Third failure point: Determine whether the three mid-year role changes are prorated from their effective dates using the new salary band midpoint, as required by policy, rather than receiving full-year increases at the new level. The agent must also use the approved salary band file rather than the circulating draft.

A strong response resolves all three judgment calls correctly, reconciles total spend to both funding pools (within rounding), and clearly documents each adjustment. A weak response runs the merit matrix against the uncorrected HRIS data, relies on the draft salary bands, and reports budget compliance that disappears once the leveling errors are corrected.

#### Rubric

1. The nine engineers hired before March are re-leveled from the legacy framework before any position-in-band calculation (legacy E3 → L4, legacy E4 → L5).

2. Each of the nine re-leveled engineers is assigned L4 (from legacy E3) or L5 (from legacy E4); no engineer remains at a legacy E-level.

3. Position-in-band is calculated using the approved 2025 salary band file (L4 midpoint $142,000; L5 midpoint $168,500).

4. Position-in-band is not calculated using the draft salary band file, whose L5 midpoint of $175,000 exceeds the approved midpoint by $6,500.

5. Position-in-band for the nine re-leveled engineers is not calculated from their uncorrected HRIS levels.

6. Each employee's merit increase matches the approved merit matrix for their performance rating and corrected quartile (for example, Exceeds/Q1 = 5.5%, Meets/Q2 = 3.5%, Meets/Q4 = 2.0%).

7. Employees with the same performance rating and quartile receive the same merit increase percentage.

8. No employee receives a merit increase outside the approved matrix other than authorized retention and equity adjustments.

9. Total merit spending equals approximately $784,000 (4% of the $19.6M Engineering salary base), within rounding.

10. Equity adjustments ($15,200 total) and the $10,260 retention increase are charged to the 0.5% equity-adjustment pool, leaving an approximately $72,500 balance of the $98,000 pool.

11. The 6% retention increase ($10,260 on the named L5 engineer's $171,000 salary) is funded from the equity-adjustment pool rather than the merit budget.

12. The retention increase is recorded as an off-cycle adjustment with the required compensation committee approval, separate from the employee's merit increase.

13. Each promotion (effective April 1, June 16, and August 1) receives a prorated increase equal to 9/12, 6.5/12, and 5/12 of the annual increase, respectively, calculated using the new salary band's midpoint.

14. None of the promoted employees receives a full-year increase at the new level.

15. The increase file includes all 128 Engineering employees from the HRIS export exactly once.

16. Each employee's final salary equals the current base salary plus the stated increase amount.

17. Total reported merit spending equals the sum of the 128 individual merit increases.

18. The response identifies the approved 2025 salary band file as the governing source and notes that the higher-midpoint draft band file is also in circulation.

19. The documentation lists each of the nine re-leveled engineers with the original level, corrected level, and applied legacy-to-new mapping.

20. The three unexplained pay-equity outliers receive the recommended equity adjustments of $6,500, $4,900, and $3,800, or include a documented investigation supporting an alternative disposition.

21. The two documented outliers (shift differential and acquisition retention terms) are identified as explained and receive no equity adjustment.

22. The pay-equity analysis reports that the regression controls for job level, job family, tenure, and location.

23. The increase file contains no blank, placeholder, or "TBD" values.

24. All compensation calculations, merit allocations, and pay-equity analyses are completed in the deliverable rather than deferred to the reviewer.

### Sales, Business Development & Account Management: Q3 Commission True-Up with Disputed Deals

#### Scenario

Lakeview Systems is preparing the Q3 commission payout for its 45-person sales organization. The year began under Compensation Plan v2025.1, but a mid-year addendum (v2025.2) changed the accelerator tiers for deals booked on or after August 1. Commissions are based on signed quota letters, accelerators apply above 100% attainment, and a Q3 SPIF pays an additional 2% on a designated focus product line.

Several payouts aren't straightforward. Rep A closed a deal in the CRM on July 29, but Finance booked it on August 3, so the applicable compensation plan depends on how the effective date is interpreted. Rep B claims a 50/50 commission split with a sales engineer that isn't reflected in the CRM. Rep C argues the SPIF should stack on top of the accelerator, but the compensation policy states that the SPIF is paid on the base commission rate and does not count toward attainment. There are a few more complications. A customer who churned in September triggers the plan's 90-day clawback provision, one rep transferred territories on August 15 and requires a prorated calculation, and the commission system's draft payout was generated using the outdated compensation plan.

#### Prompt

Complete the Q3 commission review for the Central region and prepare the final payout package for the VP's approval.

#### Context files

1. 2025 Sales Compensation Plan: Executed FY2025 compensation plan, including commission rates, accelerator tiers, split-credit policy, and clawback provisions. Defines the baseline compensation rules.

2. Compensation Plan Addendum (Effective August 1, 2025): Approved policy update introducing revised accelerator tiers and product-specific commission changes. May supersede portions of the base plan depending on applicability.

3. Quota & Territory Assignment Letters: Individual quota agreements for Central region account executives, including mid-year territory changes and quota proration. Documents rep-specific compensation terms.

4. CRM Opportunity Export (Q3): Closed-won opportunities with close dates, products, contract values, and credited representatives. Provides the sales team's operational record of completed deals.

5. Finance Bookings Report (Q3): Official booking dates and recognized contract values for Q3 transactions. Provides the finance system's record of booked business.

6. Commission Dispute Tracker: Open disputes submitted by sales managers covering split credits, booking dates, territory ownership, and commission exceptions. Captures transactions requiring manual review.

7. Cancellation & Credit Memo Log: Customer cancellations, contract amendments, and credit memos issued during Q3. Documents events that may affect earned commissions.

8. Q3 Product Incentive (SPIF) Announcement: Sales incentive announcement, eligibility rules, payout schedule, and frequently asked questions. Describes the quarter's promotional incentive program.

9. Year-to-Date Attainment Report: Individual attainment, prior commission payments, and cumulative performance metrics. Summarizes sales performance through the current quarter.

10. Sales Operations Policy Library: Archived compensation plans, historical SPIF announcements, draft policy revisions, and prior territory maps. Provides historical reference materials that may not reflect current policy.

#### Solution and where agents fail

Correct solution: Produce a regional commission payout file where every deal is paid under the correct plan version, attainment reflects the churn clawback and territory proration, the three compensation disputes are resolved with citations to the plan, and total payouts reconcile to the quota letters and commission rate tables.

Most critical check (primary failure point): Determine whether the agent identifies the correct plan version using the finance booking date rather than the CRM close date. Rep A's deal booked on August 3 falls under the revised commission tiers. Applying the wrong plan changes the rep's accelerator tier and, because attainment is cumulative, miscalculates every subsequent payout for the quarter.

Second failure point: Determine whether the September churn clawback is removed from attainment before accelerator tiers are calculated. Failing to do so overstates attainment, qualifies multiple reps for higher accelerator tiers, and results in overpayments - the same error present in the draft commission system output.

Third failure point: Determine whether the SPIF is paid at the base commission rate without counting toward attainment, as specified in the FAQ, and whether Rep B's split commission is calculated according to the plan's split-credit rules. The sales engineer's credit should be funded from the separate SE pool rather than by reducing the sales representative's credit.

A strong response produces a reconciled payout file, resolves each dispute with citations to the applicable plan provisions, and explains every difference from the draft commission system output. A weak response accepts the draft calculations at face value and resolves disputes based on narrative rather than the governing compensation plan.

#### Rubric

1. Plan applicability is determined by the finance booking date: deals booked on or after August 1 are paid under Addendum v2025.2, while earlier deals are paid under Compensation Plan v2025.1.

2. Rep A's disputed $150,000 deal (closed July 29, booked August 3) pays $15,000 under Addendum v2025.2 (10% at 104% attainment), rather than the $18,000 that would result under Compensation Plan v2025.1.

3. Rep A's deal is not paid using Compensation Plan v2025.1's accelerator tiers.

4. Every deal booked before August 1 is paid using the Compensation Plan v2025.1 rate tables.

5. The $85,000 deal cancelled on September 12 (originally booked July 8) is clawed back under the plan's 90-day clawback provision.

6. The $85,000 clawback is removed from attainment before accelerator tiers are determined, reducing the affected representative's attainment from 102% to 96%.

7. Accelerator tiers are not determined using attainment that includes the clawed-back $85,000.

8. The clawback dispute resolution cites the plan's 90-day clawback provision.

9. Each representative's cumulative attainment equals year-to-date booked revenue (net of the $85,000 clawback) divided by the representative's prorated annual quota.

10. Each commission rate matches the governing plan: Compensation Plan v2025.1 pays 8% base and 12% above 100% attainment, while Addendum v2025.2 pays 8% base, 10% from 100% to 110%, and 14% above 110% for the deals it governs.

11. The DataSync SPIF pays $4,800 (2% of Rep C's $240,000 in Q3 DataSync bookings) in addition to base commission.

12. SPIF payments are excluded from attainment calculations.

13. SPIF payments are not calculated using accelerated commission rates.

14. SPIF payments apply only to DataSync product-line deals.

15. Rep B's split-credit dispute is resolved by paying the sales engineer the plan's 3% incentive from the separate sales engineer incentive pool.

16. Rep B retains 100% deal credit.

17. The representative with the August 15 territory change receives a blended annual quota of approximately $1.75M (45 of 92 days at a $1.6M quota and 47 days at a $1.9M quota), calculated using the quota letter's day-weighted methodology.

18. Each of the three disputes (Rep A booking date, Rep B split credit, and Rep C SPIF stacking) includes a written resolution citing the applicable plan provision.

19. The payout file includes all 12 Central Region representatives from the quota letters exactly once.

20. Each representative's commission equals the sum of the representative's deal-level commission amounts.

21. The regional commission total equals the sum of the 12 representative-level payouts.

22. The corrected regional commission total of approximately $348,700 is reconciled to the draft total of $359,000, with the approximately $10,300 difference attributed to the plan-version correction (approximately $3,000), clawback reversal (approximately $6,100 across two representatives), and SPIF de-stacking (approximately $1,200).

23. The commission-system draft, calculated entirely under Compensation Plan v2025.1, is not adopted without recalculation.

24. The payout file contains no blank, placeholder, or "TBD" amounts.

25. All commission calculations, attainment calculations, and payout reconciliations are completed in the deliverable rather than deferred to the reviewer.

### Marketing, Brand & Communications: Campaign Spend Reconciliation and Channel ROI Ranking

#### Scenario

Fernwood Home Goods, a DTC housewares retailer, is reviewing its H1 marketing performance to decide how to allocate its H2 media budget. The company spent $2.4M across paid search, paid social, CTV, email, and affiliates, and the CMO wants a defensible ROI ranking by channel that will hold up under Finance's review.

The underlying data isn't clean. For some managed channels, the agency's 10% management fee is included in invoice totals, while for others it's billed separately. Platform-reported spend doesn't match invoices because of timing differences and a $60K CTV make-good credit issued after a delivery shortfall. The attribution policy requires blended triangulation factors rather than platform-reported last-click conversions, which systematically overcredit paid search and undercredit CTV. To make matters worse, the ecommerce revenue export uses a different channel taxonomy than the media plan: its "social" category includes unmanaged influencer revenue that should not be attributed to paid social.

#### Prompt

Evaluate H1 marketing performance and prepare a recommendation for how the H2 budget should be allocated.

#### Context files

1. Approved H1 media plan: Final marketing budget by channel and month, totaling $2.4M. Defines the planned spend used as the baseline for performance analysis.

2. Marketing spend package: Agency invoices (January-June), platform spend exports for paid search, paid social, and CTV, the agency fee schedule, and the CTV make-good credit memo. Contains the actual costs that must be reconciled into a consistent net-spend view.

3. Channel taxonomy mapping guide: Maps the ecommerce revenue taxonomy to the media plan channel structure and explains known classification issues, including the influencer overlap within "Social."

4. Attribution methodology memo: Defines the approved blended attribution methodology by channel and explicitly notes that platform last-click metrics should not be used for executive reporting.

5. Ecommerce revenue export: Revenue by marketing channel using the ecommerce reporting taxonomy. Must be reconciled to the media plan before ROI can be calculated.

6. Shared marketing cost allocation: Email platform contract and affiliate network statement, including the rules for allocating fixed platform costs and network fees to individual channels.

7. Finance GL extract: Marketing expense by month from the general ledger, used to reconcile spending against invoices and platform reports.

8. H2 budget guidance email: CFO guidance for the upcoming budget reallocation, including strategic priorities, funding constraints, and any required investment shifts.

9. Marketing performance dashboard: Executive summary of H1 campaign performance and channel metrics used to support the H2 planning discussion.

10. Historical planning materials (distractors): Includes the v1 draft media plan with superseded budgets, a platform dashboard showing deprecated last-click ROAS, and a prior-year agency invoice.

#### Solution and where agents fail

Correct solution: Produce a reconciliation that ties the media plan to vendor invoices and the general ledger, calculates channel ROI using a consistent net spend methodology (including agency fee allocation, make-good credits, and blended attribution), and recommends a budget reallocation that aligns with the CFO's stated constraints.

Most critical check (primary failure point): Determine whether the agent normalizes spend to a consistent net basis before calculating ROI. Agency fees should not be double-counted for managed channels or omitted for CTV, and the $60K make-good credit must reduce CTV's net spend. Errors at this step change the channel ROI rankings and lead to the wrong reallocation recommendation.

Second failure point: Determine whether revenue is attributed using the blended attribution methodology defined in the attribution memo rather than platform-reported last-click conversions. Relying on last-click attribution overstates paid search performance, understates CTV, and produces the wrong investment recommendation.

Third failure point: Determine whether revenue is classified using the correct channel taxonomy by excluding unmanaged influencer revenue from the social channel and allocating the fixed email subscription cost according to the contract rather than treating email as having no associated cost.

A strong response reconciles the media plan, invoices, and general ledger; reports net spend and attributed revenue for each channel; and produces a reallocation recommendation that remains consistent with the CFO's constraints. A weak response mixes gross and net spend, relies on last-click attribution, and recommends shifting budget toward the channel whose performance is artificially inflated by its own methodology.

#### Rubric

1. Each channel's spend is reported on a net basis, and the agency-fee treatment is documented.

2. The 10% agency management fee is included exactly once per channel: embedded in the paid search and paid social invoices, and added once for CTV, where the $50K fee is billed separately.

3. Net CTV spend equals approximately $490K ($500K gross spend plus the separately billed $50K agency fee, less the $60K make-good credit).

4. The $60K CTV make-good credit is applied to H1 CTV spend.

5. Email marketing includes approximately $48K of cost (one-half of the $96K annual subscription), allocated according to the contract.

6. Affiliate spend includes both the approximately $210K in commissions and the approximately $18K network fee.

7. Channel revenue is calculated using the blended attribution factors (CTV ×1.8, paid search ×0.7, all other channels ×1.0) rather than platform-reported conversions.

8. Channel rankings are not based on platform last-click conversions.

9. CTV ranks above paid search on blended ROI (approximately 4.2 versus approximately 3.9), reversing the platform last-click ranking.

10. Approximately $310K of unmanaged influencer revenue is excluded from paid social according to the taxonomy mapping guide.

11. The exported social-media revenue is separated into paid social and unmanaged influencer before ROI is calculated.

12. The spend reconciliation bridges the approved $2.4M media plan to approximately $2.326M of January-June invoiced spend, identifying the approximately $74K CTV under-delivery.

13. Invoice totals reconcile to the finance general ledger, with timing differences identified.

14. Differences between platform-reported and invoiced spend are reconciled rather than averaged.

15. Each channel's ROI equals attributed revenue divided by normalized net spend, calculated consistently across all five channels.

16. All five channels (paid search, paid social, CTV, email, and affiliates) are included in both the reconciliation and the ROI ranking.

17. The H2 media plan reallocates budget toward the highest-ROI channels while maintaining the CFO's approved $2.4M budget.

18. The H2 recommendation allocates the largest budget increases to email and CTV (ranked first at approximately 28 and second at approximately 4.2 in the ROI analysis) and does not increase spending on the lowest-ranked paid social channel (approximately 3.4).

19. The response does not introduce spend, revenue, attribution, or fee values that are not supported by the source files.

20. Total H1 net spend of approximately $2.326M equals the sum of the five channel amounts (approximately $940K paid search, $620K paid social, $490K CTV, $48K email, and $228K affiliates).

21. Total attributed revenue of approximately $10.1M equals the sum of the five channel revenue amounts after applying the blended attribution factors.

22. The deliverable contains no blank, placeholder, or "TBD" values.

23. All spend reconciliations, attribution calculations, and ROI calculations are completed in the deliverable rather than deferred to the reviewer.

### Customer Success, Support & Service Operations: Enterprise SLA Breach Analysis for the QBR

#### Scenario

Vantage Software's largest enterprise customer, Northstar Software, has its quarterly business review in two weeks. The initial support report shows 14 apparent SLA breaches in Q2, and the results will determine whether the customer is owed service credits. The contract defines P1 response time as one business hour and P2 as four business hours on a 24×5 support schedule, with SLA pauses while waiting on the customer.

The ticket data requires careful interpretation. Several flagged tickets spent time in approved customer-wait states, which pause the SLA clock under the contract. Two tickets were assigned the wrong priority, and the priority-change audit log must be reconciled with the contract's severity definitions. A major outage in May generated five related tickets that the contract treats as a single P1 incident for service-credit purposes. To complicate matters further, the account team has been quoting response targets from the original sales proposal, which are more stringent than the terms in the executed support agreement.

#### Prompt

Review Q2 SLA performance for the Northstar Software account and prepare the customer summary for the upcoming QBR.

#### Context files

1. Northstar Software Support Agreement: Master support contract and SLA exhibit defining business hours, priority levels, pause states, incident consolidation rules, and the service credit calculation methodology.

2. Q2 support ticket export: Complete Q2 ticket history for the Northstar Software account, including timestamps, priorities, status changes, pause periods, and resolution details.

3. Priority and escalation audit: Priority change history for all modified tickets, including who made each change, the justification provided, and required escalation timing by priority.

4. Support operations calendar: Business holiday calendar and on-call schedule used to determine SLA clock calculations during Q2.

5. Major incident report: Root cause analysis for the May service outage, including the five related support tickets and incident timeline used to evaluate ticket consolidation.

6. Customer correspondence: Email thread documenting Northstar's dispute over two ticket classifications and the support team's responses.

7. Support quality review: QA scorecard results for a representative sample of Q2 tickets, providing additional context on ticket handling quality.

8. Prior service credit example: Previous quarter's approved service credit calculation and customer communication, provided as the standard format for preparing the current recommendation.

9. Account health summary: Customer usage metrics, support trends, and satisfaction indicators used to prepare the QBR narrative and account summary.

10. Superseded contract materials (distractors): Includes the sales proposal containing marketing SLA targets that were never incorporated into the executed agreement and a draft contract amendment that was never signed.

#### Solution and where agents fail

Correct solution: Produce a ticket-by-ticket SLA assessment showing the response and resolution clock calculations, compute service credits only for confirmed breaches using the contract formula, and prepare a root cause summary that categorizes the confirmed breaches and recommends appropriate corrective actions.

Most critical check (primary failure point): Determine whether the agent applies the contractual business-hours calendar and pause states rather than raw elapsed time. Correct SLA clock calculations eliminate several of the 14 initially flagged tickets. Miscalculating the clocks changes both the total service credits owed and the root cause distribution presented in the QBR.

Second failure point: Determine whether the five outage-related tickets are consolidated into a single P1 incident under the contract's incident aggregation clause. Treating them as separate incidents overstates service credits by roughly fivefold and distorts the root cause analysis.

Third failure point: Determine whether SLA performance is evaluated against the executed contract rather than the sales proposal, and whether the two misprioritized tickets are reclassified using the contract's priority definitions and the audit log. Using the proposal's stricter targets or the incorrect priorities results in additional unsupported breaches.

A strong response documents the SLA clock calculations for each ticket, computes service credits only for confirmed breaches, and presents a root cause analysis with a credible remediation plan. A weak response accepts the raw ticket export at face value, scores performance against the sales proposal instead of the executed contract, and reports 14 breaches with service credits the contract does not support.

#### Rubric

1. Each flagged ticket's response time is calculated using the contract's 24×5 business-hours calendar (P1 target: 1 business hour; P2 target: 4 business hours).

2. Time spent in waiting-on-customer status is excluded from the response-time calculation.

3. Memorial Day and Juneteenth are excluded from the business-hours calculation.

4. Raw elapsed time is not used. Ticket #47950, reported at 6.2 elapsed hours, is calculated as approximately 3.4 business hours after excluding pause time and holidays and is determined not to be a breach.

5. Each of the 14 flagged tickets includes a breach determination with the response-time calculation documented.

6. Six of the 14 flagged tickets are identified as SLA breaches, and eight are determined not to be breaches after applying the correct business-hours calculation and incident consolidation.

7. Tickets #48822 through #48826 from the May 14 outage are consolidated into a single P1 incident for service-credit purposes in accordance with the contract.

8. Service credits are not calculated separately for the five May 14 outage tickets.

9. Ticket #48213 is reclassified from P2 to P1 because the audit log documents a production-down impact meeting the contract's P1 definition.

10. Ticket #48377 remains classified as P2 because the documented impact was limited to a single user, consistent with the contract's P2 definition.

11. Breach determinations use the executed contract's SLA targets rather than the sales proposal.

12. Service credits are calculated as 5% of the monthly fee for each confirmed breach, subject to the contract's 15% monthly cap.

13. Uncapped service credits of $12,600 (six confirmed breaches at $2,100 each) are reduced to $6,300 by the monthly cap because all confirmed breaches occurred in May.

14. Service credits are calculated only for confirmed SLA breaches.

15. The confirmed SLA breaches are assigned root causes consisting of the consolidated outage incident, three overnight staffing gaps, and two misrouted escalations.

16. Each root-cause category includes a corresponding remediation action.

17. The QBR breach totals match the ticket-level breach determinations.

18. Each issue raised in the customer's dispute emails is addressed in the analysis.

19. The deliverable contains no blank, placeholder, or "TBD" sections.

20. All response-time calculations, SLA determinations, service-credit calculations, and root-cause analyses are completed in the deliverable rather than deferred to the reviewer.

### Operations, Supply Chain & Logistics: Q4 Demand Forecast and S&OP Package

#### Scenario

Cascade Beverage Co., a regional beverage manufacturer with about 40 SKUs, is preparing its Q4 forecast for the October S&OP review. The forecast will drive purchasing, safety stock targets by ABC class, and a capacity check across two bottling lines, one of which loses a week of production to the holiday shutdown.

The demand history isn't straightforward. July includes a one-time BOGO promotion that inflated sales and shouldn't carry into the baseline forecast. A discontinued SKU was replaced mid-year, so its demand history needs to roll forward to the replacement item; otherwise, the new SKU forecasts near zero while the discontinued SKU continues to show demand. Sales has also signed a major retail customer whose committed volume begins in November. That business is reflected in the top-down sales plan but not in the historical unit demand. As a result, the top-down plan and bottom-up forecast won't align, and the difference needs to be reconciled and explained rather than force-fit.

Brightline Outdoor Products, a $120M manufacturer of camping equipment with two distribution centers, is selecting a single third-party logistics (3PL) provider to manage its parcel and LTL freight. Three bids have been received, including one from the incumbent, Cardinal Freight Solutions. Before Friday's steering committee meeting, the procurement manager must score the proposals using the approved evaluation matrix, build a three-year total cost of ownership comparison, and recommend a vendor.

The evaluation isn't straightforward. Two versions of the scoring matrix are circulating: the original RFP version and a later steering committee revision with different weighting and a new mandatory requirement for $5M in cargo liability coverage. One bidder doesn't meet that requirement, but only discloses the exception in an appendix. The pricing workbooks also aren't directly comparable. One bidder excludes fuel surcharges from its LTL rates while the other two include them, and one priced its proposal using the original forecast even though a later demand-planning memo projects a 15% reduction in outbound volume after the loss of a major retail customer, changing the applicable pricing tier. There are additional complications. Cardinal's proposal excludes the early termination and transition costs that would be incurred if it isn't selected, and its own monthly scorecards show on-time, in-full performance below the contractual SLA in four of the last six months. Finally, an email from the COO states that "a 3PL transition before peak season is not realistic, and the incumbent should get the benefit of the doubt," introducing potential executive bias into the decision.

#### Prompt

Review the available planning data and prepare the Q4 S&OP package for the October review.

#### Context files

1. Historical sales export (24 months): Monthly shipments by SKU showing baseline demand, seasonality, and the July promotional spike used as the starting point for the Q4 forecast.

2. Commercial planning package: Promo calendar, new item transition memo, and retail win announcement describing planned promotions, SKU transitions, and the committed customer volumes beginning in November.

3. Q4 sales plan: Sales team's top-down revenue plan by month, used to reconcile the bottom-up demand forecast with commercial targets.

4. Product price list: Current selling prices by SKU used to convert the unit demand forecast into revenue for comparison with the sales plan.

5. Inventory and supply snapshot: Current inventory, allocated inventory, and open purchase orders showing available supply and inbound replenishment.

6. Supply planning policies: Safety stock policy and supplier lead-time file defining inventory targets and replenishment timing requirements.

7. Manufacturing capacity model: Production capacity by manufacturing line, including units per shift, changeover assumptions, and other planning constraints.

8. Production calendar: Manufacturing calendar showing planned downtime, including the Line 2 holiday shutdown and other scheduling constraints that affect available capacity.

9. Previous S&OP package: Prior planning cycle's demand plan, assumptions, and presentation format, provided as a reference for preparing the October review materials.

10. Superseded planning materials (distractors): Includes an outdated Q4 sales plan prepared before the new retail customer was signed and a cancelled October promotion proposal that was never approved.

#### Solution and where agents fail

Correct solution: Produce a Q4 demand forecast that removes the July promotional spike from the baseline, chains the discontinued SKU to its replacement, incorporates the retail customer win beginning in November, reconciles the bottom-up forecast to the sales plan, and develops a buy plan and capacity assessment that respect inventory, supplier lead times, and the planned Line 2 shutdown.

Most critical check (primary failure point): Determine whether the agent removes the July promotional spike from the historical baseline before forecasting demand. Treating the promotion as recurring demand inflates the Q4 forecast, resulting in excessive purchase recommendations, overstated safety stock, and an artificial capacity shortfall.

Second failure point: Determine whether the discontinued SKU is correctly chained to its replacement. Without this adjustment, the replacement SKU is significantly underforecast, the buy plan under-orders the new product, and demand for the discontinued SKU incorrectly carries forward into purchasing.

Third failure point: Determine whether the bottom-up unit forecast is reconciled to the top-down sales plan using the approved price list, with the retail customer win explaining most of the variance and any remaining differences explicitly reconciled rather than force-fit. The capacity assessment should also account for the planned Line 2 shutdown week.

A strong response documents each forecasting adjustment, clearly reconciles the demand forecast to the sales plan, and identifies the shutdown-week capacity constraint with a practical mitigation strategy, such as pre-building inventory or scheduling overtime. A weak response forecasts directly from the raw sales history, force-fits the results to the sales plan, and produces a buy plan distorted by the July promotion.

#### Rubric

1. July's 96,000 promoted-SKU cases are baseline-adjusted to approximately 70,000 by removing the 38% BOGO promotion lift before the forecast is generated.

2. The baseline forecast does not incorporate the July promotional lift.

3. Baseline adjustments are applied only to the six promoted SKUs.

4. Discontinued SKU CB-104's demand history is transferred to replacement SKU CB-118, and CB-118 is forecast using the combined demand history.

5. No forecast demand is assigned to CB-104, and its remaining 3,200 on-hand cases are consumed before new CB-118 production is planned.

6. The retail win's committed volume of 22,000 cases per month is incorporated beginning in November for the two sparkling-water SKU families identified in the announcement.

7. The bottom-up Q4 forecast totals approximately $8.26M at price-list rates (approximately $7.71M baseline plus approximately $0.55M from the retail win) and is reconciled to the $8.6M sales plan.

8. The remaining approximately $340K gap to the sales plan is attributed to the club-channel stretch target and is not eliminated by increasing the forecast.

9. Safety stock is calculated for each SKU family using the service level assigned to its ABC classification (A = 98%, B = 95%, C = 90%).

10. The buy plan subtracts on-hand inventory before calculating replenishment requirements.

11. The buy plan subtracts open purchase orders before calculating replenishment requirements.

12. Purchase orders supporting December demand are scheduled to meet the six-week co-packer lead time, with can orders placed four weeks and label orders two weeks before their production runs.

13. Capacity requirements are calculated using the capacity model's production rates (Line 1: 9,000 cases per shift; Line 2: 7,500 cases per shift).

14. The capacity calculation excludes Line 2's holiday shutdown week from available production capacity.

15. December demand is identified as requiring approximately 46 Line 2 shifts versus 40 available shifts, resulting in an approximately 45,000-case shortfall and a documented mitigation (November pre-build or overtime).

16. The S&OP package includes the demand forecast, sales-plan reconciliation, buy plan, and capacity analysis.

17. The buy plan and capacity analysis use the same Q4 forecast quantities reported in the demand forecast.

18. The deliverable contains no blank, placeholder, or "TBD" values.

19. All forecasting, inventory planning, capacity planning, and sales-plan reconciliation are completed in the deliverable rather than deferred to the reviewer.

### Procurement, Sourcing & Vendor Management: Weighted Bid Scoring and 3PL Award Recommendation

#### Scenario

Brightline Outdoor Products, a $120M manufacturer of camping equipment with two distribution centers, is selecting a single third-party logistics (3PL) provider to manage its parcel and LTL freight. Three bids have been received, including one from the incumbent, Cardinal Freight Solutions. Before Friday's steering committee meeting, the procurement manager must score the proposals using the approved evaluation matrix, build a three-year total cost of ownership comparison, and recommend a vendor.

The evaluation isn't straightforward. Two versions of the scoring matrix are circulating: the original RFP version and a later steering committee revision with different weighting and a new mandatory requirement for $5M in cargo liability coverage. One bidder doesn't meet that requirement, but only discloses the exception in an appendix. The pricing workbooks also aren't directly comparable. One bidder excludes fuel surcharges from its LTL rates while the other two include them, and one priced its proposal using the original forecast even though a later demand-planning memo projects a 15% reduction in outbound volume after the loss of a major retail customer, changing the applicable pricing tier. There are additional complications. Cardinal's proposal excludes the early termination and transition costs that would be incurred if it isn't selected, and its own monthly scorecards show on-time, in-full performance below the contractual SLA in four of the last six months. Finally, an email from the COO states that "a 3PL transition before peak season is not realistic, and the incumbent should get the benefit of the doubt," introducing potential executive bias into the decision.

#### Prompt

Evaluate the three 3PL proposals using the RFP materials and prepare an award recommendation for Friday's steering committee.

#### Context files

1. Transportation RFP package: Issued RFP describing the scope, service requirements, submission instructions, and the baseline shipment volume file provided to bidders.

2. Source selection criteria: Steering committee-approved evaluation matrix (v2), September meeting minutes documenting its approval, and the procurement policy governing proposal scoring, mandatory requirements, and award recommendations.

3. Cardinal Freight Solutions proposal: Proposal narrative, pricing workbook, and supporting materials from the incumbent carrier, including its assumption of no transition costs.

4. TruNorth Logistics proposal: Proposal, pricing workbook, and fuel surcharge appendix containing the complete pricing needed to evaluate its bid.

5. Vellum Supply Chain proposal: Proposal, pricing workbook, and exceptions appendix disclosing its exception to the required $5 million cargo liability coverage.

6. Business planning update: Demand planning memo describing the projected 15% reduction in outbound volume following the loss of a major retail customer, affecting volume-tier pricing assumptions.

7. Current carrier performance package: Current Cardinal contract, recent monthly performance scorecards, and the governing SLA definitions used to evaluate incumbent performance and transition obligations.

8. Procurement correspondence: Bidder Q&A log and the COO's email regarding transition timing and incumbent considerations. Provides additional context but must be weighed against the formal evaluation process.

9. Award recommendation template: Standard procurement award memo template used for presenting the final recommendation to leadership.

10. Historical procurement materials (distractors): Includes the draft evaluation matrix (v1), the 2021 RFP results and historical rate cards, an incomplete proposal from a bidder that withdrew before the deadline, a Cardinal marketing one-pager claiming "99%+ on-time performance," and a generic freight-rate benchmark report that does not reflect Brightline's shipping profile.

#### Solution and where agents fail

Correct solution: Produce an award recommendation memo containing a completed scoring matrix, a normalized three-year total cost of ownership comparison, a mandatory requirements compliance review, and a transition risk assessment. The recommendation should apply the approved procurement process, normalize all bids to a common basis, evaluate incumbent performance using documented evidence, and recommend the bidder that provides the best overall value.

Most critical check (primary failure point): Determine whether the agent screens proposals for compliance with the mandatory requirements before scoring. Vellum's proposal takes exception to the required $5 million cargo liability coverage in an appendix, making the bid non-compliant under the approved procurement policy despite offering the lowest initial price. This requirement appears only in the approved v2 evaluation matrix, so this also verifies that the correct evaluation criteria are being applied.

Second failure point: Determine whether pricing is normalized before comparing bids. This includes adding TruNorth's fuel surcharge from its rate appendix, repricing all proposals using the revised shipment volumes from the demand planning update, and including Cardinal's early termination and transition costs in any switch scenario. Omitting any of these adjustments changes the total cost of ownership comparison and can alter the award recommendation.

Third failure point: Determine whether incumbent performance is evaluated using the documented OTIF scorecards rather than Cardinal's marketing materials, and whether the COO's email expressing a preference for the incumbent is treated as a transition planning consideration rather than a scoring input. Both documents are relevant context but should not override the approved evaluation methodology or the documented performance record.

A strong response disqualifies Vellum under the mandatory requirements, documents the pricing normalization process, recommends TruNorth based on the normalized evaluation, and addresses the COO's peak-season concern through a transition plan rather than by changing the scoring. A weak response scores all three bids without first screening for compliance, compares unadjusted pricing, relies on marketing claims or executive preference instead of documented evidence, and recommends the incumbent despite the procurement record supporting a different outcome.

#### Rubric

1. The mandatory-requirements compliance screen is completed before any bidder is scored.

2. Vellum is disqualified for taking exception to the mandatory $5M cargo liability requirement by offering only $2M.

3. The disqualification cites Procurement Policy §4.2 governing unwaived exceptions to mandatory requirements.

4. Vellum is excluded from the scoring matrix.

5. Scoring uses the steering-committee-approved v2 evaluation matrix (cost 30%, service 25%, past performance 25%, transition 20%).

6. Scoring does not use the draft v1 evaluation matrix with a 40% cost weighting.

7. The $5M cargo liability requirement is treated as a mandatory requirement and is not waived.

8. TruNorth's three-year cost includes the approximately $1.65M fuel surcharge omitted from its pricing workbook.

9. TruNorth's total cost is not evaluated using the workbook pricing as submitted.

10. All bidders are repriced using Tier 2 volume rates reflecting the 15% post-RFP volume reduction, increasing TruNorth's cost by approximately $120K and Cardinal's by approximately $180K.

11. Pricing is not based on the original RFP volumes.

12. The switch analysis includes approximately $410K of early-termination and transition costs under the Cardinal contract.

13. TruNorth's normalized three-year TCO of approximately $11.90M is calculated from its approximately $9.72M submitted cost plus the approximately $1.65M fuel surcharge, approximately $120K of Tier 2 repricing, and approximately $410K of switching costs. Cardinal's normalized three-year TCO of approximately $12.40M is calculated from its approximately $12.22M submitted cost plus approximately $180K of Tier 2 repricing.

14. The TCO reconciliation separately identifies the fuel-surcharge adjustment, Tier 2 repricing, and switching costs.

15. Past-performance scores are based on six months of OTIF scorecards showing Cardinal averaging 91.4% against the 95% target and missing the target in four of six months.

16. Cardinal's "99%+ on-time" marketing claim is not used in the past-performance evaluation.

17. The COO email expressing an incumbent preference is excluded from the evaluation.

18. The memo identifies the COO email as unsupported by the documented evaluation criteria.

19. Each bidder's weighted score is calculated using the approved v2 evaluation matrix, and the weighted total equals the sum of the individual criterion scores.

20. The weighted totals are approximately 82 for TruNorth and approximately 78 for Cardinal, with the five-point past-performance difference (20.0 versus 15.0 of 25) supported by the OTIF scorecards.

21. The award recommendation is TruNorth.

22. The transition plan addresses the COO's peak-season concern by beginning in mid-January, after peak season, and completing the 90-day transition before the spring volume increase.

23. The evaluation memo includes the compliance screen, completed v2 evaluation matrix, normalized TCO comparison, and transition plan.

24. TruNorth's stated fuel-surcharge exclusion is added back during normalization, while Cardinal's surcharge-inclusive pricing is left unchanged.

25. Each bidder's three-year TCO equals the sum of its reported cost components (base transportation, fuel surcharge where applicable, Tier 2 repricing, and switching costs where applicable).

26. The deliverable contains no blank, placeholder, or "TBD" values.

27. All compliance screening, cost normalization, bid evaluation, and TCO calculations are completed in the deliverable rather than deferred to the reviewer.

### Strategy, Corporate Development & Competitive Analysis: Market Entry Business Case with Conflicting TAM Estimates

#### Scenario

Juniper Analytics, an $80M B2B data company, is evaluating whether to expand into the mid-market segment. The board wants a go/no-go recommendation for the January planning meeting, using a stated investment hurdle of payback within 24 months. The market sizing isn't straightforward: two analyst reports estimate the opportunity at $3.4B and $1.2B, but the larger figure includes an adjacent segment that falls outside Juniper's ideal customer profile.

The internal data is just as challenging. Win rates and churn differ significantly by customer size, so enterprise unit economics can't simply be applied to the mid-market. A pricing study suggests customers are unwilling to pay current list prices, and some existing smaller enterprise customers would likely migrate to a lower-priced mid-market offering, creating cannibalization that must be accounted for. Two different implementation cost estimates are circulating: a detailed bottom-up go-to-market plan and an older top-down estimate. Meanwhile, Finance's blended CAC and LTV assumptions mask the segment-level differences that ultimately determine whether the proposal clears the board's payback threshold.

#### Prompt

Prepare a recommendation on whether the company should enter the mid-market segment.

#### Context files

1. Market opportunity research: Two analyst reports estimating the addressable market using different market definitions, including supporting segmentation data. The reports conflict and must be reconciled using the company's target market definition.

2. Ideal Customer Profile (ICP) definition: Internal document defining the target customer profile and the criteria for determining which market segments should be included in the opportunity assessment.

3. Commercial performance analysis: Win/loss analysis by customer segment and deal size, along with churn and retention trends by customer size, used to estimate achievable revenue and long-term customer value.

4. Pricing and customer research: Pricing study evaluating willingness to pay across customer segments, including customer feedback on migration risk and purchase considerations.

5. Financial model assumptions: Finance memo containing CAC/LTV assumptions and unit economics used for business case modeling. Some metrics are blended across segments and require further interpretation.

6. Go-to-market investment plan: Bottom-up estimate of hiring, marketing, tooling, and operating costs required to launch the new segment.

7. Sales capacity model: Sales hiring, quota ramp, and productivity assumptions used to estimate revenue capacity over the first two years.

8. Board investment guidance: Board memo describing the required 24-month payback threshold, investment criteria, and risk tolerance for new market expansion initiatives.

9. Competitive landscape review: Analysis of competing mid-market offerings, including pricing, packaging, and positioning used to evaluate market competitiveness.

10. Historical strategy materials (distractors): Includes an older top-down cost estimate that conflicts with the approved bottom-up investment plan, a 2023 market sizing report using outdated segment estimates, and a vendor-sponsored whitepaper with an inflated TAM.

#### Solution and where agents fail

Correct solution: Produce a market entry business case that reconciles TAM, SAM, and SOM to the company's ICP definition, models segment-specific unit economics, accounts for revenue cannibalization, selects and justifies the appropriate go-to-market cost estimate, and evaluates payback against the board's 24-month investment hurdle with appropriate sensitivity analysis.

Most critical check (primary failure point): Determine whether the agent reconciles the market opportunity to the company's ICP definition. The $3.4 billion market estimate includes an adjacent segment that falls outside the ICP. Using it as the starting point overstates TAM, SAM, SOM, and projected revenue, leading to an inaccurate payback calculation and the wrong investment recommendation.

Second failure point: Determine whether the business case uses segment-specific win rates, churn, pricing, and unit economics rather than the blended CAC/LTV metrics in the finance memo. The blended assumptions overstate lifetime value and understate acquisition cost for the mid-market segment, allowing the investment to appear to satisfy the board's hurdle when it does not.

Third failure point: Determine whether projected revenue is reduced for existing customer migration using the pricing study's cannibalization analysis, and whether the investment model is based on the approved bottom-up go-to-market plan rather than the outdated top-down cost estimate. Ignoring either adjustment materially overstates the project's financial return.

A strong response explicitly reconciles the market opportunity to the ICP, builds the financial model using segment-specific assumptions, includes sensitivity analysis around the key drivers, and makes a recommendation that remains defensible under those assumptions. A weak response adopts the larger market estimate, relies on blended unit economics, ignores customer migration, uses the outdated cost estimate, and recommends market entry based on a business case that does not actually satisfy the board's investment criteria.

#### Rubric

1. The addressable market is restated to ICP-qualified segments, explaining the difference between the $3.4B and $1.2B market estimates based on their segment definitions.

2. The business case does not use the $3.4B market estimate without reconciling it to the ICP definition.

3. A TAM-SAM-SOM bridge is presented (approximately $1.2B TAM, $340M SAM, and approximately $9.5M Year 3 gross ARR) with the assumptions supporting each step.

4. The approximately 22% mid-market win rate from the segment-level win/loss analysis is used instead of the 31% blended average.

5. The LTV calculation uses the approximately 18% mid-market churn rate rather than the 8% enterprise churn rate.

6. Payback is not calculated using the blended CAC/LTV memorandum.

7. The approximately $14K mid-market CAC from the segment analysis is used instead of the blended $9K CAC.

8. The approximately $6.8M Year 1-3 investment from the bottoms-up GTM plan is carried into the payback calculation.

9. Mid-market pricing uses the pricing study's median willingness-to-pay of approximately $1,150 per month rather than the $2,400 enterprise list price.

10. Cannibalization is reflected by reducing Year 3 net-new ARR by approximately $1.1M based on the pricing study's finding that approximately 12% of the existing $18M smaller-enterprise ARR base migrates to the lower-priced tier.

11. The revenue forecast incorporates existing-customer migration rather than treating all mid-market revenue as net new.

12. The business case uses the bottoms-up GTM investment estimate of approximately $6.8M rather than the older $4.5M top-down estimate, and the rationale is documented.

13. Revenue phasing is consistent with the capacity model's hiring plan of six mid-market representatives in Year 1 and a six-month productivity ramp.

14. Payback is calculated as approximately 29 months and compared with the board's 24-month investment hurdle.

15. The sensitivity analysis varies win rate (±5 percentage points), churn (±3 percentage points), and CAC (±$2K), showing payback ranging from approximately 24 to 37 months.

16. The recommendation is no-go or conditional entry, consistent with the approximately 29-month payback relative to the board's 24-month hurdle.

17. The vendor-sponsored whitepaper's $5B market estimate is not used in the market sizing.

18. Year 3 net-new ARR of approximately $8.4M (approximately $9.5M gross ARR less approximately $1.1M of cannibalization) equals the sum of the cohort-level revenue forecast.

19. The response does not introduce market sizes, win rates, churn rates, pricing assumptions, or investment costs that are not supported by the source files.

20. The business case contains no blank, placeholder, or "TBD" values.

21. All market sizing, financial modeling, sensitivity analysis, and payback calculations are completed in the deliverable rather than deferred to the reviewer.

### Product Management & Go-to-Market: A/B Test Rollout Decision with a Contaminated Cohort

#### Scenario

Parkside, a consumer fintech app, recently tested a redesigned onboarding flow. The experiment dashboard reports a 6% increase in activation, and the product team is eager to roll out the new experience. The experiment plan pre-registered the primary success metric, minimum detectable effect, test duration, and two guardrails: support contact rate and 30-day retention.

The results aren't as clear as they first appear. The data team's sample ratio mismatch (SRM) monitor flagged the first week of the experiment, and a bug report confirms that assignment was misconfigured for one iOS build for six days, contaminating part of the treatment group. A referral promotion also overlapped the first half of the test, so the activation lift needs to be evaluated separately for promotional and non-promotional periods. Finally, while the overall guardrail metrics appear unchanged, support contact rates increased significantly for users on older devices, and the pre-registered rollout criteria specify that any material guardrail regression blocks launch.

#### Prompt

Review the onboarding experiment and prepare the decision package for the product leadership team.

#### Context files

1. Experiment design specification: Pre-registered experiment plan defining the primary success metric, minimum detectable effect, experiment duration, guardrail metrics, and rollout criteria used to evaluate the test.

2. Experiment results package: Executive results dashboard along with the raw assignment and exposure data used to validate the reported experiment outcomes.

3. Experiment quality review: Sample ratio mismatch (SRM) analysis and the engineering bug ticket documenting an iOS assignment issue that affected part of the experiment.

4. Guardrail metrics report: Support contact rates, D30 retention, and other guardrail metrics by customer segment used to assess potential negative impacts.

5. Customer segment definitions: Documentation describing the experiment's reporting segments, including the older-device cohort used in the analysis.

6. Product analytics funnel: Step-by-step conversion funnel used to diagnose where differences between the control and treatment groups occurred.

7. Marketing activity calendar: Product promotion and referral campaign calendar identifying overlapping initiatives that could have influenced experiment results.

8. Historical experimentation summary: Prior experiments on the same onboarding surface, including historical conversion rates and seasonality trends used to provide context for the current results.

9. Rollout playbook: Standard rollout checklist describing the staged deployment process and approval requirements for production launches.

10. Historical experiment materials (distractors): Includes a celebratory Slack thread highlighting the headline +6% activation lift without discussing data quality issues and an older experiment design document for a different test that used different success criteria.

#### Solution and where agents fail

Correct solution: Produce an experiment decision memo that recalculates the treatment effect using clean exposure data, evaluates the pre-registered primary metric and guardrail metrics by segment, accounts for the overlapping referral promotion, and recommends an appropriate rollout strategy with a post-launch monitoring plan.

Most critical check (primary failure point): Determine whether the agent excludes or corrects the contaminated week-one iOS cohort using the sample ratio mismatch analysis and engineering bug documentation before evaluating experiment performance. Including the affected cohort overstates the measured lift and leads to the wrong rollout decision.

Second failure point: Determine whether the rollout recommendation follows the pre-registered success criteria. The increase in support contacts among the older-device segment violates a guardrail metric, so the appropriate recommendation is a staged rollout or an excluded-segment rollout with continued monitoring rather than a full deployment.

Third failure point: Determine whether the overlapping referral promotion is accounted for by evaluating performance during non-promotion periods. Without separating the referral campaign from the experiment, the observed lift cannot be attributed confidently to the new onboarding experience.

A strong response reports the corrected treatment effect with appropriate uncertainty, evaluates each pre-registered success criterion, and recommends a staged rollout with explicit monitoring triggers based on the rollout checklist. A weak response accepts the dashboard's reported +6% lift at face value, ignores the data quality and guardrail issues, and recommends an immediate full rollout.

#### Rubric

1. Approximately 31,000 users affected by the six-day iOS build 5.2 assignment misconfiguration are excluded or reassigned before the treatment effect is calculated.

2. The exclusion is supported by the week-one SRM check (58/42 observed versus 50/50 expected) and the corresponding bug ticket.

3. The corrected Day 7 activation lift is approximately +2.1% rather than the dashboard's reported +6%.

4. The rollout decision is not based on the dashboard's reported +6% lift.

5. The corrected Day 7 activation lift of approximately +2.1%, with a confidence interval excluding zero, is reported as below the design document's +3% rollout threshold.

6. The rollout decision is based on the pre-registered primary metric of Day 7 activation.

7. The analysis does not substitute a different success metric for the pre-registered primary metric.

8. Both pre-registered guardrails are evaluated: Day 30 retention remains approximately flat (-0.2 percentage points) and the support-contact rate exceeds the guardrail for the older-device segment.

9. The approximately 14% increase in support-contact rate for the older-device segment (devices four or more years old, approximately 18% of users) is identified.

10. The older-device support-contact guardrail breach is treated as a rollout gate in accordance with the design document.

11. The recommendation is not an unconditional full rollout.

12. Treatment effect is calculated separately for the three non-promotion weeks (approximately +1.8%) and the referral-promotion period (approximately +2.6%), and the rollout decision is based on the non-promotion estimate.

13. Guardrail metrics are evaluated by user segment rather than only at the overall level.

14. The rollout plan uses staged or segment-based deployment by holding the older-device segment while expanding the remaining users to 25% and then 100% over two tact rate or more than a 1 nercentage-noint decline in nav 30 retention weeks, with rollback triggers of more than an 8% increase in support-contact rate or more than a 1 percentage-point decline in Day 30 retention.

15. The handling of the contaminated cohort is documented so the analysis can be reproduced from the raw assignment data.

16. The celebratory Slack thread is not used as experimental evidence.

17. The corrected approximately +2.1% treatment effect is reported consistently in the summary, analysis, and recommendation.

18. The response does not introduce metrics, user segments, experiment parameters, or statistical results that are not supported by the source files.

19. The memo contains no blank, placeholder, or "TBD" sections.

20. All experiment reanalysis, statistical calculations, guardrail evaluations, and rollout recommendations are completed in the deliverable rather than deferred to the reviewer.

### Project, Program & Change Management: Program Replan After a Vendor Migration Slip

#### Scenario

A mid-market insurer is 14 months into replacing its claims system when the systems integrator reports a three-week delay to the data migration milestone. The vendor attributes the delay to client data-quality issues, but the program's own issue log paints a more nuanced picture. The steering committee meets in ten days and expects a revised project plan, budget impact assessment, and formal change request.

The schedule impact extends well beyond three weeks. User acceptance testing can't begin until data migration is complete, training depends on UAT, and the planned cutover falls immediately before the annual open-enrollment blackout, when production changes are prohibited from November 1 through December 15. A simple three-week shift pushes cutover into the blackout window, delaying go-live until January. The revised schedule also conflicts with a shared DBA already committed to another project, while the contract's delay and liquidated damages provisions determine whether the resulting costs are the client's responsibility or the systems integrator's.

#### Prompt

Review the current status of the Claims Modernization program and prepare an updated plan for the steering committee.

#### Context files

1. Program baseline plan: Baseline project schedule with task durations, dependencies, milestones, and the critical path approved at the start of the program.

2. Vendor contract package: Vendor statement of work defining milestones, contractual delay provisions, liquidated damages, and the applicable rate card for change requests.

3. Vendor delay correspondence: Vendor notification claiming the migration delay is client-caused, along with the supporting data-quality issue log documenting evidence for both vendor- and client-related delays.

4. Program constraints and readiness plan: Cutover blackout calendar, UAT plan, and training plan defining deployment windows, entry criteria, and downstream dependencies that affect the schedule.

5. Resource allocation plan: Project staffing plan showing resource assignments, including the shared DBA supporting multiple initiatives and other critical resource constraints.

6. Program financials: Budget tracker and burn report showing project actuals, forecasted spend, remaining contingency, and budget status.

7. Program governance log: RAID log tracking current risks, issues, assumptions, decisions, and mitigation activities across the program.

8. Workstream status reports: Current status reports from each workstream, including progress updates that conflict with one another and require reconciliation before executive reporting.

9. Steering committee governance: Steering committee meeting minutes documenting prior decisions, change-control thresholds, and the required change request template used for executive approval.

10. Historical scheduling materials (distractors): Includes the retired baseline v1 schedule and an informal draft schedule circulated by a workstream lead before formal approval.

#### Solution and where agents fail

Correct solution: Produce an updated project plan that reflects the true critical path, quantifies the schedule and budget impact of the delay, and prepares a change request presenting viable options with a recommended path forward. The revised schedule should account for project dependencies, resource constraints, and the planned cutover blackout period.

Most critical check (primary failure point): Determine whether the agent rebuilds the critical path through UAT and training while accounting for the cutover blackout window. The resulting schedule reflects an effective seven-week delay into January, not simply a three-week shift. Missing this constraint produces an unrealistic implementation plan and invalidates the remainder of the analysis.

Second failure point: Determine whether responsibility for the schedule delay is assessed by applying the vendor contract to the evidence in the data quality log. The available evidence supports a mixed allocation of responsibility rather than assigning fault entirely to one party, and that conclusion directly affects whether liquidated damages offset a portion of the project extension costs.

Third failure point: Determine whether the shared DBA resource conflict is identified and resolved through rescheduling, backfilling, or escalation rather than leaving the resource double-booked, and whether the budget impact is calculated using the contracted rate card and current project burn rather than rough estimates.

A strong response presents a revised critical path, quantifies the incremental schedule and cost impacts, addresses the resource conflict, and recommends a well-supported change request with clear implementation options. A weak response shifts the schedule uniformly, assigns responsibility without engaging the contractual evidence, overlooks the shared resource constraint, and leaves the project governance committee to discover that the revised plan cannot realistically meet the proposed cutover date.

#### Rubric

1. The three-week migration delay is propagated through the project dependency chain (migration → UAT entry → training → cutover) rather than applying a uniform schedule shift.

2. UAT entry moves from October 6 to October 27 following migration completion and satisfies the UAT entry criteria (migration complete and fewer than 25 open Sev-2 defects).

3. Training is rescheduled to November 24 through December 12 following UAT, while only production cutover is constrained by the blackout period.

4. The November 1 through December 15 blackout period is treated as a hard constraint on production cutover.

5. Production go-live is rescheduled to approximately January 12, resulting in an effective seven-week project delay.

6. The replanned schedule does not include a November production cutover.

7. The updated critical path is identified as migration, UAT, training, and the post-blackout production cutover.

8. The schedule analysis concludes that delay responsibility is shared under the SOW because eight of the fourteen migration defects are attributable to vendor transformation errors and six to client source data.

9. The excusability analysis does not rely solely on the vendor's attribution letter and reconciles it against the data-quality log.

10. The liquidated-damages analysis concludes that approximately $150K is recoverable rather than the $250K maximum available for full vendor responsibility.

11. The budget impact includes approximately $684K of extended program costs (seven weeks at approximately $98K per week).

12. Contractor extension costs of approximately $210K are calculated using the SOW rate card.

13. The net budget impact of approximately $744K after the liquidated-damages offset is stated.

14. The shared DBA's December 1 commitment to the finance-system upgrade is identified as a resource conflict.

15. The replan includes a documented resolution or escalation for the DBA resource conflict (rescheduling, backfill, or steering committee decision).

16. The reported 85% completion of the data workstream is reconciled against the open-defect counts or identified as inconsistent, together with any conflicting completion claims for the remaining workstreams.

17. The change request completes the required template sections (impact summary, options, cost, schedule, risks, and decision requested).

18. The change request evaluates at least two implementation options: the recommended January 12 production cutover and a phased alternative with the reporting module following in February.

19. The change request's go-live date, net budget impact (approximately $744K), and critical-path summary are consistent with the replanned schedule.

20. The response does not introduce dates, costs, resource assignments, or contract terms that are not supported by the source files.

21. The deliverable contains no blank, placeholder, or "TBD" sections.

22. All schedule analysis, dependency analysis, budget analysis, and change-request documentation are completed in the deliverable rather than deferred to the reviewer.

### Business Analytics, Reporting & Performance Management: Bookings Anomaly Root-Cause and QBR Reconciliation

#### Scenario

The May bookings metric in the executive dashboard is down 14% from April, and the CRO wants to know how much of the decline is real before the upcoming QBR. The CRM, billing system, and Finance extract all report different numbers, and the analytics team has to produce a single reconciled answer.

Several changes occurred at the same time. The metric catalog shows that the bookings definition changed from TCV to ACV effective May 1, so April and May aren't directly comparable. The ETL change log reveals that the dashboard still pulls from a deprecated view that excludes late-May data loads. A data migration merged duplicate customer accounts mid-month, a large EUR deal changed value after an exchange-rate update, and one deal was backdated into April following an approval email sent after the April reporting snapshot had already been taken. The final analysis should separate these reporting and data issues from the true change in bookings so leadership understands what actually happened.

#### Prompt

Investigate the change in May bookings and prepare the reconciled results for the upcoming QBR.

#### Context files

1. Executive reporting package: Executive dashboard export showing April and May bookings, along with the prior QBR package used as the reporting format and historical reference.

2. Metric governance: Current metric definition catalog documenting the transition from TCV to ACV (Bookings v2.3) effective May 1 and identifying Finance as the system of record.

3. Sales transaction export: CRM closed-won opportunities for April and May, including contract values, terms, and close dates used to support bookings calculations.

4. Finance bookings data: Finance bookings extract and billing system invoice data used to reconcile reported bookings against financial records.

5. Data pipeline documentation: ETL change log describing the dashboard's continued use of a deprecated data view and the production cutover timeline.

6. Data quality log: Data import records documenting the duplicate account merge completed in mid-May, including the affected account IDs and reconciliation notes.

7. Reference data package: FX rate table and account hierarchy mapping used to ensure consistent currency conversion and parent-child account rollups across reporting systems.

8. Accounting adjustments: Backdated deal approval documenting a transaction moved into April after the month-end reporting snapshot and requiring reconciliation.

9. Reporting guidance: Standard reporting instructions and reconciliation expectations for preparing the executive bookings package.

10. Historical reporting materials (distractors): Includes the prior year's metric definition catalog (v1.9), which uses the retired bookings methodology, and a Sales Operations spreadsheet containing undocumented manual adjustments that are not part of the approved reporting process.

#### Solution and where agents fail

Correct solution: Produce a reconciled April-to-May bookings bridge that explains the reported decline by separating methodology changes, data quality issues, and underlying business performance. The final QBR package should reconcile to the Finance system of record and quantify the remaining change after all adjustments.

Most critical check (primary failure point): Determine whether the agent recognizes the transition from TCV to ACV and restates April using the current metric definition before comparing the two months. Most of the apparent 14% decline is driven by the reporting methodology, so analyzing the raw month-over-month change without first restating April leads to an incorrect root cause analysis.

Second failure point: Determine whether the agent identifies that the executive dashboard is sourced from a deprecated ETL view and rebuilds the analysis using the Finance bookings extract. The deprecated view excludes late-May loads, making the reported decline appear larger and preventing the CRM, dashboard, and Finance data from reconciling.

Third failure point: Determine whether the remaining differences are individually quantified and attributed, including the duplicate account merge, the foreign exchange adjustment on the EUR deal, and the backdated transaction that should be reported in April. The final bridge should explain each adjustment explicitly rather than relying on an unexplained residual.

A strong response presents a fully reconciled bridge that quantifies every adjustment, ties the final results to the Finance system of record, and clearly distinguishes reporting methodology changes from genuine business performance. A weak response averages results across systems, skips the ACV restatement, and presents executives with a root cause analysis for a decline that is largely explained by changes in reporting methodology.

#### Rubric

1. The May 1 bookings definition change (TCV to ACV under catalog v2.3) is identified as the primary driver of the apparent decline.

2. April bookings are restated from $12.4M (TCV basis) to approximately $11.3M (ACV basis) before any month-over-month comparison.

3. The definition change is quantified as approximately $1.1M (about 9 percentage points of the apparent 14% decline).

4. The month-over-month analysis is not performed using the unrestated $12.4M April figure.

5. The dashboard is identified as reading the deprecated _bookings_legacy view according to the ETL change log.

6. May bookings are rebuilt from the finance extract as the source of truth rather than from the dashboard or an average of multiple systems.

7. The reconciled May bookings are not calculated by averaging the CRM, billing, and finance values.

8. Approximately $240,000 of late-May bookings omitted from the deprecated view are restored to the May total.

9. The mid-May duplicate-account merge removes approximately $120,000 of double-counted renewals.

10. The revised FX table reduces the €1.0M European deal by approximately $60,000.

11. The $130,000 deal approved before month-end but loaded after the April snapshot is assigned to April.

12. The April-to-May bridge separates the movement into approximately $1.1M of definition changes, approximately $550,000 of data corrections, and approximately $125,000 of underlying business decline.

13. The bridge assigns a dollar value to each component, and the components reconcile to the total $1.7M movement with no unexplained difference.

14. The underlying business decline is reported as approximately $125,000 after separating definition and data effects.

15. The final April (approximately $11.3M) and May (approximately $11.16M) bookings totals reconcile to the finance extract on an ACV basis.

16. Both April and May are presented using the same ACV definition.

17. The QBR documents the v2.3 definition change and its effect on historical comparisons.

18. The undocumented manual adjustments in the Sales Ops spreadsheet are not used in the reconciliation.

19. Differences among the CRM, billing, and finance systems are attributed to the documented causes (definition change, deprecated view, duplicate merge, FX update, and backdated booking).

20. The response does not introduce booking amounts, exchange rates, or booking definitions that are not supported by the source files.

21. The deliverable contains no blank, placeholder, or "TBD" values.

22. All reconciliation and restatement calculations are completed in the deliverable rather than deferred to the reviewer.

### Executive, Administrative & Workplace Operations: Board Pre-Read Assembly from Conflicting Submissions

#### Scenario

The Chief of Staff at a growth-stage company is preparing the Q3 board pre-read from six department submissions. The final deck is due to the board portal in five days. The board template defines the section order, page limits, and executive summary metrics, while the CEO has asked that three strategic topics be highlighted.

The source material isn't fully aligned. Finance's revenue actuals and Sales' bookings deck report different "revenue" figures because they use different definitions and reporting periods. Product submitted two versions of its update, and a follow-up email instructs the team to use v2, which quietly changes the roadmap presented to the board last quarter. The departmental headcount tables also exceed the HR system of record because two teams counted approved but unfilled requisitions as filled positions. The final board pre-read must reconcile these inconsistencies where possible, and any unresolved issues should be documented in an open-items memo for the CEO rather than left unexplained.

#### Prompt

Prepare the Q3 board pre-read using the submitted department materials.

#### Context files

1. Board pre-read guidance: Board pre-read template defining the required section order, page limits, summary metrics, and overall presentation format.

2. Financial performance package: Finance submission containing revenue actuals, forecasts, cash position, and the metric definition note explaining the distinction between recognized revenue and bookings and which metric belongs on the executive summary.

3. Sales performance package: Sales submission summarizing bookings performance and supporting commercial results for the quarter.

4. Product organization update: Final Product submission (v2) and the accompanying email confirming it supersedes the earlier draft.

5. Workforce summary: HR headcount system extract and department headcount reports used to prepare the organization update. Some departmental reports include open requisitions as filled positions and must be reconciled with the HR system of record.

6. Engineering performance report: Engineering submission covering product delivery metrics, operational performance, and significant production incidents.

7. Marketing performance report: Marketing submission summarizing pipeline contribution, campaign performance, and quarterly spend.

8. Executive priorities and board follow-ups: CEO email identifying the key strategic topics to emphasize, along with the open items tracker documenting outstanding board requests from prior meetings.

9. Previous board materials: Prior quarter's board pre-read provided for continuity, formatting reference, and comparison with current strategic updates.

10. Historical draft materials (distractors): Includes the superseded Product submission (v1), an earlier Sales deck prepared before quarter-end, and last year's board pre-read template with an outdated section order.

#### Solution and where agents fail

Correct solution: Produce a board pre-read that follows the required template, presents the correct executive metrics, incorporates the latest approved departmental updates, reconciles cross-functional data to the appropriate systems of record, and includes an open-items memo documenting any unresolved issues and proposed follow-up actions.

Most critical check (primary failure point): Determine whether the revenue discrepancy is resolved using the correct metric definitions. The executive summary should report recognized revenue, as required by the metric guidance, while bookings should remain clearly labeled in the Sales section. Mixing the two metrics or selecting whichever value is larger misstates quarterly performance to the board.

Second failure point: Determine whether headcount is reconciled to the HR system of record rather than the departmental submissions. The two departmental reports incorrectly count open requisitions as filled positions, and those errors should be corrected before preparing the executive summary.

Third failure point: Determine whether the final board package incorporates the approved Product v2 submission, highlights the roadmap change from the prior quarter rather than silently replacing it, and addresses the CEO's three priority topics while remaining within the template's page limits.

A strong response delivers a reconciled, template-compliant board pre-read that uses the correct metrics, resolves conflicting departmental data, incorporates the latest approved materials, and includes a concise open-items memo assigning ownership for unresolved issues. A weak response assembles the departmental submissions without reconciliation, leaves the revenue and headcount inconsistencies unresolved, uses superseded materials, and fails to highlight the roadmap change for the board.

#### Rubric

1. The executive summary reports Finance's recognized revenue of $48.2M, not Sales' $61.5M bookings.

2. Sales' $61.5M figure appears only where explicitly identified as bookings.

3. Recognized revenue and bookings are not blended or averaged.

4. The distinction between recognized revenue and bookings is applied consistently in every section where either metric appears.

5. Company headcount is reported as 642 from the HR system of record rather than 655 from the departmental reports.

6. The 13-position difference is attributed to open requisitions counted as filled (8 in Engineering and 5 in Marketing), and both department reports are corrected.

7. The 655 headcount is not carried into any section of the pre-read.

8. The Product section uses submission v2 attached to the CPO's follow-up email rather than the earlier v1 submission.

9. The analytics-suite launch delay from Q4 to Q1, introduced in Product v2, is identified in the pre-read or the accompanying open-items memo.

10. The pre-read does not present the Product v2 roadmap as unchanged from the prior quarter's board roadmap.

11. The pre-read follows the required template order: Executive Summary, Financials, Go-to-Market, Product & Engineering, People, and Open Items.

12. The pre-read does not exceed the template's 12-page limit.

13. The executive summary includes all four required metrics: recognized revenue ($48.2M), cash ($73.5M), headcount (642), and net revenue retention (118%).

14. Each of the CEO's three requested topics (enterprise expansion, the security-incident retrospective, and the hiring plan) is addressed.

15. Information from all six department submissions (Finance, Sales, Product, Engineering, Marketing, and HR) is incorporated.

16. The recognized revenue ($48.2M) and headcount (642) values are consistent across every section in which they appear.

17. The deliverable includes both the board pre-read and an accompanying open-items memo.

18. The open-items memo identifies the bookings-definition alignment (owner: CFO), analytics-suite launch delay (owner: CPO), and requisition-counting correction (owner: CHRO).

19. The September 28 Sales deck containing pre-quarter-close pipeline data is not used; the October 6 final Sales submission is used instead.

20. The response does not introduce figures or narrative content that are not supported by the department submissions or the HR extract.

21. The deliverable contains no blank, placeholder, or "TBD" sections.

22. All document assembly, reconciliation, and consistency checks are completed in the deliverable rather than deferred to the reviewer.

### Risk, Insurance & Business Continuity: Property Program Renewal with Coverage Gaps

#### Scenario

Harbor Foods, a multi-site food manufacturer, has three property insurance renewal quotes to evaluate before its renewal in 30 days. Since last year's placement, the company has added a warehouse in Savannah, and a recent flood determination places the site in Zone AE. The latest loss runs also include a $1.8M ammonia leak claim, making the renewal market more challenging.

The proposals aren't directly comparable. Carrier A excludes flood coverage entirely, Carrier B includes flood but with a $1M sublimit that is below the Savannah exposure, and Carrier C offers broader coverage at a higher premium. The broker's summary misstates Carrier A's flood coverage, so relying on the summary instead of the policy forms leads to the wrong conclusion. The business income values haven't been updated since the Savannah expansion, and a key customer contract requires coverage limits and endorsements that not every quote satisfies. The deductible structures also differ enough that comparing premiums alone produces a misleading recommendation.

#### Prompt

Prepare the property insurance renewal recommendation for the CFO.

#### Context files

1. Current insurance program: Expiring property policy, including forms, endorsements, coverage limits, sublimits, and deductibles that establish the current coverage baseline.

2. Renewal market submissions: Renewal quotes from Carriers A, B, and C, including their proposed pricing, coverage terms, endorsements, and policy differences.

3. Broker placement summary: Broker cover note summarizing the renewal options and recommendations. Contains an error regarding Carrier A's flood coverage that must be verified against the actual policy forms.

4. Property schedule: Statement of Values (TIV) listing all insured locations and values, including the newly added Savannah warehouse.

5. Property risk assessment: Flood zone determination and property engineering (COPE) reports describing each site's construction, occupancy, protection, exposures, and catastrophe risk.

6. Loss history and retention analysis: Five-year loss runs and deductible analysis summarizing historical claims experience, current retentions, and loss frequency used to evaluate appropriate risk sharing.

7. Business interruption analysis: Business income worksheet used to estimate business interruption values. The analysis predates the facility expansion and should be evaluated for completeness.

8. Customer insurance requirements: Key customer contract requirements specifying minimum insurance limits, required endorsements, and contractual insurance obligations.

9. Renewal recommendation template: Standard insurance renewal evaluation template used to compare carrier options, identify coverage gaps, and prepare the recommendation for the CFO.

10. Historical marketing materials (distractors): Includes last year's renewal quotations and a Carrier C marketing brochure describing its products.

#### Solution and where agents fail

Correct solution: Produce an insurance renewal recommendation that compares each carrier's coverage using the policy forms, evaluates business income adequacy following the facility expansion, verifies compliance with contractual insurance requirements, normalizes premiums for deductible differences, and recommends the most appropriate renewal option.

Most critical check (primary failure point): Determine whether the flood coverage analysis is based on the actual policy forms rather than the broker's summary. Carrier A excludes flood coverage, while Carrier B provides only a $1 million flood sublimit, which is insufficient for the Savannah warehouse located in Flood Zone AE. Relying on the broker's incorrect summary leads to a recommendation that leaves a significant flood exposure uninsured.

Second failure point: Determine whether business income limits are recalculated using the updated operating profile for the expanded Savannah facility rather than carried forward from the pre-expansion analysis. Using the outdated values understates the required coverage, creating a risk of underinsurance and potential coinsurance penalties that materially affect the adequacy of the renewal options.

Third failure point: Determine whether each proposal satisfies the insurance requirements in the customer contracts and whether premiums are compared on a consistent basis by accounting for differences in deductibles and retentions. Comparing quoted premiums without normalizing for coverage differences results in an inaccurate value comparison.

A strong response presents a coverage gap analysis supported by citations to the policy forms, quantifies the Savannah flood exposure under each proposal, evaluates business income adequacy and contractual compliance, and recommends the preferred carrier along with any required endorsements or coverage enhancements. A weak response compares premiums at face value, relies on the broker's summary instead of the policy language, and recommends a program that leaves significant coverage gaps for the expanded operation.

#### Rubric

1. Flood coverage is determined from the carrier quote forms rather than the broker cover note.

2. Carrier A's quote is identified as excluding flood coverage according to its forms schedule.

3. Carrier B's flood coverage is identified as subject to a $1M sublimit.

4. Carrier C's quote is identified as providing full-limit flood coverage without a Savannah location restriction.

5. The broker cover note's incorrect statement that Carrier A includes flood coverage is identified and corrected using the policy forms.

6. The flood coverage comparison is not based on the broker cover note.

7. The Savannah warehouse's Zone AE flood exposure is quantified as approximately $12M of the scheduled $28M total insured value.

8. Carrier B's $1M flood sublimit is identified as leaving approximately $11M of Savannah flood exposure uninsured.

9. Business income exposure is recalculated as approximately $31M by incorporating the Savannah expansion into the pre-expansion $22M worksheet.

10. The recommendation does not rely on the outdated $22M business income value.

11. The coinsurance risk resulting from reporting $22M of business income against an actual exposure of approximately $31M is identified.

12. Each carrier quote is evaluated against the customer contract's insurance requirements of $5M per-occurrence liability and a waiver-of-subrogation endorsement.

13. Carrier A is identified as non-compliant because it omits the required waiver-of-subrogation endorsement.

14. Premiums are normalized to a common $100K deductible by adjusting Carrier B's $1.27M premium upward by approximately $85K of expected retained losses associated with its $250K deductible.

15. The recommendation is not based solely on the unadjusted quoted premiums ($1.19M, $1.27M, and $1.41M).

16. The normalized comparison shows Carrier C at approximately $1.41M and Carrier B at approximately $1.50M after adding the approximately $140K flood buy-up.

17. The 2024 Kingsland ammonia-leak claim (approximately $1.8M) is reflected in the loss-history analysis and in each carrier's pricing response.

18. A coverage-gap matrix compares the three quotes across at least flood, business income, and waiver-of-subrogation coverage, citing the supporting policy torm or endorsement for each comparison.

19. The recommendation selects Carrier C, or Carrier B with the flood buy-up only if its normalized total cost is shown to be lower than Carrier C's.

20. The recommended insurance program covers the Savannah flood exposure without leaving the approximately $11M coverage gap.

21. The recommended insurance program satisfies the customer contract's $5M liability limit and waiver-of-subrogation requirements.

22. The recommended insurance program is consistent with the response's own coverage-gap matrix and normalized premium comparison.

23. Prior-year quotes and the Carrier C marketing brochure are not used as evidence.

24. The response does not introduce limits, sublimits, premiums, or exposure values that are not supported by the source files.

25. The deliverable contains no blank, placeholder, or "TBD" values.

26. All coverage comparisons, exposure analyses, and premium normalizations are completed in the deliverable rather than deferred to the reviewer.

### IT, Business Systems & Process Improvement: Customer Master Migration Validation for an ERP Consolidation

#### Scenario

A regional distributor is consolidating two legacy ERPs onto a single platform, and the first complete customer master extract has just been loaded into the target system. User acceptance testing can't begin until the migration is validated, and although the ETL team's report confirms the source and target row counts match, the UAT entry criteria explicitly state that row-count reconciliation alone is not sufficient.

The detailed validation is where the real work begins. The approved field-mapping document is version 3, but version 2, which maps payment terms differently, remains on the shared drive and was used during an earlier test cycle. Nearly 4,000 customers exist in both legacy systems, and the survivorship rules specify that billing addresses come from System B while credit limits come from System A, so a simple "winner takes all' merge silently corrupts one field or the other. System B also stores credit limits using a different currency convention, tax IDs follow two different formats, and the known-issues log identifies defects that the validation must confirm have either been resolved or are still outstanding before UAT can begin.

#### Prompt

Validate the customer master migration for the ERP consolidation and prepare the UAT sign-off package.

#### Context files

1. Source system data extracts: Customer master exports from Systems A and B containing customer records, credit limits, payment terms, addresses, currencies, and other master data used as the migration source.

2. Target system extract: Customer master data loaded into the target system, used to validate that records were migrated accurately and transformed correctly.

3. Migration mapping specification: Approved field-mapping workbook (v3) defining the authoritative source-to-target mappings for the migration.

4. Data transformation rules: Survivorship rules, credit limit conversion rules, Tax ID formatting specifications, and address standardization guidelines describing how overlapping records and legacy data should be standardized in the target system.

5. Target data model: Target system schema and data dictionary defining required fields, accepted formats, validation rules, and business definitions for the migrated customer master.

6. Migration validation results: ETL validation report summarizing migration results and record counts. Confirms load completeness but does not verify field-level accuracy.

7. User acceptance testing (UAT) guidance: UAT entry criteria defining field-level accuracy thresholds, materiality limits, validation requirements, and go/no-go criteria for production deployment.

8. Known issues register: Log of known migration defects, approved exceptions, and unresolved issues identified during previous test cycles.

9. Migration validation workbook: Standard validation worksheet used to document field-level discrepancies, transformation errors, and overall migration readiness.

10. Historical migration materials (distractors): Includes the superseded field-mapping workbook (v2) and a target-system extract from an earlier test run.

#### Solution and where agents fail

Correct solution: Produce a field-level migration validation report that evaluates the migrated customer master against the approved mapping and transformation rules, categorizes exceptions by root cause, measures validation results against the UAT acceptance criteria, and provides a go/no-go recommendation supported by the findings.

Most critical check (primary failure point): Determine whether the agent validates the migration against the approved field mapping (v3) rather than the superseded v2 version. The payment terms mapping changed between versions, so validating against v2 incorrectly passes records that would be invalid in production and propagates errors into downstream processes.

Second failure point: Determine whether survivorship rules are validated on a field-by-field basis for overlapping customer records. The approved rules require different systems of record for different attributes (for example, System B for billing addresses and System A for credit limits). A one-system-wins approach can pass record count validation while silently corrupting thousands of field values.

Third failure point: Determine whether the validation extends beyond record counts to verify field-level accuracy, including credit limit currency conversions, Tax ID formatting, required fields, and other transformation rules, and whether the go/no-go recommendation is based on the UAT materiality thresholds rather than the ETL report's successful row-count reconciliation.

A strong response reports field-level validation results, quantifies pass rates against the UAT criteria, groups exceptions by root cause with proposed corrective actions, and provides a defensible go/no-go recommendation. A weak response relies on matching record counts, performs only limited spot checks, and recommends deployment despite unresolved mapping, survivorship, and transformation errors.

#### Rubric

1. Validation is performed using the approved mapping workbook v3.

2. Validation is not performed using the superseded v2 workbook still on the shared drive.

3. The response identifies that v2 maps legacy payment-terms codes to the customer_notes field, while v3 maps them to the payment_terms field, and identifies v3 as authoritative.

4. The 48,300-record target extract is reconciled against both System A (31,200 records) and System B (21,100 records), rather than only one source.

5. Field-level survivorship is validated for the approximately 4,000 customers present in both systems.

6. Billing addresses for overlapping customers match System B's values.

7. Credit limits for overlapping customers match System A's values.

8. The 512 overlapping customer records that retained System A's billing address are reported as survivorship exceptions rather than passed.

9. System B's CAD credit limits are converted to USD using the conversion rule's fixed 0.74 planning rate before comparison.

10. The 361 records with unconverted or incorrectly converted CAD credit limits are reported as conversion exceptions.

11. Tax IDs are validated against the required XX-XXXXXXX format.

12. The 298 records containing System B's unhyphenated nine-digit tax IDs are reported as formatting exceptions.

13. The 85 records missing required credit_terms or sales_region values are reported as completeness exceptions.

14. Validation includes content-level checks in addition to the ETL report's row-count reconciliation.

15. The go/no-go recommendation is not based solely on matching row counts.

16. Every exception identifies the affected customer records.

17. Exceptions are grouped by root cause: survivorship (512), conversion (361), formatting (298), and completeness (85).

18. Each exception category includes a proposed remediation: rerun the merge using field-level survivorship, apply the 0.74 conversion rate, reformat the tax IDs, or backfill the required fields.

19. Both items in the known-issues log are dispositioned: the duplicate-merge issue is confirmed resolved, while the CAD conversion issue remains open.

20. The total of 1,256 failing records equals the sum of the four exception categories.

21. The field-level pass rate is reported as approximately 97.4% (47,044 passing and 1,256 failing records out of 48,300).

22. The recommendation is no-go because the approximately 97.4% pass rate is below the UAT entry threshold of 99.0%.

23. The recommendation section reports the same approximately 97.4% pass rate and 1,256-record exception total as the validation detail, and applies the 99.0% threshold to those figures.

24. The month-old test-run extract is not used as the validation target.

25. The response does not introduce records, mappings, conversion rates, or thresholds that are not supported by the source files.

26. The exception log contains no blank, placeholder, or "TBD" entries.

27. All reconciliation, validation, and exception analysis are completed in the deliverable rather than deferred to the reviewer.

### Real Estate, Construction, Architecture & Facilities: CAM Reconciliation and True-Up Dispute

#### Scenario

A tenant leasing 42,000 square feet in a 300,000-square-foot office park has received its 2025 operating expense reconciliation showing a $118K true-up due. The original lease was executed in 2019, a 2021 first amendment expanded the premises mid-year and changed the tenant's pro rata share, and a 2023 second amendment reset the base year to 2023 while capping controllable operating expenses at 5% annually on a cumulative basis.

The reconciliation doesn't appear to reflect the lease as amended. Controllable expenses seem to have been left uncapped, the expense detail includes a $240K parking garage project that appears to be a capital replacement subject to exclusion or amortization under the lease, and the landlord's gross-up calculation assumes 100% occupancy even though the lease specifies 95%. A recent BOMA remeasurement also changed the building's rentable square footage, affecting the tenant's pro rata share. Finally, the lease file contains an unexecuted draft third amendment with different expense-cap language that must not be treated as controlling. The final analysis should determine the correct reconciliation under the executed lease documents and identify any items that should be disputed with the landlord.

#### Prompt

Review the landlord's 2025 operating expense reconciliation and prepare the tenant response package.

#### Context files

1. Lease agreement package: Executed lease and all fully executed amendments defining operating expense recoveries, base year methodology, pro-rata share, gross-up provisions, controllable expense cap, and tenant audit rights.

2. 2025 operating expense reconciliation: Landlord's 2025 reconciliation statement and supporting operating expense detail showing the calculation of the annual true-up.

3. Base year reference package: 2023 base year expense statement and the 2024 reconciliation used to verify the application of the reset base year and consistency with prior-year recoveries.

4. Capital project documentation: Parking garage repair invoice and supporting scope documentation used to determine whether the expense is recoverable under the lease.

5. Gross-up methodology: Landlord's gross-up methodology explaining how occupancy adjustments were calculated for recoverable operating expenses.

6. Building measurement documentation: BOMA remeasurement memo documenting revised rentable square footage that may affect the tenant's pro-rata share.

7. Vendor contract support: Janitorial and security service contracts supporting the controllable operating expense categories included in the reconciliation.

8. Utility expense support: Utility summaries supporting the non-controllable operating expenses allocated to the property.

9. Lease audit workpaper template: Standard lease audit worksheet used to document findings, calculate disputed amounts, and prepare the tenant's response to the landlord.

10. Historical lease materials (distractors): Includes an unexecuted draft third amendment containing different expense cap language and the 2022 operating expense reconciliation prepared under the previous base year methodology.

#### Solution and where agents fail

Correct solution: Produce a recalculated operating expense reconciliation that applies the governing lease provisions, quantifies all disputed charges, and includes a tenant dispute letter citing the applicable lease and amendment provisions. The reconciliation should apply the correct base year, expense cap, gross-up methodology, pro-rata share, and capital expense treatment.

Most critical check (primary failure point): Determine whether the second amendment's 2023 base-year reset and 5% cumulative compounding cap on controllable operating expenses are applied correctly. The landlord's reconciliation uses the wrong base year and does not apply the cap as required. Correcting these provisions accounts for the largest portion of the disputed amount, and the cap must be applied cumulatively rather than as a simple annual limit.

Second failure point: Determine whether the $240,000 parking garage repair is treated in accordance with the lease's capital expense provisions. The expense should either be excluded entirely or amortized as permitted by the lease rather than being recovered in full during the 2025 reconciliation.

Third failure point: Determine whether operating expenses are recalculated using the lease's 95% gross-up methodology and the updated pro-rata share from the BOMA remeasurement, while disregarding the unexecuted third amendment. Applying the wrong gross-up methodology, using the outdated rentable area, or relying on unexecuted lease language produces an incorrect reconciliation.

A strong response produces a line-by-line reconciliation that bridges the landlord's $118,000 true-up to the recalculated amount, supports each adjustment with citations to the executed lease documents, and prepares a well-supported dispute letter. A weak response accepts the landlord's expense classifications, overlooks the cumulative expense cap, and challenges only the parking garage repair while leaving the larger reconciliation errors unaddressed.

#### Rubric

1. The recalculation uses the 2023 base year established by Second Amendment §3.

2. The recalculation is not performed using the original 2019 lease base year.

3. Janitorial, security, landscaping, and management fees are classified as controllable, while taxes, insurance, and utilities are classified as non-controllable according to the lease definitions, and the cap is applied only to the controllable expenses.

4. The 2023 controllable-expense base of approximately $1.42M is taken from the base-year statement.

5. The 5% controllable-expense cap is compounded from the 2023 base, producing a 2025 allowable controllable expense level of approximately 110.25% of the base.

6. The controllable-expense cap is not applied as a simple non-compounding 5% increase.

7. The controllable-expense cap reduces the tenant's billed share by approximately $36K.

8. The $240K garage repair is classified as a capital replacement under lease §6.2.

9. The $240K garage repair is either excluded or amortized at approximately $8K per year over its 30-year useful life, with only the amortized portion included in 2025 operating expenses.

10. The full $240K garage repair is not included in the 2025 operating-expense pool, reducing the tenant's billed share by approximately $32K.

11. The gross-up is recalculated using lease §6.4's 95% occupancy methodology, reducing the tenant's billed share by approximately $6K compared with the landlord's 100% method.

12. The tenant's pro-rata share is recalculated from 14.00% (42,000 of 300,000 RSF) to approximately 13.76% using the BOMA-remeasured 305,200 RSF, reducing the billed share by approximately $3K.

13. The post-expansion pro-rata share applies throughout the 2023 base year, and no pre-expansion share is blended into the calculation.

14. The unexecuted draft Third Amendment is not used to determine the controllable-expense cap.

15. The recalculated 2025 true-up is approximately $41K rather than the landlord's $118K.

16. A reconciliation schedule bridges the landlord's $118K true-up to the recalculated approximately $41K true-up through four adjustments: controllable-expense cap (approximately -$36K), capital exclusion (approximately -$32K), gross-up correction (approximately -$6K), and pro-rata share correction (approximately -$3K).

17. The four reconciliation adjustments total the approximately $77K reduction between the landlord's and recalculated true-up amounts.

18. Each reconciliation adjustment cites its governing authority: Second Amendment §4 for the cap, lease §6.2 for the capital exclusion, lease §6.4 for the gross-up, and the BOMA remeasurement memo for the pro-rata share.

19. The treatment of the janitorial and security contracts is consistent with the 2024 reconciliation.

20. The disputed amount in the letter (approximately $77K) equals the total adjustment shown in the supporting reconciliation schedule.

21. The dispute letter cites the governing lease or amendment provision supporting each adjustment.

22. The dispute letter invokes lease §6.7's audit rights and 180-day dispute window.

23. The response does not introduce expenses, square footages, or lease terms that are not supported by the source files.

24. The reconciliation schedule contains no blank, placeholder, or "TBD" values.

25. All lease-expense recalculations, cap adjustments, and reconciliations are completed in the deliverable rather than deferred to the reviewer.

### Government, Public Sector & Nonprofit: Federal Grant Annual Performance Report with Budget Modification Determination

#### Scenario

A nonprofit workforce development agency is preparing the Year 2 annual performance report for its $2.1M Department of Labor grant. The award incorporates 2 CFR 200, requires prior approval for transfers exceeding 10% between budget categories, and defines performance outcomes for reporting purposes. For example, 'placement means employment obtained within the specified timeframe and verified according to the grant agreement, not the agency's broader internal definition.

The financial records require careful review before the report can be submitted. An internal memo instructs staff to apply the 10% de minimis indirect cost rate, even though the agency has a negotiated indirect cost rate agreement (NICRA) allowing 15.5% of modified total direct costs (MTDC). Using the correct rate changes both total expenditures and budget category balances. The travel records include an unallowable alcohol expense, a $6,200 laptop purchase raises questions about equipment and prior approval requirements, and the subrecipient monitoring report identifies $18K of questioned costs that cannot be reported without resolution. After those corrections are made, the personnel category exceeds the 10% budget transfer threshold, requiring the report to identify the variance and flag that a formal budget modification is needed.

#### Prompt

Prepare the Year 2 annual performance report for the DOL workforce grant.

#### Context files

1. Grant award package: Executed grant agreement, award terms, and governing federal requirements, including the approved prior-approval requirements, budget transfer thresholds, and program outcome definitions.

2. Approved grant budget: Negotiated award budget organized by SF-424A cost categories, establishing the authorized spending plan for Year 2.

3. Financial expenditure package: General ledger expenditure extract and supporting payroll allocation records documenting grant expenditures and personnel costs charged during Year 2.

4. Indirect cost guidance: Negotiated Indirect Cost Rate Agreement (NICRA) defining the approved indirect cost rate and Modified Total Direct Cost (MTDC) base, along with an internal staff memo incorrectly instructing employees to apply the 10% de minimis rate.

5. Subrecipient monitoring file: Subrecipient invoices, monitoring documentation, and identified questioned costs requiring evaluation before final reporting.

6. Cost share documentation: Match documentation supporting in-kind contributions and other required non-federal cost sharing reported under the award.

7. Program performance report: Participant enrollment, placement, and retention data used to evaluate performance against the grant's required outcome measures.

8. Supporting expenditure documentation: Equipment purchase records and travel expense documentation supporting selected grant expenditures that require verification for allowability and compliance.

9. Prior reporting package: Year 1 performance report provided as a formatting reference and baseline for preparing the current annual report.

10. Historical budget materials (distractors): Includes the original grant application budget that was superseded during award negotiations and a draft budget modification that was never submitted or approved.

#### Solution and where agents fail

Correct solution: Produce a grant reconciliation that validates expenditures by budget category, applies the approved indirect cost methodology, identifies unallowable and questioned costs, determines whether a budget modification is required, and reports program outcomes using the definitions established in the grant agreement.

Most critical check (primary failure point): Determine whether indirect costs are calculated using the approved 15.5% NICRA rate and the correct Modified Total Direct Cost (MTDC) base rather than the staff memo's 10% de minimis rate. Because the organization has an approved NICRA, the de minimis rate cannot be used. Applying the wrong rate changes total expenditures, category balances, and whether the budget modification threshold is exceeded.

Second failure point: Determine whether unallowable and questioned costs are identified and handled appropriately. This includes removing the alcohol expense as unallowable under 2 CFR 200, evaluating the laptop purchase against the grant's equipment and prior approval requirements, and excluding or separately identifying the subrecipient's $18,000 in questioned costs rather than reporting them as allowable expenditures.

Third failure point: Determine whether the corrected financial results require a budget modification under the grant agreement and whether program outcomes are calculated using the agreement's approved outcome definitions rather than the organization's internal reporting methodology. The personnel category exceeds the 10% transfer threshold only after the required financial corrections are applied.

A strong response reconciles every budget category, supports each adjustment with citations to the grant agreement or applicable federal guidance, clearly identifies unallowable and questioned costs, determines whether a budget modification is required, and reports outcomes using the governing grant definitions. A weak response reports expenditures directly from the general ledger, applies the incorrect indirect cost rate, overlooks compliance issues, and reports financial and performance results that are inconsistent with the grant requirements.

#### Rubric

1. Indirect costs are calculated using the negotiated 15.5% NICRA rate on an MTDC base of approximately $1.38M, yielding approximately $214K.

2. Indirect costs are not calculated using the staff memo's 10% de minimis rate.

3. The response identifies that an organization with a negotiated indirect cost rate may not elect the 10% de minimis rate.

4. The MTDC base excludes the $6,200 laptop purchase and the $285K portion of the $310K subaward above the first $25,000.

5. The $312 alcohol charge included in the June conference banquet is excluded as an unallowable cost under 2 CFR 200.

6. The $6,200 laptop purchase (five units at $1,240 each) is classified as supplies rather than equipment because each unit is below the $5,000 capitalization threshold.

7. The subrecipient's $18K of unsupported participant stipends identified in the monitoring report is excluded from reported expenditures or reported as questioned costs.

8. The program manager's $9,400 of Q3 salary lacking personnel activity documentation is reported as unsupported.

9. All remaining salary charges are supported by personnel activity reports and timesheets.

10. Expenditures are reconciled by SF-424A budget category (personnel, fringe, travel, equipment, supplies, contractual, other, and indirect) against the approved award budget.

11. The reconciliation is not performed against the original application budget.

12. Budget-category variances are calculated after applying the indirect-cost, allowability, reclassification, and questioned-cost corrections.

13. Corrected personnel expenditures of approximately $966K against the $860K budget (approximately 12% over budget) are identified as exceeding the 10% transfer threshold.

14. The response identifies that a prior-approved budget modification is required under 2 CFR 200.308.

15. The report does not treat pre-correction budget variances as final.

16. Reported matching contributions of approximately $538K (volunteer time and donated space at documented values) are compared with the required $525K match.

17. Placement outcomes include only participants verified as employed within 90 days of program exit through wage records or employer documentation.

18. The placement rate is reported as approximately 61% (252 of 411 exiters), rather than the program's internally reported 74% based on any self-reported employment.

19. The placement rate is compared with the 68% performance target, and the approximately 7 percentage point shortfall is identified.

20. Each performance measure is reported against its target: enrollment (412 versus 400), placement (61% versus 68%), and six-month retention (79% versus 82%).

21. Total reported expenditures equal the sum of the SF-424A budget categories, including the recalculated indirect-cost amount of approximately $214K.

22. The draft budget modification that was never submitted is not treated as an approved award amendment.

23. The report contains no blank, placeholder, or "TBD" values.

24. All expenditure reconciliations, indirect-cost calculations, and performance calculations are completed in the deliverable rather than deferred to the reviewer.

### Compliance & Corporate Affairs: Privacy Data Map and Gap Analysis for a New Customer Data Platform

#### Scenario

A national retailer is preparing to launch a customer data platform (CDP) that will centralize customer profiles and share data with advertising partners. Before launch, the privacy team must complete a data map and gap analysis. An applicability assessment confirms the company is subject to California, Colorado, and Virginia privacy laws, while the existing consent management platform was implemented before the CDP was introduced.

The supporting documentation isn't fully aligned. The vendor's architecture diagram lists fewer data ingestion sources than the tag audit and integration inventory, and the data processing agreement is missing the subprocessor list altogether. One advertising partner agreement describes an audience matching arrangement that may qualify as "sharing" for cross-context behavioral advertising under the CPRA, triggering opt-out obligations that the current consent platform cannot support. Marketing has requested a seven-year retention period, the corporate retention schedule specifies 24 months, and the CDP is configured to retain data indefinitely by default. The current DSAR procedure also doesn't account for data stored in the new platform. The final assessment should identify the compliance gaps that must be addressed before the CDP can be launched.

#### Prompt

Prepare the privacy readiness assessment for the customer data platform rollout.

#### Context files

1. CDP implementation overview: Integration inventory, architecture diagram, and data flow documentation showing how data enters, moves through, and is shared by the customer data platform.

2. Data collection assessment: Tag and cookie audit and the CDP data dictionary documenting observed data collection, identifiers, inferred attributes, and other data elements processed by the platform.

3. Vendor documentation: CDP vendor contract, Data Processing Agreement (DPA), and supporting security questionnaire describing the vendor relationship, security controls, and contractual obligations. The DPA should be evaluated for any missing required disclosures, including subprocessors.

4. Privacy compliance framework: Current privacy policy and the state law applicability memo outlining applicable privacy laws, required disclosures, and the organization's compliance obligations.

5. Third-party data sharing: Data-sharing agreements with advertising and marketing partners, including audience-matching arrangements and other external data transters that require privacy review.

6. Data governance policies: Data retention schedule and consent management platform configuration defining retention periods, consent handling, and opt-out signal processing for customer data.

7. Individual rights procedures: Data Subject Access Request (DSAR) process documentation describing the organization's procedures for responding to consumer privacy requests.

8. Record of processing activities: Current Record of Processing Activities (RoPA) documenting the organization's processing purposes, data categories, systems, and recipients.

9. Privacy assessment template: Standard privacy readiness assessment used to document findings, identify compliance gaps, and prepare recommendations before the CDP launch.

10. Historical privacy materials (distractors): Includes the outdated 2022 Record of Processing Activities and a draft privacy policy that was never adopted.

#### Solution and where agents fail

Correct solution: Produce a privacy readiness assessment that maps the actual data flows into and out of the CDP, identifies applicable legal and policy requirements, documents compliance gaps, and provides a prioritized remediation plan before launch. The assessment should include RoPA-ready processing entries, required contractual updates, and recommended operational changes.

Most critical check (primary failure point): Determine whether the audience-matching arrangement is correctly classified as sharing for cross-context behavioral advertising under the CPRA. This classification triggers consumer opt-out rights and opt-out signal handling requirements that the current consent configuration does not satisfy. Missing this issue omits the highest-risk compliance gap from the assessment.

Second failure point: Determine whether the data map is built from the observed data flows documented in the tag audit and integration inventory rather than the vendor's architecture diagram. The observed flows identify two additional data ingestion sources that are absent from the vendor documentation. The review should also identify the missing subprocessor list in the Data Processing Agreement as a required contractual remediation.

Third failure point: Determine whether the retention conflict is resolved by aligning the CDP configuration with the approved 24-month retention schedule rather than extending retention to meet Marketing's request, and whether the DSAR process is expanded to include data processed by the new platform.

A strong response produces a complete data inventory, identifies each compliance gap with citations to the applicable law or internal policy, prioritizes remediation by risk, and assigns clear ownership for each action. A weak response relies on the vendor's architecture diagram, treats the advertising data flow as a routine service-provider disclosure, overlooks the contractual and consent deficiencies, and leaves the retention and DSAR gaps unresolved.

#### Rubric

1. The data map is built from the tag audit and integration inventory, documenting all 11 ingest sources rather than only the 9 shown in the vendor diagram.

2. The mobile attribution SDK and loyalty POS feed are included in the data map.

3. The data map is not limited to the nine data flows shown in the vendor diagram.

4. Each data flow identifies the categories of personal information it carries (identifiers, device IDs, purchase history, loyalty tier, and inferred preferences).

5. The loyalty POS feed is identified as collecting date of birth, and the data map flags it for collection-disclosure review.

6. The ad-partner audience-matching flow is classified as sharing for cross-context behavioral advertising under CPRA §1798.140(ah).

7. The ad-partner audience-matching flow is not classitied as a routine service-provider disclosure.

8. The response identifies that the sharing classification triggers the CPRA opt-out right (§1798.120) and the obligation to honor universal opt-out signals such as GPC (§1798.135).

9. The consent platform is identified as honoring GPC only for website interactions and not for CDP audience segments or the ad-partner synchronization.

10. The DPA's missing subprocessor list is identified as failing the CPRA service-provider contract requirements (§1798.100(d)), and a contract amendment is identified as the remediation.

11. The applicability analysis covers California (CPRA), Colorado (CPA, including universal opt-out requirements), and Virginia (VCDPA targeted-advertising opt-out).

12. The gap analysis identifies the five documented gaps: unhonored sharing opt-out, two undisclosed ingest sources, missing subprocessor list, retention conflict, and DSAR scope gap.

13. Each identified gap cites the applicable legal requirement or policy commitment.

14. The two previously unmapped data sources are compared against the privacy policy's collection disclosures, and any disclosure gap is included in the remediation plan.

15. The CDP's indefinite retention setting is identified as conflicting with the 24-month customer-marketing-data retention schedule.

16. The retention conflict is resolved by configuring the CDP to the approved 24-month retention period.

17. Marketing's proposed seven-year retention period is not adopted.

18. The DSAR process is extended to include the CDP profile store for both access and deletion requests.

19. The remediation plan includes GPC propagation to CDP audience segments and the ad-partner synchronization as the corrective action for the sharing opt-out gap.

20. Remediation items are prioritized by implementation risk, with the sharing opt-out gap ranked highest.

21. Each remediation item identifies an owner (privacy counsel, marketing operations, data engineering, or vendor management).

22. The outdated 2022 RoPA and the unapproved draft policy are not used as current-state sources.

23. Each data-map entry includes RoPA-ready fields (system, purpose, personal information categories, recipients, and retention period).

24. The deliverable contains no blank, placeholder, or "TBD" sections.

25. All data mapping, legal analysis, and gap assessment are completed in the deliverable rather than deferred to the reviewer.

### Engineering: Mezzanine Structural Calculation Package Verification

#### Scenario

A design-build firm is adding a storage mezzanine to a client's distribution center, and a junior engineer's structural calculation package has been submitted for review before it is sent to the Engineer of Record (EOR) for sealing. The basis of design specifies the governing building code, ASCE 7 loading criteria, a 125 psf storage live load, and an L/360 live-load deflection limit.

The calculation package no longer matches the current design. It was prepared using racking layout R2, but the issued R3 layout adds a concentrated load from a relocated pallet rack, and a resolved RFI increased the span of one beam. The calculations also apply a live-load reduction that is not permitted for storage occupancies under the applicable code, while the anchor and connection designs are still based on the original support reactions. Even where members continue to satisty strength requirements under the revised loading, some no longer meet the required deflection limit. The review must identify these issues member by member so the calculation package can be corrected before it is sealed.

#### Prompt

Prepare the structural review for the warehouse mezzanine design.

#### Context files

1. Structural design basis: Basis of Design document defining the governing building code, design criteria, live loads, deflection limits, and other engineering assumptions for the mezzanine.

2. Issued design drawings: Released structural framing drawings, member schedule, and the current rack layout (Revision R3) showing the approved framing configuration and loading arrangement.

3. Structural calculations: Structural calculation package documenting member and connection design checks performed for the mezzanine structure. The calculations should be evaluated for consistency with the released design documents.

4. Connection design package: Connection details and anchor bolt calculations supporting the structural connections and foundation loads.

5. Design changes and RFIs: RFI log and responses documenting approved design changes, including modifications that affect beam spans and structural loading.

6. Engineering reference data: Load combination reference, geotechnical report, and decking manufacturer capacity information used to verify structural adequacy under the governing design conditions.

7. Material documentation: Material certifications confirming the structural steel grades, fastener specifications, and other materials incorporated into the design.

8. Independent design review: Prior checker comments documenting unresolved review items and engineering feedback from the previous design submission.

9. Structural review template: Standard engineering review worksheet used to document calculation checks, design discrepancies, and approval recommendations before construction.

10. Superseded design materials (distractors): Includes the previous rack layout (Revision R2) and an earlier structural calculation package prepared using outdated loading assumptions.

#### Solution and where agents fail

Correct solution: Produce a structural review that verifies every member and connection against the released design, confirms compliance with both strength and serviceability requirements, recalculates foundation reactions where required, and identifies the design changes needed before approval.

Most critical check (primary failure point): Determine whether the review is performed against the released R3 layout and the updated beam span documented in the approved RFI response rather than the superseded R2 design. The relocated rack loading and increased span change the governing load case, causing at least one previously acceptable beam to fail and altering the reactions used to design the connections, columns, anchors, and foundations.

Second failure point: Determine whether the impermissible live load reduction is removed before evaluating the structural members. Storage live loads at this magnitude are not eligible for reduction under the governing code, so applying the reduction overstates structural capacity and results in unconservative member designs.

Third failure point: Determine whether serviceability is evaluated independently of strength and whether the anchor bolt calculations are updated using the revised reactions. Members that satisfy strength requirements may still exceed the L/360 deflection limit under the concentrated rack loads, and carrying forward the previous anchor calculations without recalculating reactions leaves the foundation design inconsistent with the revised structure.

A strong response provides a member-by-member and connection-by-connection verification, identifies the governing load combination and demand-to-capacity ratio for each critical element, recalculates the affected anchor reactions, and produces a clear list of required design revisions. A weak response spot-checks only selected members against the superseded layout, retains the improper live load reduction, and approves a design package without evaluating the governing loading condition.

#### Rubric

1. The structural verification uses released layout R3, including the relocated rack row's 12-kip concentrated load at midspan of bay 3.

2. Beam B-12 is verified using the 27'-6" span documented in RFI-014 rather than the original 24'-0" span.

3. The structural verification is not performed using layout R2.

4. Layout R2 is identified as superseded by R3.

5. The approximately 20% live-load reduction applied in the calculation package is removed from all member checks.

6. The 125 psf storage live load is treated as non-reducible in accordance with ASCE 7 §4.7.3.

7. Strength checks use the basis-of-design ASCE 7 load combinations, with 1.2D + 1.6L (including the 12-kip concentrated load) governing the bay 3 members.

8. Member demands are recalculated using the R3 loading rather than carried forward from the calculation package.

9. Beam B-7 (W12×19, bay 3) is identified as inadequate in flexure under the R3 loading, with a demand-capacity ratio of approximately 1.12.

10. The required correction for Beam B-7 is identified (for example, increasing the section to W14×22 or adding a support post beneath the rack row).

11. Beam B-12 is shown passing the strength check at the RFI-014 span with a demand-capacity ratio of approximately 0.97, and the calculation is documented.

12. Live-load deflection is evaluated independently of the strength checks using the L/360 criterion.

13. Beam B-9 is identified as exceeding the L/360 deflection limit (approximately L/292) while remaining adequate for strength.

14. Connection design uses end reactions recalculated under the R3 loading.

15. The C-3 anchor group is rechecked at the recalculated 14.1-kip demand, identified as inadequate relative to the package's 9.8-kip design, and the required anchor upgrade (for example, 5/8-inch to 3/4-inch anchors) is identified.

16. The package's anchor calculations are not carried forward without recalculation.

17. The recalculated C-3 column load (approximately 86 kips) is checked against the geotechnical report's 3,000 psf allowable bearing pressure and shown to comply.

18. Deck capacity under the 12-kip concentrated load is verified using the vendor cut sheets, and the required bearing-plate detail is identified.

19. The result for each member identifies the governing check (flexure, shear, or deflection) together with its demand-capacity ratio.

20. The member verification table includes all 42 beams and girders and all 12 columns.

21. Every member or connection identified as inadequate includes a required design modification (resize, add support, or strengthen the connection).

22. The executive summary identifies the same inadequate items as the detailed results table: Beam B-7 (strength), Beam B-9 (deflection), and the C-3 anchor group.

23. Material properties for ASTM A992 steel (Fy = 50 ksi) are used for all W-shapes in accordance with the material certifications.

24. The deliverable contains no blank, placeholder, or "TBD" results.

25. All structural calculations, code checks, and design verifications are completed in the deliverable rather than deferred to the reviewer.
