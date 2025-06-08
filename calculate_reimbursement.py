#!/usr/bin/env python3
"""Pure rule-based reimbursement calculator (no external model)."""


def reimburse(days: int, miles: int, receipts: float) -> float:
    intercept = 266.71
    coef_days = 50.05
    coef_miles = 0.4456
    coef_receipts = 0.3829

    capped_miles = 800 + (miles - 800) * 0.25 if miles > 800 else miles
    capped_receipts = 1800 + (receipts - 1800) * 0.15 if receipts > 1800 else receipts

    amount = intercept + coef_days * days + coef_miles * capped_miles + coef_receipts * capped_receipts

    receipts_str = f"{receipts:.2f}"
    if receipts_str.endswith('.49') or receipts_str.endswith('.99'):
        amount *= 0.457
    else:
        high_value = receipts > 1800 or miles > 800
        if days == 5:
            amount *= 0.92
        elif 7 <= days <= 8 and high_value:
            amount *= 1.25
        elif 11 <= days <= 14 and high_value:
            amount *= 0.85
        elif 13 <= days <= 14 and high_value:
            amount *= 1.20
        elif days < 2:
            amount *= 1.15

        miles_per_day = miles / days if days > 0 else 0
        if 180 <= miles_per_day <= 220:
            amount *= 1.03

    return round(amount, 2)
