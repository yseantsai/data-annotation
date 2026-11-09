#!/usr/bin/env python3
"""Prove the checks are live: run them on the tripwire fixture and compare codes.

    python3 tools/selftest.py

A checker that never fires is indistinguishable from a checker that passes. The
fixture in tools/check_fixtures/tripwire is written to trip one of each code.
Exit 1 if an expected code went silent or an unexpected one appeared.

A21 is deliberately absent from the expectation: it needs twenty or more
sentences in one document before it will measure a share, and no rationale this
workspace writes is that long. It is carried so a long output document is still
read against it.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from evalcheck import TaskContext, run  # noqa: E402

FIXTURE = Path(__file__).resolve().parent / "check_fixtures" / "tripwire"

EXPECTED_ERRORS = {"A6", "A10", "A20", "E05", "E06", "E10", "E20", "E30", "E40", "E50", "E60", "E70", "E80"}
EXPECTED_NOTES = {"A32", "A33"}
NOT_EXPECTED_SILENT = {"A21"}   # documented above, not a failure


def main():
    if not FIXTURE.is_dir():
        print("missing fixture %s" % FIXTURE, file=sys.stderr)
        return 2
    report = run(TaskContext(FIXTURE))
    errors = set(f.code for f in report.of("ERROR"))
    notes = set(f.code for f in report.of("NOTE"))

    ok = True
    for label, got, want in (("ERROR", errors, EXPECTED_ERRORS),
                             ("NOTE", notes, EXPECTED_NOTES)):
        silent = sorted(want - got)
        extra = sorted(got - want - NOT_EXPECTED_SILENT)
        if silent:
            ok = False
            print("%s codes expected but silent: %s" % (label, ", ".join(silent)))
        if extra:
            ok = False
            print("%s codes fired unexpectedly: %s" % (label, ", ".join(extra)))
    if ok:
        print("selftest ok: %d error codes and %d note codes fired on the tripwire fixture"
              % (len(errors), len(notes)))
        print("  errors: %s" % ", ".join(sorted(errors)))
        print("  notes:  %s" % ", ".join(sorted(notes)))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
