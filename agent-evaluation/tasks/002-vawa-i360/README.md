# Task 002 — VAWA I-360 self-petition adjudication

- Category: Immigration Law (adjudication)
- Status: Prompt, input files and harness order recorded 2026-11-05. No run made.
- Required harness order: **Gemini Native first, then Antigravity** (reversed from task 001; recorded from the task page 2026-11-05)
- Instruction source/version: not yet confirmed; docs/reference/evaluation-instructions.md is the task 001 transcript and may not apply
- Submission status: Not verified
- Authorship: LLM-generated and LLM-edited workspace materials

## Context

Adjudication of a Form I-360 VAWA self-petition by Marcia Evadne Whitfield,
acting as an Immigration Services Officer at the USCIS Nebraska Service Center
on Monday, October 12, 2026.

The deliverable is one decision of four (Approve, Request for Evidence, Notice
of Intent to Deny, Deny), with detailed reasoning, eligibility findings, and
citations to specific documents with page or paragraph locators. No file format
is specified in the prompt, which is itself a thing to watch under Instruction
Following.

Most eligibility elements are stipulated as pre-reviewed in the prompt itself:
citizenship, good-faith marriage, civil status, good moral character, joint
residency. The live question is battery or extreme cruelty.

- Prompt: [prompt.md](prompt.md), recorded verbatim before any run
- Reference solution: [reference-solution.md](reference-solution.md) — **never sent to a model**, E06 guards this

The reference solution approves the petition. Most eligibility elements are
stipulated as pre-reviewed; the live question is battery or extreme cruelty,
and the record carries a deliberate October 21 / October 23 date inconsistency
between the petitioner's and Desmond Reid's accounts, which the reference
handles by acknowledging it and explaining why it does not undermine
credibility. It also requires explaining why neither an RFE nor a NOID is
warranted. Those are the three places an evaluated result is most likely to
separate.

Treat that as orientation, not as the rating standard. The reference solution
is the floor, not an answer key.

## Files

- Workflows: [../../docs/workflows/](../../docs/workflows/README.md)
- Prompt as given to both harnesses: [prompt.md](prompt.md)
- Reference solution, never sent to a model: [reference-solution.md](reference-solution.md)
- Input files as received, zip and unpacked PDFs: `inputs/`
- Each result as received: `outputs/<harness>/` (Gemini Native: final message, run transcript, output zip)
- Markdown conversions of the inputs: `evaluation/converted/inputs/`
- Antigravity final response: `outputs/antigravity/final-message.md`, copied verbatim from the completed conversation's full transcript. The Files panel and run directory were checked; the run produced a chat-only response and no separate output documents.
- Antigravity output archive: none. Because no output documents were generated, there is no `antigravity-outputs.zip`; the chat response is kept as Markdown only and the input PDFs are not mislabeled as outputs.
- Evaluation: `evaluation/` (`rationale.md`, `confidence.md`, `ratings.md`, `checks/`)

Link actual files here once available. Do not duplicate shared instructions or rationale drafts in a context bundle.

## Progress

- [x] Scaffold the task folder
- [x] Park the reference solution outside the prompt
- [x] Record the exact prompt before any run
- [x] Unpack input files in `inputs/`
- [x] Convert inputs to Markdown in `evaluation/converted/inputs/` (pypdf, page markers)
- [x] Verify the reference solution's citations against the record ([evaluation/reference-verification.md](evaluation/reference-verification.md))
- [x] Record harness order
- [ ] Record applicable instruction version
- [ ] Copy `templates/ratings.md` to `evaluation/ratings.md`
- [x] Stage 1: run **Gemini Native**; outputs filed 2026-11-05 (chat-only deliverable; prompt and inputs verified identical against the run transcript)
- [x] Stage 2: Gemini Native rated; evidence in [evaluation/stage2-gemini-native.md](evaluation/stage2-gemini-native.md), ratings in `evaluation/ratings.md`
- [x] Stage 3: Antigravity completed; final chat response saved. The Files panel was checked and contained no generated output documents.
- [x] Stage 4: Antigravity rated; evidence in [evaluation/stage4-antigravity.md](evaluation/stage4-antigravity.md), ratings in `evaluation/ratings.md`
- [x] Stage 5: preference "Antigravity is slightly better" (Gemini Native 5, Antigravity 6); [rationale](evaluation/rationale.md) and [confidence](evaluation/confidence.md) written 2026-11-05
- [x] `python3 tools/evalcheck.py tasks/002-vawa-i360` clean of ERROR (saved under `evaluation/checks/`)
- [ ] Shadow validators run on the finished text (`docs/validators/`)
- [x] Platform Check Your Task run 2026-11-05; one reconciliation asked for and made ([record](evaluation/checks/check-your-task-2026-11-05.md)); confidence recorded
- [ ] Review checker feedback and record final status

## Handoff

State the next action, unresolved questions, and which checks have actually been completed. Link shared references only when applicable.

Distinguish what was observed from what was reported. A saved check result is a
historical result for the text as it stood, not a live check and not a record
of what the platform received.

## Known check findings

- None open. The platform form refused "slightly better" while both overall
  scores were 6; Gemini Native was revised to 5 rather than the preference
  softened to "negligibly better", because the rationale's case is that the
  difference is real. Logged in ratings.md, Revisions.
- The Stage 2 ratings were entered after Antigravity had run, so the Stage 2
  before Stage 3 ordering is not evidenced in this workspace. The Stage 2
  evidence file was written before the Antigravity output was opened and its
  findings were not revised after it; its ratings were entered at the same
  time as Stage 4's.
- **Not in the folder:** the Antigravity model-picker screenshot the
  instructions require, and any Antigravity run transcript.

## Run order

The task page sets the order, and it is the reverse of task 001:

| Stage | Action |
| --- | --- |
| 1 | Run the task natively inside the project (Gemini Native) |
| 2 | Rate Gemini Native, on its own |
| 3 | Run the task in Antigravity |
| 4 | Rate Antigravity, on its own |
| 5 | Overall preference and rationale |

Rate each response before running the next one, and rate it as it is, not
against the other. Task 001 ran Antigravity first, so the habit points the
wrong way here.

## Open questions for the user

1. Whether the instructions differ from the task 001 transcript.

Expertise confirmed by the user 2026-11-05: Immigration Law is within their
professional field.

## Next action

Re-enter the revised Gemini Native Professional Judgment (Good) and the revised
rationale on the platform, rerun Check Your Task, and record its result here.
Then submit.
