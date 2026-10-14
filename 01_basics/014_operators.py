# 015_operators.py

a = 10
b = 3

# Arithmetic operators
print(a + b)  # Addition: 13
print(a - b)  # Subtraction: 7
print(a * b)  # Multiplication: 30
print(a / b)  # Division: 3.333...
print(a // b)  # Floor division: 3
print(a % b)  # Remainder: 1
print(a**b)  # Power: 1000

# Comparison operators
print(a == b)  # False
print(a != b)  # True
print(a > b)  # True
print(a < b)  # False
print(a >= b)  # True
print(a <= b)  # False

# Logical operators
print(a > 5 and b < 5)  # True
print(a > 5 or b > 5)  # True
print(not a > 5)  # False

# Assignment operators
number = 10
number += 5  # number = number + 5 -> 15
number -= 3  # number = number - 3 -> 12
number *= 2  # number = number * 2 -> 24
number /= 4  # number = number / 4 -> 6.0
number //= 2  # number = number // 2 -> 3.0
number %= 2  # number = number % 2 -> 1.0
number **= 3  # number = number ** 3 -> 1.0
print(number)  # 1.0

# Membership operators
name = "Rahul"
print("R" in name)  # True
print("z" not in name)  # True

# Identity operators (check if two variables share the same memory location)
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is z)  # True (points to the exact same object in memory)
print(x is y)  # False (different objects, even with equal values)
print(x is not y)  # True

# Bitwise operators (work on binary bit representations)
p = 6  # Binary: 0110
q = 3  # Binary: 0011

print(p & q)  # Bitwise AND: 2 (Binary: 0010)
print(p | q)  # Bitwise OR:  7 (Binary: 0111)
print(p ^ q)  # Bitwise XOR: 5 (Binary: 0101)
print(~p)  # Bitwise NOT: -7 (Formula: -(p + 1))
print(p << 1)  # Left Shift: 12 (0110 shifted left becomes 1100)
print(p >> 1)  # Right Shift: 3 (0110 shifted right becomes 0011)

# Bitwise assignment operators
flags = 6
flags &= 3  # Bitwise AND Assignment: 2
flags |= 4  # Bitwise OR Assignment: 6
flags ^= 1  # Bitwise XOR Assignment: 7
flags <<= 1  # Left Shift Assignment: 14
flags >>= 2  # Right Shift Assignment: 3

# Walrus operator (Assignment Expression) — assigns and evaluates in one step
if (n := len(name)) > 3:
    print(f"Name has {n} characters")  # Name has 5 characters
# Without Walrus, a *= 2 fails in an if statement a *= 2 is a statement, not an expression. It modifies a in place, but it does not evaluate to a result that an if condition can test. To do this without the walrus operator, you must update a beforehand.
