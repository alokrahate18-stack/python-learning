# Basics of Lists and Indexing


# Creating lists
empty = []  # Empty list
print(empty)


print(list("abc"))          # ['a', 'b', 'c']
print("a b c".split())      # ['a', 'b', 'c']
print(list(range(5)))       # [0, 1, 2, 3, 4]
print([0] * 3)              # [0, 0, 0]



# List with multiple data types
list = [ 3, 5, "Vishal", 6, 4, True, 6, 8, 9, "Rohit", "Ajay", 6, 2, 6, 9, 0, 1, 7, False, 3, 4, 8 ]


print(list)  # Lists are mutable: values can be changed, added, or modified.
print(type(list))



# Positive indexing
print()


print(list[0])   # Here, 0 is the index, i.e. the position of an element in the list.
print(list[11])
print(list[5])



# Negative indexing
print()


print(list[-11])          # Negative indexing
print(list[len(list)-11]) # Negative indexing internal working, i.e. 20 - 11 = 9
print(list[9])



# List slicing
print()


print(list[:])
print(list[0:len(list)])
print(list[2:7])
print(list[9:15])      # list(start, end)
print(list[3:15:3])    # list(start, end, jump)
print(list[::3])       # [3, 6, 6, 'Rohit', 2, 0, False, 8]
print(list[::-3])      # [8, False, 0, 2, 'Rohit', 6, 6, 3]
