# 005_recursion_02.py

# Fibonacci Sequence are the Sequence in which the new number is formed with the addition of the last two available numbers.
# For e.g. 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ......

def fibonacci(m, n):
    print(f"{m},\t{n}")
    for i in range(20):
        temp = m + n
        m = n
        n = temp
        print(f",\t{n}")

a = int(input("Enter the First Number: "))
b = int(input("Enter the Second Number: "))

print(fibonacci(a, b))
