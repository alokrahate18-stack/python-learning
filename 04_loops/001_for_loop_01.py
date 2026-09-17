"""
Write a Python program that prints:

1
4
9
16
25
36
49
64
81
100

But you are not allowed to manually write all 10 numbers.

Use a for loop and range().
"""
x = 1

for i in range(11):
    print(x * x)
    x += 1
