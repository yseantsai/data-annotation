# Pre-submission audit

One row per gate, in the order the form is filled. Walk every row against what was actually
built, after `python3 tools/alchemy_check.py tasks/NN-slug` shows no ERROR. The **Check** column
says how the row is caught: **coded** rows are reported by the script, **read** rows are not,
and each read row is a way a task gets returned.

The final check in Step 14 of `../training/starter-project-form.md` asks that the ZIP, the run,
the prompt, the rubric and the failure description agree. Section F is that check.

## A. Design

| Gate | Rules | Check | Pass when |
| --- | --- | --- | --- |
| Domain and role | D1 | read | An eligible finance domain; the Step 1 fictional role's duties are the ones that job really has, and the scenario sits inside them |
| Unaided | D2 | read | A competent colleague could do it from the files without a recipe |
| One answer | D3 | read | The correct-answer script gives one result the files support |
| Judgment | D4, D8 | read | The decisive call is not stated in either file and is not a hidden clue |
| Synthesis | D5, D6 | read | The answer needs both files, and one early decision moves the later numbers |
| Not lookup | D7 | read | No step is pulling values into a table |
| Severe | D9 | read | The targeted failure would be unusable or embarrassing at work |
| Fresh | D11 | read | Not a variation on an earlier task in `../tasks/` |

## B. Input files

| Gate | Rules | Check | Pass when |
| --- | --- | --- | --- |
| Two files | I1 | coded | Exactly a data file and a context file |
| Self-sufficient | I2 | read | Nothing the work needs is outside the files |
| Realistic | I3, I4, I6 | coded names, then read | Real document types and names; mess that the answer resolves; facts, not conclusions |
| No leakage | I5, T18 | coded, then read | No annotation, note or comment points at the planted issue; no project vocabulary |
| Clean identity | I8 | coded, then read | No PII, no real firms, no placeholders |
| Consistent | I9, I10 | coded totals, then read | Every name, date, amount and reference agrees across files, except the planted issue noted in `task.md` |
| No fingerprints | I11 | coded | No 555 numbers, false weekdays, round columns, float residue, em dashes |
| Nothing hidden | I12 | coded | No hidden sheets, rows or columns; no comments, tracked changes or speaker notes |
| Substantial | I13 | coded | No empty or thin file |
| Complete | I15 | read | Every value, name, date and term the answer uses is in a file; a document the answer depends on is present as text |
| One conflict | I16 | read | The planted conflict is the only one; no accidental mismatch inside or between files |
| ZIP | I14 | coded | `inputs/` is the only top-level folder; exactly the two files; matches the folder byte for byte |

## C. Prompt

| Gate | Rules | Check | Pass when |
| --- | --- | --- | --- |
| Size | P1, P2 | coded | 2 to 6 sentences, 10 to 180 words |
| Deliverable | P3 | coded, then read | Names the output file or files by type |
| Voice | P4, P5, P11, P12 | coded, then read | A handoff to a colleague: no role-play, no email shell, no AI or project words |
| Scope | P6, P7 | coded, then read | No long background, no procedure, no outline |
| No hints | P8 | coded, then read | Nothing points at the planted issue or hands over a derived figure |
| Askable | P9 | read, then the run | The agent neither refused nor asked a question |
| Offline | P10 | coded | Nothing to look up |
| Inputs named | P13 | coded | The inputs are named in the story; no file is glossed |
| Stakes | P14 | read | Says what the deliverable must survive; adjustments against the requester count |
| Mechanics and tells | M1 to M7, T1 to T17 | coded, then read aloud | No ERROR; each WARN fixed or noted |

## D. Rubric

| Gate | Rules | Check | Pass when |
| --- | --- | --- | --- |
| Count | R1 | coded | Exactly five (Starter); 20 or more with `--full` |
| Atomic | R2 | coded, then read | One check each |
| Self-contained | R3, R12 | coded, then read | Each carries its value, name or decision; nothing refers to unseen material |
| Clear | R4, R7 | coded, then read | One reading; no vague grading words |
| Generalizable | R5 | coded, then read | No mandated cell, tab, method or wording the prompt did not ask for |
| Shape | R6, R8 | coded | Subject + verb + expected value; no predictions |
| Not cosmetic | R9 | coded | No formatting or tone checks |
| Comprehensive | R10 | read | At least one criterion catches the targeted failure; every material point covered |
| Verified | R11 | procedural | Every value checked against the files twice; your correct answer passes all five |
| Distinct | R13 | coded, then read | No two criteria score the same thing; each figure appears in one criterion |
| No grader instructions | R14 | coded | Nothing addressed to the grader |
| Basis ties | R15 | read | Every basis written in re-derives to its figure exactly |
| Whole ask graded | R16 | read | Each part of the prompt's ask has a criterion |
| Two-question test | R10, R5 | read | Each criterion fails a wrong answer and passes any correct one (`rubric-standard.md`) |

## E. Run and failure

| Gate | Rules | Check | Pass when |
| --- | --- | --- | --- |
| Current | A3 | coded | The run on record carries today's fingerprint |
| Fails | A1 | coded | At least one criterion fails on a current run, or the escape hatch is recorded |
| Grader agrees | A1 | read | The Grading Agent's verdicts match your reading of the output files |
| Substantive | A2 | coded, then read | The failure is not a refusal, a question, a misread or formatting |
| Description | A4 to A7 | coded, then read | 50 to 350 words, drawn from the actual run; names the criteria, the file evidence, the expected value and why it matters |

## F. Agreement (Step 14)

| Gate | Check | Pass when |
| --- | --- | --- |
| ZIP = folder | coded (I14) | `inputs.zip` matches `inputs/` |
| Run = task | coded (A3) | The run fingerprint matches `prompt.md` and `inputs/` |
| Form = folder | read | The prompt, the five criteria and the failure description in the form are the ones in the folder, character for character |
| Story = files | read | Every figure in the failure description appears in the files, the run output or the rubric |
| Time | read | The time band is the actual time spent, from the Log in `task.md` |
