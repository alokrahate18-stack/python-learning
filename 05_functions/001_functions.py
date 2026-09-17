def gross_salary(basic_salary, hra, traveling_allowance):
    return basic_salary + hra + traveling_allowance

def total_deduction(provident_funds, professional_tax):
    return provident_funds + professional_tax

def net_salary(gr_sal, tot_ded):
    return gr_sal - tot_ded

basic_salary = 32000
hra = basic_salary * 0.20
traveling_allowance = basic_salary * 0.08
provident_funds = basic_salary * 0.12
professional_tax = 200

gr_sal = gross_salary(basic_salary, hra, traveling_allowance)

tot_ded = total_deduction(provident_funds, professional_tax)

net_sal = net_salary(gr_sal, tot_ded)


print("Basic Salary       = ₹",basic_salary)
print("HRA                = ₹",hra)
print("Transport          = ₹",traveling_allowance)
print("PF                 = ₹",provident_funds)
print("Professional Tax   = ₹",professional_tax)

print("\n-------------------------------------")
print("Gross Salary = ₹", gr_sal)
print("Total Deductions = - ₹", tot_ded)
print("\n-------------------------------------")
print("Net Salary = ₹", net_sal)

