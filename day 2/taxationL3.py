import taxationL2 as t2

section_87A_rebate = True

tax_amount = 0
tax_percentage = 0
if t2.taxable_income >= 0 and t2.taxable_income <= 3_00_000:
    pass
elif t2.taxable_income <= 6_00_000:
    tax_percentage = .05
elif t2.taxable_income <= 9_00_000:
    tax_percentage = .1
elif t2.taxable_income <= 12_00_000:
    tax_percentage = .15
elif t2.taxable_income <= 15_00_000:
    tax_percentage = .2
else:
    tax_percentage = .3

tax_amount = t2.taxable_income * tax_percentage
cess_amount = tax_amount * 0.04
total_tax_amount = tax_amount + cess_amount

print(
'''
₹0 - ₹3,00,000: 0%
o ₹3,00,001 - ₹6,00,000: 5%
o ₹6,00,001 - ₹9,00,000: 10%
o ₹9,00,001 - ₹12,00,000: 15%
o ₹12,00,001 - ₹15,00,000: 20%
o Above ₹15,00,000: 30%
'''
)
print(f'Cess Amount      = {cess_amount}')
if section_87A_rebate and t2.taxable_income <= 7_00_000:
    print(f'Total Tax Amount = 0')
else:
    print(f'Total Tax Amount = {total_tax_amount}')
