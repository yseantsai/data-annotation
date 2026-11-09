# Task NNN — Short title

- Category:
- Status: Not started
- Required harness order:
- Instruction source/version:
- Submission status: Not verified
- Authorship: LLM-generated and LLM-edited workspace materials

## Context

Describe the requested deliverable and link the task prompt, source materials, and any reference solution. Keep reference solutions separate from the prompt sent to evaluated models.

## Files

Paths below are relative to this task folder, once the template is copied to
`tasks/NNN-name/README.md`.

- Workflows: `../../docs/workflows/README.md`
- Prompt as given to both harnesses: `prompt.md`
- Reference solution, never sent to a model: `reference-solution.md`
- Input files as received (zip and unpacked files): `inputs/`
- Each result as received (result `.md`, output files, zip): `outputs/<harness>/`
- Evaluation: `evaluation/` (`rationale.md`, `confidence.md`, `ratings.md`, `checks/`,
  and `converted/` for the Markdown and page images the tools make)

Link actual files here once available. Do not duplicate shared instructions or rationale drafts in a context bundle.

## Progress

- [ ] Copy `templates/prompt.md` to `prompt.md`; record the exact prompt before any run
- [ ] Record source files and applicable instruction version
- [ ] Copy `templates/ratings.md` to `evaluation/ratings.md`
- [ ] Run first harness; preserve outputs and final message
- [ ] Inspect every output and record evidence for first ratings
- [ ] Run second harness with identical prompt and inputs
- [ ] Inspect every output and record evidence for second ratings
- [ ] Record comparison and uncertainties accurately
- [ ] `python3 tools/evalcheck.py tasks/NNN-name` clean of ERROR
- [ ] Shadow validators run on the finished text (`docs/validators/`)
- [ ] Platform Check Your Task run; confidence recorded (Very confident / Reasonably confident / Somewhat uncertain / Low confidence, plus the optional comment, in `evaluation/confidence.md`)
- [ ] Review checker feedback and record final status

## Handoff

State the next action, unresolved questions, and which checks have actually been completed. Link shared references only when applicable.

Distinguish what was observed from what was reported. A saved check result is a
historical result for the text as it stood, not a live check and not a record
of what the platform received.

## Known check findings

Any ERROR left standing, with the reason. Empty is normal.
