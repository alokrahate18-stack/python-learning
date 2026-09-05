def check_loan_eligibility(age, monthly_income, credit_score, existing_loan):

    if age < 18:
        return ("Rejected: Underage.")
    else:

        if monthly_income < 25000:
            return ("Rejected: Low Income.")
        else:

            if credit_score < 700:
                return ("Rejected: Low Credit Score!")
            else:

                if existing_loan == "True" or existing_loan == "yes":
                    return ("Rejected: Existing Loan")

                else:
                    return ("Loan Approved!")

age = int(input("Enter your Current Age: "))
monthly_income = int(input("Enter your Monthly Income: "))
credit_score = int(input("Enter your Current Credit Score: "))
existing_loan = str(input("Do you have any existing loan on you? "))

print("\n--------------------------------------")
print("\nChecking the Approval for the Loan:")
result = check_loan_eligibility(age, monthly_income, credit_score, existing_loan)
print(result)
print("\n--------------------------------------")
