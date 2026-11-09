# LLM prose tells

> Scope: the prose classes the platform's style-guide table does not list (the three-beat rhythm, tautology, aphorism and the shapes below), and what covers each one here.
> The platform's list is `style-guide-llm-tells.md`; read that first and this second.
> The reviewer's own short list of LLM-use signs is `reviewer-checklist.md`; class 12 below maps each of its lines to a coded check or a read.
> The grammar side is `prose-standard.md`.

Enforced mechanically by check **A10** in `tools/evalcheck/prose.py`, with the patterns in `tools/evalcheck/catalogs.py`. A10 reads the rationale and the confidence note at ERROR and each harness output at NOTE. It is a pattern net, not a substitute for reading the prose aloud.

## Why reviewers catch it

The mechanism is a structure, not a word list: messy workplace detail, then an artificial shorthand or idiom, then an analytical requirement. That three-beat rhythm is the tell. A real author writing a real memo does not set up concrete detail, pivot on an aphorism, then land an analytical demand, paragraph after paragraph. The aphorism is the giveaway: it exists to sound busy and lived-in, and it is the one part of the sentence carrying no information.

Second: it is not how most people really speak at work. Ordinary workplace writing is flatter and more redundant than fiction about workplace writing. It repeats nouns instead of finding a fresh idiom for them, and it explains things at more length than a slogan would.

---

## Pattern classes

### 1. Tautology / "X is X"

The highest-confidence tell. "Committed work is committed." "Policy 6.3 is still policy." "Paragraph 8 is the whole story."

**Fix:** say the rule and its consequence. "Committed work is committed" becomes "Released project work is covered before counter stock, and it does not get cut to protect the counter."

Coded: A10, label `tautology`.

### 2. Aphorism / slogan as a sentence

Short declarative punch lines, usually opening or closing a paragraph. "September is use it or lose it." "Chestnut Ridge is where the money hurts." "Nobody promises what is not coming." "Anything that goes short has to show as short." Reviewers describe the class as punchy phrases from an LLM trying too hard to sound real and busy.

**Fix:** state the mechanism instead of the moral. "September is use it or lose it" becomes "September ceiling that we do not order against is not available later in the period."

Coded: A10, label `slogan`.

### 3. Idiom and metaphor in place of the fact

"I would rather walk into that call knowing where we are naked." "What we leave on the counter where we cannot cover it." "Not quietly dropped."

**Fix:** name the quantity. "What we leave on the counter" becomes "the counter sales we cannot fill, and the margin on them."

Coded: A10, label `idiom for a quantity`.

### 4. Compressed first-person filler

Narration of the author's own legwork, in shorthand. "I pulled the rest." "The rest of it has to follow her without me rebuilding the file." Compressed shorthand stops parsing before the writer notices, and a reviewer reads it as incoherent, not merely stylised.

**Fix:** drop the narration, or make it a plain complete sentence.

Coded: A10, label `first-person filler`.

### 5. Fragment used as a heading inside prose

"Front tab: what she needs to run that call." Or a terms line that is a fragment, a comma splice and a second fragment in one breath: "Terms. Subject to prior sale, and I mean that this month, the phone has not stopped. Net 15." Trade documents do use terse terms lines, but they punctuate them.

**Fix:** complete sentences, or a real labelled line ("Terms: net 15 days.").

A read; A20 catches the comma splice where it joins two clauses.

### 6. Em-dash density

Em dashes in the heading and throughout nearly every short paragraph is the punctuation pattern reviewers name first. The platform's style guide lists em-dash overuse as HIGH.

**Fix:** zero em dashes in anything we type into the platform. A harness output is read at density.

Coded: A6. ERROR for any em dash in authored prose; NOTE on an output document at 4 or more dashes and 12 or more per 1000 words, or 3 or more and 8 or more per 1000.

### 7. Run-ons, comma splices and missing punctuation

Two clauses joined by a comma is the commonest instance: "Not one classified breaker goes into Hamilton or Stroud township, Meixell has been red tagging them since the spring." The rules are in `prose-standard.md`.

Coded: A20 for a bare conjunction opening a new clause and for three or more clauses in one sentence. The comma splice and the serial comma stay a read.

### 8. Aphoristic parallelism (the semicolon-balanced maxim)

"A charge a customer hears about from their salesman is a policy; a charge they meet cold on a statement is an insult." The balanced "X is a noun; Y is a noun" maxim is a class-2 slogan doubled: two aphorisms hinged on a semicolon.

**Fix:** state the consequence once, plainly. "A charge the salesman explains in advance is accepted as policy. A charge a customer first discovers on a statement causes lasting resentment."

Coded: A10, label `aphoristic parallelism (semicolon-balanced maxim)`.

### 9. Scene-setting fragments as openers

"Word travels. Two things before the pencil comes out." Nobody with a truly urgent issue speaks in less-than-clear language. Real senders open with the subject, not atmosphere.

**Fix:** "I heard the delivery sheet is being reworked. Two things need to be settled before any changes are made."

Coded: A10, label `scene-setting fragment`.

### 10. Urgency performed instead of stated, and folksy metonymy

"The July statement has the outbound delivery line circled in my handwriting, and it is going to stay circled until the sheet we hand customers matches what the trucks cost." "The seventy five was old when gas was cheap." "Just build it so I can stand at a counter and defend it."

If there is urgency, state it. An urgent memo says "This is urgent" and names the deadline; it does not stage a prop (the circled line, the pencil, the counter) and let the image carry the demand.

**Fix:** same speaker, same facts, the image replaced with the plain statement. "This is urgent. The outbound delivery line on the July statement is far out of line with what the trucks actually cost us, and the delivery sheet we hand customers has to be corrected before the October statements go out."

Coded: A10, labels `idiom for a quantity` and `first-person filler`.

### 11. Place metonymy for the deliverable, and the unpunctuated clause break

"That is what goes on the door." "Read quickly that is the clean end of the account."

Two shapes. The first is a physical surface standing in for the document: there is no door, and "what goes on the door" means the posted list. The test is whether the phrase says which artifact it is. The second is a clause break left unpunctuated, so the sentence reads as a fragment and the sense only arrives in the next one.

The metonymy pattern requires the subjectless relative ("what goes on the ..."), because that is what makes the surface stand in for the noun. A declarative with a real subject, "the notice goes on the noticeboard", is literal and stays silent.

**Fix:** name the artifact. "What goes on the door" becomes "Lines to keep out of the magnet room". And close the sentence: "Read quickly, that is the clean end of the account."

Coded: A10, labels `place metonymy for the deliverable` and `unpunctuated clause break reading as a fragment`.

---

### 12. The reviewer checklist, line by line

The reviewer-side "signs of LLM use" checklist (`reviewer-checklist.md`) is a scan list, not a severity table. Each line, and what covers it here:

| Checklist line | Coverage | Coded? |
| --- | --- | --- |
| Repeated em dashes | class 6, zero in authored prose, density in an output | A6 |
| Long instruction files, repeated or over-explained details | this workspace writes no instruction file; over-explained detail in the rationale is a read | read |
| "It's not just X, it's Y" phrasing | the pronoun-led contrast ("it is not just a price list, it is a commitment") | A10 |
| Negative parallelism ("not," "not only") | "not only X but (also) Y" and "not just X but Y" | A10; the plain "not X, but Y" is ordinary correspondence and stays a read |
| Long, highly uniform bullet lists | a run of six or more bullets with a word-count standard deviation of 1.5 or under | A33 |
| Highly polished grammar, the Oxford comma | **conflicts with A20**, which demands the serial comma. The house rule stands: punctuate correctly, and let the register vary (sentence length, a flat restatement, a noun repeated) so correctness is not the only thing a reader notices | A20 stays; the rest is a read |
| Sycophantic language | "great question", "happy to help", "I'd be happy to", "excellent point", "you're absolutely right", "absolutely!", "certainly!", "great choice", "thank you so much". "Thank you for your order" and "you are right" are correspondence and stay off the list | A10 |
| Avoiding simple verbs (serves as, stands as, boasts, features, offers, represents) | "serves as", "stands as", "boasts", "showcases" are coded. "offers", "features" and "represents" are trade vocabulary and stay a read: use "is", "has" or "holds" where the sentence means that | A10, partly |
| Rule-of-three phrasing | a read. Where three items are a list of record, keep them; where the third is padding, cut it | read |
| Excessive lexical variation | a read; writing rule 2 below: repeat the noun, never find a fresh phrase for the same quantity | read |
| Polished parallel structures | class 8 (the semicolon maxim) and A21 (the status-report skeleton) catch the two coded shapes; sentence-by-sentence parallelism across a paragraph is a read | A10, A21, partly |
| Contrast-based sentences | the coded forms above; repeated "while X, Y" and "rather than" framing is a read | A10, partly |
| Unusually consistent sentence style | a read; no length threshold separates generated from real. Read aloud and vary where a page drones | read |

Generic heading pairs in an output document ("Executive Summary" with "Recommendations", and the rest of the stock outline) are the one shape the checklist does not name that is coded: A32, as a NOTE on evidence only.

## Writing rules that follow

1. **No sentence whose only job is to sound like a person.** If deleting it loses no fact, it was a tell.
2. **Never restate a noun as itself.** No "X is X", no "still X", no "the whole story".
3. **Prefer the longer, flatter sentence.** Real memos over-explain; LLM pastiche compresses.
4. **One idiom per document, at most.** A single "we are not going to argue about it" reads human. Three in a page reads generated.
5. **Punctuate fragments into sentences** unless the document form genuinely uses labels (an invoice line, a spec paragraph, a table cell).
6. **Read a harness output under the same rule.** A tell in a model's deliverable is an observation for the Format & Presentation rating, logged with its quote, never a defect for us to fix.
