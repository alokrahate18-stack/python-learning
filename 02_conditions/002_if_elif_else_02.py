age = int(input("Enter your Current Age: "))
monthly_income = int(input("Enter your Monthly Income: "))
credit_score = int(input("Enter your Current Credit Score: "))
existing_loan = str(input("Do you have any existing loan on you? "))

if age < 18:
    print("Rejected: Underage.")
else:

    if monthly_income < 25000:
        print("Rejected: Low Income.")
    else:
        if credit_score < 700:
            print("Rejected: Low Credit Score!")
        else:
            if existing_loan == "True" or existing_loan == "yes":
                print("Rejected: Existing Loan")

            else:
                print("Loan Approved!")
