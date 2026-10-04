# notes.md

## Learning progression

```text
Day 1  → Python Basics
Day 2  → Variables and Data Types
Day 3  → Operators
Day 4  → Strings
Day 5  → Input, Output and Boolean Logic
Day 6  → Conditional Statements
Day 7  → while Loops
Day 8  → for Loops and range()
Day 9  → Functions, Scope, return and None
Day 10 → Lists
Day 11 → Tuples
Day 12 → Docstrings, Recursion, Sets and Dictionaries
```

***

# Day 1

## Topic: Python Basics, Syntax, `print()` and Comments

## Theory

### 1. What is Python?

Python is a high-level, interpreted, general-purpose programming language.

It is designed to make code readable and easy to write. Python is dynamically typed, meaning you do not have to explicitly declare the type of a variable before using it.

```python
age = 20
name = "Alok"
```

In the example above, Python automatically understands that:

- `age` refers to an integer
- `name` refers to a string

***

### 2. Python program execution

Python source code is usually written in a file ending with `.py`.

```text
Python Code
    ↓
Python Interpreter
    ↓
Execution
    ↓
Output
```

Python is commonly called an interpreted language because the Python interpreter runs the program. In practice, Python may also compile source code into bytecode internally, but you normally run Python files directly without manually compiling them first.

***

### 3. First Python program

```python
print("Hello, World!")
```

`print()` sends information to standard output, usually the terminal or console.

Output:

```text
Hello, World!
```

***

### 4. Printing multiple values

```python
print("Alok", 20, "Python")
```

Output:

```text
Alok 20 Python
```

By default, `print()` separates multiple values with a space.

***

### 5. The `sep` parameter

Use `sep` to change the separator between printed values.

```python
print("2026", "10", "04", sep="-")
```

Output:

```text
2026-10-04
```

***

### 6. The `end` parameter

Normally, `print()` moves to a new line after printing.

```python
print("Hello")
print("World")
```

Output:

```text
Hello
World
```

You can change this behavior with `end`.

```python
print("Hello", end=" ")
print("World")
```

Output:

```text
Hello World
```

***

### 7. Comments

Comments are ignored by Python. They are used to explain code.

```python
# This is a comment

print("Hello")  # This prints Hello
```

Use comments to explain *why* code exists, not just repeat what obvious code already says.

***

### 8. Indentation

Python uses indentation to define blocks of code.

```python
if True:
    print("Inside block")
```

Indentation is not just decorative in Python. It is part of the language syntax.

Incorrect indentation can cause:

```text
IndentationError
```

***

### 9. Common errors

Missing a closing bracket or quote causes a syntax error.

```python
print("Hello"
```

Output:

```text
SyntaxError
```

Incorrect indentation can cause:

```text
IndentationError
```

***

### 10. Python is case-sensitive

```python
name = "Alok"
Name = "Rahate"
```

`name` and `Name` are different variable names.

***

# Day 2

## Topic: Variables, Data Types and Type Conversion

## Theory

### 1. What is a variable?

A variable is a name that refers to an object or value.

```python
age = 20
```

Conceptually:

```text
age ─────→ 20
```

Python variables do not have one fixed type forever. The object currently referenced by the variable has a type.

***

### 2. Assignment

```python
x = 10
```

`=` means assignment.

It does **not** mean mathematical equality.

```python
x = 10
```

Means:

> Store a reference to the value `10` in the variable name `x`.

***

### 3. Multiple assignment

```python
a = b = 10
```

Both names refer to the value `10`.

```python
a, b = 10, 20
```

This assigns:

```text
a → 10
b → 20
```

***

### 4. Basic built-in data types

| Type | Meaning | Example |
|---|---|---|
| `int` | Whole numbers | `20` |
| `float` | Decimal numbers | `99.50` |
| `str` | Text | `"Alok"` |
| `bool` | `True` or `False` | `True` |

```python
age = 20
price = 99.50
name = "Alok"
passed = True
```

***

### 5. Checking a type

```python
type(20)
```

Output:

```python
<class 'int'>
```

***

### 6. Type conversion

Changing one type into another is called type conversion or type casting.

```python
int("25")
float("10.5")
str(100)
bool(1)
```

***

### 7. Important `bool()` behavior

```python
bool(0)       # False
bool(1)       # True
bool("")      # False
bool("False") # True
```

`"False"` is a non-empty string, so it is truthy.

***

### 8. Variable reassignment

```python
x = 10
x = "Python"
```

This is valid because Python is dynamically typed.

The variable name `x` first refers to an integer and later refers to a string.

***

### 9. Variable naming rules

Valid names:

```python
student_name = "Alok"
age2 = 20
_value = 10
```

Invalid names:

```python
2age = 20
student-name = "Alok"
```

Rules:

- A name cannot begin with a number.
- A name cannot contain `-`.
- A name can contain letters, digits, and `_`.
- Python names are case-sensitive.

***

### 10. Avoid using built-in names as variables

Avoid code like this:

```python
list = [1, 2, 3]
str = "Python"
sum = 100
```

This hides Python’s built-in names.

For example:

```python
list = [1, 2, 3]
list("abc")
```

This will fail because `list` no longer refers to Python’s built-in `list()` constructor.

***

# Day 3

## Topic: Operators

## Theory

### 1. What is an operator?

An operator is a symbol or keyword used to perform an operation on values.

***

### 2. Arithmetic operators

| Operator | Meaning |
|---|---|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | True division |
| `//` | Floor division |
| `%` | Remainder |
| `**` | Exponentiation |

```python
10 / 3      # 3.333...
10 // 3     # 3
10 % 3      # 1
2 ** 3      # 8
```

***

### 3. Division versus floor division

`/` performs true division and normally produces a float.

```python
8 / 2
```

Output:

```python
4.0
```

`//` performs floor division.

```python
7 // 2
```

Output:

```python
3
```

With negative numbers, floor division rounds down toward negative infinity.

```python
-7 // 2
```

Output:

```python
-4
```

***

### 4. Comparison operators

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

Comparison operators produce Boolean values.

```python
10 > 5      # True
10 == 5     # False
```

***

### 5. Assignment operators

```python
=
+=
-=
*=
/=
//=
%=
**=
```

Example:

```python
x = 10
x += 5
```

This is equivalent to:

```python
x = x + 5
```

***

### 6. Logical operators

```python
and
or
not
```

Example:

```python
age >= 18 and age <= 60
```

***

### 7. Membership operators

```python
in
not in
```

Example:

```python
"a" in "cat"       # True
"z" not in "cat"   # True
```

***

### 8. Identity operators

```python
is
is not
```

`==` asks:

> Do these objects have equal values?

`is` asks:

> Are these the same object in memory?

```python
a = [1, 2]
b = [1, 2]
c = a

a == b   # True
a is b   # False
a is c   # True
```

This distinction becomes important with lists, dictionaries, copying, and mutable objects.

***

### 9. Operator precedence

Python follows precedence rules.

```python
result = 2 + 3 * 4
```

Output:

```python
14
```

Multiplication happens before addition.

Use parentheses when clarity matters.

```python
result = (2 + 3) * 4
```

Output:

```python
20
```

***

# Day 4

## Topic: Strings

## Theory

### 1. What is a string?

A string is an immutable sequence of characters.

```python
name = "Python"
```

Conceptually:

```text
P y t h o n
0 1 2 3 4 5
```

***

### 2. Creating strings

```python
"Python"
'Python'
"""Python"""
'''Python'''
```

Single quotes and double quotes both create strings.

Triple quotes are commonly used for multi-line strings and docstrings.

***

### 3. Indexing

```python
word = "Python"

word[0]      # 'P'
word[-1]     # 'n'
```

Negative indexing starts from the end.

***

### 4. Slicing

```python
word = "Python"

word[1:4]    # 'yth'
word[:3]     # 'Pyt'
word[3:]     # 'hon'
word[::2]    # 'Pto'
word[::-1]   # 'nohtyP'
```

The stop position is exclusive.

***

### 5. Strings are immutable

```python
word = "Python"
word[0] = "J"
```

Output:

```text
TypeError
```

You cannot modify one character inside a string.

To create a changed string, create a new string.

```python
word = "Python"
word = "J" + word[1:]

print(word)
```

Output:

```text
Jython
```

***

### 6. Useful string methods

```python
word.lower()
word.upper()
word.strip()
word.replace("a", "b")
word.startswith("Py")
word.endswith("on")
word.count("t")
word.find("t")
```

***

### 7. `find()` versus `index()`

`find()` returns `-1` if the substring is not found.

```python
"Python".find("z")      # -1
```

`index()` raises `ValueError` if the substring is not found.

```python
"Python".index("z")
```

Output:

```text
ValueError
```

***

### 8. String concatenation

```python
first = "Alok"
last = "Rahate"

full = first + " " + last
```

***

### 9. Formatted strings

```python
name = "Alok"
age = 20

print(f"My name is {name} and I am {age}.")
```

f-strings are the preferred modern way to insert values into strings.

***

### 10. Escape characters

| Escape sequence | Meaning |
|---|---|
| `\n` | New line |
| `\t` | Tab |
| `\\` | Backslash |
| `\"` | Double quote |

```python
print("Hello\nWorld")
```

Output:

```text
Hello
World
```

***

### 11. Common error

```python
age = 20
print("Age: " + age)
```

Output:

```text
TypeError
```

A string cannot be directly concatenated with an integer.

Fix it:

```python
print("Age: " + str(age))
```

Or use an f-string:

```python
print(f"Age: {age}")
```

***

# Day 5

## Topic: Input, Output and Boolean Logic

## Theory

### 1. Getting user input

```python
name = input("Enter your name: ")
```

Critical rule:

> `input()` always returns a string.

Even if the user types:

```text
20
```

Python receives:

```python
"20"
```

***

### 2. Converting input

```python
age = int(input("Enter age: "))
```

For decimals:

```python
price = float(input("Enter price: "))
```

***

### 3. Input expression flow

```python
age = int(input("Enter age: "))
```

Conceptually:

```text
input()
   ↓
string
   ↓
int()
   ↓
integer
   ↓
assignment
```

***

### 4. Multiple inputs

```python
a = int(input("Enter A: "))
b = int(input("Enter B: "))
```

***

### 5. Boolean values

Python has two Boolean values:

```python
True
False
```

***

### 6. Truthiness

Python treats many values as truthy or falsy.

Common falsy values:

```python
False
None
0
0.0
""
[]
()
{}
set()
```

Most other values are truthy.

```python
bool("Python")  # True
bool([1, 2])    # True
bool([])        # False
```

***

### 7. Logical `and`

```python
True and True      # True
True and False     # False
```

Both conditions need to be true.

```python
age >= 18 and has_id
```

***

### 8. Logical `or`

```python
True or False      # True
False or False     # False
```

At least one condition must be true.

***

### 9. Logical `not`

```python
not True      # False
not False     # True
```

***

### 10. Short-circuit evaluation

Python may stop evaluating as soon as it knows the final result.

```python
False and something
```

`something` does not need to be evaluated.

Similarly:

```python
True or something
```

`something` does not need to be evaluated.

This is useful for safe checks.

```python
name = ""

if name and name[0] == "A":
    print("Starts with A")
```

Python does not try to access `name[0]` if `name` is empty.

***

### 11. Dangerous input assumption

```python
age = int(input())
```

This crashes if the user enters:

```text
twenty
```

Output:

```text
ValueError
```

Handling invalid input properly will become important later when learning exception handling.

***

# Day 6

## Topic: Conditional Statements — `if`, `elif`, `else`

## Theory

### 1. What conditional statements do

Conditional statements allow a program to make decisions.

```text
Condition
    ↓
True  → Execute block
False → Skip block
```

***

### 2. Basic `if`

```python
age = 20

if age >= 18:
    print("Adult")
```

***

### 3. `if` and `else`

```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

***

### 4. `elif`

Use `elif` when there are multiple mutually exclusive possibilities.

```python
marks = 75

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "D"
```

***

### 5. Order matters

Python checks conditions from top to bottom.

```python
if marks >= 60:
    print("C")
elif marks >= 90:
    print("A")
```

A mark of `95` prints:

```text
C
```

The first condition is already true, so Python never checks the `elif`.

Write more specific or higher conditions first.

***

### 6. Nested conditions

An `if` statement can exist inside another `if` statement.

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
```

***

### 7. Combining conditions

Instead of nesting, you can often combine conditions.

```python
if age >= 18 and has_id:
    print("Entry allowed")
```

***

### 8. Comparison chaining

Python allows chained comparisons.

```python
18 <= age <= 60
```

This is equivalent to:

```python
age >= 18 and age <= 60
```

***

### 9. Conditional expression

A simple two-way decision can be written in one line.

```python
status = "Adult" if age >= 18 else "Minor"
```

Do not use conditional expressions when they make the code difficult to read.

***

### 10. Common mistakes

`=` assigns a value.

```python
x = 10
```

`==` compares values.

```python
x == 10
```

Also remember that indentation determines which statements belong to an `if`, `elif`, or `else` block.

***

# Day 7

## Topic: `while` Loops

## Theory

### 1. What is a loop?

A loop repeatedly executes a block of code.

```text
Condition
   ↓
True → Execute → Condition
   ↑                 |
   └─────────────────┘

False → Exit
```

***

### 2. Basic `while` loop

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```text
1
2
3
4
5
```

***

### 3. The three essential parts

A controlled `while` loop normally needs:

```text
Initialisation
     ↓
Condition
     ↓
Update
```

Missing the update can create an infinite loop.

***

### 4. Infinite loop

```python
count = 1

while count <= 5:
    print(count)
```

`count` never changes, so the condition remains true forever.

***

### 5. `break`

`break` immediately exits a loop.

```python
while True:
    value = int(input("Enter 0 to stop: "))

    if value == 0:
        break
```

***

### 6. `continue`

`continue` skips the remaining code in the current iteration and moves to the next iteration.

```python
count = 0

while count < 5:
    count += 1

    if count == 3:
        continue

    print(count)
```

Output:

```text
1
2
4
5
```

***

### 7. `while ... else`

Python allows an `else` block after a loop.

```python
count = 1

while count <= 3:
    print(count)
    count += 1
else:
    print("Loop completed")
```

The `else` block runs only when the loop finishes normally.

If `break` exits the loop, the loop’s `else` block does not run.

***

### 8. When to use `while`

Use `while` when repetition depends mainly on a condition rather than a known sequence of values.

Examples:

- Password attempts
- Menus
- Input validation
- Games
- Retry mechanisms
- Repeating until the user chooses to exit

***

### 9. Common errors

- Forgetting to update the control variable
- Writing the wrong condition
- Accidentally creating an infinite loop
- Incorrect indentation

***

# Day 8

## Topic: `for` Loops, `range()`, `break` and `continue`

## Theory

### 1. What a `for` loop does

A `for` loop iterates over an iterable.

```python
for item in iterable:
    ...
```

Example:

```python
for letter in "Python":
    print(letter)
```

***

### 2. `range()`

`range()` represents a sequence of numbers that can be iterated over.

```python
range(5)
```

Represents:

```text
0 1 2 3 4
```

The stop value is exclusive.

***

### 3. Different forms of `range()`

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

Examples:

```python
range(5)          # 0, 1, 2, 3, 4
range(2, 6)       # 2, 3, 4, 5
range(1, 10, 2)   # 1, 3, 5, 7, 9
```

***

### 4. Counting backwards

```python
for i in range(5, 0, -1):
    print(i)
```

Output:

```text
5
4
3
2
1
```

***

### 5. `for` loop with strings

```python
for char in "Python":
    print(char)
```

A string is iterable.

***

### 6. `break` in a `for` loop

```python
for i in range(10):
    if i == 5:
        break

    print(i)
```

Output:

```text
0
1
2
3
4
```

***

### 7. `continue` in a `for` loop

```python
for i in range(6):
    if i % 2 == 0:
        continue

    print(i)
```

Output:

```text
1
3
5
```

***

### 8. `for ... else`

```python
for i in range(5):
    print(i)
else:
    print("Completed")
```

The `else` block executes only if the loop finishes without `break`.

***

### 9. Nested loops

A loop can contain another loop.

```python
for row in range(3):
    for column in range(3):
        print(row, column)
```

The inner loop completes all of its iterations for each outer-loop iteration.

***

### 10. Loop variable

```python
for i in range(5):
    print(i)
```

`i` receives each value produced by the iterable.

***

### 11. `for` versus `while`

| `for` loop | `while` loop |
|---|---|
| Best for iterating over data or ranges | Best for condition-controlled repetition |
| Number of iterations is often known | Number of iterations may be unknown |
| Naturally works with iterables | Based on a Boolean condition |
| Common for strings, lists, tuples, sets, and dictionaries | Common for menus, retries, and validation |

***

### 12. Important connection

Lists make `for` loops much more useful.

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

***

# Day 9

## Topic: Functions, Scope, `return`, `None` and Parameters

## Theory

### 1. What is a function?

A function is a reusable block of code designed to perform a specific task.

Instead of repeatedly writing:

```python
print("Welcome")
```

You can define a function:

```python
def welcome():
    print("Welcome")
```

***

### 2. Defining a function

```python
def greet():
    print("Hello")
```

`def` begins a function definition.

***

### 3. Calling a function

Defining a function does not execute it.

```python
def greet():
    print("Hello")

greet()
```

The function executes only when it is called.

***

### 4. Parameters and arguments

```python
def greet(name):
    print("Hello", name)

greet("Alok")
```

Here:

```text
name    → parameter
"Alok"  → argument
```

***

### 5. Multiple parameters

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

***

### 6. `return`

`return` sends a value back to the caller.

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

Output:

```text
30
```

***

### 7. `print()` versus `return`

This distinction is extremely important.

```python
def add(a, b):
    print(a + b)
```

This prints the result but does not return it.

```python
def add(a, b):
    return a + b
```

This returns the result to the caller.

```python
result = add(10, 20)
```

A returned value can be stored, reused, compared, or passed to another function.

***

### 8. What happens without `return`?

```python
def greet():
    print("Hello")

result = greet()
print(result)
```

Output:

```text
Hello
None
```

A function without an explicit `return` returns `None`.

***

### 9. `return` immediately exits a function

```python
def check(age):
    if age < 18:
        return "Minor"

    return "Adult"
```

Once `return` runs, the function stops immediately.

***

### 10. Multiple return values

```python
def calculate(a, b):
    return a + b, a - b
```

Python technically returns one tuple.

```python
result = calculate(10, 5)
print(result)
```

Output:

```python
(15, 5)
```

You can unpack it:

```python
total, difference = calculate(10, 5)
```

This becomes especially important in the Tuples topic.

***

### 11. Local variables

```python
def test():
    x = 10
    print(x)

test()
```

`x` belongs to the function’s local scope.

Trying to use it outside the function causes an error.

```python
print(x)
```

Output:

```text
NameError
```

***

### 12. Global variables

```python
x = 10

def show():
    print(x)

show()
```

A function can read a global variable.

However, modifying global state should usually be avoided when a parameter and return value can solve the problem more clearly.

***

### 13. Default parameters

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Alok")
```

Output:

```text
Hello Guest
Hello Alok
```

***

### 14. Keyword arguments

```python
def student(name, age):
    print(name, age)

student(age=20, name="Alok")
```

Arguments can be passed using parameter names.

***

### 15. Positional arguments

```python
student("Alok", 20)
```

Values are assigned based on their positions.

***

### 16. Docstrings — preview

A function can contain documentation immediately after its definition.

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b
```

Docstrings are covered in detail on Day 12.

***

### 17. Functions and mutable data — preview

Functions receive references to objects.

```python
def add_item(items):
    items.append(10)
```

If a list is passed to this function, the original list can change. This becomes important when learning about list mutability and references.

***

### 18. Common mistakes

```python
result = print("Hello")
```

`result` becomes:

```python
None
```

Remember:

```python
def add(a, b):
    return a + b
```

is different from:

```python
def add(a, b):
    print(a + b)
```

***

### 19. Why functions matter

Functions provide:

- Reusability
- Modularity
- Readability
- Easier testing
- Easier debugging
- Separation of responsibilities

Functions are the bridge from writing small scripts to building larger programs.

***

# Day 10

## Topic: Lists

## Theory

### 1. What is a list?

A list is an ordered, mutable sequence that can hold a mix of data types.

```python
items = [1, "Python", 2.5, True]
```

A list stores references to objects rather than directly containing the objects themselves. This explains important concepts such as aliasing, shallow copying, nested lists, and mutable function arguments.

***

### 2. Creating lists

```python
[]                         # Empty list
[1, "a", 2.5, True]        # Mixed types
list("abc")                # ['a', 'b', 'c']
list(range(5))             # [0, 1, 2, 3, 4]
"a b c".split()            # ['a', 'b', 'c']
[0] * 3                    # [0, 0, 0]
```

***

### 3. Indexing and slicing

Lists use indexing and slicing like strings.

```python
numbers = [10, 20, 30, 40, 50]

numbers[0]       # 10
numbers[-1]      # 50
numbers[1:4]     # [20, 30, 40]
numbers[::2]     # [10, 30, 50]
numbers[::-1]    # [50, 40, 30, 20, 10]
```

The stop value in slicing is exclusive.

```python
numbers [developers.google](https://developers.google.com/edu/python/introduction)
```

Output:

```text
IndexError
```

But slices do not raise `IndexError`.

```python
numbers[10:20]
```

Output:

```python
[]
```

***

### 4. Changing lists through slices

Unlike strings, lists can be changed through indexing and slicing.

```python
numbers = [10, 20, 30, 40, 50]

numbers[1:3] = [0]
print(numbers)
```

Output:

```python
[10, 0, 40, 50]
```

Two items were replaced by one item.

Delete by index:

```python
del numbers[0]
```

***

### 5. List methods that change the original list

Most list methods that change a list return `None`.

Do **not** write:

```python
numbers = numbers.sort()
```

`numbers` would become `None`.

| Method | Effect |
|---|---|
| `append(x)` | Adds one item to the end |
| `extend(iterable)` | Adds every item from an iterable |
| `insert(i, x)` | Inserts an item at position `i` |
| `remove(x)` | Removes the first matching value |
| `pop(i=-1)` | Removes and returns an item |
| `clear()` | Removes all items |
| `sort(key=, reverse=)` | Sorts the list in place |
| `reverse()` | Reverses the list in place |

Examples:

```python
items = [1, 2, 3]

items.append(4)
# [1, 2, 3, 4]

items.extend([5, 6])
# [1, 2, 3, 4, 5, 6]

items.insert(1, 99)
# [1, 99, 2, 3, 4, 5, 6]
```

Important difference:

```python
items.append([7, 8])
```

Adds one list as one item.

```python
items.extend([7, 8])
```

Adds `7` and `8` as separate items.

***

### 6. Tools that do not change the list

```python
len(items)
min(items)
max(items)
sum(items)
sorted(items)
reversed(items)
items.count(value)
items.index(value)
value in items
a + b
a * 3
```

Important details:

- `sorted(items)` returns a new sorted list.
- `reversed(items)` returns an iterator, not a list.
- Use `list(reversed(items))` if you need a reversed list.
- `a + b` creates a new list.
- `a * 3` creates a new list with repeated elements.

List comparisons work element by element.

```python
[1, 2] < [1, 3]  # True
```

***

### 7. Sorting details

Sorting is stable.

If two items have equal sort keys, they keep their original relative order.

```python
words = ["banana", "Apple", "cherry"]

sorted(words, key=str.lower)
```

Sort by length:

```python
words = ["cat", "elephant", "dog"]

sorted(words, key=len)
```

Sorting mixed, non-comparable types raises an error.

```python
sorted([1, "a"])
```

Output:

```text
TypeError
```

You can sort using multiple criteria by returning a tuple from a key function.

```python
players = [
    ("Asha", 90),
    ("Rohit", 95),
    ("Kiran", 90)
]

def by_score_then_name(player):
    return (-player [docs.python](https://docs.python.org/3/tutorial/datastructures.html), player[0])

sorted(players, key=by_score_then_name)
```

This sorts:

- Higher score first
- Name alphabetically when scores are equal

***

### 8. References, aliasing and copying

This is one of the most important list concepts.

```python
a = [1, 2, 3]
b = a
```

`b` is not a copy. Both names refer to the same list.

```python
b.append(4)

print(a)
```

Output:

```python
[1, 2, 3, 4]
```

Create a shallow copy using:

```python
c = a[:]
c = a.copy()
c = list(a)
```

```python
a is c   # False
a == c   # True
```

`is` checks whether objects are the same object.

`==` checks whether values are equal.

***

### 9. Shallow copying and nested lists

A shallow copy copies only the outer list.

```python
a = [[1, 2], [3, 4]]
b = a.copy()

b[0].append(99)

print(a)
```

Output:

```python
[[1, 2, 99], [3, 4]]
```

The inner lists are still shared.

For a fully independent copy of nested data:

```python
import copy

b = copy.deepcopy(a)
```

***

### 10. The nested-list multiplication trap

Avoid this:

```python
grid = [[0] * 3] * 3
```

All three rows refer to the same inner list.

```python
grid[0][0] = 7
print(grid)
```

Output:

```python
[[7, 0, 0], [7, 0, 0], [7, 0, 0]]
```

Correct approach:

```python
grid = []

for _ in range(3):
    grid.append([0] * 3)
```

Later, after learning comprehensions:

```python
grid = [[0] * 3 for _ in range(3)]
```

Each iteration creates a fresh inner list.

***

### 11. Loops and lists

Prefer:

```python
for item in items:
    print(item)
```

Instead of:

```python
for i in range(len(items)):
    print(items[i])
```

Use `enumerate()` when you need position and value.

```python
for index, item in enumerate(items, start=1):
    print(index, item)
```

Use `zip()` to loop through two lists together.

```python
names = ["Asha", "Rohit"]
marks = [90, 85]

for name, mark in zip(names, marks):
    print(name, mark)
```

`zip()` stops when the shortest iterable ends.

***

### 12. Do not modify a list while looping over it

Avoid:

```python
for item in items:
    if item < 0:
        items.remove(item)
```

Removing items changes positions, which can cause items to be skipped.

Loop over a copy instead:

```python
for item in items[:]:
    if item < 0:
        items.remove(item)
```

Or build a new list.

```python
clean_items = []

for item in items:
    if item >= 0:
        clean_items.append(item)
```

***

### 13. Unpacking lists

```python
first, *rest = [1, 2, 3, 4]
```

Results:

```python
first  # 1
rest   # [2, 3, 4]
```

```python
*head, last = [1, 2, 3, 4]
```

Results:

```python
head  # [1, 2, 3]
last  # 4
```

Swapping variables:

```python
a, b = b, a
```

***

### 14. Lists and functions

A function receives a reference to the same list object.

```python
def add_item(items):
    items.append(1)

numbers = [10, 20]
add_item(numbers)

print(numbers)
```

Output:

```python
[10, 20, 1]
```

However, rebinding the local parameter does not change the caller’s variable.

```python
def add_item(items):
    items = items +  [docs.python](https://docs.python.org/3/tutorial/datastructures.html)

numbers = [10, 20]
add_item(numbers)

print(numbers)
```

Output:

```python
[10, 20]
```

`items +  [docs.python](https://docs.python.org/3/tutorial/datastructures.html)` creates a new list and assigns it only to the local name `items`.

***

### 15. Mutable default argument trap

Avoid this:

```python
def add_item(item, box=[]):
    box.append(item)
    return box
```

The list is created once when the function is defined, so all calls without `box` share the same list.

Correct approach:

```python
def add_item(item, box=None):
    if box is None:
        box = []

    box.append(item)
    return box
```

***

### 16. Strings and lists

```python
"a,b,c".split(",")
```

Output:

```python
["a", "b", "c"]
```

```python
"-".join(["a", "b"])
```

Output:

```text
a-b
```

Items passed to `join()` must all be strings.

```python
list("abc")
```

Output:

```python
["a", "b", "c"]
```

***

### 17. Speed overview

These are rough practical ideas:

| Operation | Typical performance idea |
|---|---|
| Indexing `items[i]` | Fast |
| `append()` | Usually fast |
| `pop()` from the end | Usually fast |
| `insert(0, x)` | Slower for large lists |
| `pop(0)` | Slower for large lists |
| `remove(x)` | Scans the list |
| `x in items` | Scans the list |
| `items.count(x)` | Scans the list |

Lists are excellent when order matters and you access items by position.

***

### 18. Common errors

| Error | Typical cause |
|---|---|
| `IndexError` | Invalid index position |
| `ValueError` | Missing value passed to `remove()` or `index()` |
| `TypeError` | Sorting incompatible types or joining non-strings |
| `None` result | Writing `items = items.sort()` |

***

# Day 11

## Topic: Tuples

## Theory

### 1. What is a tuple?

A tuple is an ordered, immutable sequence.

Once created, you cannot add, remove, or replace its elements.

```python
point = (3, 4)
```

Lists are generally used for data that changes.

Tuples are generally used for fixed collections or records that should not change shape. Python’s documentation describes tuples as immutable sequences, often useful for heterogeneous records and values that can safely participate in sets or dictionary keys when their contents are hashable. [docs.python](https://docs.python.org/3/builtins/stdtypes.html)

***

### 2. Creating tuples

```python
t = (1, 2, 3)
t = 1, 2, 3
```

Parentheses are optional when multiple values are separated by commas.

```python
single = (5,)
```

The comma makes it a tuple.

```python
not_a_tuple = (5)
```

This is only the integer `5` inside parentheses.

```python
empty = ()
t = tuple([1, 2, 3])
t = tuple("abc")
```

Output:

```python
('a', 'b', 'c')
```

The single-item tuple trap is one of the most common tuple mistakes:

> No comma means no tuple.

***

### 3. Indexing and slicing

Tuples support indexing and slicing exactly like lists.

```python
t = (10, 20, 30, 40)

t[0]       # 10
t[-1]      # 40
t[1:3]     # (20, 30)
```

***

### 4. Immutability

```python
t = (1, 2, 3)
t[0] = 99
```

Output:

```text
TypeError: 'tuple' object does not support item assignment
```

You cannot replace an item stored in a tuple.

***

### 5. Tuples can contain mutable objects

A tuple itself is immutable, but it can contain mutable objects such as lists.

```python
t = ([1, 2], "fixed")

t[0].append(3)
print(t)
```

Output:

```python
([1, 2, 3], "fixed")
```

This is allowed because the list object is mutated in place.

This is not allowed:

```python
t[0] = [9, 9]
```

That tries to replace the item at position `0`, which would modify the tuple.

The tuple itself never changes shape, but mutable objects inside it can still change.

***

### 6. Tuple methods

Tuples have only two common methods because they are immutable.

```python
t.count(value)
t.index(value)
```

```python
t = (10, 20, 20, 30)

t.count(20)  # 2
t.index(30)  # 3
```

There is no:

```python
t.append()
t.sort()
t.remove()
```

***

### 7. Packing and unpacking

Packing:

```python
point = 3, 4
```

Unpacking:

```python
x, y = point
```

Extended unpacking:

```python
a, *middle, b = (1, 2, 3, 4, 5)
```

Results:

```python
a       # 1
middle  # [2, 3, 4]
b       # 5
```

The starred target becomes a list.

Swapping variables:

```python
x, y = y, x
```

Python creates values on the right side first, then unpacks them into the names on the left.

***

### 8. Why tuples exist

Tuples are useful for several important reasons.

- Returning multiple values from functions.
- Representing fixed-shape data such as coordinates and RGB colours.
- Using immutable values as dictionary keys or set members.
- Receiving data that should not be reordered or structurally modified.
- Understanding `zip()`, which produces tuples.

Example: multiple return values.

```python
def divide(a, b):
    return a // b, a % b

quotient, remainder = divide(10, 3)
```

Example: coordinate as a dictionary key.

```python
locations = {
    (0, 0): "Origin",
    (10, 20): "Point A"
}
```

A list cannot be used as a dictionary key because lists are mutable and unhashable. [docs.python](https://docs.python.org/3/tutorial/datastructures.html)

***

### 9. Hashability

A tuple is hashable only if every item inside it is hashable.

```python
hash((1, 2, 3))
```

This works.

```python
hash((1, [2, 3]))
```

This fails because a list is unhashable.

```text
TypeError
```

Examples:

```python
(1, 2, 3)       # Hashable
("A", True, 5)  # Hashable
(1, [2, 3])     # Not hashable
```

***

### 10. Tuple comparisons

Tuples compare lexicographically, element by element.

```python
(1, 2) < (1, 3)
```

Output:

```python
True
```

Python compares:

```text
1 with 1
2 with 3
```

Since `2 < 3`, the full comparison is `True`.

***

# Day 12

## Topic: Docstrings, Recursion, Sets and Dictionaries

***

## Docstrings

### 1. What is a docstring?

A docstring is a string literal placed as the first statement inside a module, function, class, or method.

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b
```

A docstring explains what the code does.

Python stores the docstring in the object’s `__doc__` attribute. [docs.python](https://docs.python.org/3/builtins/stdtypes.html)

```python
print(add.__doc__)
```

Output:

```text
Return the sum of two numbers.
```

You can also inspect documentation using `help()`.

```python
help(add)
```

***

### 2. Single-line docstrings

Use a short single-line docstring when the function is simple.

```python
def square(number):
    """Return the square of number."""
    return number * number
```

***

### 3. Multi-line docstrings

Use a multi-line docstring for more detailed explanations.

```python
def calculate_total(price, quantity):
    """
    Return the total cost.

    Parameters:
        price: Price of one item.
        quantity: Number of items.
    """
    return price * quantity
```

***

## Recursion

### 1. What is recursion?

Recursion is the process of defining something in terms of itself.

A recursive function is a function that calls itself.

A physical-world example is two parallel mirrors facing each other. An object between them appears repeatedly in reflected images.

***

### 2. Recursive function

Python functions can call other functions.

A function can also call itself.

```python
def function_name():
    function_name()
```

This is called recursion.

However, a recursive function must have a stopping condition. Without one, it continues until Python reaches its recursion limit and raises `RecursionError`.

***

### 3. Base case and recursive case

Every safe recursive function needs:

- A **base case**: the condition that stops recursion.
- A **recursive case**: the part where the function calls itself with a smaller or simpler problem.

Example: factorial.

```python
def factorial(n):
    """Return the factorial of a non-negative integer."""
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)
```

```python
print(factorial(5))
```

Output:

```text
120
```

Conceptually:

```text
factorial(5)
= 5 × factorial(4)
= 5 × 4 × factorial(3)
= 5 × 4 × 3 × factorial(2)
= 5 × 4 × 3 × 2 × factorial(1)
= 120
```

***

### 4. Safer factorial input

The simple factorial function should reject negative numbers.

```python
def factorial(n):
    """Return n! for a non-negative integer."""
    if n < 0:
        raise ValueError("n must be non-negative")

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)
```

```python
number = int(input("Enter a non-negative integer: "))
print(factorial(number))
print(factorial.__doc__)
```

For large values, recursion can hit Python’s recursion limit. Iterative solutions are often more practical for deeply repeated tasks.

***

## Sets

### 1. What is a set?

A set is an unordered collection of unique, hashable items.

```python
info = {"Ajay", 19, False, 5.9, 19}
print(info)
```

A possible output is:

```python
{False, 19, 5.9, 'Ajay'}
```

The displayed order is not something you should rely on.

Sets:

- Do not allow duplicate values.
- Do not support indexing.
- Are mutable containers.
- Require their elements to be hashable.

Important correction:

> A normal Python `set` is mutable. You can add and remove items after creating it.

What cannot be changed is an individual set element “in place” through indexing, because sets have no indexes. Set elements must also be hashable, so mutable types such as lists and dictionaries cannot be elements of a set. The official Python documentation treats dictionaries, lists, sets, and tuples as general-purpose built-in containers, while dictionaries and sets rely on hashable values for keys/elements. [docs.python](https://docs.python.org/3/tutorial/datastructures.html)

***

### 2. Creating sets

```python
s = {1, 2, 3}
s = set([1, 2, 2, 3])
s = set("hello")
```

Possible outputs:

```python
{1, 2, 3}
{'h', 'e', 'l', 'o'}
```

Create an empty set using:

```python
empty = set()
```

Do not use this:

```python
empty = {}
```

That creates an empty dictionary, not a set.

***

### 3. Sets require hashable items

This fails:

```python
{[1, 2], 3}
```

Output:

```text
TypeError
```

This works:

```python
{(1, 2), 3}
```

Lists are mutable and unhashable.

Tuples can be hashable if everything inside them is hashable.

***

### 4. Adding and removing items

```python
s = {1, 2, 3}

s.add(4)
s.update([5, 6])
s.remove(4)
s.discard(4)
s.pop()
s.clear()
```

| Method | Meaning |
|---|---|
| `add(value)` | Add one item |
| `update(iterable)` | Add multiple items |
| `remove(value)` | Remove an item; raises `KeyError` if missing |
| `discard(value)` | Remove an item safely; no error if missing |
| `pop()` | Remove and return an arbitrary item |
| `clear()` | Remove all items |

`set.pop()` does not remove a predictable position because sets are unordered.

***

### 5. Set mathematics

Sets are especially useful for mathematical set operations.

```python
a = {1, 2, 3}
b = {2, 3, 4}
```

| Operation | Code | Result |
|---|---|---|
| Union | `a | b` | `{1, 2, 3, 4}` |
| Intersection | `a & b` | `{2, 3}` |
| Difference | `a - b` | `{1}` |
| Symmetric difference | `a ^ b` | `{1, 4}` |

```python
a | b
```

Everything in either set.

```python
a & b
```

Only items present in both sets.

```python
a - b
```

Items in `a` but not in `b`.

```python
a ^ b
```

Items in exactly one of the sets.

Think of these operations using Venn diagrams.

***

### 6. Set comparisons

```python
{1, 2} <= {1, 2, 3}
```

Output:

```python
True
```

This asks whether the left set is a subset of the right set.

```python
{1, 2, 3} >= {1, 2}
```

Output:

```python
True
```

This asks whether the left set is a superset of the right set.

Readable method forms:

```python
{1, 2}.issubset({1, 2, 3})
{1, 2, 3}.issuperset({1, 2})
{1, 2}.isdisjoint({3, 4})
```

`isdisjoint()` returns `True` when two sets have no common items.

***

### 7. Removing duplicates while preserving order

A set removes duplicates, but a set alone should not be used when output order matters.

Use a set for fast membership checking and a list for preserving order.

```python
items = ["a", "b", "a", "c", "b"]

seen = set()
unique_in_order = []

for item in items:
    if item not in seen:
        seen.add(item)
        unique_in_order.append(item)

print(unique_in_order)
```

Output:

```python
['a', 'b', 'c']
```

This pattern is common in real Python programs.

***

### 8. `frozenset`

`frozenset` is an immutable version of `set`.

```python
frozen = frozenset({1, 2, 3})
```

You cannot add or remove items from a `frozenset`.

Because it is immutable and hashable when its contents are hashable, a `frozenset` can be used as a dictionary key or stored inside another set.

***

### 9. Set comprehensions — preview

Set comprehensions are a later topic.

```python
squares = {n * n for n in range(5)}
```

Output:

```python
{0, 1, 4, 9, 16}
```

***

### 10. Why membership testing is fast in sets

When checking membership in a list:

```python
value in items
```

Python may need to inspect items one by one.

With a set:

```python
value in values_set
```

Python uses hashing, making membership checks typically much faster for large collections.

Use a set when:

- You need unique values.
- You frequently check membership.
- You need mathematical set operations.
- The order of items does not matter.

***

### 11. Common set mistakes

| Mistake | Explanation |
|---|---|
| Using `{}` for an empty set | `{}` creates an empty dictionary |
| Trying `s[0]` | Sets have no indexes |
| Expecting output order | Set order should not be relied upon |
| Calling `pop()` expecting a specific item | `pop()` removes an arbitrary item |
| Adding a list to a set | Lists are unhashable |

***

## Dictionaries

### 1. What is a dictionary?

A dictionary is a collection of key-value pairs.

```python
student = {
    "name": "Alok",
    "age": 20
}
```

Instead of finding values by numeric position, dictionaries find values through meaningful keys.

A dictionary is often called a mapping or associative array. Dictionary keys must be unique and hashable. [docs.python](https://docs.python.org/3/tutorial/datastructures.html)

Modern Python dictionaries preserve insertion order as a language guarantee. However, dictionaries should still be chosen for key-based lookup rather than because you need list-like positional access.

***

### 2. Creating dictionaries

```python
d = {}
d = {"name": "Alok", "age": 20}
d = dict(name="Alok", age=20)
d = dict([("a", 1), ("b", 2)])
```

***

### 3. Dictionary keys must be hashable

This works:

```python
d = {(0, 0): "origin"}
```

This fails:

```python
d = {[0, 0]: "origin"}
```

Output:

```text
TypeError
```

Lists cannot be dictionary keys because they are mutable and unhashable.

Dictionary values can be almost anything:

```python
data = {
    "numbers": [1, 2, 3],
    "student": {"name": "Alok"},
    "function": print
}
```

***

### 4. Accessing values

```python
d = {"name": "Alok", "age": 20}

d["name"]
d.get("name")
d.get("city", "N/A")
"name" in d
```

| Expression | Result |
|---|---|
| `d["name"]` | Returns the value; raises `KeyError` if missing |
| `d.get("name")` | Returns the value or `None` if missing |
| `d.get("city", "N/A")` | Returns `"N/A"` if missing |
| `"name" in d` | Checks keys only |

Use square brackets when a missing key means there is likely a bug.

```python
student_id = d["student_id"]
```

Use `.get()` when missing data is normal.

```python
city = d.get("city", "Unknown")
```

***

### 5. Adding and changing values

```python
d = {"name": "Alok", "age": 20}

d["city"] = "Nagpur"
d["age"] = 21
```

The same syntax adds a new key or overwrites an existing key.

```python
d.update({"age": 21, "job": "developer"})
```

`update()` merges multiple key-value pairs.

***

### 6. Removing values

```python
del d["city"]
d.pop("age")
d.pop("age", None)
d.popitem()
d.clear()
```

| Operation | Meaning |
|---|---|
| `del d["key"]` | Removes a key; raises `KeyError` if missing |
| `d.pop("key")` | Removes and returns the value; raises `KeyError` if missing |
| `d.pop("key", default)` | Removes and returns the value or `default` if missing |
| `d.popitem()` | Removes and returns the last inserted key-value pair |
| `d.clear()` | Removes all items |

***

### 7. Looping through dictionaries

Loop over keys:

```python
for key in d:
    print(key)
```

Explicitly loop over keys:

```python
for key in d.keys():
    print(key)
```

Loop over values:

```python
for value in d.values():
    print(value)
```

Loop over both keys and values:

```python
for key, value in d.items():
    print(key, value)
```

`items()` is the most common choice when you need both the key and value. [docs.python](https://docs.python.org/3/tutorial/datastructures.html)

***

### 8. Dictionary views

```python
d.keys()
d.values()
d.items()
```

These return dynamic view objects, not normal lists.

```python
d = {"name": "Alok"}

keys = d.keys()
print(keys)

d["age"] = 20
print(keys)
```

The view reflects later dictionary changes.

Use `list()` if you need a separate list snapshot.

```python
key_list = list(d.keys())
```

***

### 9. Do not change dictionary size while looping directly

Avoid:

```python
for key in d:
    if key.startswith("_"):
        del d[key]
```

This can cause:

```text
RuntimeError: dictionary changed size during iteration
```

Loop over a list copy of the keys.

```python
for key in list(d.keys()):
    if key.startswith("_"):
        del d[key]
```

***

### 10. Dictionary comprehensions — preview

Dictionary comprehensions are a later topic.

```python
squares = {n: n * n for n in range(5)}
```

Output:

```python
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

***

### 11. Nested dictionaries

Real-world data is often nested.

```python
students = {
    "Asha": {"age": 20, "marks": [82, 90]},
    "Rohit": {"age": 21, "marks": [55, 60]}
}
```

Access nested values step by step.

```python
students["Asha"]["marks"].append(95)
```

This changes Asha’s marks list.

Nested dictionaries and lists are common in JSON data, APIs, configuration files, and web development.

***

### 12. Merging dictionaries

Python 3.9 and later support `|`.

```python
dict_a = {"a": 1, "b": 2}
dict_b = {"b": 20, "c": 3}

merged = dict_a | dict_b
print(merged)
```

Output:

```python
{"a": 1, "b": 20, "c": 3}
```

When keys clash, the right dictionary wins.

Merge into the existing dictionary:

```python
dict_a |= dict_b
```

***

### 13. `setdefault()`

`setdefault()` returns the current value for a key.

If the key does not exist, it creates the key with a default value.

```python
d = {}

d.setdefault("tags", []).append("python")
print(d)
```

Output:

```python
{"tags": ["python"]}
```

This is similar to:

```python
if "tags" not in d:
    d["tags"] = []

d["tags"].append("python")
```

***

### 14. Counting pattern

Dictionaries are ideal for counting occurrences.

```python
words = ["python", "java", "python", "c", "python", "java"]

counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)
```

Output:

```python
{"python": 3, "java": 2, "c": 1}
```

This pattern replaces the need for parallel lists and repeated `.index()` lookups.

***

### 15. Dictionary equality and copying

Dictionary equality compares key-value content.

```python
a = {"x": 1}
b = {"x": 1}

a == b   # True
a is b   # False
```

Copying is shallow by default.

```python
a = {"x": [1, 2]}
b = a.copy()

b["x"].append(3)

print(a)
```

Output:

```python
{"x": [1, 2, 3]}
```

The nested list is still shared.

Use `copy.deepcopy()` for a fully independent nested copy.

```python
import copy

b = copy.deepcopy(a)
```

***

### 16. Dictionary versus list

| Use a list when | Use a dictionary when |
|---|---|
| Order matters | You need lookup by a meaningful name or ID |
| You access by numeric position | You access by key |
| Duplicate values are meaningful | Keys must be unique |
| You need a sequence of items | You need key-value relationships |

Examples:

```python
marks = [80, 75, 90]
```

A list is suitable when values are mainly accessed by position.

```python
marks = {
    "Asha": 80,
    "Rohit": 75,
    "Kiran": 90
}
```

A dictionary is suitable when values are accessed by meaningful names.

***

### 17. Common dictionary errors

| Error | Typical cause |
|---|---|
| `KeyError` | Accessing or deleting a missing key with `[]` or `del` |
| `TypeError: unhashable type: 'list'` | Using a list as a dictionary key |
| `RuntimeError` | Changing dictionary size while iterating directly |
| Unexpected shared nested data | Using a shallow copy when a deep copy was needed |

***
