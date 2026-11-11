"""Correct answer for task 03: Sagebrush Drug 2025 CAM reconciliation at Fernhill Commons."""
from decimal import Decimal as D, ROUND_HALF_UP
c = lambda x: D(x).quantize(D("0.01"), ROUND_HALF_UP)

SHARE = D("0.1478")          # lease 6.1: 14,250 / 96,400, stated as 14.78%
FEE_RATE = D("0.04")         # lease 6.2(f): 4% of OpEx excl. taxes, insurance and the fee
MONTHLY_EST = D("4216.35")  # 2025 estimated OpEx billed monthly

# 2025 GL, CAM pool, by account (detail lines summed)
taxes      = D("148612.40")
insurance  = D("41287.00")
electric   = D("22914.63")
water      = D("8406.18")
landscape  = D("26880.00")
snow       = D("19452.50")
sweeping   = D("7800.00")
pk_patch   = D("1264.75")    # 6420 pothole patch, March: repair, include
pk_seal    = D("9850.00")    # 6420 sealcoat and restripe, May: maintenance, include (decoy)
pk_overlay = [D("57600.00"), D("28800.00")]  # 6420 mill and overlay Ph 1-2, Ph 3: capital, exclude
rm_general = D("6318.92")
security   = D("11040.00")
trash      = D("4935.60")

overlay = sum(pk_overlay)
fee_base_booked = (electric + water + landscape + snow + sweeping + pk_patch + pk_seal + overlay
                   + rm_general + security + trash)
fee_booked = c(fee_base_booked * FEE_RATE)
fee_base_ok = fee_base_booked - overlay
fee_ok = c(fee_base_ok * FEE_RATE)

opex_draft = taxes + insurance + fee_base_booked + fee_booked
opex_ok = taxes + insurance + fee_base_ok + fee_ok
est_paid = MONTHLY_EST * 12

share_draft = c(opex_draft * SHARE)
share_ok = c(opex_ok * SHARE)
print("overlay excluded", overlay)
print("fee base booked", fee_base_booked, "fee base correct", fee_base_ok)
print("fee booked", fee_booked, "fee correct", fee_ok, "fee difference", fee_booked - fee_ok)
print("OpEx draft", opex_draft, "OpEx correct", opex_ok, "difference", opex_draft - opex_ok)
print("estimates paid", est_paid)
print("tenant share draft", share_draft, "balance", share_draft - est_paid)
print("tenant share correct", share_ok, "balance", share_ok - est_paid)
# wrong path: decoy sealcoat also excluded
fb2 = fee_base_ok - pk_seal; f2 = c(fb2 * FEE_RATE); o2 = taxes + insurance + fb2 + f2
print("over-exclusion (sealcoat out too): share", c(o2*SHARE), "balance", c(o2*SHARE) - est_paid)
# wrong path: overlay removed but booked fee kept
o3 = taxes + insurance + fee_base_ok + fee_booked
print("overlay out, fee not recomputed: share", c(o3*SHARE), "balance", c(o3*SHARE) - est_paid)
# wrong path: overlay amortized over 15 years and included
o4 = opex_ok + c(overlay/15) + c(overlay/15*FEE_RATE)
print("overlay amortized 15y incl.: share", c(o4*SHARE), "balance", c(o4*SHARE) - est_paid)
