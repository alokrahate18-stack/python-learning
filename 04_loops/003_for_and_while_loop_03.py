balance = 50000
MAX_ATTEMPTS = 5

for attempt in range(MAX_ATTEMPTS):
    amount = int(input("Enter withdrawal amount: "))
    if amount <= 0:
        print("Please enter a valid amount.")
    elif amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print(f"₹{amount} debited. Remaining balance: ₹{balance}")
        if balance == 0:
            print("Balance is zero.")
            break
