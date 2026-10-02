"""Given marks = [72, 45, 98, 60, 88, 33, 91, 55], write a function analyze(marks) that returns [highest, lowest, average] without using max(), min(), or sum(). Use a loop and comparisons instead. Then print it as:

Highest: 98 | Lowest: 33 | Average: 67.75
- By Claude"""

marks = [72, 45, 98, 60, 88, 33, 91, 55]

def analyse(marks):

    high = marks[0]
    low = marks[0]
    avg = 0

    for i in range(len(marks)):

        avg += marks[i]

        if (high < marks[i]):
                high = marks[i]

        if (low > marks[i]):
                low = marks[i]

    avg /= len(marks)

    print(f"| Highest: {high} | Lowest: {low} | Average: {avg} |")

