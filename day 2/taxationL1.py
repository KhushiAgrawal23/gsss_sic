name = input('enter name')
EmpID = int(input('enter emp id'))
basic_salary = int(input('enter basic salary'))
special_allowances= int(input('special allowances'))
bonus_percentage = int(input('enter percent'))
gross_monthly_salary = basic_salary + special_allowances
annual_gross_salary = (gross_monthly_salary*12) + (gross_monthly_salary*12)*(bonus_percentage/100)
print(name)
print(EmpID)
print(gross_monthly_salary)
print(annual_gross_salary )

