# Prompt rules

Every rule has an id, a one-sentence statement, and a note on how it is checked: **coded**
means `tools/prompt_check.py` detects it (ERROR blocks, WARN needs a read), **read** means
only a human reading catches it. A coded check is a net, not a judge: clean output is the
floor, and reading the prompt aloud is still the test.

The platform's own requirements, from `../instructions.md`, sit behind every rule here:
challenging, realistic, natural, phrased as a normal person would phrase it, producing a model
response that is a failure or essentially flawed, with no adversarial content and no private
information about real people.

## F: Frame and voice

| Id | Rule | Check |
| --- | --- | --- |
| F1 | The prompt carries who is asking, who the output is for and what decision it feeds, woven into the ask. | read |
| F2 | No persona opener: never "You are a...", "As a ..., you", "Your task is to", "utilizing your expertise". | coded, ERROR |
| F3 | It reads as a person briefing a colleague or an assistant, not as a test question or a product description. | read |
| F4 | The stakes are concrete: a decision, a deadline, an amount at risk, a person waiting. | read |
| F5 | Every person and company is fictional; no private information about any real person. Public facts about public companies are allowed only when they are public. | read |
| F6 | No adversarial, unsafe, sensitive, criminal or controversial topics (the lists in `../instructions.md`). | coded WARN on keywords, then read |
| F7 | Data goes in the way a person types or pastes it: tab-separated rows copied from a spreadsheet, short lines, or figures in sentences. No markdown table syntax, headings or bold; nobody formats a chat message that way. A short hyphen list is fine when a person would type one. | coded: ERROR on a markdown table, WARN on headings and bold |

A frame that passes F1 to F4 does not introduce the requester to a colleague who already knows
them. Context rides on the things the work touches: "the board pack goes out Thursday", "our
Delaware C-corp", "the lender's covenant letter from March".

Finance-flavored pair. The left reads as engineered, the right as lived:

| Reads as model-written | Reads as a person |
| --- | --- |
| You are a senior equity analyst. Utilizing your expertise in valuation, analyze the provided financials and produce a comprehensive, well-structured investment memo covering: (1) a DCF, (2) trading comparables, (3) key risks, and (4) a recommendation. | My partner wants to put another $400k into Haldane Precision before their Series A prices, and the founder sent over a model that shows them cash-flow positive by Q3 next year. Their last three quarters of actuals are in the deck I'm pasting below, and the model's revenue line grows 18 percent a quarter while headcount stays flat. Tell me what you make of the model, whether the pre-money they're asking for holds up, and what I should push back on before Friday. |

## D: Difficulty

| Id | Rule | Check |
| --- | --- | --- |
| D1 | Not answerable by recall; the answer depends on the scenario's own facts and on multi-step reasoning over them. | read |
| D2 | The scenario carries a trap: a fact that changes the answer, a default method that is wrong here, or a convention the model will confuse. | read |
| D3 | The facts can support the answer the requester does not want, so a model that plays along is gradeably wrong. | read |
| D4 | A prompt is submitted only when the Generate response is OK, Pretty Bad or Terrible. | procedural |
| D5 | Not a minor variation of an earlier attempt in `submissions/`. | read against the folder |
| D6 | Complexity is the scenario's own; no constraints that exist only to trip the model. | read |
| D7 | The prompt is long enough to carry its facts and no longer: under 60 words is almost always a softball, over 650 is almost always padding. | coded, WARN |
| D8 | Size budget: the whole task, from design through the rating and explanation, fits in about three hours of human work. One decisive question beats several stacked ones; a practitioner should be able to answer the prompt in about an hour. Difficulty comes from the trap, never from volume. | read |

## S: Specification

| Id | Rule | Check |
| --- | --- | --- |
| S1 | What, not how: no numbered procedure, no dictated sections, columns or formulas, no stack of "should include / make sure / ensure". | coded WARN on step lists and requirement stacks, then read |
| S2 | No pitfall warning and no derived parameter stated as a given; if noticing it is the test, the prompt does not hand it over. | read |
| S3 | No stacked quality adjectives ("a clear, comprehensive analysis, not vague or superficial"); name the specific thing wanted instead. | coded, WARN |
| S4 | If the form of the output matters (a memo, a table, a one-paragraph answer), it is named once in plain words. | read |
| S5 | Round figures only where a real person would quote a round figure; working numbers carry realistic precision. | coded WARN on round currency amounts, then read |

## M: Sentence mechanics

| Id | Rule | Check |
| --- | --- | --- |
| M1 | Zero em dashes. Commas, colons, semicolons, parentheses or a new sentence instead. | coded, ERROR |
| M2 | A comma before and, but, so, or, yet when it joins two independent clauses. | coded, WARN (heuristic) |
| M3 | Never three independent clauses in one sentence. | coded, WARN (heuristic) |
| M4 | No comma splice: two sentences are not joined with a bare comma. | coded, WARN (heuristic) |
| M5 | The serial comma in every list of three or more. | read |
| M6 | Complete sentences; no fragments standing as headings inside prose. | read |
| M7 | No spelling or grammar errors. | read |

Correct, ordinary punctuation reads more human here, not less. The voice that pushes toward
clipped, breathless prose is the one reviewers call "a model trying to sound busy".

## T: Prose tells

The catalog with examples and fixes is `llm-prose-tells.md`. The ids below are the ones the
script reads.

| Id | Shape | Check |
| --- | --- | --- |
| T1 | Tautology: "X is X", "X is still X", "is the whole story". | coded, ERROR |
| T2 | Slogan or aphorism standing as a sentence. | coded WARN on known phrases, then read |
| T3 | Idiom or metaphor in place of a quantity or a fact. | read |
| T4 | Negative parallelism: "not just X but Y", "not only X but also Y". | coded, WARN |
| T5 | "It's not X, it's Y" contrast. | coded, WARN |
| T6 | A simple verb avoided: serves as, stands as, boasts, showcases. | coded, WARN |
| T7 | Sycophancy: "great question", "happy to help", "absolutely". | coded, ERROR |
| T8 | Pre-counted list: "there are three key factors". | coded, WARN |
| T9 | Hedging filler: "it is worth noting", "it is important to consider", "one could argue". | coded, WARN |
| T10 | Clinical or corporate vocabulary: utilize, leverage, robust, holistic, facilitate, delve, in order to. | coded, WARN |
| T11 | Three or more sentences in one paragraph opening on the same two-word stem. | coded, WARN |
| T12 | A run of six or more bullets of near-identical length. | coded, WARN |
| T13 | The semicolon-balanced maxim: "X is a policy; Y is an insult." | coded, WARN |
| T14 | A scene-setting fragment opening a paragraph ("Word travels.") or urgency performed with props instead of stated. | coded WARN on short openers, then read |
| T15 | Rule-of-three padding: lists of three where the third item carries nothing. | coded WARN on density, then read |
| T16 | Excessive lexical variation: the same quantity renamed in every sentence. Repeat the noun. | read |

## R: Rating and explanation

| Id | Rule | Check |
| --- | --- | --- |
| R1 | The rating and the explanation describe the actual Generate response pasted in the task file; nothing is inferred or invented. | procedural |
| R2 | The explanation names the specific mistakes, their severity, whether the model started well, a theory of why it failed, and what the correct answer is. Keep it short: about 150 to 200 words in two or three paragraphs, one decisive mistake with its figures ahead of the minor ones, and the full list of flaws left in the Outcome notes. | read, plus `--task` on the task file |
| R3 | Amazing and Pretty Good are never selected; such a response sends the prompt back to design. | procedural |

## Adding a rule

When a prompt is returned or a response reveals a pattern worth catching, add the lesson here
first, with the date and what happened, then code it in `tools/prompt_check.py` if a regex can
read it, and add a fixture line to the script's self-test so it keeps firing.
