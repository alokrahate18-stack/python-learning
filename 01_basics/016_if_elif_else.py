balance = 50000
withdrawal = int(input("Enter the amount you wish to Withdraw: "))
account_active = str(input("Enter the amount you wish to Withdraw (True or False): "))

if account_active == False:
    print("Account is Inactive.")
elif withdrawal > balance:
    print("Insufficient Balance.")
elif withdrawal == balance:
    print("Account will be Empty.")
else:
    print("Withdrawal Approved")
    print("Rs.", withdrawal , "withdrawn ")
    print("Rs.", withdrawal , "debited from the account.")
