# 014_id_and_is.py

# == checks whether two values are equal (value equality).

# is checks whether two variables refer to the same object in memory (identity equality).

# id() returns an object’s identity as an integer that remains unique for that object during its lifetime. In CPython, it is generally related to the object’s memory location, but you should not rely on it as a memory-address feature in portable Python code.


# 1. MUTABLE OBJECTS (Lists, Dictionaries, Sets)
a = [10, 20]
b = [10, 20]
c = a

print(a == b)  # True: values are the same
print(a is b)  # False: they are different list objects

print(a is c)  # True: c refers to the same list as a

print(id(a))
print(id(b))
print(id(c))

# Modifying 'a' affects 'c' because they share the exact same object
a.append(30)
print(c)       # [10, 20, 30]
print(a is c)  # True


# 2. IMMUTABLE OBJECTS & INTEGER CACHING (Small Integer Optimization)
# Python caches small integers (typically from -5 to 256) to optimize memory reuse.
x = 100
y = 100
print(x == y)  # True
print(x is y)  # True: both variables point to the same cached integer object

p = 1000
q = 1000
print(p == q)  # True
print(p is q)  # False (or True depending on compiler optimizations, but distinct objects logically)


# 3. STRING INTERNING
# Short strings without special characters are often interned (reused) automatically.
str1 = "hello"
str2 = "hello"
print(str1 is str2)  # True: string interning points both to the same object

str3 = "hello world!"
str4 = "hello world!"
print(str3 == str4)  # True
print(str3 is str4)  # False (or True in interactive/repl optimizations)


# 4. TUPLES (Immutable Sequences)
# Empty tuples or identical literal tuples can share identity due to immutability optimizations.
t1 = (1, 2)
t2 = (1, 2)
print(t1 == t2)  # True
print(t1 is t2)  # May be False or True depending on implementation optimizations

# BUT if a tuple contains a mutable item, modifying the inner item does NOT change the tuple's identity:
t3 = ([1, 2], 3)
print(id(t3))
t3[0].append(99)
print(t3)        # ([1, 2, 99], 3)
print(id(t3))    # Same tuple id!


# 5. THE 'None' SINGLETON
# In Python, None is a singleton object. ALWAYS use 'is' or 'is not' to test for None.
val = None
print(val is None)      # True (Best Practice)
print(val is not None)  # False


# 6. COPY vs DEEPCOPY (Creating New Objects)
import copy

original_list = [[1, 2], [3, 4]]
shallow_copied = copy.copy(original_list)
deep_copied = copy.deepcopy(original_list)

print(original_list is shallow_copied)       # False: new outer list object
print(original_list[0] is shallow_copied[0]) # True: inner list references are shared!

print(original_list[0] is deep_copied[0])    # False: inner lists are completely cloned objects
