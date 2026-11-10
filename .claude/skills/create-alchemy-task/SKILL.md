---
name: create-alchemy-task
description: Design and draft a new Alchemy Starter Project task in alchemy/tasks/NN-slug/ (the scenario's fictional field and role, scenario, failure plan, worked correct answer, the two input-file descriptions, the prompt and a rubric draft), following that project's training, rules and templates, and run its coded checks. Use it whenever the user runs /create-alchemy-task [requirement], or asks for a new Alchemy task, a starter project, a scenario for the Alchemy form, or the next Alchemy task, even without naming the command. For changing an existing task use revise-alchemy-task; for reading an Attempting Agent run use review-alchemy-run.
---

# Create an Alchemy task

`/create-alchemy-task [optional requirement]`

The project is `alchemy/` under the workspace root (the folder that holds `.claude/`). Work from
that folder so the tool paths resolve. Every rule lives in the project folder; this skill
follows those files rather than restating them.

The requirement, if given, constrains the task: a domain ("commercial lending"), a failure type
("wrong source when documents conflict"), or a difficulty note ("harder than 01"). With none,
pick from the user's field and the difficulty sources in the workflow.

## 1. Read the project, in full

In this order: `requirements.md`, `training/project-guidelines.md`, `training/faq.md`,
`training/starter-project-form.md` (the platform's text, which wins on any conflict), then
`README.md`, `docs/workflow.md`, `docs/rules.md`, `docs/rubric-standard.md`,
`docs/llm-prose-tells.md`, `templates/task.md`, and the docstring of `tools/alchemy_check.py`.

## 2. The field and role belong to the scenario

Step 1 of the form describes a fictional role for the scenario, in an eligible finance domain
(rule D1, `docs/workflow.md` Stage 0). Draft it in the first person, in a plain, natural
voice ("I'm a ... at ..., so most of my work is ..."): the domain, the role, and the
responsibilities and typical work that job really carries. Run the prose checks on it like any
other form text. If the user named a domain or role,
use it. The role is invented; its duties, documents and decisions must not be. Never present this
text as the user's own qualifications.

## 3. Learn what is spent

```
python3 tools/alchemy_check.py --list
```

Read each earlier task's Failure plan and its Runs notes. Traps an agent already caught are
spent (D11). Take the number from `python3 tools/alchemy_check.py --next`.

## 4. Design, and compute the answer first

Follow Stage 1 of `docs/workflow.md`: the requester and decision, the deliverable, the judgment
call no file states, the dependency, and the split between the data file and the context file.
Then compute every figure with a short Python script, and put the script's result in
`task.md` under Correct answer before anything else is written. The figures in the file
descriptions and the rubric come from that script and nowhere else.

Size it to the Starter Project: small data a person can verify by hand, one decisive judgment
(D8, D10).

## 5. Write the task folder

Copy `templates/` to `tasks/NN-slug/`. Fill in `task.md`: Field and role, Scenario (first person, in the
Step 1 voice, with the scenario source), Failure plan (first person too), both file descriptions, Correct answer, and Design with Planted issues. Write
`prompt.md` to Stage 3 of the workflow. Write `rubric.md` as a draft of five criteria to
`docs/rubric-standard.md`, marked in `task.md` as a draft to compare with the Rubric Drafter's
output later. Leave Failure description, Runs and Time spent empty with their comments. Never
invent a platform result.

The file descriptions say what each file contains, with the real figures. They never ask for a
"hidden error the analyst must catch" in words the File Builder could copy into the file.

## 6. Check

```
python3 tools/alchemy_check.py tasks/NN-slug --only prompt
python3 tools/alchemy_check.py tasks/NN-slug --only rubric
```

Fix every ERROR. Read every WARN and either fix it or note in `task.md` why it stands. Read the
prompt aloud once. Add a dated line to the Log.

## 7. Hand over

Report the folder, the targeted failure in one sentence, and the prompt's word and sentence
count. The user's next steps are on the platform: paste the Step 1, 3, 4 and 6 text, run the
helpers and the File Builder, and download the two files into `inputs/`. Then
`/review-alchemy-run NN` after a run, or ask for the inputs to be checked with
`python3 tools/alchemy_check.py tasks/NN-slug --only inputs`. Do not submit anything and do not
predict what the agent will do.
