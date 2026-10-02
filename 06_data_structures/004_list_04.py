# More List Methods and Operations



# remove()
print()


numbers = [10, 20, 30, 20, 40]


numbers.remove(20)  # Removes the first occurrence of the specified element.
print(numbers)      # [10, 30, 20, 40]



# pop()
print()


numbers = [10, 20, 30, 40]


removed_element = numbers.pop()  # Removes and returns the last element.
print(removed_element)           # 40
print(numbers)                   # [10, 20, 30]



# pop(index)
print()


numbers = [10, 20, 30, 40]


removed_element = numbers.pop(1)  # Removes and returns the element at index 1.
print(removed_element)            # 20
print(numbers)                    # [10, 30, 40]



# clear()
print()


numbers = [10, 20, 30]


numbers.clear()  # Removes every element from the list.
print(numbers)   # []



# copy()
print()


numbers = [10, 20, 30]


copied_numbers = numbers.copy()  # Creates an independent shallow copy.
copied_numbers.append(40)


print(numbers)         # [10, 20, 30]
print(copied_numbers)  # [10, 20, 30, 40]



# sorted()
print()


numbers = [9, 3, 7, 1]


sorted_numbers = sorted(numbers)  # Returns a sorted new list without changing the original.


print(numbers)         # [9, 3, 7, 1]
print(sorted_numbers)  # [1, 3, 7, 9]



# min(), max(), and sum()
print()


numbers = [10, 50, 20, 40, 30]


print(min(numbers))  # 10
print(max(numbers))  # 50
print(sum(numbers))  # 150



# len()
print()


names = ["Vishal", "Rohit", "Ajay"]


print(len(names))  # 3



# Membership operators: in and not in
print()


numbers = [10, 20, 30, 40]


print(20 in numbers)      # True
print(50 in numbers)      # False
print(50 not in numbers)  # True



# Repetition using *
print()


numbers = [1, 2, 3]


repeated_numbers = numbers * 3
print(repeated_numbers)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]



# Concatenation using +
print()


first_list = [1, 2, 3]
second_list = [4, 5, 6]


combined_list = first_list + second_list
print(combined_list)  # [1, 2, 3, 4, 5, 6]



# Slice deletion
print()


numbers = [10, 20, 30, 40, 50]


del numbers[1:4]  # Deletes elements from index 1 up to, but not including, index 4.
print(numbers)    # [10, 50]



# Unpacking a list
print()


numbers = [10, 20, 30]


first, second, third = numbers


print(first)   # 10
print(second)  # 20
print(third)   # 30



# Unpacking with *
print()


numbers = [10, 20, 30, 40, 50]


first, *middle, last = numbers


print(first)   # 10
print(middle)  # [20, 30, 40]
print(last)    # 50



# enumerate()
print()


names = ["Vishal", "Rohit", "Ajay"]


for index, name in enumerate(names):
    print(index, name)  # Prints index and element together.



# enumerate() with start=1
print()


names = ["Vishal", "Rohit", "Ajay"]


for position, name in enumerate(names, start=1):
    print(position, name)  # Positions begin from 1 instead of 0.



# zip()
print()


names = ["Vishal", "Rohit", "Ajay"]
marks = [85, 90, 78]


for name, mark in zip(names, marks):
    print(name, mark)  # Combines matching items from both lists.



# reversed()
print()


numbers = [10, 20, 30, 40]


reversed_numbers = list(reversed(numbers))  # Creates a reversed new list.


print(numbers)           # [10, 20, 30, 40]
print(reversed_numbers)  # [40, 30, 20, 10]



# Comparing lists
print()


first_list = [1, 2, 3]
second_list = [1, 2, 3]
third_list = [1, 2, 4]


print(first_list == second_list)  # True: both lists have the same elements in the same order.
print(first_list == third_list)   # False
print(first_list < third_list)    # True: comparison happens element by element.



# Nested lists
print()


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]


print(matrix[0])     # [1, 2, 3]
print(matrix[1][2])  # 6: row index 1, column index 2.



# Safely creating a nested list
print()


matrix = [[0] * 3 for row in range(3)]


matrix[0][0] = 1


print(matrix)  # [[1, 0, 0], [0, 0, 0], [0, 0, 0]]



# Shallow copy with nested lists
print()


original = [[1, 2], [3, 4]]
copied = original.copy()


copied[0][0] = 100  # Inner lists are still shared in a shallow copy.


print(original)  # [[100, 2], [3, 4]]
print(copied)    # [[100, 2], [3, 4]]


from copy import deepcopy



# Deep copy of a nested list
print()


original = [[1, 2], [3, 4]]
copied = deepcopy(original)


copied[0][0] = 100


print(original)  # [[1, 2], [3, 4]]
print(copied)    # [[100, 2], [3, 4]]
