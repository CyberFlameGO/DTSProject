#!/user/bin/env python3.10
"""
Tax calc with if and elif because lazy
"""


# https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/tax-rates-for
# -individuals
def calculate_income_tax(weekly_pay: float):
    """

    :param weekly_pay:
    :return:
    """
    bracket_10_5 = 14000 * 0.105
    bracket_17_5 = 34000 * 0.175
    bracket_30 = 22000 * 0.3
    bracket_33 = 110000 * 0.33

    if weekly_pay <= 14000:
        tax_paid = weekly_pay * 0.105
    elif weekly_pay <= 48000:
        tax_paid = ((weekly_pay - 14000) * 0.175) + bracket_10_5
    elif weekly_pay <= 70000:
        tax_paid = ((weekly_pay - 62000) * 0.3) + bracket_10_5 + bracket_17_5
    elif weekly_pay <= 180000:
        tax_paid = ((weekly_pay - 132000) * 0.33) + bracket_10_5 + bracket_17_5 + bracket_30
    else:
        tax_paid = ((weekly_pay - 132000) * 0.39) + bracket_10_5 + bracket_17_5 + bracket_30 + bracket_33
    return tax_paid


income_after_tax = calculate_income_tax(int(input("Enter your weekly pay: ").strip()))
print("$", income_after_tax, sep = "")
