# Finance & Investing prompt project

One job: write a realistic, natural prompt in finance or investing that a state-of-the-art
model answers badly, test it with the project's Generate button, then rate and explain the
response. The platform's own text is in `instructions.md` and `submission-form.md`; on any
conflict with the files below, the platform text wins.

## Layout

```
finance-investing-prompt/
├── instructions.md          platform instructions (authoritative)
├── submission-form.md       platform form, field by field (authoritative)
├── README.md                this file
├── docs/
│   ├── workflow.md          the stages, from picking a failure target to the submitted form
│   ├── prompt-rules.md      every rule with an id; which are coded and which are a read
│   ├── llm-prose-tells.md   the sentence shapes that read as model-written, with fixes
│   └── spent-traps.md       every trap the model has caught or failed on, kept after a task is deleted
├── tools/
│   └── prompt_check.py      the coded checks; on every prompt before Generate, and on task.md (--task)
├── templates/
│   ├── prompt.md            the prompt alone, exactly as pasted into the form
│   ├── result.md            the Generate response, pasted unedited
│   └── task.md              design notes, self-check, outcome, rating, explanation, log
└── submissions/             NN-slug/ folders, one per submittable task, each holding prompt.md, result.md and task.md
```

## The short version

1. Pick a failure target: a place where models get finance wrong, not a topic you find interesting.
2. Design the scenario so the obvious answer is the wrong one, and sketch the correct answer first.
3. Write the prompt as a person briefing a colleague or an assistant. Context, stakes, the ask.
4. Run `python3 tools/prompt_check.py submissions/NN-slug/prompt.md` and fix every ERROR, then read every WARN. Run it with `--task submissions/NN-slug/task.md` on the task file whenever that file changes.
5. Read the prompt aloud. If it sounds like a product description or a test question, rewrite.
6. Generate. If the response is right on the whole, log what it caught in `docs/spent-traps.md`, delete the task, and create a new one.
7. Rate the response from what it actually says, write the explanation, and copy the fields into the form.

## Skills

Three slash commands drive the loop; each reads the files above rather than restating them.

| Command | What it does |
| --- | --- |
| `/create-finance-investing [requirement]` | designs and writes the next task folder, runs the checks, stops before Generate |
| `/review-finance-investing-result NN` | grades `result.md` against the task's worked answer and fills Outcome, Rating and Explanation; if the response is not submittable, logs the spent traps, deletes the task, and creates the next one |
| `/revise-finance-investing-prompt NN [direction]` | for a submitted task the platform returns, or a change you ask for: archives the round to `history/`, rewrites `prompt.md`, re-runs the checks |

`python3 tools/task_status.py NN` (or `--list`, `--next`) shows where any task stands.

## Where to start

| If you want to... | Read |
| --- | --- |
| Run one attempt end to end | `docs/workflow.md` |
| Know whether a sentence is allowed | `docs/prompt-rules.md`, then `docs/llm-prose-tells.md` |
| See what the script checks and why | the docstring at the top of `tools/prompt_check.py` |
| See which traps are spent | `docs/spent-traps.md` |
| Start a new task | copy `templates/` to `submissions/NN-slug/`; the prompt goes in `prompt.md`, everything else in `task.md` |
