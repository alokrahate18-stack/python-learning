# List Comprehension



# Creating a list of numbers from 0 to 149
list = [i for i in range(150)]
print(list)



# Creating a list of squares from 0 to 49
print()


list = [i * i for i in range(50)]  # How you wish to show the for loop
print(list)



# Creating a list of squares of even numbers from 0 to 49
print()


list = [
    i * i
    for i in range(50)
    if i % 2 == 0
]  # How you wish to show the for loop, then the condition


print(list)



# More examples



# Creating a list of odd numbers from 0 to 19
print()


list = [i for i in range(20) if i % 2 != 0]
print(list)



# Creating a list of cubes from 0 to 9
print()


list = [i * i * i for i in range(10)]
print(list)



# Converting each name into uppercase
print()


names = ["Vishal", "Rohit", "Ajay"]
uppercase_names = [name.upper() for name in names]


print(uppercase_names)



# Selecting names whose length is greater than 4
print()


long_names = [name for name in names if len(name) > 4]
print(long_names)



# Creating a list of the first letter from each name
print()


first_letters = [name[0] for name in names]
print(first_letters)



# Conditional expression inside a list comprehension
print()


list = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]
print(list)
