# Ratings — Task NNN

Instruction source: `docs/reference/evaluation-instructions.md`
Rated on: YYYY-MM-DD

Fill one column per harness, named exactly as its folder under `outputs/`.
Dimensions use the platform's five-point scale: Poor, Below par, Acceptable,
Good, Excellent. The form's anchors: **Excellent** means a strong professional
would hand it in as-is on this dimension; **Acceptable** means it does the job
with rough edges; **Poor** means it would be sent back. Rate each dimension
alone, and route issues to the dimension that owns them: inaccurate content to
Correctness, poor domain choices or framing to Professional Judgment,
structural or visual quality to Format & Presentation unless the prompt
explicitly required the feature, in which case it stays under Instruction
Following.
Overall quality is 1 (unacceptable) to 7 (exemplary, you would hand it in as-is).

Rate each result on its own, before running the next harness. Do not revise an
earlier column after seeing the later result; if a rating genuinely changes,
say so under Revisions below rather than overwriting it silently.

| Dimension | antigravity | gemini-native |
| --- | --- | --- |
| Instruction Following |  |  |
| Correctness |  |  |
| Professional Judgment |  |  |
| Format & Presentation |  |  |
| Overall quality (1-7) |  |  |

Preference:

One of the platform's eight options, in its exact words, with the harness
named as on the form (captured 2026-11-05):

- `<Harness> is much better`
- `<Harness> is better`
- `<Harness> is slightly better`
- `Unsure or <Harness> is negligibly better`

"Slightly better" is a real preference with a small margin. The Unsure option
is only for two results that are almost equal, and the rationale then has to
say which way it leaned. `evalcheck` E80 reads this line against the overall
scores, so it has to name a harness.

## Evidence for each rating

One line per rating that is not self-evident, naming the file and the location
that decided it. These lines are what the rationale is later built from.

- Instruction Following / <harness>:
- Correctness / <harness>:
- Professional Judgment / <harness>:
- Format & Presentation / <harness>:

## Revisions

Date, what changed, and why. Empty is normal.
