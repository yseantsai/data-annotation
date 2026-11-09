# Shadow validators

The platform judges a submission with model-driven checks we cannot call:
**Check Your Task** on the rationale, and the reviewer-side read for signs of
LLM use. These files reproduce what those checks ask for, so a finding arrives
before the platform's does.

They are **mocks**, in the precise sense: reconstructions from the platform
instructions and the prose references in `docs/reference/prose/`, not the platform's
implementation. A clean shadow run is evidence that the obvious failures are
absent. It is not a prediction of the platform's verdict, and it never
overrides the platform's actual result.

Each one shadows a check it cannot call, codes each rule to the failure that
produced it, and treats a clean local run as a floor.

## How to run one

A validator is a prompt with a fixed output contract, executed by a model
against the finished artifacts. Three rules make the result worth having:

1. **Run it on finished text.** A judge pointed at a draft grades the draft.
2. **Give it the artifacts, not your conclusion.** Hand over the rationale, the
   ratings and the outputs. Do not tell it what you think the answer is: a
   judge handed a hypothesis tends to return it confirmed.
3. **Keep the verdict separate from the fix.** Record the finding first, then
   decide. The instructions ask you to explain disagreement, not to edit until
   the checker is quiet.

A fresh session, or a subagent with no stake in the draft, gives a cleaner read
than the session that wrote it.

| Validator | Shadows | Blocks? |
| --- | --- | --- |
| [check-your-task.md](check-your-task.md) | the platform's Check Your Task | A Major blocks; the platform's own run decides |
| [authorship-read.md](authorship-read.md) | the reviewer "signs of LLM use" checklist | Advisory; A6/A10/A20/A33 carry the mechanical part |
