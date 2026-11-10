#!/usr/bin/env python3
"""Check task 01's two input files: the export's arithmetic and traps, and the thread's facts.

    python3 tasks/01-kestrel-final-settlement/design/verify_inputs.py

Data file (the CSV in inputs/):
  - every net_settlement equals gross - refunds - chargebacks - chargeback fees - processing fees
    - reserve hold + reserve release
  - every reserve_balance equals the previous balance + hold - release, starting from the header's
    opening balance
  - processing fees tie to 2.90% + $0.30 through 2026-09-21 and 2.40% + $0.30 from 2026-09-22
    (the late billing load the task turns on)
  - the traps are present: two HELD-TERM batches, one SCHEDULED release, one PENDING chargeback
Context file (the other input):
  - carries each fact the answer depends on, and none of the answer's own figures or verdict
  - no placeholder email domains
Then prints the answer from design/answer_inputs.py. Exit status 1 on any finding.
"""
import datetime as dt
import re
import sys
from decimal import Decimal
from pathlib import Path

HERE = Path(__file__).resolve().parent
TASK = HERE.parent
sys.path.insert(0, str(TASK.parent.parent / "tools"))
sys.path.insert(0, str(HERE))
import alchemy_check as ac  # noqa: E402
import answer_inputs as ans  # noqa: E402

CONTEXT_FACTS = [
    ("2.40% rate", r"2\.40\s?%"),
    ("effective September 15", r"September 15"),
    ("billing load date (the 22nd)", r"September 22|the 22nd"),
    ("termination date September 30", r"September 30"),
    ("Section 11.4 retention including scheduled releases", r"otherwise be released"),
    ("180 days", r"one hundred eighty|180"),
    ("Section 11.6 set-off order", r"first from settlement funds"),
    ("Darren's promise of the October 1 release", r"scheduled for October 1"),
    ("the returned payout and its code", r"PO-0929-5628.{0,40}R02"),
    ("chargeback fees not refundable", r"not refundable"),
]
CONTEXT_LEAKS = [
    ("states the payout", r"41,31\d\.\d\d|19,07\d\.\d\d|17,25\d\.\d\d"),
    ("states the returned amount", r"22,238\.43"),
    ("explains the return code", r"account (?:was )?closed|closed account"),
    ("states the fee credit", r"273\.8\d"),
    ("says to hold the reserve", r"\b(?:hold|retain|keep) (?:the|all|their) (?:entire |whole |full )?reserve\b"),
    ("states the release date", r"March 29, 2027"),
    ("points at the fee check", r"pricing check|check the (?:fees|pricing|rate)|overcharg"),
    ("placeholder email domain", r"@[\w.-]+\.(?:example|invalid|test)\b"),
]


def main():
    bad = 0
    data = ans.DATA
    rows = ans.load(data)
    header = data.read_text(encoding="utf-8-sig").split("batch_date")[0]
    m = re.search(r"opening[_ ]reserve[_ ]balance\D*([\d,]+\.\d\d)", header, re.I)
    prev = Decimal(m.group(1).replace(",", "")) if m else None
    if prev is None:
        print("header: no opening reserve balance")
        bad += 1
    for r in rows:
        v = lambda k: ans.val(r, k)  # noqa: E731
        d = r["batch_date"]
        net = (v("gross_sales") - v("refunds") - v("chargebacks") - v("chargeback_fees") - v("processing_fees")
               - v("reserve_hold") + v("reserve_release"))
        if net != v("net_settlement"):
            print(f"{d}: net_settlement {v('net_settlement')} but the columns give {net}")
            bad += 1
        if prev is not None and prev + v("reserve_hold") - v("reserve_release") != v("reserve_balance"):
            print(f"{d}: reserve_balance {v('reserve_balance')} but the running balance gives "
                  f"{prev + v('reserve_hold') - v('reserve_release')}")
            bad += 1
        prev = v("reserve_balance")
        if r["txn_count"] != "0":
            rate = ans.OLD if dt.date.fromisoformat(d) < ans.BILLING_LIVE else ans.NEW
            fee = ans.q(v("gross_sales") * rate + ans.PER_TXN * int(r["txn_count"]))
            if fee != v("processing_fees"):
                print(f"{d}: processing_fees {v('processing_fees')} but {rate * 100}% + $0.30 gives {fee}")
                bad += 1
    counts = {s: sum(r["payout_status"] == s for r in rows) for s in ("HELD-TERM", "SCHEDULED", "PENDING")}
    for s, want in (("HELD-TERM", 2), ("SCHEDULED", 1), ("PENDING", 1)):
        if counts[s] != want:
            print(f"status {s}: {counts[s]} row(s), the design wants {want}")
            bad += 1
    print(f"data file {data.name}: {len(rows)} rows, " + ("arithmetic and traps hold" if not bad else f"{bad} finding(s)"))

    for p in sorted((TASK / "inputs").iterdir()):
        if p == data or not p.is_file() or p.name.startswith("."):
            continue
        rep = ac.Report()
        _, text, _ = ac.read_input(p, rep, p.name)
        for label, rx in CONTEXT_FACTS:
            if not re.search(rx, text, re.I):
                print(f"context {p.name}: missing {label}")
                bad += 1
        for label, rx in CONTEXT_LEAKS:
            hit = re.search(rx, text, re.I)
            if hit:
                print(f'context {p.name}: {label} ("{hit.group(0)}")')
                bad += 1
        print(f"context file {p.name}: {len(ac.words(text))} words, "
              + ("facts present, nothing leaks" if not bad else "see findings above"))
    print()
    ans.main()
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
