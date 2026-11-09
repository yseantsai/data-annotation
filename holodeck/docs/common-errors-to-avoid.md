# Holodeck Project - Common Errors to Avoid

*A reference guide for building realistic, challenging tasks*

This document collects the most common issues we've been seeing across Holodeck submissions. The goal is to help you spot and fix these before submitting.

The errors are grouped into four areas: how realistic your context files look, whether those files hold together under scrutiny, how the task itself is designed, and how the grading guidance pins down what "correct" looks like.

## 1. Context Files: Making Them Feel Real

*If the files read as synthetic, the task loses its signal. Graders and models can both spot generic, stock content in seconds. Build worlds that feel lived-in.*

### 1. Mismatched Generation Footers

"Generated on..." or "Created by [tool]" footers at the bottom of files often contradict the dates in the file itself. This makes the document feel synthetic on sight. Remove auto-generated footers, or make them consistent with the document's internal dates.

### 2. HTML Tags Leaking into Documents

Models attempting to bold cells in tables or format emphasis frequently leave raw tags like `<b>...</b>` or `<strong>...</strong>` in the output. Always scan the final file for stray markup, especially inside tables, which are the most common source.

### 3. Missing Letterheads and Real-World Formatting

Files lacking letterheads, headers, signature blocks, logos, or typical document structure read as fake immediately. A clinical note without a clinic header, an invoice without company branding, or a memo without a "From / To / Date" block all signal that something is off. Match the formatting conventions of the real-world document you're imitating.

### 4. Placeholder Data Giveaways

555 phone numbers, `@email.com` addresses, generic "John Doe" names, and stray Office lock files (`~$filename.docx`) all flag content as synthetic. Use realistic area codes for your fictional location, plausible-but-fake email domains, and clean out temp/lock files before submitting.

### 5. Files That Are Too Short or Too Clean

Real work documents are long, messy, and full of context the reader has to skim past. If your context files are short and tightly scoped, there's nothing to hunt through, which means the task is too easy. Add length. Add distractor information. Include tangential details that a real professional would see on their desk.

### 6. Obvious Distractor File Naming

Don't label distractor files as `distractor_notes.pdf`, and don't drop them in a `/distractors/` folder the model can see. Give them names that fit the rest of the file set so the model actually has to reason about relevance instead of filtering on filename.

## 2. Context Files: Integrity and Consistency

*Even realistic-looking files fail the task if the numbers don't hold up or if the files disagree with each other. These errors break the world before the model ever touches it.*

### 1. Broken or Corrupted Source Files

External workbook links pointing to a worker's local hard drive make the data completely inaccessible once the file is shared. Before submitting any Excel file, verify that all formulas resolve without external references, or paste values to break the links.

### 2. Broken Spreadsheet Formulas

Formulas returning `#REF!`, `#N/A`, or plainly wrong values. This includes internal inconsistencies like trial balances that don't balance and deposit tracking files with incorrect SUMs. Open every spreadsheet, click through the cells, and confirm the math works end to end.

### 3. Conflicting Details Across Files

Mismatched DOBs, institution names, dates, figures, lab values, medication names, or clinical notes that disagree across documents. Example: edema documented in one visit note but not another for the same appointment. Create a single source-of-truth record for any recurring detail and cross-check every file against it.

### 4. Unrealistic Assumptions

Numbers that don't pass a sanity check: for example, a property appreciating from $574K to $1.325M in two years. Even fictional data has to follow real-world patterns. Run plausibility checks on every major number: does this growth rate, margin, or timeline make sense in the real world?

### 5. Notation and Currency Issues

Non-US shorthand like "mn" or "bn" instead of "mil" or "B" when the task context is US-based. Mixed currencies without explicit USD/EUR/GBP labels. Pick a regional convention and apply it consistently, and always label currencies explicitly when more than one appears.

## 3. Task and Prompt Design

*A well-built world still fails the test if the prompt is too loose, too tight, or out of sync with what the grader actually expects.*

### 1. Overly Prescriptive Prompts

Hand-holding the model through each step of the solution defeats the purpose of the test. If the prompt reads like a recipe ("First look at file X, then calculate Y, then format as Z"), you're not measuring reasoning; you're measuring instruction-following. Give the model an objective, not a procedure.

### 2. Overly Open-Ended Prompts

The opposite problem: prompts like "What's the best way to..." or "Give me your analysis of..." invite freeform answers with no clear correct response. This makes consistent grading impossible. Prompts should have a definite, checkable answer or output.

### 3. No Cascading Dependencies

If all the subtasks can be done in parallel with no dependencies between them, the difficulty collapses. Real professional work requires doing step A before step B before step C, where each step relies on the output of the previous. Design tasks where early decisions constrain later ones.

### 4. Prompt and Grading Format Mismatch

The prompt asks for one type of analysis while the grading guidance expects something different, or the grading specifies an output format that the prompt never asked the model to produce. Before submitting, do a final pass: read the prompt, then read the grading guidance, and confirm they're asking for the exact same thing.

## 4. Grading Guidance

*Grading guidance has to pin down what the right answer actually is, and tie cleanly to the source files. Vague or inconsistent guidance makes it impossible to grade submissions reliably.*

### 1. No Target Numbers for Verification

"They should reconcile" or "accept any reasonable answer" isn't enough. Graders need the actual expected value: specific totals, final balances, journal entry amounts, or, at a minimum, a concrete range (e.g., "~$XX,000" or "between $X and $Y"). Vague acceptance criteria make consistent grading impossible.

### 2. Numbers Not Tying

Transposed figures, incorrect totals, or values with the wrong sign that cascade into downstream errors throughout the guidance. One wrong number at the top of a worksheet propagates through every calculation that references it. Work the problem end-to-end yourself before writing the guidance, and double-check every figure.

### 3. Allocation Method Conflicts

Grading guidance uses a different allocation method (straight-line vs. weighted, LIFO vs. FIFO, etc.) than the source policy documents specify. If the policy doc says one thing and the grading expects another, the model is in a no-win situation. Make sure the method in the source files and the method in the grading guidance are the same.

### 4. Date and Fiscal Year Errors

FY2026 appearing where FY2025 was intended, or vice versa. Date confusion is one of the most common sources of cascade errors because dates drive which data rows apply. Pick your fiscal year deliberately at the start, label it clearly in the task description, and check every date reference against it.

### 5. Factual and Terminology Errors

Wrong technical terms (e.g., using "unintended hyperopia" incorrectly in a clinical context), incorrect demographic or institutional details, or references to files that don't exist in the submission. If you're unsure about domain-specific terminology, verify it, and check your grading guidance for every filename it mentions to confirm they all exist.

### 6. Only One Valid Approach Acknowledged

When there are multiple valid methods or answers, latching onto only one without explaining why or identifying the alternatives makes the guidance brittle. If your task could reasonably be solved two or three ways, the grading guidance should list each acceptable approach and the expected result for each, not just score based on one path.
