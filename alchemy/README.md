# Alchemy

One job: build a realistic finance task (two input files, a short prompt and a rubric) that a
capable AI agent gets meaningfully wrong, prove it with an Attempting Agent run, and describe
the failure. The platform's own text is in `requirements.md` and `training/`. On any conflict
with the files below, the platform text wins.

## Layout

```
alchemy/
├── requirements.md              eligibility, phases, onboarding (platform, authoritative)
├── training/                    platform, authoritative
│   ├── project-guidelines.md    the trainer's instructions and Lessons 1 to 7
│   ├── faq.md                   the lesson questions and answers
│   └── starter-project-form.md  the Starter Project form, step by step
├── README.md                    this file
├── docs/
│   ├── workflow.md              the stages, mapped to the form's 14 steps
│   ├── rules.md                 every rule with an id; which are coded and which are a read
│   ├── rubric-standard.md       how to write criteria a grader applies the same way every time
│   ├── llm-prose-tells.md       the shapes that read as model-written, in prompts and in files
│   └── audit.md                 the pre-submission gate table
├── tools/
│   └── alchemy_check.py         the coded checks; run on every change
├── templates/                   copied to tasks/NN-slug/ to start a task
│   ├── task.md                  the form fields, then design, correct answer, checks, log
│   ├── prompt.md                the prompt alone, exactly as pasted
│   ├── rubric.md                the five criteria, numbered
│   ├── run.md                   copied to runs/run-N.md for each Attempting Agent run
│   ├── inputs/                  the two input files
│   └── runs/                    run records and the agent's output files
└── tasks/                       NN-slug/ folders, one per task
```

## The short version

1. Pick an eligible finance domain and a fictional role in it (Step 1), with duties that job
   really has. Pick a scenario in that role.
2. Design the judgment call and the targeted failure, then **compute the correct answer before
   any file exists**.
3. Describe the two files with the real figures, build them with the File Builder, download them
   into `inputs/`, and clean them: no leakage, no fabrication tells, everything ties out.
4. `python3 tools/alchemy_check.py tasks/NN-slug --zip`, then upload `inputs.zip`.
5. Write a 2 to 6 sentence handoff that names the deliverable file and gives no hints.
6. Draft the rubric, then rewrite all five criteria to `docs/rubric-standard.md`.
7. Record the fingerprint, run the Attempting Agent, save the response, outputs and grading in
   `runs/`.
8. If no criterion fails, harden one lever at a time and rerun. If one fails, write the failure
   description.
9. `python3 tools/alchemy_check.py tasks/NN-slug`, walk `docs/audit.md`, submit.

## Skills

| Command | What it does |
| --- | --- |
| `/create-alchemy-task [requirement]` | designs the next task folder: form text, correct answer, file descriptions, prompt and rubric draft, checks; stops where the platform takes over |
| `/review-alchemy-run NN` | reads the latest run and its output files against the correct answer, checks the grading, and writes the failure description, or says to harden |
| `/revise-alchemy-task NN [direction]` | archives the round to `history/`, moves the difficulty to what the agent missed, updates the files, prompt and rubric, reruns the checks |

`python3 tools/alchemy_check.py --list` shows where every task stands.

## Where to start

| If you want to... | Read |
| --- | --- |
| Run one task end to end | `docs/workflow.md` |
| Know whether a sentence, file or criterion is allowed | `docs/rules.md`, then `docs/llm-prose-tells.md` |
| Write or fix the rubric | `docs/rubric-standard.md` |
| Check before submitting | `docs/audit.md` |
| See what the script checks | the docstring at the top of `tools/alchemy_check.py` |
| Start a task | copy `templates/` to `tasks/NN-slug/`, with NN from `--next` |
