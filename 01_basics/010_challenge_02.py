'''
Build a program that asks the user for:

Name
Age
Height
College name
Whether they know Python (True/False)

Then display something like:
========== PROFILE ==========

Name       : Alok
Age        : 20
Height     : 5.8
College    : ABC College
Python     : True

=============================
Requirements
Your program must correctly use:

str
int
float
bool

And after taking each input, print its type.


⚔️ Bonus Challenge
Don't stop at the basic solution.

Try to calculate:
Age after 5 years
Current Age : 20
After 5 Years : 25

And:
Height in centimeters

If:
Height = 5.8 feet

calculate its approximate centimeter value.
You'll need to figure out the conversion yourself.
Don't Google the Python code.
'''

name = input("\nEnter your Name: ")
age = int(input("\nEnter your Age: "))
height = float(input("\nEnter your Height (in feet): "))
college = input("\nEnter your College Name: ")
python = bool(input("\nDo you Know Python Programming language (True or False): "))

print("\n============Profile============")
print("\nName:",name)
print("\nAge:",age)
print("\nHeight:",height)
print("\nCollege:",college)
print("\nPython:",python)

print("\nAge (After 5 years):",age+5)
print("\nHeight (in cm):",(height*30.48))

print("\n===============================")

