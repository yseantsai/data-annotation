#!/usr/bin/env python3
"""Check task 02's two input files, then print the answer computed from them.

    python3 tasks/02-larchwood-fx-correction/design/verify_inputs.py

Data file (the CSV in inputs/):
  - every usd_converted equals gross_local x ref_rate rounded to the cent (billing's multiply-every-rate
    error, which the task turns on), fx_margin is 1.20% of it rounded to the cent, and usd_settled is
    the difference
  - ref_rate sits in the market-convention band for its currency (USD/CAD and USD/CHF as foreign units
    per USD, EUR/USD and GBP/USD as USD per unit)
  - September rows are PAID and the October 2 rows PENDING for October 6
Context file (the other input):
  - carries each fact the answer depends on, and none of the answer's own figures or reasoning
Exit status 1 on any finding.
"""
import re
import sys
from decimal import Decimal
from pathlib import Path

HERE = Path(__file__).resolve().parent
TASK = HERE.parent
sys.path.insert(0, str(TASK.parent.parent / "tools"))
sys.path.insert(0, str(HERE))
import alchemy_check as ac  # noqa: E402
import answer as ans  # noqa: E402

BANDS = {"CAD": (Decimal("1.30"), Decimal("1.45")), "CHF": (Decimal("0.83"), Decimal("0.93")),
         "EUR": (Decimal("1.03"), Decimal("1.13")), "GBP": (Decimal("1.20"), Decimal("1.33"))}
CONTEXT_FACTS = [
    ("market convention", r"market convention"),
    ("the four pairs named", r"USD/CAD.{0,20}USD/CHF|USD/CHF.{0,20}USD/CAD"),
    ("feed live September 1", r"September 1"),
    ("nothing else in billing changed", r"[Nn]othing else"),
    ("the CHF complaint", r"Swiss franc|CHF shortfall"),
    ("CAD said to look fine", r"Canadian.{0,40}fine"),
    ("the promise for October 6", r"October 6"),
    ("Schedule C conversion and margin", r"1\.20% of the converted amount"),
    ("rounding rule", r"rounded to the nearest cent"),
    ("7.3 shall recover", r"shall recover any amount overpaid"),
    ("7.4 set-off", r"set off any amount"),
]
CONTEXT_LEAKS = [
    ("states a corrected figure", r"69,80\d|61,38\d|35,89\d|8,42\d\.\d\d|25,48\d"),
    ("mentions a CAD overpayment", r"(?:Canadian|CAD)[^.]{0,60}overpa|overpa[^.]{0,60}(?:Canadian|CAD)"),
    ("explains the conversion direction", r"\bdivid|\binvert|per US dollar|per USD\b|units? per"),
    ("placeholder email domain", r"@[\w.-]+\.(?:example|invalid|test)\b"),
]


def main():
    bad = 0
    cands = list((TASK / "inputs").glob("*.csv"))
    if len(cands) != 1:
        print(f"expected one CSV in inputs/, found {len(cands)}")
        return 2
    data = cands[0]
    rows = ans.load(data)
    for r in rows:
        tag = f"{r['batch_date']} {r['currency']}"
        g, rate = Decimal(r["gross_local"]), Decimal(r["ref_rate"])
        conv, mar, sett = Decimal(r["usd_converted"]), Decimal(r["fx_margin"]), Decimal(r["usd_settled"])
        if ans.q(g * rate) != conv:
            print(f"{tag}: usd_converted {conv} but gross x rate is {ans.q(g * rate)}")
            bad += 1
        if ans.q(conv * ans.MARGIN) != mar:
            print(f"{tag}: fx_margin {mar} but 1.20% of usd_converted is {ans.q(conv * ans.MARGIN)}")
            bad += 1
        if conv - mar != sett:
            print(f"{tag}: usd_settled {sett} but usd_converted - fx_margin is {conv - mar}")
            bad += 1
        lo, hi = BANDS[r["currency"]]
        if not lo <= rate <= hi:
            print(f"{tag}: ref_rate {rate} outside the market-convention band {lo} to {hi}")
            bad += 1
        want = "PENDING" if r["batch_date"].startswith("2026-10") else "PAID"
        if r["payout_status"] != want:
            print(f"{tag}: payout_status {r['payout_status']}, the design wants {want}")
            bad += 1
    pend = [r for r in rows if r["payout_status"] == "PENDING"]
    if len(rows) != 40 or len(pend) != 4 or any(r["payout_date"] != "2026-10-06" for r in pend):
        print(f"rows {len(rows)} (want 40), PENDING {len(pend)} (want 4, paying 2026-10-06)")
        bad += 1
    print(f"data file {data.name}: {len(rows)} rows, " + ("arithmetic, rates and statuses hold" if not bad else f"{bad} finding(s)"))

    for p in sorted((TASK / "inputs").iterdir()):
        if p == data or not p.is_file() or p.name.startswith("."):
            continue
        rep = ac.Report()
        _, text, _ = ac.read_input(p, rep, p.name)
        before = bad
        for label, rx in CONTEXT_FACTS:
            if not re.search(rx, text, re.S):
                print(f"context {p.name}: missing {label}")
                bad += 1
        for label, rx in CONTEXT_LEAKS:
            hit = re.search(rx, text, re.I)
            if hit:
                print(f'context {p.name}: {label} ("{hit.group(0)}")')
                bad += 1
        print(f"context file {p.name}: {len(ac.words(text))} words, "
              + ("facts present, nothing leaks" if bad == before else "see findings above"))
    print()
    sys.argv = [sys.argv[0], "--inputs"]
    ans.main(sys.argv)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
