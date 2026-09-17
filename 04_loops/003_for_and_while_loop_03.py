"""
A bank account starts with
Balance = ₹50,000

The user can make up to 5 withdrawal attempts.

For every attempt:
    Ask withdrawal amount.
    If amount > balance → print "Insufficient Balance"
    Otherwise deduct it and print remaining balance.
    If balance becomes 0 → stop immediately.
    After 5 attempts → stop automatically.
    If the user enters 0 or a negative amount, reject it.
"""

Balance = 50000
withdraw_attempt = 5

for i in range(withdraw_attempt):

    withdraw_amt = int(input("Enter Withdrawal amount: "))
    while Balance > 0:

        if withdraw_amt > Balance:
            print("Insufficient Balance!")

        elif withdraw_amt <= 0:
            print("Please enter a valid number.")

        else:
            Balance -= withdraw_amt
            print(withdraw_amt, "has been successfully debited")
            

        if Balance == 0:
            attempt = 0  # Transaction stopped.
            print("Balance is zero")
