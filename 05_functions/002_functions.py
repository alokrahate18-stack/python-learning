def check_loan_eligibility(age, monthly_income, credit_score, existing_loan):

    if age < 18:
        return "Rejected: Underage."

    elif monthly_income < 25000:
        return "Rejected: Low Income."

    elif credit_score < 700:
        return "Rejected: Low Credit Score!"
        if existing_loan.strip().lower() in ("true", "yes"):
            return "Rejected: Existing Loan"
        return "Loan Approved!"

age = int(input("Enter your Current Age: "))
monthly_income = int(input("Enter your Monthly Income: "))
credit_score = int(input("Enter your Current Credit Score: "))
existing_loan = str(input("Do you have any existing loan on you? "))

print("\n--------------------------------------")
print("\nChecking the Approval for the Loan:")
result = check_loan_eligibility(age, monthly_income, credit_score, existing_loan)
print(result)
print("\n--------------------------------------")
