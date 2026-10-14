age = input("Enter you Age: ")

print(age)
print(type(age))

age = int(age)
print(type(age))


'''
Suppose you enter:
20

Initially:
20
<class 'str'>

After:
age = int(age)
you get:
20
<class 'int'>

Why?
Because:
input()
returns a string.

Even if the user types:
500

Python initially receives:
"500"

not:
500
That's a fundamental programming concept.

🧠 Now Your First Mental Model

Remember this:
USER
 ↓
input()
 ↓
STRING
 ↓
TYPE CONVERSION
 ↓
INTEGER / FLOAT / BOOLEAN
 ↓
PROCESSING
 ↓
OUTPUT

This simple pipeline will appear repeatedly throughout your programming career.
'''
