# 013_exception_handling_01.py

a = input("Enter the Number: ")

print(f"Multiplication of the Table of {a} is:")

try:
    for i in range(1, 11):
        print(f"{a} * {i} = {int(a)*i}")
except Exception as e:
    print(e)

print("End of the Code.")
