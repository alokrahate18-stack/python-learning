# Breaks means break/ exit the loop.
# Continue means skip the current value and continue without it.

# Let try Writing Table of 5 up to 100 times. But, skipping every time divisible by 4.

for count in range(151):

    if (count == 100):
        break

    if ((count % 4) == 0):
        continue
    
    print(f"5 * {count} = {count * 5}")

