# LLM prose tells

The sentence shapes that make a prompt read as written by a model rather than by a person at
work. Each class has the shape, why it reads that way, an example, and the fix. The script in
`../tools/prompt_check.py` catches the mechanical ones (rule ids in `prompt-rules.md`, T
series); the rest are caught by reading aloud.

## Why this matters here

The instructions want prompts phrased the way a normal person would ask an assistant. A prompt
that reads as engineered fails that bar even when the scenario is hard. There is a second,
quieter reason: the shapes below are also the shapes models produce, and a prompt written in
them tends to be answered well, because the model recognises its own register and the implied
structure. A flat, specific, slightly redundant workplace sentence is both more natural and
harder.

## The underlying mechanism

Most of the classes below are one rhythm: a piece of concrete detail, then a shorthand or
idiom that carries no information, then an analytical demand. The middle beat is the giveaway.
A real person writing a real request does not pivot on an aphorism every paragraph. Ordinary
workplace writing is flatter and more redundant than fiction about workplace writing: it
repeats the noun instead of finding a fresh phrase, and it explains things at more length than
a slogan would.

## Classes

### 1. Tautology (T1)

"Committed capital is committed." "The covenant is still the covenant." "Paragraph 8 is the
whole story." The highest-confidence tell. Fix: state the rule and its consequence. "Once the
capital is called it cannot be returned to the LPs, and it does not count toward the next
close."

### 2. Slogan or aphorism as a sentence (T2)

"September is use it or lose it." "This is where the money hurts." "At the end of the day the
market decides." Short punch lines that open or close a paragraph. Fix: state the mechanism.
"Budget not spent by the end of September is not carried into the next quarter."

### 3. Idiom or metaphor in place of the fact (T3)

"I want to know where we are naked before the lender does." "What we leave on the table."
"Bleeding cash." Fix: name the quantity. "The covenants we would breach at the current burn,
and by how much."

### 4. Negative parallelism (T4, T5)

"It's not just a valuation, it's a statement of intent." "Not only is the margin thin, but the
working capital is also negative." The plain "not X, but Y" is ordinary correspondence and is
fine; the "not just / not only ... but also" and the pronoun-led "it's not X, it's Y" are the
tell. Fix: say the second half on its own.

### 5. A simple verb avoided (T6)

"The term sheet serves as the basis for the valuation." "The fund boasts a 22 percent IRR."
Fix: is, has, holds. "The term sheet is the basis for the valuation."

### 6. Sycophancy (T7)

"Great question." "Happy to help." "Absolutely!" These sit where a model answers a requester,
and a requester never writes them.

### 7. Pre-counted lists (T8)

"There are three key considerations." "Four main risks stand out." A person writing a request
does not count their points before making them. Fix: make the points.

### 8. Hedging filler (T9)

"It is worth noting that..." "It is important to consider..." "One could argue..." "This may
suggest..." Practitioners state what they think. Fix: delete the frame and keep the claim.

### 9. Clinical and corporate vocabulary (T10)

Utilize, leverage, comprehensive, robust, holistic, facilitate, optimize, synergies, delve,
in order to, ensure that. "Leverage" is a real finance word when it means debt; the tell is
"leverage the existing data". Fix: the plain verb. Use, thorough, sound, cover.

### 10. Stacked quality adjectives (S3)

"A clear, well-structured analysis, not vague or incomplete." "A robust, comprehensive review,
not shallow or rushed." Two adjectives, a noun, and a list of failures avoided. Fix: name the
thing wanted. "Tell me whether the post-money they are asking for is supported by the three
quarters of actuals."

### 11. Repeated sentence openers (T11)

"It should show... It should list... It should recommend... Finally, it should state..." A
templated deliverable paragraph. Fix: vary the shape so each ask carries its own sentence, or
collapse them into one plain request.

### 12. Uniform bullet runs (T12)

Six or more bullets of the same length and grammar. People's lists are ragged: a two-word item,
a two-line item, one with a parenthesis. Fix: vary, or fold the short ones into a sentence.

### 13. The semicolon-balanced maxim (T13)

"A fee the client hears about in advance is a policy; a fee they find on a statement is an
insult." Two aphorisms hinged on a semicolon. Fix: say the consequence once. "A fee the client
first discovers on a statement causes lasting resentment."

### 14. Scene-setting fragments and performed urgency (T14)

"Word travels. Two things before the pencil comes out." "The July statement has the line
circled in my handwriting, and it stays circled until the numbers match." A person with an
urgent problem does not stage props. Fix: "This is urgent. The July statement's management
fee line does not match the agreement, and the Q3 statements go out on the 15th."

### 15. Rule-of-three padding (T15)

"Risks, exposures, and vulnerabilities." "Clear, concise, and actionable." Three where two or
one carry the meaning. Where three items are a list of record (three funds, three quarters),
keep them. Where the third is padding, cut it.

### 16. Lexical variation for its own sake (T16)

The same figure called "the valuation", then "the price tag", then "the number", then "the
ask" in four sentences. Fix: repeat the noun. Real memos are redundant.

### 17. Persona and clinical openers (F2)

"You are a senior financial analyst." "As an experienced portfolio manager, you..." "Utilizing
your expertise in..." The platform's own banned shape. Fix: open on the situation in the
requester's voice.

### 18. Compressed first-person filler

"I pulled the rest." "The rest has to follow her without me rebuilding the file." Shorthand
narration of the writer's legwork, often incoherent on a second read. Fix: drop it, or write
the complete sentence.

### 19. Fragments as headings inside prose

"Terms. Net 30, and I mean it this quarter. Subject to credit." A fragment, a comma splice and
a second fragment in one breath. Fix: complete sentences, or a real labelled line.

### 20. Em dashes (M1)

A long dash setting off an aside in the middle of a sentence ("The model, as expected, shows"
written with dashes instead of the commas). One per paragraph is the fingerprint. The rule
here is zero, because density is the tell and zero is the only count no reader notices.

### 21. Markdown formatting in a typed request (F7)

A cash-flow schedule written as a markdown table, with pipes and a `| --- |` separator row, or a
prompt with headings and bold labels. A finance manager copying from Excel pastes tab-separated
rows; one typing from a statement writes short lines or puts the figures in sentences. The
formatting tells the reader the prompt was composed for a model. Fix: paste the range as
tab-separated rows under a one-line lead-in ("Here's what I pulled into a spreadsheet:"), with
the dates and number formats the spreadsheet shows.

## Writing rules that follow

1. No sentence whose only job is to sound like a person. If deleting it loses no fact, it was
   a tell.
2. Never restate a noun as itself.
3. Prefer the longer, flatter sentence. Real requests over-explain; pastiche compresses.
4. One idiom per prompt at most. One reads human, three read generated.
5. Punctuate fragments into sentences.
6. Repeat the noun. Do not find a fresh phrase for the same quantity.
7. State urgency and the date. Do not perform it.
8. Correct, ordinary punctuation. A comma before the conjunction joining two clauses, never
   three clauses in a sentence, the serial comma.

## Adding a class

When a prompt is flagged or a sentence reads wrong on the read-aloud and no class above covers
it, add the class here with the flagged sentence and its fix, then add a regex to the script if
one can read it without catching ordinary English.
