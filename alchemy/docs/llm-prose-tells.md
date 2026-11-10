# LLM prose tells

The shapes that make text read as written by a model rather than by a person at work. Each class
has the shape, an example and the fix. `../tools/alchemy_check.py` catches the mechanical ones
(ids from `rules.md`, T, M and I series); the rest are caught by reading aloud.

They apply to everything in the task: the prompt, both input files, the rubric and the failure
description. The input files need the closest read, because the File Builder writes them with a
model and its first draft carries these shapes.

## Why it matters here

Two reasons. A prompt or a file that reads as generated fails the realism bar: the training asks
for realistic work documents and a handoff to a trusted colleague. And text in a model's own
register is easier for a model: it recognises the shape and the structure it implies. Flat,
specific, slightly redundant workplace writing is both more realistic and harder.

## The underlying rhythm

Most of the classes are one pattern: a piece of concrete detail, then a shorthand or idiom that
carries no information, then an analytical demand. The middle beat is the giveaway. Real
workplace writing is flatter and more redundant than fiction about workplace writing. It repeats
the noun instead of finding a fresh phrase, and it explains at more length than a slogan would.

## Prose classes

### 1. Tautology (T1)

"A breach is a breach." "The covenant is still the covenant." "Section 4.2 is the whole story."
The highest-confidence tell. Fix: state the rule and its consequence. "Any quarter above 3.25x
is an event of default under section 7.1, whether or not the lender has sent notice."

### 2. Slogan or aphorism as a sentence (T2)

"Cash is king." "At the end of the day the lender decides." "This is where the money hurts."
Fix: state the mechanism. "The lender can call the loan once the cure period ends."

### 3. Idiom in place of the fact (T3)

"Where we are exposed." "What we leave on the table." "Bleeding cash." Fix: name the quantity.
"The three facilities that breach at the current run rate, and by how much."

### 4. Negative parallelism (T4, T5)

"It's not just a pricing question, it's a governance question." "Not only is the margin thin,
but the working capital is also negative." The plain "not X, but Y" is ordinary and fine. Fix:
say the second half on its own.

### 5. A simple verb avoided (T6)

"The amendment serves as the basis for the new definition." "The fund boasts a 22 percent IRR."
Fix: is, has, holds.

### 6. Sycophancy (T7)

"Great question." "Happy to help." "Absolutely!" A requester never writes these, and a real
email thread rarely does.

### 7. Pre-counted lists (T8)

"There are three key considerations." A person makes the points without counting them first.

### 8. Hedging filler (T9)

"It is worth noting that..." "It is important to consider..." Fix: delete the frame, keep the
claim.

### 9. Clinical vocabulary (T10)

Utilize, leverage the data, robust, holistic, facilitate, delve, seamless, in order to.
"Leverage" is a finance word when it means debt; the tell is "leverage the existing data". Fix:
use, sound, help, to.

### 10. Repeated openers (T11)

"It should show... It should list... It should recommend..." Fix: one plain request, or vary the
shape.

### 11. Uniform bullet runs (T12)

Six or more bullets of the same length and grammar. People's lists are ragged.

### 12. The semicolon maxim (T13)

"A fee the client hears about is a policy; a fee they find on a statement is an insult." Two
slogans on a hinge. Fix: say the consequence once.

### 13. Scene-setting fragments and performed urgency (T14)

"Word travels. Two things before the pencil comes out." "The line is circled in red, and it stays
circled until the numbers match." A person with an urgent problem says so. Fix: "This is urgent.
The Q3 statement's fee line does not match the agreement, and statements go out on the 15th."

### 14. Rule-of-three padding (T15)

"Risks, exposures, and vulnerabilities." Keep lists of record (three funds, three quarters); cut
the padding.

### 15. Lexical variation for its own sake (T16)

The same figure called "the valuation", then "the price tag", then "the number". Fix: repeat the
noun.

### 16. A place or object for the document (T17)

"What goes on the door" for the posted exclusion list. "What lands on her desk" for the memo.
Fix: name the artifact. "The exclusion list we post in the branch."

### 17. Compressed first-person filler

"I pulled the rest." "It has to follow her without me rebuilding the file." Shorthand narration
that stops parsing on a second read. Fix: drop it, or write the full sentence.

### 18. Fragments as headings inside prose (M6)

"Terms. Net 30, and I mean it this quarter." Fix: a complete sentence, or a real labelled line
("Terms: net 30 days.").

### 19. Em dashes (M1)

One per paragraph is the fingerprint. The rule is zero, because density is the tell and zero is
the only count no reader notices.

### 20. Role-play openers (P4)

"You are a senior credit analyst." "As an experienced controller, you..." The training bans the
shape outright. Fix: open on the work.

## Input-file classes

These come from generated documents, and the File Builder is a generator.

### 21. Annotation voice (T18, I5)

"Note: the Q2 figure is outdated." "Important: use the amended rate." "Key takeaways:" A real
export or email does not explain itself to whoever reads it next. When the annotation points at
the planted issue, it is also answer leakage. Fix: delete it. If a real document would carry the
fact, state it the way that document would ("Per the March 4 amendment, the cap is $250,000.").

### 22. Tidy data (I11)

Every amount a multiple of 100, every date on the first of the month, every name of the same
length, no blanks, no late corrections. Real exports carry variance: $41,882.50, a blank
approver field, a row keyed on the 31st. Fix: the figures from your correct-answer script, with
the precision a ledger or system would hold.

### 23. Fabrication fingerprints (I11)

555 phone numbers. A weekday that does not match the date ("Monday, October 6, 2026" is a
Tuesday). Float residue such as 0.30000000000000004. "Acme", "John Doe", "Company A". Fix: plausible
values, a calendar check, rounding to keyed precision, fictional names that sound like real
firms in the region.

### 24. Uniform correspondence

Every email in a thread the same length, signed the same way, written in the same register, each
one ending on a question. Real threads have a one-line reply, a forwarded block, an
out-of-office, a signature with a title. Fix: vary length and register to the people writing.

### 25. Over-explained policy

A policy note that walks through its own rule as a worked example, or that lists exactly the
cases the scenario turns on. Real policies state the rule and its exceptions in the house style.
Fix: write the clause as the policy would carry it, and let the case in the data file test it.

### 26. File glossing in the prompt (P13)

"settlement_export.csv has the September batches and thread.docx holds the contract sections."
Pairing each file with what it contains reads as engineered, and it does the agent's reading for
it. Naming no file at all is the opposite defect. Fix: name the files inside the story and say
nothing about what is in them.

### 27. Self-describing text (T19)

"This thread contains the relevant contract sections." "The sections that follow set out the
terms." "Yellow cells are the inputs." Real documents do not narrate themselves. Fix: delete the
sentence; let the content stand.

### 28. Recycled stock phrasing

The same handoff moves reused task after task (the same opener about being buried, the same
closing line about the numbers updating themselves, the same "the rest is attached") read as a
template, and reviewers spot them across a portfolio. Fix:
write each prompt fresh in that requester's voice, and check new prompts against earlier ones in
`../tasks/`.

### 29. Uniform status tokens in prose

Prose that shouts the same ALL-CAPS status word in every sentence ("PAID", "HELD", "FLAGGED").
Status codes belong in the export's status column, where the system put them. In the memo or the
email, use the ordinary word.

## Writing rules that follow

1. No sentence whose only job is to sound like a person. If deleting it loses no fact, it was a
   tell.
2. Never restate a noun as itself.
3. Prefer the longer, flatter sentence. Real requests over-explain; pastiche compresses.
4. One idiom per document at most.
5. Punctuate fragments into sentences, except where the document form uses labels (an invoice
   line, a table cell, a header field).
6. Repeat the noun. Do not find a fresh phrase for the same quantity.
7. State urgency and the date. Do not act it out.
8. Correct, ordinary punctuation: a comma before the conjunction joining two clauses, never
   three clauses in a sentence, the serial comma.
9. Input files carry facts, never commentary about them.

## Adding a class

When something reads wrong on the read-aloud and no class covers it, add the class here with the
sentence and its fix. Then add a pattern to the script if one can read it without catching
ordinary English, with a self-test fixture.
