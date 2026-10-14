basic_salary = 32000
hra = basic_salary * 0.20
traveling_allowance = basic_salary * 0.08
provident_funds = basic_salary * 0.12
professional_tax = 200

gross_salary = basic_salary + hra + traveling_allowance
total_deduction = provident_funds + professional_tax
net_salary = gross_salary - total_deduction

print("Basic Salary       = ₹",basic_salary)
print("HRA                = ₹",hra)
print("Transport          = ₹",traveling_allowance)
print("PF                 = ₹",provident_funds)
print("Professional Tax   = ₹",professional_tax)

print("\n-------------------------------------")
print("Gross Salary = ₹", gross_salary)
print("Total Deductions = - ₹", total_deduction)
print("\n-------------------------------------")
print("Net Salary = ₹", net_salary)
