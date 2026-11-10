#!/usr/bin/env python3
"""Worked answer for task 01: Kestrel Ridge Outfitters final settlement.

    python3 tasks/01-kestrel-final-settlement/design/answer.py

Builds the reference settlement export (design/kestrel_settlements_reference.csv) that the data
file must match, and prints every figure the rubric uses. Deterministic: same output every run.

Contract terms (context file):
  6.2  rolling reserve: 10% of each batch's gross held, released 90 days after the batch date
  fee  2.90% + $0.30 per transaction; amendment: 2.40% + $0.30 for transactions processed on or
       after 2026-09-15. Billing loaded the new rate on 2026-09-22, so the 09-15 to 09-21 batches
       were charged at 2.90%.
  11.4 on termination all reserve funds then held, including amounts scheduled for release after
       the Termination Date, are retained until 180 days after it (2026-09-30 + 180 = 2027-03-29)
  11.5 unpaid settlement funds plus amounts owed to the merchant are paid within 10 business days
  11.6 amounts owed by the merchant on or after termination come first out of unpaid settlement
       funds, then out of the reserve
"""
import csv
import datetime as dt
import random
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

HERE = Path(__file__).resolve().parent
C = Decimal("0.01")


def money(x):
    return Decimal(str(x)).quantize(C, rounding=ROUND_HALF_UP)


OLD, NEW, PER_TXN = Decimal("0.029"), Decimal("0.024"), Decimal("0.30")
AMEND_FROM = dt.date(2026, 9, 15)
BILLING_LIVE = dt.date(2026, 9, 22)
TERMINATION = dt.date(2026, 9, 30)
HOLIDAYS = {dt.date(2026, 9, 7)}
OPENING_RESERVE = money("78904.17")

rng = random.Random(20260930)
days = [dt.date(2026, 9, d) for d in range(1, 31)]
days = [d for d in days if d.weekday() < 5 and d not in HOLIDAYS]

refund_days = {dt.date(2026, 9, 3): "214.50", dt.date(2026, 9, 9): "89.99", dt.date(2026, 9, 14): "412.80",
               dt.date(2026, 9, 17): "159.00", dt.date(2026, 9, 23): "64.95", dt.date(2026, 9, 28): "327.40"}
cb_days = {dt.date(2026, 9, 10): "389.95", dt.date(2026, 9, 24): "1214.00", dt.date(2026, 9, 28): "-1214.00"}
cb_memo = {dt.date(2026, 9, 10): "cb dsp-206904", dt.date(2026, 9, 24): "cb dsp-207561",
           dt.date(2026, 9, 28): "cb reversal dsp-207561 rep won, cb fee not refunded"}
refund_memo = {dt.date(2026, 9, 14): "rfnd x3", dt.date(2026, 9, 3): "rfnd x2"}

rows = []
reserve = OPENING_RESERVE
for i, d in enumerate(days):
    monday = d.weekday() == 0
    n = rng.randint(118, 164) if monday else rng.randint(61, 104)
    gross = money(n * rng.uniform(104, 131))
    refunds = money(refund_days.get(d, "0"))
    cb = money(cb_days.get(d, "0"))
    cb_fee = money("15.00") if cb > 0 else money("0")
    charged_rate = NEW if d >= BILLING_LIVE else OLD
    fee = money(gross * charged_rate + PER_TXN * n)
    hold = money(gross * Decimal("0.10"))
    release = money(rng.uniform(842, 1688))
    net = gross - refunds - cb - cb_fee - fee - hold + release
    reserve = reserve + hold - release
    if d < dt.date(2026, 9, 29):
        status, ref = "PAID", f"PO-{(d + dt.timedelta(days=1 if d.weekday() < 4 else 3)).strftime('%m%d')}-{4471 + i}"
    else:
        status, ref = "HELD-TERM", ""
    rows.append(dict(batch_date=d.isoformat(), txn_count=n, gross_sales=gross, refunds=refunds, chargebacks=cb,
                     chargeback_fees=cb_fee, processing_fees=fee, reserve_hold=hold, reserve_release=release,
                     net_settlement=net, reserve_balance=reserve, payout_status=status, payout_ref=ref,
                     memo=cb_memo.get(d) or refund_memo.get(d, "")))

reserve_at_term = reserve
oct1_release = money("1371.86")  # 10% of the 2026-07-03 batch, scheduled by the system
rows.append(dict(batch_date="2026-10-01", txn_count=0, gross_sales=money(0), refunds=money(0), chargebacks=money(0),
                 chargeback_fees=money(0), processing_fees=money(0), reserve_hold=money(0),
                 reserve_release=oct1_release, net_settlement=oct1_release,
                 reserve_balance=reserve_at_term - oct1_release, payout_status="SCHEDULED", payout_ref="",
                 memo="auto rsv release batch 2026-07-03"))
cb_post, cb_post_fee = money("642.18"), money("15.00")
rows.append(dict(batch_date="2026-10-02", txn_count=0, gross_sales=money(0), refunds=money(0), chargebacks=cb_post,
                 chargeback_fees=cb_post_fee, processing_fees=money(0), reserve_hold=money(0),
                 reserve_release=money(0), net_settlement=-(cb_post + cb_post_fee),
                 reserve_balance=reserve_at_term - oct1_release, payout_status="PENDING", payout_ref="",
                 memo="cb dsp-208813 orig txn 2026-08-18"))

PREAMBLE = [
    ["Halvard Payments merchant settlement export"],
    ["Merchant: KESTREL RIDGE OUTFITTERS LLC", "MID 4410-2287", "Agreement MA-2022-0417"],
    ["Range: 2026-09-01 to 2026-10-02", "Run 2026-10-05 08:12 MT", "User icalloway"],
    ["Opening reserve balance 2026-09-01: 78904.17", "Reserve rate 10.00%", "Release lag 90 days"],
    [],
]
with open(HERE / "kestrel_settlements_reference.csv", "w", newline="") as f:
    csv.writer(f).writerows(PREAMBLE)
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader()
    for r in rows:
        w.writerow({k: (f"{v:.2f}" if isinstance(v, Decimal) else v) for k, v in r.items()})

# ------------------------------------------------------------ the answer
sept = rows[:-2]
held = [r for r in sept if r["payout_status"] == "HELD-TERM"]
unpaid_settlement = sum(r["net_settlement"] for r in held)

over_rows = []
for r in sept:
    d = dt.date.fromisoformat(r["batch_date"])
    correct = money(r["gross_sales"] * (NEW if d >= AMEND_FROM else OLD) + PER_TXN * r["txn_count"])
    if r["processing_fees"] != correct:
        over_rows.append((r["batch_date"], r["processing_fees"], correct, r["processing_fees"] - correct))
overcharge = sum(x[3] for x in over_rows)

post_term_owed = cb_post + cb_post_fee
final_payout = unpaid_settlement + overcharge - post_term_owed
release_date = TERMINATION + dt.timedelta(days=180)

# the likely wrong answers
wrong_fee_window = sum(money(r["gross_sales"] * (OLD - NEW)) for r in sept
                       if dt.date.fromisoformat(r["batch_date"]) >= AMEND_FROM)
wrong_with_oct1 = final_payout + oct1_release
wrong_full_release = final_payout + reserve_at_term
naive_unpaid_rows = unpaid_settlement + oct1_release - post_term_owed

print(f"batches in September: {len(sept)}; gross ${sum(r['gross_sales'] for r in sept):,.2f}")
print(f"opening reserve 2026-09-01:            ${OPENING_RESERVE:,.2f}")
print(f"reserve balance at 2026-09-30 close:   ${reserve_at_term:,.2f}")
print(f"Oct 1 scheduled release (retained):    ${oct1_release:,.2f}")
held_parts = ", ".join("{} ${:,.2f}".format(r["batch_date"], r["net_settlement"]) for r in held)
print(f"unpaid settlement, Sept 29 + Sept 30:  ${unpaid_settlement:,.2f}  ({held_parts})")
print("fee overcharge by batch (charged, correct, over):")
for b, ch, co, ov in over_rows:
    print(f"    {b}  ${ch:,.2f}  ${co:,.2f}  ${ov:,.2f}")
print(f"fee overcharge owed to merchant:       ${overcharge:,.2f}  ({len(over_rows)} batches, 09-15 to 09-21)")
print(f"post-termination chargeback + fee:     ${post_term_owed:,.2f}")
print(f"FINAL PAYOUT NOW:                      ${final_payout:,.2f}")
print(f"RESERVE RETAINED:                      ${reserve_at_term:,.2f} until {release_date.isoformat()}")
print(f"payout due by (10 business days):      2026-10-14")
print("likely wrong answers:")
print(f"    fee credit over 09-15 to 09-30:    ${wrong_fee_window:,.2f}")
print(f"    payout incl. Oct 1 release:        ${wrong_with_oct1:,.2f}")
print(f"    payout incl. whole reserve:        ${wrong_full_release:,.2f}")
print(f"    sum of non-PAID rows, no fee fix:  ${naive_unpaid_rows:,.2f}")
