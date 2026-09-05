point = (0,5)

match point:
    case (0,0):
        print("Origin.")
    case (0,y):
        print("On Y-axis.")
        print(f"Point is on Y-axis at {y}")
    case (x,0):
        print("On X-axis.")
        print(f"Point is on Y-axis at {x}")
    case (x,y):
        print("Somewhere else.")
        print(f"Point is on Y-axis at ({x}, {y})")
    case _:
        print("Invalid Choice!")

# Note: Order matters. Python checks cases from top to bottom. Python chooses the FIRST matching case, not the "best" or "most exact" case. More specific patterns should generally come before more general patterns.

                # Specific
                #    ↓
                # More specific
                #    ↓
                # General
                #    ↓
                # Very general (_)




# *rest means:
# "Collect all remaining items into a list."

# Example:
data = [10, 20, 30, 40]

match data:
    case [first, *rest]:
        print(first)
        print(rest)


# [first, *rest]
#     ↓       ↓
#    10    [20,30,40]
# rest is just a variable name. You could write:

# case [1, *remaining]:

# Then the remaining elements are stored in remaining.

# Easy memory trick:
# *rest = "Give me everything that's left."
