# 014_exception_handling_02.py

a = input("Enter the Number: ")

print(f"Multiplication of the Table of {a} is:")

try:
    for i in range(1, 11):
        print(f"{a} * {i} = {int(a)*i}")
except:
    print("Sorry, there is a slight issue in the program.")

print("End of the Code.")
