is_student = True
is_python_easy = True
is_python_difficult = False

'''The value does not get accepted if True or False is written as true or false.

Assume:
is_student = true

ERROR:
NameError: name 'true' is not defined. Did you mean: 'True'?
'''

print(is_student)
print(is_python_easy)
print(is_python_difficult)
print(type(is_student))
