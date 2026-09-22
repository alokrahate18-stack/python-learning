marks = [72, 45, 98, 60, 88, 33, 91, 55]

def analyse(marks):

    high = marks[0]
    low = marks[0]
    avg = 0

    for i in range(7):

        avg += marks[i]

        if (high < marks[i]):
                high = marks[i]

        if (low > marks[i]):
                low = marks[i]

    avg /= 8

    print(f"| Highest: {high} | Lowest: {low} | Average: {avg} |")
