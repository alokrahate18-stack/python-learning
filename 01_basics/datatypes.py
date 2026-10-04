# 015_data_types_overview.py

# 1. BUILT-IN PRIMITIVE DATA TYPES

# Numeric Types: int, float, complex
a = 10
print(a, type(a))  # <class 'int'> -> Stores integer values (arbitrary precision in Python)

a = 10.56
print(a, type(a))  # <class 'float'> -> Stores double-precision floating-point numbers

a = 10 + 2j
print(a, type(a))  # <class 'complex'> -> Stores complex numbers (real + imaginary parts)

# Text Sequence Type: str
a = "Hello"
print(a, type(a))  # <class 'str'> -> Stores sequence of Unicode characters (Immutable)

# Boolean Type: bool
a = True
print(a, type(a))  # <class 'bool'> -> Subclass of int; stores True or False

# Binary Sequence Types: bytes, bytearray, memoryview
a = b"Hello"
print(a, type(a))  # <class 'bytes'> -> Immutable sequence of single bytes (0-255)

a = bytearray(b"Hello")
print(a, type(a))  # <class 'bytearray'> -> Mutable version of bytes

a = memoryview(b"Hello")
print(a, type(a))  # <class 'memoryview'> -> Access inner memory of objects without copying

# None Type: NoneType
a = None
print(a, type(a))  # <class 'NoneType'> -> Represents the absence of a value (Singleton)



# 2. DATA STRUCTURE (CONTAINER) DATA TYPES

# Sequence Types: list, tuple, range
a = [10, 20, 30]
print(a, type(a))  # <class 'list'> -> Ordered, mutable, allows duplicate elements

a = (10, 20, 30)
print(a, type(a))  # <class 'tuple'> -> Ordered, immutable, allows duplicate elements

a = range(1, 10)
print(a, type(a))  # <class 'range'> -> Immutable sequence of numbers commonly used in loops

# Set Types: set, frozenset
a = {10, 20, 30}
print(a, type(a))  # <class 'set'> -> Unordered, mutable, unique elements only (no duplicates)

a = frozenset([10, 20, 30])
print(a, type(a))  # <class 'frozenset'> -> Immutable version of set (hashable)

# Mapping Type: dict
a = {10: "Mehul", 20: "Pranav"}
print(a, type(a))  # <class 'dict'> -> Key-value pairs (Keys must be unique & immutable)


"""
SUMMARY OF PYTHON DATA TYPES:

1) Numeric Types:
   - int: Stores whole integer values (e.g., 10, -5).
   - float: Stores floating-point real numbers (e.g., 10.56, 3.14).
   - complex: Stores numbers with real and imaginary parts (e.g., 10 + 2j).

2) Text Type:
   - str: Stores sequences of characters (e.g., 'Hello').

3) Boolean Type:
   - bool: Stores truth values (True or False).

4) None Type:
   - NoneType: Represents null or empty values (None).

5) Sequence Data Structures:
   - list: Mutable ordered collection [1, 2, 3].
   - tuple: Immutable ordered collection (1, 2, 3).
   - range: Immutable integer sequences for iteration range(0, 10).

6) Set Data Structures:
   - set: Unordered collection of unique items {1, 2, 3}.
   - frozenset: Immutable set frozenset([1, 2, 3]).

7) Mapping Data Structure:
   - dict: Key-value pair mappings {key: value}.

8) Binary Types:
   - bytes: Immutable byte arrays.
   - bytearray: Mutable byte arrays.
   - memoryview: Direct memory access interface.
"""
