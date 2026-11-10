# Rules

Every rule has an id, a one-sentence statement and a note on how it is checked. **coded**
means `tools/alchemy_check.py` detects it (ERROR blocks, WARN needs a read). **read** means
only a person reading the files catches it. **procedural** means it is a step in the workflow,
not a property of a file. A coded check is a net, not a judge: a clean run is the floor.

The platform's own text sits behind every rule here: `../requirements.md`,
`../training/project-guidelines.md`, `../training/faq.md` and
`../training/starter-project-form.md`. On any conflict, the training text wins and the rule
here is corrected the same day.

## D: Design

| Id | Rule | Check |
| --- | --- | --- |
| D1 | The task is realistic work in a finance domain from the eligible list in `../requirements.md`, done by the fictional role described in Step 1. The role's responsibilities match what that job really does. Teaching and training work is excluded. | read |
| D2 | A competent colleague could do it from the files without a step-by-step recipe. | read |
| D3 | The files support one defensible answer. A professional reading them reaches the same conclusion. | read |
| D4 | The answer turns on a judgment call that no single file states. | read |
| D5 | Information is spread across both files, so the answer needs both. | read |
| D6 | Later steps depend on an earlier decision, so one wrong call carries into the downstream numbers. | read |
| D7 | Not a lookup or extraction exercise, and not one simple task repeated several times. | read |
| D8 | Difficulty comes from expertise, synthesis, conflicting but resolvable sources, edge cases or branching. It never comes from irrelevant material, hidden clues, manufactured ambiguity, or a question a professional could not answer either. | read |
| D9 | The targeted failure is severe: a professional would not accept the output from a colleague, and fixing it takes real time. | read |
| D10 | Size: the Starter Project fits about three hours of work and is reported at no more than six. | procedural |
| D11 | Not a minor variation of an earlier task in `../tasks/`. | read against the folder |

## I: Input files

| Id | Rule | Check |
| --- | --- | --- |
| I1 | Exactly two files: a data file and a context file. | coded, ERROR |
| I2 | Every fact the work needs is in the files. The agent has no web access, so nothing depends on a lookup beyond standard professional knowledge. | read |
| I3 | Realistic document types and file names. Not `data_file.csv`, `input1.docx` or `sample.xlsx`. | coded WARN on generic names, then read |
| I4 | Realistic mess where the scenario calls for it: a superseded figure, a typo, a gap, uneven formatting. Each planted issue is one the correct answer resolves. | read |
| I5 | No file explains the answer or tells the agent what to notice. No annotation that flags the planted issue, no "correct figure is" line, no project or evaluation vocabulary. | coded, ERROR on project vocabulary; WARN on signposting phrases, then read |
| I6 | Files state facts, not conclusions. | read |
| I7 | Files cross-reference each other only where a real workplace document would. | read |
| I8 | No PII, no real client or company names, no placeholders. | coded: ERROR on ID-number shapes and placeholder text, WARN on well-known firm names and personal email domains, then read |
| I9 | Names, dates, amounts, account numbers and reference numbers agree across both files, except where a disagreement is the planted issue. | read |
| I10 | Numbers tie out: totals equal their parts, except where a mismatch is the planted issue and is noted in `task.md`. | coded WARN on CSV and workbook total rows, then read |
| I11 | No fabrication tells: 555 phone numbers, weekday and date pairs the calendar contradicts, a numeric column with no variance, float residue such as 0.30000000000000004, em dashes, the prose tells in `llm-prose-tells.md`. | coded, WARN |
| I12 | No hidden content: hidden sheets, rows or columns, cell comments, tracked changes, or a generator library named as the file's author. | coded, WARN |
| I13 | Each file has enough substance to be used. No empty file and no thin stub. | coded: ERROR when empty, WARN under 60 words |
| I15 | Every value, name, date and term the correct answer uses is in one of the two files. A document the answer depends on (an amendment, a policy clause) is present as its own text, quoted or attached, not only described. | read |
| I16 | The only contradiction inside or between the files is the planted one. Accidental mismatches (a total that does not sum, a date that disagrees with the thread, a signature date after the email that sends it) are fixed. | read |
| I14 | The upload is one ZIP whose only top-level folder is `inputs`, holding exactly the two files, with no File Builder run records and no system files. | coded, ERROR |

## P: Prompt

| Id | Rule | Check |
| --- | --- | --- |
| P1 | Two to six sentences. | coded, ERROR |
| P2 | Ten to 180 words (the form's limits). | coded, ERROR; WARN above 150 |
| P3 | It asks for one or more output files and names them by type. A chat answer alone is not a deliverable. | coded WARN when no file type is named, then read |
| P4 | No role-play: never "You are a...", "As a ..., you", "Act as". | coded, ERROR |
| P5 | No email formatting: no greeting line, sign-off or subject line. | coded, ERROR |
| P6 | No long background. Background, constraints and reference facts go into the files. | coded WARN on more than two paragraphs or a sentence over 45 words, then read |
| P7 | What, not how: no numbered procedure, no outline of sections, no stack of "make sure" requirements. | coded WARN, then read |
| P8 | Nothing that reveals the answer: no pitfall warning, no hint that a file is outdated, no derived figure handed over as a given. | coded WARN on warning phrases, then read |
| P9 | Clear enough that the agent neither refuses nor asks a question. A refusal or a clarifying question is a prompt defect, not a failure. | read, then confirmed by the run |
| P10 | No request for a web lookup or a "current" external figure. | coded, WARN |
| P11 | Reads as a direct handoff to a trusted colleague who knows the domain. | read |
| P12 | No project or evaluation vocabulary (rubric, grader, LLM, AI, agent, the project name). | coded, ERROR |
| P13 | The inputs are named inside the story, and no file name is paired with a description of what the file holds. Naming no input at all is also a defect. | coded, WARN |
| P14 | The prompt says what the deliverable has to survive (a challenge from the counterparty, a committee, an audit), not how to build it. Where an adjustment could cut against the requester, one line says it counts too. | read |

## M: Sentence mechanics

These apply to the prompt, both input files, the rubric and the failure description.

| Id | Rule | Check |
| --- | --- | --- |
| M1 | Zero em dashes. Use a comma, colon, semicolon, parentheses or a new sentence. | coded, ERROR (WARN inside input files) |
| M2 | A comma before and, but, so, or, yet when it joins two independent clauses. | coded, WARN (heuristic) |
| M3 | Never three independent clauses in one sentence. | coded, WARN (heuristic) |
| M4 | No comma splice. | coded, WARN (heuristic) |
| M5 | The serial comma in every list of three or more. | read |
| M6 | Complete sentences. No fragments standing as headings inside prose. | read |
| M7 | No spelling or grammar errors. | read |

## T: Prose tells

The catalog with examples and fixes is `llm-prose-tells.md`. These ids are the ones the script
reports.

| Id | Shape | Check |
| --- | --- | --- |
| T1 | Tautology: "X is X", "X is still X", "is the whole story". | coded, ERROR |
| T2 | Slogan or aphorism standing as a sentence. | coded WARN on known phrases, then read |
| T3 | Idiom or metaphor in place of a quantity or a fact. | read |
| T4 | Negative parallelism: "not just X but Y", "not only X but also Y". | coded, WARN |
| T5 | "It's not X, it's Y" contrast. | coded, WARN |
| T6 | A simple verb avoided: serves as, stands as, boasts, showcases. | coded, WARN |
| T7 | Sycophancy: "great question", "happy to help", "absolutely!". | coded, ERROR |
| T8 | Pre-counted list: "there are three key factors". | coded, WARN |
| T9 | Hedging filler: "it is worth noting", "it is important to consider". | coded, WARN |
| T10 | Clinical or corporate vocabulary: utilize, leverage the data, robust, holistic, facilitate, delve, in order to. | coded, WARN |
| T11 | Three or more sentences in one paragraph opening on the same two words. | coded, WARN |
| T12 | A run of six or more bullets of near-identical length. | coded, WARN |
| T13 | The semicolon-balanced maxim: "X is a policy; Y is an insult." | coded, WARN |
| T14 | A scene-setting fragment opening a paragraph, or urgency acted out with props instead of stated. | coded WARN on short openers, then read |
| T15 | Rule-of-three padding. | coded WARN on density, then read |
| T16 | The same quantity renamed in every sentence. Repeat the noun. | read |
| T17 | A place or object standing in for the document ("what goes on the door" for the posted list). | coded WARN on the "what goes on the" shape, then read |
| T19 | Self-describing text: "this document contains", "the sections that follow", "yellow cells are the inputs". | coded WARN inside input files, then read |
| T18 | Annotation voice in an input file: "Note:", "Important:", "Key takeaway", bolded asides addressed to whoever reads the file next. | coded WARN inside input files, then read |

## R: Rubric

Read `rubric-standard.md` before writing the first criterion.

| Id | Rule | Check |
| --- | --- | --- |
| R1 | Five criteria for the Starter Project; at least 20 for a full task. | coded, ERROR (`--full` switches the band) |
| R2 | Atomic: one criterion checks one thing. | coded WARN on two sentences, semicolons and joined claims, then read |
| R3 | Self-contained: the criterion carries the value, name or decision it checks, because the grader sees only the criterion and the agent's response and output files. | coded WARN when no value, quote or named decision is present, then read |
| R4 | Clear: one reasonable reading. | read |
| R5 | Generalizable: any correct response passes. No mandated method, cell, tab, section order, wording or count (of actions, sections, figures) unless the prompt asked for it. | coded WARN on location, method and count phrases, then read |
| R6 | Shape: subject (the deliverable or the part of it) + verb + expected value or decision. | coded WARN on "the response should", "the model", "must", then read |
| R7 | No vague grading words (correct, appropriate, adequately, properly, reasonable, comprehensive) and no hedges (roughly, approximately, or equivalent, etc.). A tolerance is written as figures. | coded, WARN |
| R8 | No predictions of model behavior ("the model will fail to"). | coded, ERROR |
| R9 | No cosmetic criteria: font, color, bold, layout, tone, spelling. | coded, WARN |
| R10 | Comprehensive: every material point that could make the answer wrong has a criterion, and at least one criterion catches the targeted failure. | read |
| R11 | Every value in every criterion is checked against the files, then checked again. | procedural |
| R12 | No reference to material the grader cannot see: the gold-standard answer, "the input file", "as described in the context file". | coded: ERROR on gold-standard references, WARN on input-file references |
| R13 | No two criteria score the same thing, and each figure is asserted in one criterion only. | coded WARN on near-duplicate wording, then read |
| R14 | No grader instructions: "award partial credit", "credit is given for", "do not penalize". | coded, ERROR |
| R15 | Any basis a criterion states re-derives to its figure exactly. "$1,097.90, being 2% of $54,894.50" fails, because 2% of $54,894.50 is $1,097.89. | read, against the correct-answer script |
| R16 | Every part of the prompt's ask is graded by at least one criterion. | read |

## A: Attempt, grading and failure description

| Id | Rule | Check |
| --- | --- | --- |
| A1 | At least one Attempting Agent run fails at least one criterion, or the escape hatch is used and recorded. | coded from `runs/`, ERROR |
| A2 | The failure is substantive: not a refusal, a clarifying question, a misread of an unclear prompt, formatting or a typo. | coded WARN on those words in the failure description, then read |
| A3 | The run on record reflects the final prompt and input files. A run made before a change that affects the task is stale and is deleted. | coded by fingerprint, ERROR |
| A4 | The failure description is 50 to 350 words, drafted from the actual run and files. | coded, ERROR |
| A5 | It names the rubric criterion number or numbers that capture the failure, and those numbers exist. | coded: WARN when none, ERROR when out of range |
| A6 | It cites the evidence from the source files and the correct expected result. | coded WARN when no input file or figure is named, then read |
| A7 | It says why the error makes the deliverable incorrect, unusable or meaningfully less useful. | read |
| A8 | The escape hatch is used only when the maximum time is near and the agent still passes every criterion; the attempts are described. | procedural |

## Adding a rule

When a task comes back with feedback, or a run shows a pattern worth catching, add the lesson
here first with the date and what happened. Then code it in `tools/alchemy_check.py` if a
pattern can read it without catching ordinary English, and add a fixture to the script's
self-test so it keeps firing.
