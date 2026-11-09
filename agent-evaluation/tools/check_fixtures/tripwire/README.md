# Fixture: tripwire

Not a real task, and not under `tasks/`, so no default run picks it up.

A deliberately defective evaluation that every E-code and the A-codes
must fire on. `tools/selftest.py` runs the checks against it and compares the
codes that fired to the ones it expects, so a checker that has gone silent is
distinguishable from a checker that is passing.

The expected codes live in `tools/selftest.py`, not in this folder. A21 is
deliberately not among them: it needs twenty or more sentences in one document
before it measures anything, which no rationale here reaches.

Add a defect here whenever a check is added, and add its code to the
expectation in the same change.
