#!/usr/bin/env python3
"""
Test and calibrate the reimbursement calculator
"""

from calculate_reimbursement import reimburse


def test_specific_cases():
    """Test specific cases to understand the calculation pattern"""
    test_cases = [
        (3, 93, 1.42, 364.51),
        (1, 55, 3.6, 126.06),
        (1, 47, 17.97, 128.91),
        (5, 130, 306.90, 574.10),
        (5, 173, 1337.90, 1443.96),
    ]

    print("Testing specific cases:")
    print("-" * 80)
    print(f"{'Days':>5} {'Miles':>6} {'Receipts':>10} {'Expected':>10} {'Calculated':>12} {'Error':>10}")
    print("-" * 80)

    for days, miles, receipts, expected in test_cases:
        calculated = reimburse(days, miles, receipts)
        error = calculated - expected
        print(f"{days:5d} {miles:6d} {receipts:10.2f} {expected:10.2f} {calculated:12.2f} {error:10.2f}")


if __name__ == "__main__":
    test_specific_cases()
