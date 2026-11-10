# Workflow: one Starter Project, start to finish

Each task lives in one folder, `tasks/NN-slug/`, copied from `templates/`. The number is the
next unused one (`python3 tools/alchemy_check.py --next`). Every form field is copied out of
the folder, so nothing is typed into the form from memory.

| File | Holds |
| --- | --- |
| `task.md` | the form fields in the form's order, then the working notes: design, correct answer, check output, log |
| `prompt.md` | the final prompt alone, exactly as pasted into the form |
| `rubric.md` | the five criteria, numbered, one per item |
| `inputs/` | the two input files exactly as uploaded |
| `inputs.zip` | built by `--zip`; its only top-level folder is `inputs/` |
| `runs/` | `run-N.md` per Attempting Agent run (fingerprint, final response, grading), `run-N/` for its output files |

Rule ids in brackets are defined in `rules.md`. The form's steps are in
`../training/starter-project-form.md`; the stage headings below give the step numbers each
stage fills.

The platform's helpers do some of the work: the scenario helper, the plan-review helper, the
File Builder, the Rubric Drafter, the Attempting Agent and the Grading Agent. An LLM may also
draft the text for any step, Steps 1 to 14. Each helper and each draft is a starting point or a
test, not an authority. Everything they produce is read and corrected here before it goes back
to the form.

## Stage 0: the scenario's field and role (Step 1)

Choose a finance domain from the eligible list in `../requirements.md` and a fictional role in it,
then write three or four sentences on the role's responsibilities and typical work [D1]. Write
it in the first person, the way someone describes their own job to a new colleague: plain,
specific, a little redundant, with no "fictional" label inside the text (the invented company
name carries that). The scenario helper matches its ideas to this text, so specific beats
general: "I'm a settlement analyst at a card processor; I reconcile merchant batches, track
reserves and prepare final payouts when a merchant leaves" gives better scenarios than "I work in
fintech". The prose tells apply here as everywhere.

The role is fictional, but its work is not: the duties, documents and decisions must be the ones
that job really carries, or the scenario will read as invented.

This Step 1 text describes the scenario, not you. The onboarding form in `../requirements.md` is
separate: there, the domains and qualifications you select must be your own.

## Stage 1: scenario, targeted failure and correct answer (Steps 2 to 5)

Generate three scenario ideas with the scenario helper or an LLM, then pick, combine or replace
them. Record the scenario source on the form: adapted from a suggestion, or a new scenario with
or without LLM assistance. Hold the chosen scenario
to the strong-task shape before writing anything else:

1. **The requester and the decision.** Who hands this over, what decision it feeds, and when.
2. **The deliverable.** The one or two files a professional would produce (a workbook, a memo,
   a revised schedule).
3. **The judgment call.** The point where expertise, not lookup, picks the answer, and that no
   single file states [D4].
4. **The dependency.** The earlier decision that changes later numbers, so one wrong call
   carries downstream [D6].
5. **The split.** What the data file holds and what the context file holds, so the answer
   needs both [D5].

Write the Step 3 scenario in the same first-person voice as Step 1: the analyst describing the
job in front of them ("One of our merchants ended its agreement on September 30, and I have to
close out the account"). Plain sentences, the deliverable named at the end, and the prose checks
run on it.

Then write the failure plan (Step 4), also in the first person ("What I expect the agent to get
wrong is..."): the mistake a capable model is likely to make, the judgment a careful professional
applies instead, and the consequence, with the figures from the correct-answer script. Aim at the severe
failures the training names: a calculation error that cascades, a missed edge case that
changes the outcome, a failure to synthesize across the files, a misclassified key item, the
wrong source chosen when documents conflict [D9].

**Work the correct answer now, before any file exists.** Compute every figure the scenario
implies with a short script and write the result into `task.md` under Correct answer. This is
the Phase 1 "description of the correct response", the source of every rubric value, and the
only way to know the files will support one defensible answer [D3]. A scenario whose answer
has not been computed is a guess, not a task.

Run the plan-review helper (Step 5). Use its comments where they help and read them critically:
it can be wrong in both directions.

### Where difficulty comes from

Use these sources, from cheapest to build to dearest:

- **Conflicting but resolvable sources.** An older figure in the data file and a later
  instruction in the context file that changes it. The agent has to decide which one governs.
- **A step hidden in a field people skim.** A status, effective date, flag or basis column
  that real exports carry anyway, where one value changes how a row is treated.
- **A candidate set to eliminate.** Several items that look eligible, each wrong one excluded
  by a different property only the files reveal.
- **The answer the requester does not want.** Files that support a breach, a decline, a
  restatement or a write-down. An agent that tells the requester what they hoped for fails
  in a way anyone can grade.
- **Branching.** A later fact that forces the agent to revise an earlier assumption.

Volume is not difficulty. More rows or more line items add build time and no judgment. Keep
the data small enough to verify by hand and spend the effort on the decision [D8].

Trap shapes that make strong models fail, in general form:

- **A convention mismatch.** The counterparty or the export measures one way (ship date, posting
  date, gross), the governing document another (invoice date, delivery date, net), and the
  difference is stated once, in passing.
- **An effective date.** An amendment changes a rate or an eligibility rule from a date, and the
  system or a prior figure does not reflect it, or reflects it late.
- **Records that belong to another period.** A credit dated after period end that relates to an
  invoice inside it; a migration that silently dropped a month.
- **Raw-export noise that changes a figure.** An exact duplicate, a reversal and rebill, a line
  in an excluded category.
- **A later instruction that overrides the printed terms, but only on what it addresses.**
- **A relationship visible only in the details.** A shared address or surname that makes a
  reference a related party; the applicant's own ledger contradicting its certification.
- **Thresholds crossed only after the corrections.** A cap that binds, a tier that one candidate
  clears and another just misses.
- **Dates computed, not read.** A deadline from a document date plus a window, in business days,
  across a holiday.
- **Decoys.** A one-off spike, a reading outside the window, a claim on a day with no event.
  Models over-flag these.
- **The headline flips.** Once the details are worked, the obvious "approve as stated" or "pay
  as promised" is wrong.

### Discard early

- Anything answerable from general knowledge or the prompt alone.
- Extraction dressed up as analysis: pulling values into a table [D7].
- One simple task repeated across several items [D7].
- A scenario that needs a current external figure the files do not carry [I2].
- Work you have not done yourself [D1].
- A near-copy of an earlier task in `tasks/` [D11].

## Stage 2: the two input files (Steps 6 to 8)

### Describe them (Step 6)

The File Builder writes the files from your descriptions, so the descriptions are the design.

- **Data file.** The format (CSV, workbook, export), the key fields and rows, the realistic
  inaccuracies to include and where. Give the actual figures from your correct-answer script
  so the File Builder does not invent its own.
- **Context file.** The document type (an email chain, meeting minutes, a policy note, a call
  note), who writes it to whom, and the facts that make the judgment call possible.

Say what the file contains. Never ask the File Builder to "include a hidden error the analyst
must catch" in words it might copy into the file. Generated files tend to annotate their own
planted issues ("Note: this figure is outdated"), and that annotation leaks the answer [I5].

### Build, download, check, edit (Steps 7 and 8)

### Make the documents read as real

Reviewers reject files that read as generated, and an agent treats a tidy file more kindly than
a raw one. What real documents carry:

- **A system export:** a run header (company, account, date range, run time, user), status codes,
  terse lowercase memos ("cb reversal dsp-207561"), and the noise real systems leave in, such as
  a reversal next to the item it reverses. Exact cents, never float tails.
- **An email thread:** a print header ("Printed from Outlook by IC, most recent first"), full
  From, Sent, To, Cc, Subject and Attachments lines, signatures with title and company, replies
  that refer to calls and attachments, and an ordinary register with an occasional typo.
- **A policy or agreement:** the document name and number, an adoption or amendment line,
  numbered clauses (6.2, 11.4(a)) with cross-references, and rules written in general terms, never
  around the case.
- **Enough length to be real.** A thread, memo or policy of a few dozen words reads as a stub.
  Extend it in the writer's own voice, with no new rules [I13].

Carry each planted issue in passing: a housekeeping aside ("the new rate card went live on the
22nd, sorry it reached us late"), a footnote stating a convention, a ledger line, a shared
address. Never as a warning or a note to the reader [I5, T18].

Every value, name, date and term the correct answer uses must be in one of the two files. A
document the answer depends on, such as an amendment, is quoted or attached as text, not only
mentioned [I15]. And the only contradiction anywhere in the files is the planted one [I16].

### Download and check

Download the two files one at a time into `inputs/`, not the whole archive (it holds the File
Builder's run records). Then:

```
python3 tools/alchemy_check.py tasks/NN-slug --only inputs
```

Fix every ERROR. Read every WARN. Then read both files in full against the Stage 1 design:

- Every figure matches the correct-answer script, except the planted issue [I9, I10].
- The planted issue is present, plausible, and resolved by the other file [I4].
- Nothing explains the answer, flags the issue or addresses whoever reads it next [I5, T18].
- Names, dates, amounts and reference numbers agree across files [I9].
- No placeholders, no real firms, no PII [I8]. Generated files have used a `.example` email
  domain.
- No 555 numbers, no weekday that the calendar contradicts, no column of perfectly round
  figures [I11].
- The Word file's properties (File > Info, or `docProps/core.xml`) carry no generator text. A
  File Builder thread has come back with "generated by python-docx" in its description field;
  clear it [I12].
- Each document reads like the real thing: an email has a sender and a date, a policy has a
  section number, an export has the column names a system would use [I3].

Small fixes are made by hand. If the changes are large, revise the descriptions and run the
File Builder again. Then build and check the ZIP:

```
python3 tools/alchemy_check.py tasks/NN-slug --zip
```

Upload `inputs.zip`. Its only top-level folder is `inputs/`, holding exactly the two files [I14].

## Stage 3: the prompt (Step 9)

Write the handoff a professional would give a trusted colleague who knows the domain:

- Open on the event, the deadline and whose decision it is: "the agreement ended on
  September 30, and Darren has promised their CFO a figure by Friday" [P11].
- Two to six sentences, 10 to 180 words [P1, P2].
- Name the input files inside the story and the output files by name. Never pair a file name
  with a description of what it holds [P13].
- Say what the deliverable has to survive: "a figure I can defend if their CFO questions it".
  Where an adjustment could cut against the requester, one line says it counts too: "if anything
  works in their favor, it goes in the number" [P14].
- A single generic caution is fine when a real person would say it ("it is straight off the
  system, nobody has scrubbed it"). Naming the defect is not [P8].
- The situation in a clause, the deliverable named by type, and the decision or deadline it
  feeds [P3, P11].
- What to produce, never how. No steps, no section outline, no "make sure" stack [P7].
- No hint about the planted issue, no "one of the files may be outdated" [P8].
- No role-play, no greeting or sign-off, no long background [P4, P5, P6]. Background lives in
  the context file.
- No request to look something up [P10].
- Complete enough that the agent neither refuses nor asks a question [P9]. Hidden requirements
  are a prompt defect, not difficulty.

```
python3 tools/alchemy_check.py tasks/NN-slug --only prompt
```

Fix every ERROR, read every WARN, then read the prompt aloud. If a sentence exists only to sound
like a person, delete it.

## Stage 4: the rubric (Step 10)

Run the Rubric Drafter once the ZIP is uploaded and the prompt is in. Copy its five criteria
into `rubric.md` before doing anything else: generating again replaces all five.

Then rewrite each criterion against `rubric-standard.md` and the correct-answer script. At
least one criterion catches the targeted failure directly; the rest cover the other material
points that could make the answer wrong [R10]. Check every value against the files, then check
again [R11].

```
python3 tools/alchemy_check.py tasks/NN-slug --only rubric
```

Paste the final five back into the form.

## Stage 5: the Attempting Agent (Step 11)

Before clicking Run Task, record the fingerprint of what the agent is about to see:

```
python3 tools/alchemy_check.py tasks/NN-slug --fingerprint
```

Copy `templates/run.md` to `runs/run-N.md` and put the fingerprint in it. When the run finishes
(allow up to 15 minutes), paste the final response into the run file unedited, then open the
sandbox snapshot and download every output file into `runs/run-N/`. Read every output file,
not only the chat reply. The failure is usually in the workbook, not the summary.

| What the run shows | Next |
| --- | --- |
| A refusal, a clarifying question, or a misread of the deliverable | Prompt defect [P9]: fix the prompt, delete the run, run again |
| A stall or an error | Refresh; if it persists, ask in the project chat before changing the task |
| A substantive error matching or beating the failure plan | Stage 6 |
| The correct answer | Stage 7 |

## Stage 6: the Grading Agent (Step 12)

Click Grade Selected and record each criterion's result in the run file as
`Criterion N: PASS` or `Criterion N: FAIL`. Then compare the Grading Agent's verdicts with your
own reading of the output files. If it passed a criterion the output fails, or the reverse, the
criterion is unclear or not self-contained [R3, R4]: rewrite it and grade again.

At least one criterion must fail on a current run [A1]. If none does, go to Stage 7.

## Stage 7: hardening, when the agent passes

Note in `task.md` what the agent handled correctly. Those traps are spent. Then use one
lever at a time, re-running after each meaningful change:

- Add a thread the agent must weigh: a second message in the context file that changes one
  condition.
- Add realistic mess: a superseded figure kept in the export, a mislabelled column, a late
  correction.
- Move the decision from lookup to judgment: the rule needs interpreting, not applying.
- Add a branch: a fact near the end of the context file that forces revising an early
  assumption.
- Add a red flag a domain expert would notice and a generalist would not.

Never bury the key fact where a professional could not find it, and never declare an answer
the files do not support [D8].

Any change to the prompt or the files makes earlier runs stale. Delete them on the platform and
run again. The checker reports a stale run as an A3 ERROR.

If the time limit is close and the agent still passes every criterion, use the escape hatch:
tick the box, describe what was tried, and write `**Escape hatch:** yes` in `task.md` [A8].

## Stage 8: the failure description (Step 13)

Write 50 to 350 words [A4] that a reviewer can verify without rerunning anything. An LLM may
draft it, but only from the actual run, its output files and the source files; every figure and
quote is checked against them:

- What the agent did wrong or failed to do, with its figure or a short quote from its output.
- The evidence in the source files and the correct expected result, with the file named [A6].
- The rubric criterion numbers that capture the failure [A5].
- Why the error makes the deliverable incorrect, unusable or meaningfully less useful [A7].

```
python3 tools/alchemy_check.py tasks/NN-slug --only failure
```

## Stage 9: final check and submit (Step 14)

Run everything and walk `audit.md`:

```
python3 tools/alchemy_check.py tasks/NN-slug
```

The ZIP, the prompt, the run on record, the rubric and the failure description must all
describe the same task. Tick the ready-to-submit box, then record the actual time spent from the
Log (the form's bands are under 2 hours, 2 to 4, and 4 to 6). Feedback is optional and may be
LLM-drafted from your notes. Submit, and add a dated line to the Log in `task.md`.

## Phase 2 and the full task

After a Phase 1 task is accepted, Phase 2 builds the gold-standard answer and a rubric of at
least 20 criteria. The correct-answer script from Stage 1 is where the gold-standard answer
starts. Check the larger rubric with `--full`. Address reviewer feedback in the task folder
first, with a dated entry under Revisions saying what changed and why.

## Revising a task

A task keeps its number and folder across rounds. Before changing the prompt or files, copy the
round's `prompt.md`, `rubric.md` and `inputs/` to `history/rN/`, and add a dated entry under
Revisions in `task.md`: the reason, what moved and what was kept. The difficulty moves to what
the agent missed; the traps it caught are spent.
