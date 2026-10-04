t =(1, 2, 3)
print(t)
print(type(t))

t = 1, 2, 3 # parentheses are optional for multiple items
print(t)
print(type(t))

t = (5, ) # the COMMA makes it a tuple, not the parentheses
print(t)
print(type(t))

t = (5) # this is just the int 5 in parentheses!
print(t)
print(type(t))

t = ()
print(t)
print(type(t))

t = tuple([1, 2, 3]) # convert from a list
print(t)
print(type(t))

t = tuple("abc") # ('a', 'b', 'c')
print(t)
print(type(t))
