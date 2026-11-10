# Alchemy training: questions and answers

## Lesson 1: What is Alchemy?

### 1. What is the goal of Alchemy?

**Answer:** Create realistic tasks where state-of-the-art models produce a meaningfully wrong output, the kind of output you would not accept from a colleague.

### 2. Which task is most valuable for training?

**Answer:** A realistic task that a competent professional would handle correctly, but the model gets meaningfully wrong.

### 3. What does “environment” refer to?

**Answer:** The prompt, input files, and rubric you build.

## Lesson 2: Project phases

### 4. What are you submitting in Phase 1?

**Answer:** A complete, tested task: the prompt, input files, model runs showing severe failures, and a description of what a correct response looks like.

### 5. What are you submitting in Phase 2?

**Answer:** The gold-standard answer to your own task, plus the grading rubric.

### 6. Should you start Phase 1 only if you will also be available for Phase 2?

**Answer:** True.

## Lesson 3: Building a task

### 7. Which scenario is stronger?

**Answer:** A revenue-operations analyst is handed a disputed Q3 commission run and finds a mid-quarter territory realignment was never applied, one enterprise deal credited to two reps, and a missed clawback for a cancelled contract.

### 8. What is the best way to make a task harder for the AI agent?

**Answer:** Include documents that appear to disagree, such as an outdated budget alongside a newer memo with revised numbers, where the agent must determine which one governs.

### 9. What is wrong with five independent vendor-contract expiration reviews?

**Answer:** It is one simple task repeated five times, not a complex task with sequential dependencies.

## Lesson 4: Creating input files

### 10. Is it acceptable to require the agent to look up the current IRS standard mileage rate on the IRS website?

**Answer:** No. The agent has no web access. Anything the task needs beyond standard professional knowledge must be included in the input files.

### 11. What is wrong with extracting every deductible, copay, and enrollment deadline from an 80-page benefits guide?

**Answer:** It is information extraction disguised as analysis. The agent can locate values and place them in a table without using professional judgment.

## Lesson 5: Writing the prompt

### 12. The agent keeps asking clarifying questions during testing. What should you fix?

**Answer:** The prompt. A refusal or clarifying question is a prompt problem, not a model failure.

### 13. Which GASB 34 prompt is better?

**Answer:** “Prepare the district's GASB 34 conversion for governmental funds for fiscal 2025. Provide the two required reconciliations between the fund financial statements and the government-wide statements.”

### 14. Which workforce-plan prompt is better?

**Answer:** “Prepare the Q3 workforce plan for the support organization, including revised headcount by team and the backfill schedule.”

### 15. Which change requires a model re-run?

**Answer:** A change to the prompt or input files that could change what a correct response looks like.

## Lesson 6: Designing the rubric

### 16. Does “the output should be accurate” give a clear grading signal?

**Answer:** False.

### 17. Which is the better rubric criterion?

**Answer:** “The revised staffing plan reports a Q3 support headcount of 47 FTE, after removing the duplicated seasonal-hire request.”

### 18. What is wrong with “The response should identify the correct root cause and produce an appropriate corrective-action plan”?

**Answer:** It does not name the specific root cause, define “appropriate,” or state what the corrective-action plan must contain. A grader could not use it to check the work.

## Lesson 7: What is difficult for models?

### 19. Which is a good source of difficulty?

**Answer:** Parallel threads the model must hold open and weigh together before reaching a conclusion (branchiness).

### 20. Which grader-report finding is a severe failure?

**Answer:** The agent misclassified a key item, which changed the recommendation and the downstream numbers.

### 21. The task is too easy. Which lever should you use?

**Answer:** Add more objective professional judgment: decisions where expertise, not lookup, picks the answer.
