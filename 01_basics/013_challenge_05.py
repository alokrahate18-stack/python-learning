age = int(input("Enter your Age: "))
has_Id = bool(input("Do you have ID? (True or False) "))
has_permission = bool(input("Do you have Permission? (True or False) "))


if (age >=18 & has_Id == "True" & has_permission == "True"):
    print("You are allowed to Enter!")
else:
    print("You are not allowed")
