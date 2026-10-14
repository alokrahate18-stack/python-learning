# 015_exception_handling_03.py


try:
    num = input("Enter the Number: ")

except (
    ValueError
):  # Here, if you wish to tackle any specific type of error in different ways. You can handle as many specific errors as you want.
    print("Number entered is not an integer. ")

except IndexError:
    print("Index Error!")
