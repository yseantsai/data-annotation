# Alchemy Starter Project: adapted practice template

This practice adaptation uses a fictional professional role and synthetic scenario. An LLM can draft and revise content for Steps 1-14. These local adaptations differ from the original form's authorship and experience requirements.

## Project scope

Build a small Alchemy task based on realistic work in a chosen professional domain. The Starter Project uses:

- Two input files.
- Five rubric criteria.
- A prompt that asks for one or more deliverable files.
- An Attempting Agent run that should contain at least one severe failure.
- A Grading Agent check against the rubric.

If you need help, use the project chat. State the step you are on and what you have already tried.

## Step 1: Describe the scenario's professional field and role

Choose a professional field and a fictional role for the scenario. Describe the responsibilities and typical work in enough detail to guide scenario generation.

**Field and role:**

> [Describe the chosen professional field, fictional role, and typical responsibilities.]

Example: “The scenario follows a developer at a fictional financial technology company who builds and supports software for payments and financial operations.”

## Step 2: Generate scenario ideas

Use an LLM or the scenario helper to generate three short, realistic work scenarios for the chosen domain. Choose one, combine ideas, or develop a new scenario. If the ideas do not fit, add more detail to Step 1 and generate again.

## Step 3: Describe your scenario

Describe the realistic professional task you want to build. It should be work a capable colleague could complete without a step-by-step recipe.

**Scenario:**

> [Describe the situation, the work needed, and the deliverable a professional would produce.]

**Scenario source:**

- [ ] Used or adapted one of the suggested scenarios
- [ ] Developed a new scenario, with or without LLM assistance

## Step 4: Describe the targeted failure

Use an LLM to draft the targeted failure plan. State the judgment call the Attempting Agent should get wrong and what a careful professional would do instead.

Target a severe failure: an error that makes the result unusable in the professional field. Formatting slips and minor typos do not count.

**Failure plan:**

> [Describe the model's likely mistake, the correct professional judgment, and the consequence of the mistake.]

## Step 5: Review the failure plan

Use the plan-review helper to assess whether the scenario is likely to make the Attempting Agent fail. Use its comments to revise the scenario or failure plan when useful. Review the suggestions yourself because automated suggestions can be wrong.

## Step 6: Describe the two input files

The File Builder creates two files from the scenario, failure description, and file descriptions:

1. **Data file:** contains the data needed to solve the task, including its format and key fields. The file should be complete enough to use, but it may contain realistic inaccuracies if the failure plan depends on a professional catching them. Describe the inaccuracies to include.
2. **Context file:** explains how to interpret the data. It can be an email chain, meeting minutes, call note, policy note, or similar workplace document. It should contain the context needed to make the judgment call.

**Data-file description:**

> [Describe the file format, data included, key fields, and any realistic issues the professional should catch.]

**Context-file description:**

> [Describe the document type, participants or source, relevant background, and how it guides interpretation of the data.]

## Step 7: Build and download the input files

1. Select **File Builder**.
2. Click **Run Task**.
3. Wait for the run to finish and read the reply.
4. Download both files from **Your files**.
5. Download the two files individually. Do not download the whole archive because it also contains File Builder run records.

## Step 8: Check and upload the input files

Open each generated file and verify:

- It is readable and usable.
- It targets the failure mode from Step 4.
- Names, dates, amounts, account numbers, reference numbers, and other identifiers are consistent.
- The correct answer can be derived from the files. A professional judgment may be required even if the answer is not stated verbatim.

Edit the files to correct mistakes. If the changes are substantial, revise the descriptions and run File Builder again.

When satisfied:

1. Put both files in a folder named `inputs`.
2. Make sure `inputs` is the only top-level folder in the archive.
3. Zip the `inputs` folder.
4. Upload the ZIP file.

## Step 9: Craft the prompt

Write a natural handoff to a trusted colleague who understands the domain and has the needed resources.

Prompt requirements:

- Use 2-6 sentences and at least 10 words.
- Clearly state the expected deliverable.
- Keep the request realistic and specific without becoming a step-by-step recipe.
- Avoid role-playing such as “You are a financial analyst.”
- Avoid email formatting, long background paragraphs, and instructions that reveal the answer.
- The Attempting Agent receives only the prompt and uploaded input files and cannot search the web.
- LLMs may draft, edit, and refine the prompt.
- The form accepts 10-180 words.

**Final prompt:**

> [Write the task handoff here.]

## Step 10: Draft the rubric

After the ZIP is uploaded and the prompt is written, run the Rubric Drafter. It reads the files, prompt, and plan and drafts five criteria. Generating again replaces all five criteria, so review the draft before regenerating.

The criteria should be specific, atomic, self-contained, generalizable, and comprehensive. Include expected values or decisions rather than vague quality labels.

## Step 11: Test with the Attempting Agent

1. Select **Attempting Agent**.
2. Click **Run Task**.
3. Allow up to 15 minutes for the run.
4. Open the completed run and inspect the final response.
5. Open the sandbox snapshot and inspect every output file the agent produced.

If a run stalls or errors, refresh the page. If the issue persists, ask in the project chat before changing the task.

If the agent refuses, asks for clarification, or misunderstands an unclear deliverable, fix the prompt. That is a prompt problem, not the target failure.

If the prompt or files change in a way that affects the task, delete the stale run and create a new run.

## Step 12: Check the Grading Agent

After the Attempting Agent run finishes, click **Grade Selected**. The Grading Agent checks the run against the five rubric criteria.

- The Attempting Agent should fail at least one criterion.
- If it passes every criterion, revise the task, files, prompt, or rubric and test again.
- Use the escape hatch only when you are approaching the maximum time and still cannot make the Attempting Agent fail a criterion. Check the box, describe what you attempted, and submit.

## Step 13: Describe the failure

Use an LLM to draft the most important substantive failure description from the actual run and files. Base the description on observed results and source evidence.

Include:

- What the Attempting Agent did wrong or failed to do.
- The source-file evidence and correct expected result.
- The rubric criterion number or numbers that capture the failure.
- Why the error makes the deliverable incorrect, unusable, or meaningfully less useful.

Examples of severe failures:

- An incorrect calculation that affects later numbers.
- A missed edge case that changes the outcome.
- Failure to synthesize information across files.
- Misclassification of an important item.
- Choosing the wrong source when documents conflict.
- Reaching an unsupported conclusion.
- Omitting a required part of the deliverable.

Minor issues do not count as the target failure, including formatting or style problems, misunderstanding an unclear prompt, a refusal, or a follow-up question instead of a response.

**Failure description:**

> [Draft 50-350 words and support the explanation with evidence from the run and files.]

## Step 14: Final check and submission

Before submitting, verify that these all agree:

- The ZIP file and its two input files.
- The Attempting Agent response and output files.
- The final prompt.
- The five rubric criteria.
- The failure description.

Confirm that you are ready to submit.

**Ready to submit:**

- [ ] I confirm that I am ready to submit.

## Time spent

Record the actual time spent working on the project.

- [ ] Less than 2 hours
- [ ] 2 to 4 hours
- [ ] 4 to 6 hours

## Feedback and comments (optional)

Use an LLM to draft feedback from notes about what helped, what was unclear, and what could improve.

> [Add feedback about the training or leave blank.]
