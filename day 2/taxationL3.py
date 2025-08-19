import taxationL1, taxationL2
if 0<= taxationL2.taxable_income <= 3_00_000:
    tax_percentage = 0
elif 300001<= taxationL2.taxable_income <=600000: 
    tax_percentage = 5
elif 600001<= taxationL2.taxable_income <=900000: 
    tax_percentage = 10
elif 900001<= taxationL2.taxable_income <=1200000:
    tax_percentage = 15
elif 1200001<= taxationL2.taxable_income <=1500000:
    tax_percentage = 15
else:
    tax_percentage = 30
