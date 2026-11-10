# NN · Short title

<!-- Copy templates/ to tasks/NN-slug/. The sections down to Step 14 are the form, numbered as the form numbers them; fill them as the workflow reaches each step. Everything under "Working notes" is for this folder only. -->

**Status:** <!-- designing / files built / prompt drafted / rubric drafted / run N graded / ready to submit / submitted / revising -->

**Escape hatch:** no

## Step 1: Field and role

<!-- Step 1. Three or four sentences in the first person, natural and plain ("I'm a ... at ..., so most of my work is ..."): the finance domain, the role, and its day-to-day duties. The role and company are fictional; the duties must be real ones. No "fictional" label inside the text. -->

## Step 2: Scenario ideas

<!-- The three ideas from the scenario helper or an LLM, one line each, and whether the scenario below uses or adapts one. Ideas not used go to the hardening queue under Working notes. -->

## Step 3: Scenario

<!-- Step 3. First person, in the Step 1 role's voice: the situation, the work needed, and the deliverable ("One of our merchants ..., and I have to ..."). Run the prose checks on it. -->

**Scenario source:** <!-- Used or adapted one of the suggested scenarios / Developed a new scenario, with or without LLM assistance -->

## Step 4: Failure plan

<!-- Step 4. First person, in the Step 1 voice ("What I expect the agent to get wrong is ..."): the likely mistake, the correct professional judgment, and the consequence, with figures from the correct-answer script. Run the prose checks on it. -->

## Step 5: Plan review

<!-- The plan-review helper's verdict, each comment, and what was changed or kept and why. -->

## Step 6: Data-file description

<!-- Step 6. Format, data, key fields, the figures from the correct-answer script, and the realistic issues to include. Say what the file contains; never ask for a "hidden error the analyst must catch" in words the File Builder could copy into the file. -->

## Step 6: Context-file description

<!-- Step 6. Document type, who writes to whom, background, and the facts that make the judgment call possible. -->

## Steps 7 and 8: Input files

<!-- Download the two files one at a time into inputs/, renamed to the names the prompt uses. Then run `python3 tools/alchemy_check.py tasks/NN-slug --only inputs`, fix and re-check, and build the upload with `--zip`. Note what was edited by hand. -->

## Step 9: Final prompt

Copy the whole of `prompt.md` into **Your Final Prompt**.

## Step 10: Rubric

Copy the five criteria from `rubric.md`, in order.

## Steps 11 and 12: Attempting Agent run and grading

<!-- Each run is recorded in runs/run-N.md (fingerprint, grading lines, final response) with its output files in runs/run-N/. One line here per run: date, criteria failed, verdict. -->

## Step 13: Failure description

<!-- Step 13. 50 to 350 words, from the actual run and files: what the agent did, with its figure; the file evidence and the correct expected result; the criterion numbers; why the deliverable is unusable. -->

## Step 14: Time spent

<!-- The actual time spent, from the Log: Less than 2 hours / 2 to 4 hours / 4 to 6 hours. -->

## Step 14: Feedback and comments

<!-- Optional. May be LLM-drafted from notes on what helped, what was unclear and what could improve; or "Leave blank." -->

## Working notes

Reference only, not for the form.

## Correct answer

<!-- The worked answer, computed before any file exists: every figure, with the script or the arithmetic. Every rubric value comes from here. This is also Phase 1's description of the correct response. -->

## Design

**Requester and decision.** <!-- who hands this over, what it feeds, when -->

**Judgment call.** <!-- the point no single file states -->

**Dependency.** <!-- the early decision that moves later numbers -->

**Split.** <!-- what the data file carries, what the context file carries -->

**Planted issues.** <!-- each inaccuracy, where it sits, and which fact resolves it. A total that does not tie on purpose is listed here (rule I10). -->

## Hardening queue

<!-- Ideas held back for Stage 7, one lever per round. -->

## Checks

<!-- Paste the latest alchemy_check.py output. One line for each WARN kept, saying why. Tick the MANUAL rows. -->

## Runs

<!-- One line per run: date, fingerprint, criteria failed, what the agent caught and missed. Traps it caught are spent. -->

## Revisions

<!-- One dated entry per round after the first: the reason, what changed, what was kept. Earlier rounds live in history/rN/. -->

## Log

- YYYY-MM-DD: started
