# Ratings — Task 002 (VAWA I-360)

Instruction source: `docs/reference/evaluation-instructions.md`
Rated on: 2026-11-05 (both stages; evidence in stage2-gemini-native.md and stage4-antigravity.md)

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

Columns are in run order: **Gemini Native is Stage 1 and rated at Stage 2**,
Antigravity is Stage 3 and rated at Stage 4.

Rate each result on its own, before running the next harness. Do not revise an
earlier column after seeing the later result; if a rating genuinely changes,
say so under Revisions below rather than overwriting it silently.

| Dimension | gemini-native | antigravity |
| --- | --- | --- |
| Instruction Following | Good | Good |
| Correctness | Good | Good |
| Professional Judgment | Good | Excellent |
| Format & Presentation | Acceptable | Acceptable |
| Overall quality (1-7) | 5 | 6 |

Preference: Antigravity is slightly better

One of the harness names above, or `Unsure or negligibly better`. `evalcheck`
E80 reads this line against the overall scores, so it has to name a column.

## Evidence for each rating

One line per rating that is not self-evident, naming the file and the location
that decided it. These lines are what the rationale is later built from.

- Instruction Following / gemini-native: neutral-language instruction broken in ten places, "Weaponization … and Sabotage" as a heading (§ III.6.B)
- Instruction Following / antigravity: same instruction broken in nine places, "Deliberate Sabotage" as a heading (§ III.7.B)
- Correctness / gemini-native: eleven Chapter 4–5 PDF page locators in the wrong chapter; seven over-statements (stage2 faults 1–10)
- Correctness / antigravity: all 32 Manual locators land; five over-statements, D.5(E) cited for the wrong proposition (stage4 faults 3–7)
- Professional Judgment / gemini-native: date-conflict reconciliation, marriage bars, Hale weighed against D.2(E)(2); calling three derivative accounts of the spitting "independent sources" (§ III.6.A) is an evidentiary judgment an officer would not sign, so Good rather than Excellent
- Professional Judgment / antigravity: date-conflict reconciliation, Desmond ¶10 candour, non-discretionary framing per D.5(D)(1), collateral actions
- Format & Presentation / gemini-native: 4,561 words, 91 code-font filenames, dual pagination, generic frame
- Format & Presentation / antigravity: garbled Bengali token at § III.7.C, 101 local-path hyperlinks

## Revisions

2026-11-05. Gemini Native Professional Judgment revised from Excellent to Good
after the platform's Check Your Task asked for the rating to be reconciled with
the rationale's findings. The over-statements were already carried under
Correctness and the headings under Instruction Following; the "independent
sources" characterisation is a judgment call on evidence weight, and Excellent
means it would go out as-is. It would not. Overall scores unchanged.

2026-11-05, later. Gemini Native overall revised from 6 to 5. The platform
form refuses any preference but "Unsure or negligibly better" when the two
overall scores are equal, and the rationale's case is that the difference is
real: Gemini Native's repair is eleven citations re-located, seven statements
re-checked and a cut by half, which is a rewrite, while Antigravity's is a
find-and-replace and one word. With Professional Judgment already at Good,
Gemini Native trails on one dimension and on the size of the rework, and 5
states that. Preference unchanged: Antigravity is slightly better.
