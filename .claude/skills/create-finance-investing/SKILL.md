---
name: create-finance-investing
description: Author a new Finance & Investing prompt task in finance-investing-prompt/ (a realistic prompt designed to make a frontier model fail, with design notes, a worked correct answer, and the coded self-check run), following that project's instructions, rules, and template. Use it whenever the user runs /create-finance-investing [requirement], or asks for a new finance prompt, a new task, the next task, or a new submission for the finance project, even without naming the command. For changing an existing task use revise-finance-investing-prompt; for grading a Generate response use review-finance-investing-result.
---

# Create a finance task

`/create-finance-investing [optional requirement]`

The project is `finance-investing-prompt/` under the workspace root (the folder that holds
`.claude/`). Its job is to produce one realistic finance or investing prompt that a
state-of-the-art model answers badly, so the response can be rated and the failure explained.
Every rule that matters lives in the project folder, and this skill follows those files rather
than restating them. Work from the project folder so the tool paths below resolve.

The requirement, if given, is a constraint on the task: a use case ("portfolio rebalancing"),
a topic ("lease accounting"), a difficulty note ("harder than 01"), or a trap to aim at. With
no requirement, pick the concept from the failure targets in the workflow and from what earlier
tasks have shown the model can already handle.

## 1. Read the project's rules, in full

In this order: `instructions.md` and `submission-form.md` (the platform's text, which wins on
any conflict), then `README.md`, `docs/workflow.md`, `docs/prompt-rules.md`,
`docs/llm-prose-tells.md`, and `templates/task.md`. Then the docstring at the top of
`tools/prompt_check.py`. These are short, and the submission is judged on their fine print:
the banned topics, the three-outcome test, the voice the prompt must have, the rule that a
model answering correctly on the whole sends the prompt back to design.

## 2. Learn what is already spent

```
python3 tools/task_status.py --list
```

Open each earlier task's `task.md` and read its Failure target and Outcome. The Outcome of a
graded task lists the traps the model handled; those are spent for this prompt family and the
new task must not rely on them (rule D5 and the uniqueness note in the instructions). A new
task may share a domain with an old one only when its trap and reasoning path are different.

Take the next sequence number from `python3 tools/task_status.py --next`.

## 3. Design before writing

Follow Stage 0 and Stage 1 of `docs/workflow.md`. The non-negotiable part is the worked correct
answer: compute every figure the scenario implies with a short Python snippet before the prompt
exists, so the trap is deliberate and the later review has something to grade against. A
scenario whose correct answer you have not computed is a guess, not a task.

Size the task to rule D8: the whole task, design through rating, fits in about three hours of
human work, so build one decisive question a practitioner answers in about an hour.

Prefer traps the model is likely to miss over traps it has shown it catches: what a buyer or
investor must actually pay or bring (working capital, fees, taxes), conventions it confuses
(day counts, compounding, pre- versus post-money, gross versus net, nominal versus real),
methods whose assumptions fail quietly, facts that conflict, and questions whose honest answer
is the one the requester does not want. Present facts as a person would, as raw figures and
quoted lines, never as the conclusion the solver should reach.

## 4. Write the task folder

Create `drafts/NN-slug/` by copying `templates/`:

- `prompt.md` holds only the prompt text, exactly as it will be pasted into the form.
- `task.md` holds the failure target, the design notes with the worked answer, the self-check
  record, and empty Generate response, Outcome, Rating and Explanation sections with a one-line
  note on what fills each. Never invent a platform result.
- `result.md` stays empty until the human pastes the Generate response into it.

Write the prompt in the voice `docs/prompt-rules.md` describes: the requester briefing a
colleague or an assistant, context woven in, stakes concrete, what to produce and never how,
zero em dashes, clean comma mechanics, none of the shapes in `docs/llm-prose-tells.md`.

## 5. Check, then read aloud

```
python3 tools/prompt_check.py drafts/NN-slug/prompt.md
```

Fix every ERROR. Read every WARN and either fix it or record why it stands. Walk the MANUAL
rows the script prints and tick them in `task.md` with a word on each. Rule S2 deserves a
second look every time: any sentence that draws the inference for the model ("so the fee is
not one-time") is removed, and the bare facts stay. Read the prompt aloud once; a sentence
whose only job is to sound like a person goes.

Add a dated line to the task's Log.

## 6. Hand over

Report the task folder path, the failure target in one sentence, the character count, and
that the human's next step is to paste `prompt.md` into the platform, click Generate, and save
the full response into `result.md`. Then `/review-finance-investing-result NN` grades it. Do
not submit anything and do not predict what the model will do.
