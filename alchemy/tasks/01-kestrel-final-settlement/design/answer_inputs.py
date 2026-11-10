#!/usr/bin/env python3
"""Worked answer for task 01, computed from the actual data file in inputs/.

    python3 tasks/01-kestrel-final-settlement/design/answer_inputs.py

The File Builder rebuilt the export's batch rows itself (the reference table did not reach it),
so the answer is computed from the shipped file, not from design/answer.py's reference ledger.
Same rules as answer.py:

  11.5 unpaid settlement funds (HELD-TERM batches) are paid, plus amounts owed to the merchant
  fee  2.40% + $0.30 applies from 2026-09-15; billing loaded it 2026-09-22, so the 09-15 to 09-21
       batches were charged at 2.90%: the difference is owed to the merchant
  11.6 amounts owed by the merchant on or after termination (the PENDING chargeback and its fee)
       come out of unpaid settlement funds first
  11.4 the reserve held at termination is retained in full, including the SCHEDULED release,
       until 2026-09-30 + 180 days = 2027-03-29
Charges already netted inside a batch (the 2026-09-30 chargeback) are not deducted again.
Round 2: the treasury email of 2026-10-02 reports payout PO-0929-5628 (the 2026-09-28 batch) returned
as ACH R02 (account closed). The export still shows it PAID; its net is owed to Kestrel again (11.5,
"any other amounts owed to Merchant"). Chargeback fees are not refundable (Schedule A item 2), so the
dsp-207561 fee is not credited back.
"""
import csv
import datetime as dt
import io
import sys
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

TASK = Path(__file__).resolve().parent.parent
DATA = TASK / "inputs" / "settlement_export_MID44102287_20260901_20261002.csv"
OLD, NEW, PER_TXN = Decimal("0.029"), Decimal("0.024"), Decimal("0.30")
AMEND_FROM, BILLING_LIVE = dt.date(2026, 9, 15), dt.date(2026, 9, 22)
TERMINATION = dt.date(2026, 9, 30)
RETURNED_REFS = {"PO-0929-5628": "R02"}


def q(x):
    return x.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def load(path=DATA):
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    start = next(i for i, ln in enumerate(lines) if ln.startswith("batch_date"))
    return list(csv.DictReader(io.StringIO("\n".join(lines[start:]))))


def val(r, k):
    return Decimal(r[k] or "0")


def answer(rows):
    held = [r for r in rows if r["payout_status"] == "HELD-TERM"]
    pending = [r for r in rows if r["payout_status"] == "PENDING"]
    scheduled = [r for r in rows if r["payout_status"] == "SCHEDULED"]
    unpaid = sum(val(r, "net_settlement") for r in held)
    over = []
    for r in rows:
        d = dt.date.fromisoformat(r["batch_date"])
        if r["txn_count"] != "0" and AMEND_FROM <= d < BILLING_LIVE:
            correct = q(val(r, "gross_sales") * NEW + PER_TXN * int(r["txn_count"]))
            over.append((r["batch_date"], val(r, "processing_fees"), correct, val(r, "processing_fees") - correct,
                         val(r, "gross_sales")))
    credit = sum(o[3] for o in over)
    credit_once = q(sum(o[4] for o in over) * (OLD - NEW))
    owed = sum(val(r, "chargebacks") + val(r, "chargeback_fees") for r in pending)
    close = next(r for r in rows if r["batch_date"] == TERMINATION.isoformat())
    returned = [r for r in rows if r["payout_ref"] in RETURNED_REFS]
    back = sum(val(r, "net_settlement") for r in returned)
    return dict(held=held, unpaid=unpaid, over=over, credit=credit, credit_once=credit_once, pending=pending,
                owed=owed, scheduled=scheduled, reserve=val(close, "reserve_balance"), returned=returned, back=back,
                payout=unpaid + back + credit - owed, payout_once=unpaid + back + credit_once - owed,
                release_date=TERMINATION + dt.timedelta(days=180), close=close)


def main():
    rows = load()
    a = answer(rows)
    print(f"unpaid settlement (HELD-TERM):     ${a['unpaid']:,.2f}  "
          f"({', '.join('{} ${:,.2f}'.format(r['batch_date'], val(r, 'net_settlement')) for r in a['held'])})")
    for r in a["returned"]:
        print(f"returned payout {r['payout_ref']} ({RETURNED_REFS[r['payout_ref']]}): batch {r['batch_date']}, "
              f"${val(r, 'net_settlement'):,.2f} owed again")
    print("fee overcharge by batch (charged, correct, over):")
    for b, ch, co, ov, _ in a["over"]:
        print(f"    {b}  ${ch:,.2f}  ${co:,.2f}  ${ov:,.2f}")
    print(f"fee credit owed to Kestrel:        ${a['credit']:,.2f}  (0.50% applied once: ${a['credit_once']:,.2f})")
    for r in a["pending"]:
        print(f"post-termination chargeback + fee: ${val(r, 'chargebacks'):,.2f} + ${val(r, 'chargeback_fees'):,.2f}"
              f" = ${a['owed']:,.2f}  ({r['memo']})")
    print(f"already netted in the 09-30 batch: chargeback ${val(a['close'], 'chargebacks'):,.2f} + fee "
          f"${val(a['close'], 'chargeback_fees'):,.2f} (not deducted again)")
    print(f"FINAL PAYOUT NOW:                  ${a['payout']:,.2f}  (or ${a['payout_once']:,.2f})")
    for r in a["scheduled"]:
        print(f"scheduled release retained:        ${val(r, 'reserve_release'):,.2f}  ({r['memo']})")
    print(f"RESERVE RETAINED:                  ${a['reserve']:,.2f} until {a['release_date'].isoformat()}")
    late = sum(q(val(r, "gross_sales") * (OLD - NEW)) for r in rows
               if r["txn_count"] != "0" and dt.date.fromisoformat(r["batch_date"]) >= AMEND_FROM)
    sched = sum(val(r, "reserve_release") for r in a["scheduled"])
    print("likely wrong answers:")
    print(f"    returned payout missed:            ${a['payout'] - a['back']:,.2f}")
    print(f"    returned payout missed, +$25 fee:  ${a['payout'] - a['back'] + 25:,.2f}  (run 1's answer)")
    print(f"    dsp-207561 fee credited back:      ${a['payout'] + 25:,.2f}")
    print(f"    fee credit over 09-15 to 09-30:    ${late:,.2f}")
    print(f"    payout incl. Oct 1 release:        ${a['payout'] + sched:,.2f}")
    print(f"    payout incl. whole reserve:        ${a['payout'] + a['reserve']:,.2f}")
    print(f"    09-30 chargeback deducted twice:   ${a['payout'] - val(a['close'], 'chargebacks') - val(a['close'], 'chargeback_fees'):,.2f}")
    print(f"    Oct 2 chargeback from the reserve: ${a['unpaid'] + a['back'] + a['credit']:,.2f} paid, reserve "
          f"${a['reserve'] - a['owed']:,.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
