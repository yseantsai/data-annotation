# Holodeck Project Training

## What's the Ultimate Goal?

The client is building **AI agents** that can handle complex, realistic professional work across a variety of domains.

- These aren't simple chatbots that answer quick questions.
- The client is training agents that can work through the kind of multi-step, document-heavy workflows that land on a professional's desk in real life.
  - For example: a vendor bid evaluation where two scoring matrices conflict, a marketing budget reallocation where a buried email changes the channel assumptions, or a workforce plan where a revised attrition rate shifts the hiring roadmap.
- To train these agents, we need **difficult realistic tasks**: tasks that require synthesizing information across many documents, handling dependencies between steps, and exercising professional judgment.

**That's where you come in.**

- You know what real professional work looks like, what makes it hard, and where less experienced professionals (or AI) are likely to go wrong.
- We want you to design a realistic task that tests whether an AI agent can do the kind of work you do and to define what "getting it right" looks like.

## How to Train an AI Agent

### What Is an "Environment"?

In AI training, the **environment** is the world the agent operates in.

- For a chess-playing AI, the environment is the board and pieces.
- For a self-driving car, it's the road, traffic, and weather.

For this project, **the environment is the professional scenario you create.**

- You'll build a set of context files (project plans, contracts, research reports, dashboards, briefs, statements of work, emails, memos, spreadsheets, etc.) and pair them with a prompt. Creating context files from scratch is hard, so we'll provide you access to Claude Cowork, and ChatGPT's Codex, to help with this.
- The agent reads these files, reasons about them, and produces a deliverable (one or more output files).
- **Ideally, the agent does a bad job -- ideally, the deliverable has issues.**

### How AI Agents Learn

AI agents learn through a process called **reinforcement learning**. Here's how this works in Holodeck:

1. The AI agent is given a **task** (a prompt) to complete within an **environment** (a set of documents).
2. The AI agent produces an **output**: its attempt at completing the task.
3. Using Grading Guidance (or a rubric) that you have written, the AI agent's output is evaluated (by another AI, a grader AI).
4. The AI agent **learns from the evaluation**, adjusting its approach to do better next time.

Over thousands of tasks and evaluation cycles, the agent incrementally improves. This process is called **"hill-climbing"** like climbing a hill one step at a time, where each step takes the agent to slightly higher ground (better performance).

### Why the Agent Needs to Fail

Here's a crucial insight that shapes everything about this project: **the agent learns from its mistakes.**

- If a task is **so easy** that the agent always gets it right, there's **nothing to learn from**. No useful training signal.
- If a task is **impossible** or completely random, the agent can't extract useful signal either.
- The **sweet spot** is tasks where the agent gets *some things right* and *some things wrong*. That's where hill-climbing happens -- the agent gets a signal about what to do differently.

This is why we ask you to design tasks that are **genuinely challenging**. We *want* the agent to fail on some aspects of your task. Those failures, combined with your Grading Guidance (or rubric) that explains what the correct answer should be, become the training signal that teaches the agent what matters in professional work.

**Think of it like mentoring a junior colleague:**

- You give them real work, they make mistakes, and you explain what they got wrong and why it matters.
- Over time, they develop professional judgment.
- That's what's happening here, at scale.

### Your Grading Guidance/Rubric Is the Scoring Function

When the agent's output gets evaluated against your Grading Guidance/Rubric, that evaluation is the signal that teaches the agent what matters. In reinforcement learning, this is called the **scoring function** (or "reward signal"). It's how the agent knows whether it's climbing the hill or sliding back down.

If you've created data that's been used to train AI models before, you may be familiar with the concept of a rubric -- a set of specific, concrete criteria that's used to evaluate a model response. The Grading Guidance is kind of like that, but it's meant to be more realistic.

#### Grading Guidance

**The Grading Guidance is the guidance you would give to a colleague to check someone's work, where you don't want the colleague to have to solve the problem themselves.**

- You'd give the colleague specific information that has to be in the output, to the extent there is such specific information.
- You'd give the colleague guidance to ensure that certain things were done.
- You'd likely point out common mistakes that might have been made, to ensure the colleague checks to see whether those mistakes were made.
- This can be written in a narrative format (like paragraph-style).
- Your Grading Guidance will be read by an LLM and converted into a rubric, so it's also fine to write your Grading Guidance with an LLM reader in mind.

#### Rubric

- A rubric is a set of criteria, where each criterion is a statement about what should be in a good response to the prompt.
- In Phase 2 you'll either write a rubric directly, or write Grading Guidance that then gets converted into a rubric (by an LLM).
- Different AI companies use rubrics in different ways -- so you'll see rubrics treated differently in different projects at DataAnnotation.
- In this project, we aren't picky about rubric format -- though we do want each criterion to be:
  - ***atomic*** -- about a single element of the response
  - ***self-contained*** -- someone could use the criterion to determine whether the response passes or fails the criterion, without having to check anything else (e.g. without having to check the input files).

### You'll Have Three Jobs in This Holodeck Project

1. **Build the Environment** -- a realistic scenario with documents that creates meaningful professional complexity.
2. **Write the Prompt** -- a realistic task that's hard for the AI agents.
3. **Write the Grading Guidance/Rubric** -- specific enough that a colleague (or an AI grader) encountering the task can evaluate any response, without having to independently solve the prompt themselves.

## Designing Your Task

### Realism Is the Top Priority

The single most important quality of your task: **it must be grounded in real professional work you've actually done.**

The best tasks come from actual engagements, cases, or workflows you've performed. The specific complications you encountered -- the sales rep who logs a deal under the wrong territory, the client stakeholder who gives vague sign-off, the ops manager who buries a revised assumption in an email thread -- these are the details that make a task valuable.

We are not looking for textbook exercises or hypothetical scenarios. We need the messy, specific details that only come from real experience. That's what makes this data uniquely useful for training, and it's why we need domain experts like you, not prompt engineers.

- **Good Task Idea:** A revenue-operations analyst is handed a disputed Q3 commission run and finds that a mid-quarter territory realignment was never applied, one enterprise deal was credited to two reps, and a clawback for a cancelled contract was missed. The quota attainment that sets each rep's bonus tier depends on all three being corrected.
- **Bad Task Idea:** A sales analyst reviews the quarter's closed deals and calculates commissions for the team.

The first is specific and grounded in real experience. The second is generic and could have been written by anyone, or by an LLM.

### The Prompt Should Be Realistic and Non-Hand-Holdy

**Put yourself in the mindset of a user actually writing out a prompt for a model.**

- **Good Prompt:** *"Run a sales/use tax audit for Q2. Get me an excel workbook including a schedule and net adjustment."*
- **Bad Prompt:** *"You are an auditor at a mid-level consumer-goods company. Complete a Q2 audit by following these seven steps..."*

- **Persona-based prompts (prompts that start "You are a") tend to be unrealistic** -- real users don't write that way.
- While spelling out how a model should do something step-by-step might be realistic, that's only because the model isn't so smart and the user is trying to get the model to succeed.
  - In this project, since we want the task to be so challenging that the model fails, **we don't want to hand-hold the model.**
  - If the prompt tells the agent exactly what to do, the reasoning lives in the prompt, not the task. The agent should have to **figure out what matters by working through the documents.** That's the professional skill we're trying to train.

### Strong Tasks Have Sequential Dependencies

Strong tasks have **dependencies between steps**, where the result of one part feeds into others. This means an early error can cascade and affect downstream results just like in real professional work.

- **Good:** Size the addressable audience from the segment data → allocate budget by each segment's acquisition cost → forecast the pipeline that budget produces → set the quarter's lead target. If the audience sizing is wrong, every downstream number is off.
- **Bad:** Pull last month's click-through rates for three unrelated campaigns. Each is standalone so getting one wrong doesn't affect the others. This is one simple task repeated, not a complex one.

Your task doesn't need to be *fully* sequential from start to finish; that's often not how real work operates. But it should have **meaningful dependencies** where at least some early decisions affect later parts of the output. The key question: if the agent gets something wrong early on, does it matter downstream?

### Context Files: Building the Agent's World

Your context files are the agent's entire world for the task. Think of them as the documents sitting on your desk when you start a real assignment.

**Requirements:**

- **Minimum 10 files.** Strong tasks often have 15-20+, but don't rely on volume alone. Complexity should come from the task requirements themselves, not the sheer number of documents.
- **Recognizable professional documents.** Each file should be something a professional in your domain would immediately recognize: "campaign performance dashboard," "vendor statement of work," "employee compensation matrix," "master services agreement." Avoid generic labels like "project files" or "supporting documents."
- **Specific descriptions.** In Phase 1, you don't create the actual files, you describe them. Be specific about what each file contains and why it matters to the task.

**Examples:**

- **Specific:** "March 2024 rent roll for Maple Court Apartments, 48 units, showing 4 vacancies and $612,400 in annualized in-place rent"
- **Generic:** "Rent roll"

### Deliberate Traps, Not Tricks

Remember, the goal is for the agent to fail in **professionally meaningful ways** -- the same kinds of mistakes a less experienced colleague might make. You're not trying to trick the AI with arbitrary gotchas or contrived puzzles. Instead, you're creating the kind of **realistic complexity** that professionals navigate every day.

**Strategies for building difficulty:**

- **Spread critical information across documents.** A pricing exception that depends on a clause buried in the master services agreement. An amended vendor quote in an email chain that supersedes the one in the bid folder. A requirement captured in a stakeholder interview that never made it into the product spec.
- **Create controlled conflicts between documents.** A formal media budget with outdated acquisition-cost assumptions vs. an informal email from the channel lead with the corrected numbers. A signed SOW listing one deliverable scope while the kickoff deck shows another.
- **Include plausible distractor files.** Prior drafts with different numbers, superseded policies, unrelated correspondence, or meeting notes whose action items were never adopted. In real work, not every document on your desk is relevant and knowing what to ignore is part of the expertise.
- **Leave out information the task needs.** In real work, sometimes a document is missing or an assumption is unstated. A strong agent should notice the gap and flag it, rather than silently fabricating a value.
- **Require the agent to update its understanding.** Early documents suggest one conclusion, but later documents reveal information that changes the correct answer. A market segment looks like the top opportunity until a churn analysis reveals far worse retention, flipping the priority.

For each trap, think about **what the wrong-but-plausible answer looks like.** If you can predict the specific mistake the agent is likely to make and describe how it cascades, you deeply understand the complexity of your task.

*Note: some versions of the project give more detailed guidance on sources of difficulty. For example, favoring parallel-thread synthesis, forcing the agent to revise an early hypothesis, and red-flag recognition over simply hiding information in hard-to-find places (which can come across as contrived). Always follow your specific project's instructions.*

### The Prompt Must Be Specific Enough That Some Outputs Are Right and Some Are Wrong

- The output must be something that an expert colleague could look at and reliably say "this is right" or "this is wrong."
- This doesn't mean there's only one correct solution. It means you'd expect expert consensus on which solutions are correct, which are partially correct, and which are fundamentally flawed.

### Writing Strong Grading Guidance

Remember: your Grading Guidance/Rubric is the scoring function. It needs to be so specific enough that a knowledgeable professional encountering the task for the first time could evaluate any response consistently.

In Phase 1, you write a general description of the correct solution to your prompt. You don't need exact values yet (those depend on context files you haven't created), but you need to demonstrate that you understand what the correct answer looks like and what makes it checkable. Your outline should address:

- **What does the correct solution look like?** Describe the deliverable, the key steps to get there, and the critical judgment calls.
- **What's most critical to check?** What are the most important things a reviewer should verify first?
- **Where do you expect the agent to fail?** What specific mistakes is the agent likely to make, and how do those mistakes cascade into downstream errors?

**Examples:**

- **Good:** "The revised staffing plan must reconcile to the forecasted ticket volume. The key adjustments involve a duplicated seasonal-hire request, an unaccounted-for attrition rate, and a training-ramp lag that delays when new hires reach full capacity."
- **Bad:** "The agent should staff the team correctly."

The pattern: **name specific aspects of the output that can be checked.** Identify particular adjustments, decisions, values, or judgment calls a reviewer would look for. If your Grading Guidance just restates the prompt without adding checkable specifics, the agent can't learn from it.

## The Holodeck Pipeline

### Four Parts

Understanding the full pipeline helps you make better decisions at each stage.

| Phase | Who | What Happens |
| --- | --- | --- |
| Phase 1 | You | Submit your scenario, prompt, context file descriptions, and general description of the correct answer. |
| Phase 1 R&R | A domain-expert admin | An admin ensures that your Phase 1 submission is the sort of submission we're looking for. |
| Phase 2 | You | Create all context files, write the final prompt and Grading Guidance/Rubric, test with AI agent, iterate until the agent fails meaningfully. |
| Phase 2 Evaluation | A domain-expert admin | Your task runs through an automated evaluation pipeline. An admin then evaluates your task, making edits as needed. |

*Note: some versions of the project skip Phase 1 entirely -- but only for workers who have already completed a Phase 1 and a Phase 2. Once you've been through the full pipeline, you may be invited to projects where you go straight to building the complete task (files, prompt, and rubric/Grading Guidance) with no proposal-approval step. The design principles in this training still apply there.*

### Phase 1 Is a Proposal, Not a Finished Product

In Phase 1, you are pitching a task idea and demonstrating that you have the domain expertise and specific scenario to build it out. You are **not** creating actual context files yet (though you may upload any you've started). Your submission has four parts:

1. **Scenario** -- The background of your task: the setting, context, and what makes it realistic.
2. **Prompt** -- A specific, actionable task directive that requests a concrete deliverable.
3. **Context Files** -- Descriptions of at least 10 files that make up the agent's environment.
4. **General Description of the Solution** -- What the correct output looks like, how to evaluate any response, and where you expect the agent to fail.
   - In Phase 2, you will transform this general description into a Rubric/Grading Guidance.

Phase 1 reviewers are evaluating potential, not perfection. But a detailed Phase 1 proposal forces you to think through the scenario concretely enough that Phase 2 is about building and refining, not starting from scratch.

## Keep in Mind

### Avoid Faux Complexity

A complicated situation does not automatically make a complex task. Before submitting, check your proposal against these common traps:

- **Complex inputs, simple output.** If understanding the source material is hard but producing the deliverable is straightforward, the task is too simple. The agent needs to reason, not just read.
- **Parallel work disguised as one big task.** Doing the same thing independently for multiple accounts or cases is one simple task repeated. Strong tasks have dependencies across components.
- **Information extraction disguised as analysis.** If the agent can produce the correct output by locating values and placing them in a template, that's extraction, not reasoning.
- **The prompt does the thinking.** If the prompt tells the agent exactly what to look for and in what order, the reasoning lives in the prompt, not the task. The agent should discover what matters by working through the documents.
- **No cascading consequences.** If one part is wrong but the rest stays correct, the task is too contained. Strong tasks have at least some points where an early mistake affects downstream results.

**A good self-check:** After the agent reads the documents, does the actual workflow still require multiple connected decisions? If the task can mostly be completed by reading through files once and writing as you go, it's probably not complex enough.

### Important Rules

#### LLM Usage

- **Please make sure the submission relies on your own professional expertise, and YOU are the writer of all content, including the prompt, scenario, solution description, Grading Guidance, and explanations.** You may use an LLM for planning, but we are interested in YOUR experience, not an LLM's.
- You must write the prompt yourself -- this is especially important.
- **Do not copy the project instructions into an LLM and ask it to generate a proposal for you.** It is obvious to reviewers when people do this, and it will result in removal from the project.
- You can use an LLM to brainstorm details. In Phase 2, when you build your task, you can also use LLMs to generate synthetic data files, draft supporting materials for your context files, and assist with calculations -- but you must verify everything. (In Phase 1 you only describe your context files -- you don't create them yet.)
- The best tasks come from real professional experience. Don't outsource the design thinking to an LLM.

#### Data Privacy

- **No real PII or PHI.** Names, addresses, SSNs, account/ID numbers, dates of birth, and company names must be entirely fictional. It is safer to create documents from scratch than to redact real files. (It's fine -- and helpful -- to use a real document as a template.)
- **Public filings are fine.** You may use real public documents (e.g., SEC filings, government reports, or published standards).
- Use realistic fictional names -- avoid obviously fake names like "John Doe" or "123 Fake Street."

#### Other Requirements

- **All scenarios must be US-based.** You don't need to be a US-based worker yourself -- international workers are welcome as long as the scenario, framework references (e.g., FLSA/EEOC guidelines, FTC advertising rules, OSHA standards, ASC 842, IRS rules), and currency are US-based.
- **Tasks must not be "fresh."** The correct answer should not change day over day or week over week. If someone checked your task a year from now, the correct answer would still be the same.
- **The agent has no web access.** Your task must be solvable from the prompt and the context files alone -- the agent cannot look anything up online. If solving your task requires information beyond standard professional knowledge (current rates, published guidelines, company specifics), put it in a context file.

## In Closing: Key Takeaways

- You're building an **environment** (realistic scenario + documents) and a **scoring function** (Grading Guidance) that will be used to train an AI agent.
- The agent learns by **hill-climbing** -- it needs tasks hard enough to produce meaningful failures, not so hard that there's no useful signal.
- **Realism** is the top priority. Ground your task in work you've actually done.
- Design tasks with **sequential dependencies** where early errors can cascade.
- Put the complexity in the **documents**, not the prompt. The prompt should be a short professional handoff.
- Make Grading Guidance/Rubric **specific and checkable**. Name the particular decisions, values, and judgment calls a reviewer should look for.
- Phase 1 is a **proposal**. Show that you have a real scenario, the expertise to build it, and a plan for what "correct" looks like.
