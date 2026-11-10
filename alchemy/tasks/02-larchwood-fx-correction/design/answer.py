#!/usr/bin/env python3
"""Worked answer for task 02: Larchwood Fly Supply, September FX settlement correction.

    python3 tasks/02-larchwood-fx-correction/design/answer.py            # build the reference, answer it
    python3 tasks/02-larchwood-fx-correction/design/answer.py --inputs   # answer the shipped CSV in inputs/

The scenario. Halvard Payments settles Larchwood's CAD, CHF, EUR and GBP card sales in USD. On
2026-09-01 a new reference-rate feed went live. It quotes in market convention: EUR/USD and GBP/USD
are USD per unit of the foreign currency, but USD/CAD and USD/CHF are units of the foreign currency
per USD. Billing kept multiplying gross_local by ref_rate for every currency, the old feed's
convention. EUR and GBP are right; CAD is overpaid (multiplied by about 1.37 instead of divided)
and CHF is underpaid (multiplied by about 0.88 instead of divided).

The agreement (Schedule C, item 2): converted to USD at the Halvard Reference Rate for the batch
date, less an FX margin of 1.20% of the converted amount. Section 7.3: Halvard may recover any
overpayment by deducting it from later settlement funds.

The merchant has complained only about the CHF shortfall, and the account manager has promised to
credit it with the October 6 settlement. The correct answer nets the CAD overpayment against it.
"""
import csv
import datetime as dt
import io
import random
import sys
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

HERE = Path(__file__).resolve().parent
TASK = HERE.parent
REF_CSV = HERE / "larchwood_fx_settlements_reference.csv"
MARGIN = Decimal("0.012")
USD_BASE = {"CAD", "CHF"}          # market convention: quoted as foreign units per USD
USD_QUOTE = {"EUR", "GBP"}         # quoted as USD per foreign unit
PAIR = {"CAD": "USD/CAD", "CHF": "USD/CHF", "EUR": "EUR/USD", "GBP": "GBP/USD"}


def q(x, places="0.01"):
    return x.quantize(Decimal(places), rounding=ROUND_HALF_UP)


def build_reference():
    rng = random.Random(20260930)
    batches = [dt.date(2026, 9, d) for d in (1, 4, 8, 11, 15, 18, 22, 25, 29)] + [dt.date(2026, 10, 2)]
    level = {"CAD": 1.3684, "CHF": 0.8807, "EUR": 1.0861, "GBP": 1.2714}
    vol = {"CAD": (9800, 15400), "CHF": (2600, 4900), "EUR": (2900, 5600), "GBP": (1700, 3600)}
    rows = []
    n = 0
    for b in batches:
        for cur in ("CAD", "CHF", "EUR", "GBP"):
            level[cur] *= 1 + rng.uniform(-0.0031, 0.0031)
            rate = Decimal(f"{level[cur]:.4f}")
            gross = q(Decimal(str(rng.uniform(*vol[cur]))))
            txn = max(9, int(float(gross) / rng.uniform(118, 164)))
            usd = q(gross * rate)                      # billing multiplied for every currency
            margin = q(usd * MARGIN)
            n += 1
            pay = b + dt.timedelta(days=1 if b.weekday() < 4 else 4)
            rows.append(dict(batch_date=b.isoformat(), currency=cur, txn_count=txn, gross_local=gross,
                             ref_rate=rate, usd_converted=usd, fx_margin=margin, usd_settled=usd - margin,
                             payout_date=pay.isoformat(),
                             payout_status="PENDING" if b.month == 10 else "PAID",
                             payout_ref=f"PO-{pay.strftime('%m%d')}-{7310 + n}"))
    pre = [["Halvard Payments multi-currency settlement detail"],
           ["Merchant: LARCHWOOD FLY SUPPLY LLC", "MID 4410-3176", "Agreement MA-2023-0291"],
           ["Range: 2026-09-01 to 2026-10-02", "Run 2026-10-05 07:58 MT", "User icalloway"],
           ["Rate source: Halvard Reference Rate", "FX margin 1.20%"],
           []]
    with open(REF_CSV, "w", newline="") as f:
        csv.writer(f).writerows(pre)
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        for r in rows:
            w.writerow({k: (str(v) if isinstance(v, Decimal) else v) for k, v in r.items()})
    return REF_CSV


def load(path):
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    start = next(i for i, ln in enumerate(lines) if ln.startswith("batch_date"))
    return list(csv.DictReader(io.StringIO("\n".join(lines[start:]))))


def net_correct(r):
    cur, gross, rate = r["currency"], Decimal(r["gross_local"]), Decimal(r["ref_rate"])
    c = q(gross / rate) if cur in USD_BASE else q(gross * rate)
    return c - q(c * MARGIN)


def answer(rows):
    by = {}
    pending = [r for r in rows if r.get("payout_status") == "PENDING"]
    rows = [r for r in rows if r.get("payout_status") != "PENDING"]
    for r in rows:
        cur, gross, rate = r["currency"], Decimal(r["gross_local"]), Decimal(r["ref_rate"])
        correct = q(gross / rate) if cur in USD_BASE else q(gross * rate)
        correct_net = correct - q(correct * MARGIN)
        diff = correct_net - Decimal(r["usd_settled"])           # + owed to merchant, - overpaid
        d = by.setdefault(cur, dict(gross=Decimal(0), settled=Decimal(0), correct=Decimal(0), diff=Decimal(0)))
        d["gross"] += gross
        d["settled"] += Decimal(r["usd_settled"])
        d["correct"] += correct_net
        d["diff"] += diff
    net = sum(d["diff"] for d in by.values())
    oct_billed = sum(Decimal(r["usd_settled"]) for r in pending)
    oct_correct = sum(net_correct(r) for r in pending)
    funds = oct_correct + by["CHF"]["diff"]            # 7.3: underpayment paid with the next settlement
    overpaid = -by["CAD"]["diff"]
    applied = min(funds, overpaid)                      # 7.3 and 7.4: overpayment deducted from settlement funds
    oct6 = dict(billed=oct_billed, correct=oct_correct, funds=funds, applied=applied, payout=funds - applied,
                carried=overpaid - applied, pending=pending)
    return by, net, oct6


def main(argv):
    path = None
    if "--inputs" in argv:
        cands = list((TASK / "inputs").glob("*.csv"))
        if len(cands) != 1:
            print(f"expected one CSV in inputs/, found {len(cands)}")
            return 2
        path = cands[0]
    else:
        path = build_reference()
    by, net, oct6 = answer(load(path))
    print(f"source: {path.name}")
    print(f"{'cur':4s} {'gross local':>14s} {'USD settled':>14s} {'USD correct':>14s} {'difference':>13s}")
    for cur in ("CAD", "CHF", "EUR", "GBP"):
        d = by[cur]
        print(f"{cur:4s} {d['gross']:>14,.2f} {d['settled']:>14,.2f} {d['correct']:>14,.2f} {d['diff']:>13,.2f}")
    print(f"CHF shortfall owed to Larchwood:   ${by['CHF']['diff']:,.2f}")
    print(f"CAD overpayment owed to Halvard:   ${-by['CAD']['diff']:,.2f}")
    print(f"EUR and GBP differences:           ${by['EUR']['diff']:,.2f} and ${by['GBP']['diff']:,.2f}")
    print(f"NET: Larchwood owes Halvard        ${-net:,.2f}" if net < 0 else f"NET: Halvard owes Larchwood ${net:,.2f}")
    print(f"Oct 2 batch (pays Oct 6): billed ${oct6['billed']:,.2f}, correct ${oct6['correct']:,.2f}")
    print(f"Oct 6 funds before recovery:       ${oct6['funds']:,.2f}  (correct Oct 2 batch + Sept CHF shortfall)")
    print(f"CAD overpayment applied on Oct 6:  ${oct6['applied']:,.2f}")
    print(f"OCT 6 PAYOUT TO LARCHWOOD:         ${oct6['payout']:,.2f}")
    print(f"STILL OWED BY LARCHWOOD AFTER OCT 6: ${oct6['carried']:,.2f}  (deducted from later settlements)")
    print("likely wrong answers:")
    print(f"    pay the Oct 2 batch as billed plus the CHF credit: ${oct6['billed'] + by['CHF']['diff']:,.2f}")
    print(f"    pay the correct Oct 2 batch plus the CHF credit:   ${oct6['correct'] + by['CHF']['diff']:,.2f}")
    print(f"    credit the CHF shortfall only:  Halvard pays ${by['CHF']['diff']:,.2f}, ${-by['CAD']['diff']:,.2f} left uncollected")
    print("    multiply every rate (as billing did): no difference found on any currency")
    print(f"    divide every rate: EUR and GBP also look wrong")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
