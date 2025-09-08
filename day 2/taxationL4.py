import taxationL3 as t3, taxationL1 as t1

net_annual_salary = t1.gross_annual_salary - t3.total_tax_amount
print(f'Annual Gross Salary = {t1.gross_annual_salary}')
print(f'Total Tax Amount = {t3.total_tax_amount}')
print(f'Net Annual Salary = {net_annual_salary}')