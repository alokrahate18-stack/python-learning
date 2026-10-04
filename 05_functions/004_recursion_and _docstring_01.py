# 004_recursion_01.py

# As you all know a function can call another function in itself. But, it is also possible to call the function itself , Which is called as as Recursion.

def factorial(n):
    """This is a Docstring. It comes after the Def function_ name and before function body. It tells about the function. I can also be printed using:
    print(function_name.__doc__)"""
    if n == 0 or n == 1:
        return 1
    else:
        return (n * factorial(n-1))

a = int(input("Enter nay Positive Number: "))
print(factorial(a))
print(factorial.__doc__)
