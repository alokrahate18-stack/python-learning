# List Methods



list = [3, 5, 6, 4, 6, 8, 9, 6, 2, 6, 9, 0, 1, 7, 3, 4, 8]
print(list)



# append()
print()


list.append(7)  # Used to add an element at the end of the list.
print(list)



# sort()
print()


list.sort()  # Used to sort elements in ascending order.
print(list)



# sort(reverse=True)
print()


list.sort(reverse=True)  # Used to sort elements in descending order.
print(list)



# reverse()
print()


list.reverse()  # Used to reverse the order of elements in the original list.
print(list)



# index()
print()


print(list.index(6))  # Prints the index of the first occurrence of the specified element.



# count()
print()


print(list.count(6))  # Counts the occurrences of the specified element.



# index() again
print()


print(list.index(6))  # Prints the index of the first occurrence of the specified element.



# Assignment creates a reference, not an independent copy
print()


make = list
make[0] = 12  # Change made through "make" also applies to the original list.


print(list)
print(make)



# copy() creates an independent list copy
print()


make = list.copy()
make[5] = 12  # Change made in the copied list does not apply to the original list.


print(list)
print(make)



# insert()
print()


list.insert(
    7,
    65,
)  # Used to add an element at a specified position: list.insert(index_position, element).


print(list)



# extend()
print()


stored = [78, 57, 67, 95, 24, 65, 24, 54, 21, 15]


list.extend(stored)  # Adds every element of "stored" to the end of the list.
print(list)



# Concatenation using +
print()


new = make + stored  # Concatenates both lists.
print(new)



# Slice replacement and deletion
list[1:3] = [0]  # Replaces two elements from index 1 up to index 3 with the element 0.
del list[11]     # Deletes the element at index 11.


# pop()
numbers = [10, 20, 30, 40]


removed_element = numbers.pop()  # Removes and returns the last element.
print(removed_element)           # 40
print(numbers)                   # [10, 20, 30]



# pop(index)
numbers = [10, 20, 30, 40]


removed_element = numbers.pop(1)  # Removes and returns the element at index 1.
print(removed_element)            # 20
print(numbers)                    # [10, 30, 40]



# remove()
numbers = [10, 20, 30, 20, 40]


numbers.remove(20)  # Removes only the first occurrence of 20.
print(numbers)      # [10, 30, 20, 40]



# clear()
numbers = [10, 20, 30]


numbers.clear()  # Removes all elements from the list.
print(numbers)   # []



# Sorting without modifying the original list
numbers = [9, 3, 7, 1]


sorted_numbers = sorted(numbers)


print(numbers)         # [9, 3, 7, 1]
print(sorted_numbers)  # [1, 3, 7, 9]
