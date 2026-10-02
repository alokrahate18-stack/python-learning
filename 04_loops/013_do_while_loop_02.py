# Although Do while loop is not directly part of loops in Python, but we can still emulate it.

while True:
    number = int(input("Enter any Positive Value: "))
    print(number)
    if not number > 0:
        break
