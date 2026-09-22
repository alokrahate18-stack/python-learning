balance = 50000
withdrawal = int(input("Enter the amount you wish to Withdraw: "))
account_active = str(input("Is your account active (yes or no): ")).strip().lower() == "yes"

if account_active == "no":
    print("Account is Inactive.")
elif withdrawal > balance:
    print("Insufficient Balance.")
elif withdrawal == balance:
    print("Account will be Empty.")
else:
    print("Withdrawal Approved")
    print("Rs.", withdrawal , "withdrawn ")
    print("Rs.", withdrawal , "debited from the account.")
