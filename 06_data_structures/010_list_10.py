"""
Q3: Predict and repair (lists + references + functions + loops + type conversion)
def add_score(score, board=[]):
    board.append(score)
    return board

a = add_score(10)
b = add_score(20)
grid = [[0] * 3] * 3
grid[0][0] = 7
nums = [2, 4, 6, 1, 8]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)
text = "3 1 2"
order = text.split().sort()
copy1 = nums
copy2 = nums[:]
copy1.append(99)

print(a, b, a is b)
print(grid)
print(nums)
print(order)
print(copy2)

A: Without running it, write the exact output of all five print lines.
B: Explain each surprising result in one sentence using the words "reference" or "same object".
C: Rewrite the code so it does what the author obviously intended (separate boards per call, independent rows, all even numbers removed, a sorted list of numbers in order, and copy2 unaffected).
D: Write remove_evens(items) that returns a new list and never modifies the argument. The items may be ints or numeric strings like "4" (as if typed by a user). Numeric strings must be converted, and non-numeric items must be left untouched. Use type() comparisons like in your challenge 06.
- By Claude.
"""

def add_score(score, board=None):
    if board is None:
        board = []

    board.append(score)
    return board


a = add_score(10)
b = add_score(20)

grid = [[0] * 3 for _ in range(3)]
grid[0][0] = 7

nums = [2, 4, 6, 1, 8]

odd_nums = []

for n in nums:
    if n % 2 != 0:
        odd_nums.append(n)

nums = odd_nums

text = "3 1 2"

number_parts = text.split()
numbers = []

for part in number_parts:
    numbers.append(int(part))

order = sorted(numbers)

copy1 = nums[:]
copy2 = nums[:]

copy1.append(99)

print(a, b, a is b)
print(grid)
print(nums)
print(order)
print(copy2)
