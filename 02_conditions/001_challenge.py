age = int(input("Enter your age: "))
has_id = input("Do you have ID? (yes/no): ").strip().lower() == "yes"
has_permission = input("Do you have permission? (yes/no): ").strip().lower() == "yes"

if age >= 18 and has_id and has_permission:
    print("You are allowed to enter!")
else:
    print("You are not allowed.")
