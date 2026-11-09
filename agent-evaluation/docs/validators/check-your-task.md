# Shadow validator: Check Your Task

Reconstruction of the platform's Stage 5 check, which "reviews your rationale
and whether it matches your ratings and preference". Not the platform's
implementation. See [README.md](README.md).

`tools/evalcheck.py` already settles the mechanical part: word count, both
harnesses named, per-result analysis present, location references, figure
traceability, preference against scores. Run it first. This validator reads
what a regex cannot: whether the reasons given actually support the ratings
given.

## Inputs to hand the judge

- `evaluation/rationale.md`
- `evaluation/ratings.md`
- both results: `outputs/<harness>/*.md`, or the Markdown in
  `evaluation/converted/<harness>/`, and the page images if presentation is at
  issue
- `evaluation/converted/inputs/*.md`
- the reference solution description, from the task's instruction source

Do not hand it your own view of which result is better.

## Prompt

> You are reviewing a professional's evaluation of two AI-produced
> deliverables, before it is submitted. You have the two deliverables, the
> source files they were produced from, the reference solution description, the
> evaluator's per-dimension ratings and their written rationale.
>
> The reference solution description is the minimum standard for a correct,
> complete result. It is not an answer key: a consequential error or strength
> it does not mention still counts.
>
> Check six things, in this order.
>
> 1. **Support.** Does every claim in the rationale hold up against the
>    deliverable it is about? Quote any claim that the file does not support,
>    and say what the file actually shows.
> 2. **Attribution.** Is every figure, section reference and quoted phrase
>    attributed to the result that actually contains it?
> 3. **Rating fit.** Does each dimension rating follow from the reasons given?
>    Name any rating the rationale does not account for, in either direction: a
>    low rating with no stated fault, or a high rating beside an unaddressed
>    one.
> 4. **Preference fit.** Does the stated preference follow from the ratings and
>    the reasons? If the overall scores and the preference disagree, say so.
> 5. **Omission.** Is there a consequential strength or error in either
>    deliverable that the rationale does not mention? Check the reference
>    solution's named requirements one by one against both deliverables.
> 6. **Scope.** Does the rationale critique the agent's process, speed or
>    reasoning style anywhere, rather than the deliverables? Quote it.
>
> Severity: **Major** where a finding would change a rating or the preference.
> **Minor** where it would change the wording but not the verdict.
>
> Report only what you can point at. For each finding give the file, the
> location, the quote, and what it should say instead. If a check passes, say
> it passes in one line and do not elaborate. Do not rewrite the rationale.

## Output contract

```json
{
  "validator": "check-your-task",
  "task": "NNN-name",
  "run": "YYYY-MM-DD",
  "findings": [
    {
      "check": "support|attribution|rating-fit|preference-fit|omission|scope",
      "severity": "Major|Minor",
      "artifact": "evaluation/rationale.md",
      "quote": "the text at issue",
      "evidence": "outputs/<harness>/... , what that file actually shows",
      "suggestion": "what it should say instead"
    }
  ],
  "passed": ["support", "scope"],
  "verdict": "clean|minor-only|major"
}
```

Save it as `evaluation/checks/check-your-task-<date>.json`. Like every file in
that directory, it is a historical result for the text as it stood, not a live
check and not a submission record.

## Reading the result

A Major is a reason to look again, not an instruction to edit. The platform's
own run is the one that counts, and the instructions say to explain
disagreement rather than comply with it. If you keep the text as it is, write
the reason into the task README, where the next session will find it.
