# Alchemy Starter Project: consolidated instructions and guidelines

This file consolidates the trainer instructions and guidance from the First Steps page and Lessons 1-7. It is a working reference for building the Starter Project.

## Time and workflow

- Estimated total time: about 4 hours.
- Suggested split: about 1 hour for the seven lessons and about 3 hours for the Starter Project.
- Maximum reportable time: 6 hours.
- Task timer: 48 hours; breaks are allowed.
- The Starter Project is a small version of a real Alchemy task, built from start to finish and tested against a weak AI agent.
- Read all instructions before starting, work iteratively, and save work locally.
- Ask in the project chat first if you need help. Read earlier messages, then state the section or step and what you already tried.
- The trainer has 9 sections: the instruction page, 7 lessons, and the Starter Project. Use the arrow controls at the bottom to move between sections.
- In each lesson, answer the learning questions, reveal the correct answer, and read the explanation. A correct answer reveals the next section.
- Do not click **Submit** until all sections are complete. An accidental click does not submit the work until every section's questions have been answered.

## What you are building

The Reinforcement Learning Environment (RLE) consists of:

1. A short LLM-assisted prompt.
2. Input files containing the complete work context.
3. A rubric with precise pass/fail criteria.

For the Starter Project, the training says to create two input files and five rubric criteria.

## Glossary

- **Severe failure:** A model failure with real-world consequences: an output a professional would not accept from a colleague.
- **Trajectory:** A complete record of one agent run, from reading the prompt and files through producing the final deliverable. It shows where the agent succeeded or failed.
- **Atomic:** A rubric criterion that checks exactly one thing, so a grader can mark it right or wrong without untangling multiple claims.
- **Reinforcement Learning Environment (RLE):** The package consisting of the prompt, input files, and rubric.

## Phase 1: design and test the task

1. Choose a realistic work task from your professional domain.
2. Design a scenario a competent professional could complete without step-by-step instructions.
3. Create two realistic input files for the Starter Project.
4. Write a 2-6 sentence prompt as a direct handoff to a trusted colleague.
5. Make the prompt produce one or more output files. A chat response alone is not enough.
6. Run the model from inside the browser and look for severe, valid failures.
7. If the model succeeds, increase the difficulty using the levers below and run it again.
8. Submit Phase 1 with the prompt, input files, model runs showing severe failures, and a description of the correct response.

Do not build the gold-standard answer or final rubric in Phase 1. You may use an LLM to draft, revise, and refine the final prompt.

## Phase 2: build the answer and rubric

After Phase 1 review and acceptance:

1. Review and fix the task, including reviewer feedback.
2. Create the gold-standard answer, which is the expert answer to your prompt.
3. Write the grading rubric used to evaluate model attempts.
4. Submit the answer and rubric as the Phase 2 follow-up.

Start Phase 1 only if you will also have time for Phase 2. The task is usable for training only when the answer and rubric exist.

## Input-file rules

Input files are the agent's entire world. The agent has no web access.

- Include every fact needed for the assignment in the files.
- Use two files for the Starter Project.
- Spread important information across the files so the agent must synthesize them.
- Use realistic work documents and formats, such as an email, memo, contract, dashboard, meeting note, or prior draft.
- Include realistic mess: imperfect file names, outdated or superseded material, gaps, typos, and uneven formatting where appropriate.
- Do not add a document that explains the answer or tells the agent what to notice.
- State facts rather than conclusions.
- Cross-reference other files only where a real workplace document would.
- Use realistic names and file names. Avoid placeholders, PII, and real client or company names.
- Verify every file and make sure numbers tie out and the content reflects your professional domain.
- Do not make the task a simple lookup or extraction exercise.

## Prompt rules

- Keep the final prompt to 2-6 sentences.
- Write it like a real handoff to a knowledgeable colleague.
- State the deliverable and scope without prescribing every step.
- Do not explain the agent's role, such as “you are an accountant.”
- Move background, constraints, and reference information into the input files.
- Do not make the prompt unclear by withholding information.
- If the agent refuses or asks clarifying questions, fix the prompt.
- Re-run the model after every meaningful change to the prompt or input files.
- Enter the final version in the **Your Final Prompt** field.

## What makes a strong task

A strong task has:

- Information spread across documents.
- Later steps that depend on earlier decisions.
- A judgment call whose answer is not stated directly in one file.
- A realistic workflow a qualified professional would recognize.
- One defensible answer supported by the files.
- A meaningful failure mode that requires professional judgment.

Difficulty should come from expertise, synthesis, causal reasoning, conflicting but resolvable sources, edge cases, and branching work. It should not come from irrelevant files, hidden clues, manufactured ambiguity, or a task that a professional could not answer either.

## Severe failures

A severe failure has real-world consequences. It is an output that would take significant time to fix, be unusable or embarrassing at work, or be wrong on a task a real professional would get right.

Examples include:

- A calculation error that cascades into later results.
- A missed edge case that changes the outcome.
- Failure to synthesize information across documents.
- Misclassification of a key item that changes the recommendation or downstream numbers.
- Choosing the wrong source when documents conflict.

Refusals, clarifying questions, formatting differences, minor cosmetic issues, and small mistakes a follow-up would fix are not severe failures.

## Difficulty levers

If the task is too easy, use one or more of these:

- Add context, such as another thread the model must weigh.
- Add realistic workplace mess.
- Add objective professional judgment where expertise, not lookup, determines the answer.
- Add branching or a later fact that requires revising an early hypothesis.
- Require causal reasoning or reasoning from different perspectives.
- Add a red flag that a domain expert would notice.

Do not bury key information in hard-to-find places. Do not declare one answer correct when the files do not objectively support it.

## Rubric rules

The rubric is the answer key. A grader sees only each criterion and the agent's final response and output files.

Each criterion must be:

- **Generalizable:** accepts any correct response, not only your example.
- **Clear:** has one reasonable interpretation.
- **Atomic:** checks one requirement only.
- **Self-contained:** includes the facts and values needed to grade it.
- **Comprehensive:** covers every material point that could make the answer wrong.

Write each criterion as subject + verb + expected value or decision. Include actual values. Avoid vague phrases such as “the correct rate,” “adequately addresses,” “staffs the team correctly,” or “the appropriate plan.” Avoid predictions such as “the model will fail.” Omit cosmetic requirements.

The full Alchemy task needs at least 20 criteria. The Starter Project uses five criteria. Check every criterion against the files, then check again.

## Final checks before submission

- The prompt is 2-6 sentences and may be drafted and refined with an LLM.
- The two input files contain all required facts and no PII or real client/company names.
- The task requires a deliverable file, not only a chat answer.
- The model runs reflect the final prompt and input files.
- At least one model run shows a clear, severe failure.
- The correct answer is objectively supported by the files.
- The five Starter Project rubric criteria are specific, atomic, self-contained, and testable.
- The gold-standard answer and rubric are not submitted as Phase 1 materials.
