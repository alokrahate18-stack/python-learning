Day 10
Topic: Lists

Theory

1. What a list is?

   A list is an ordered, mutable sequence that can hold any mix of types. It doesn't store the objects themselves, only references to them. This explains most of the traps below.

2. Creating lists

        []                       # empty
        [1, "a", 2.5, True]      # mixed types
        list("abc")              # ['a', 'b', 'c']
        list(range(5))           # [0, 1, 2, 3, 4]
        "a b c".split()          # ['a', 'b', 'c']
        [0] * 3                  # [0, 0, 0]

3. Indexing and slicing (you know this from strings)

    n = [10, 20, 30, 40, 50]
    n[0], n[-1]              # 10, 50
    n[1:4]                   # [20, 30, 40]  (stop is exclusive)
    n[::2]                   # [10, 30, 50]  (step)
    n[::-1]                  # reversed copy
    n[10]                    # IndexError
    n[10:20]                 # [] (slices never raise IndexError)

Lists can be changed through slices, which strings can't:


    n[1:3] = [0]             # replaces two items with one: [10, 0, 40, 50]
    del n[0]                 # delete by index

4. Methods that change the list.
   They return None, so never write x = x.sort().

        Methods             	Effect
        append(x)	            add one item to the end
        extend(iterable)    	add each item (append([1,2]) adds one list; extend([1,2]) adds two items)
        insert(i, x)           	insert at position i
        remove(x)	            delete the first match (ValueError if none)
        pop(i=-1)	            delete and return the item
        clear()	                empty the list
        sort(key=, reverse=)	sort in place
        reverse()	            reverse in place

5. Tools that don't change the list:

   len, min, max, sum, sorted(x) (returns a new list), reversed(x) (returns an iterator, not a list), x.count(v), x.index(v), v in x, a + b (new list), a * 3.
   Comparisons like [1, 2] < [1, 3] work element by element.

6. Sorting details

    • Sorting is stable, so equal items keep their original order.

    • key= takes a function that maps each item to what you sort by: sorted(words, key=len) or key=str.lower.

    • Multi-level sort: key=lambda isn't needed if you write your own function that returns a tuple, e.g. def by(p): return (-p[1], p[0]).

    • Sorting mixed types like [1, "a"] raises TypeError.

7. References, aliasing and copying (the most important part)

    a = [1, 2, 3]
    b = a            # NOT a copy: same list, two names
    b.append(4)      # a is now [1, 2, 3, 4]

    c = a[:]         # shallow copies: also a.copy() or list(a)
    a is c           # False (different objects)
    a == c           # True  (equal contents)

A shallow copy copies the outer list only. Inner lists are still shared, so copy.deepcopy is used for nested data. This leads to the classic trap:

    grid = [[0] * 3] * 3      # the SAME inner list 3 times
    grid[0][0] = 7            # changes all three rows
    grid = [[0] * 3 for _ in range(3)]   # correct (comprehension, coming later)
    # or with a loop: create a fresh [0, 0, 0] each iteration and append it

8. Loops and lists

    • Use for item in items: instead of range(len(items)).

    • for i, item in enumerate(items, start=1): gives the position and the value.

    • for a, b in zip(list1, list2): walks two lists together and stops at the shorter one.

    • Never add or remove items from a list while looping over it. The loop's internal position shifts and items get skipped. Loop over a copy (for x in items[:]) or build a new list.

9. Unpacking

    first, *rest = [1, 2, 3, 4]     # 1, [2, 3, 4]
    *head, last = [1, 2, 3, 4]      # [1, 2, 3], 4
    a, b = b, a                     # swap

10.   Lists and functions

    • A function receives a reference to the same list, so items.append(1) inside a function changes the caller's list.

    • items = items + [1] inside a function creates a new list and leaves the caller's list alone.

    • Mutable default argument trap: def f(x, box=[]) creates the list once, when the function is defined, and every call without box shares it. The fix is box=None and then if box is None: box = [].

11.  Strings ↔ lists.

    "a,b,c".split(",") gives a list, and "-".join(["a", "b"]) gives a string. The items must all be strings. list("abc") splits a string into characters.

12.  Speed (rough idea):

    append, pop() and indexing are fast. insert(0, x), pop(0), remove, in and count scan the list, so they get slower as the list grows.

13.   Common errors:

   IndexError (bad position), ValueError (remove or index of a missing item), TypeError (mixed-type sort, or joining non-strings), and None from x = x.sort().

Day 11

Topic: Tuples

Theory

1. What a tuple is. An ordered, immutable sequence. Once created, you cannot change, add, or remove its elements. Lists are for things that change; tuples are for things that shouldn't.

2. Creating tuples

t = (1, 2, 3)
t = 1, 2, 3          # parentheses are optional for multiple items
single = (5,)         # the COMMA makes it a tuple, not the parentheses
not_a_tuple = (5)     # this is just the int 5 in parentheses!
empty = ()
t = tuple([1, 2, 3])  # convert from a list
t = tuple("abc")      # ('a', 'b', 'c')

The single = (5,) trap is the single most common tuple mistake. No comma = no tuple.

3. Indexing, slicing — identical to lists.

t = (10, 20, 30, 40)
t[0], t[-1], t[1:3]   # all work exactly like lists

4. Immutability — the core idea.

t = (1, 2, 3)
t[0] = 99             # TypeError: 'tuple' object does not support item assignment

But — important trap — if a tuple contains a mutable object, that inner object can still change:

t = ([1, 2], "fixed")
t[0].append(3)        # legal! t is now ([1, 2, 3], "fixed")
t[0] = [9, 9]          # illegal — this would replace what's AT position 0

The tuple itself never changes shape, but what's inside a mutable slot can still mutate.

5. Tuple methods — only two, because immutability leaves little to do:

t.count(value)   # how many times value appears
t.index(value)   # position of first match (ValueError if missing)

No .append(), .sort(), .remove() — none of that exists for tuples.

6. Packing and unpacking

point = 3, 4              # packing
x, y = point               # unpacking
a, *middle, b = (1, 2, 3, 4, 5)   # a=1, middle=[2,3,4], b=5 — note middle becomes a LIST
x, y = y, x                 # the classic swap — this works because Python builds a tuple (y, x) first, then unpacks it

7. Why tuples exist (use cases) — this is the "mastery" part most tutorials skip:

Multiple return values: def divide(a, b): return a // b, a % b — this actually returns one tuple, which the caller unpacks.
Dictionary keys / set members: tuples are hashable (if their contents are), lists are not. {(0,0): "origin"} works; {[0,0]: "origin"} crashes. This matters a lot once you learn dicts.
zip() produces tuples: zip([1,2], ["a","b"]) → (1, "a"), (2, "b").
Fixed-shape records: representing a point (x, y) or an RGB color (255, 0, 0) — the fixed size signals "this shouldn't change shape," which is self-documenting code.
Safety: passing a tuple into a function guarantees the function can't accidentally reorder or mutate your data.

8. Hashability detail: a tuple is only hashable if everything inside it is hashable. (1, 2, 3) is hashable; (1, [2, 3]) is not, because it contains a list.

9. Comparison: works lexicographically, same as lists — (1, 2) < (1, 3) is True, compared element by element.

Day 12

Topic: Docstring, Recursions, Sets and Dictionaries

Theory
 docstring are the string literals that appear right after the definition of a function, method, class, or module.

Recursion is the process of defining something in terms
of itself.

A physical world example would be to place two parallel
mirrors facing each other. Any object in between them
would be reflected recursively.
 Recursive Function

In Python, we know that a function can call other
functions. It is even possible for the function to call
itself. These types of construct are termed as recursive
functions.

def factorial(n):
    """This is a Docstring. It comes after the Def function_ name and before function body. It tells about the function. I can also be printed using:
    print(function_name.__doc__)"""
    if n == 0 or n == 1:
        return 1
    else:
        return (n * factorial(n-1))

a = int(input("Enter nay Positive Number: "))
print(factorial(a))
print(factorial.__doc__)

Sets

Sets are unordered collection of data items. They
store multiple items in a single variable. Set items are
separated by commas and enclosed within curly
brackets {}. Sets are unchangeable, meaning you
cannot change items of the set once created. Sets do
not contain duplicate items.

Example:

info = {"Ajay", 19, False, 5.9, 19}
print( info)

Output:

{False, 19, 5.9, 'Ajay'}

Here we see that the items of set occur in random
order and hence they cannot be accessed using index
numbers. Also sets do not allow duplicate values.

Quick Quiz: Try to create an empty set. Check using
the type0 function whether the type of your variable
is a set

1. What a set is. An unordered collection of unique items — duplicates are automatically dropped, and there's no indexing (s[0] doesn't work, because there's no "position"). Sets exist for two jobs: removing duplicates, and fast membership/math operations.

2. Creating sets

s = {1, 2, 3}
s = set([1, 2, 2, 3])     # {1, 2, 3} — duplicates vanish
s = set("hello")           # {'h', 'e', 'l', 'o'} — unique characters
empty = set()               # NOT {} — that creates an empty DICT, a classic trap
3. Sets require hashable items — same rule as dict keys. {[1,2], 3} crashes; {(1,2), 3} works.

4. Adding and removing

s.add(4)              # add one item
s.update([5, 6])       # add several
s.remove(4)            # KeyError if missing
s.discard(4)            # safe version — no error if missing
s.pop()                  # removes and returns an ARBITRARY item (no order!)
s.clear()
5. Set math — this is the real reason sets exist

a = {1, 2, 3}
b = {2, 3, 4}

a | b     # union: {1,2,3,4} — everything in either
a & b     # intersection: {2,3} — in both
a - b     # difference: {1} — in a but not b
a ^ b     # symmetric difference: {1,4} — in exactly one, not both
Mental picture: Venn diagrams. |=combine both circles, &=overlap only, -=left circle minus overlap, ^=everything except overlap.

6. Comparisons

{1,2} <= {1,2,3}    # True — subset
{1,2,3} >= {1,2}    # True — superset
{1,2}.issubset({1,2,3})      # same as <=, more readable
{1,2,3}.issuperset({1,2})
{1,2}.isdisjoint({3,4})       # True — no overlap at all
7. The classic use case — dedupe while keeping order isn't automatic, since sets don't preserve order. A set alone can't do what your Q3 question D wanted. But sets are the fast way to check membership:

seen = set()
unique_in_order = []
for item in items:
    if item not in seen:       # checking "in" on a set is much faster than on a list
        seen.add(item)
        unique_in_order.append(item)
This pattern — set for speed, list for order — is extremely common in real code.

8. Frozenset. An immutable version of a set — frozenset({1,2,3}). Exists because, just like tuples, you sometimes need a "set-like" value that's hashable enough to be a dict key or live inside another set.

9. Set comprehensions (preview, full topic later): {n*n for n in range(5)} → {0,1,4,9,16}.

10. Why in is fast on sets/dicts but slow on lists. A list checks membership by walking through every item one by one — the bigger the list, the slower. Sets and dicts use hashing internally, which lets them jump almost straight to the answer regardless of size. This is the single biggest performance reason to reach for a set over a list when you only care about "is this in here?" and not order or duplicates.

11. Common gotchas: set() vs {} (empty dict trap above), sets print in unpredictable order, s.pop() doesn't let you choose which item comes out.

Dictionaries

1. What a dictionary is. An unordered-by-nature (but insertion-ordered since Python 3.7) collection of key → value pairs. Instead of finding things by position (like lists), you find them by a meaningful name. This is the tool that would have made your word-counter and inventory shell dramatically shorter.

2. Creating dictionaries

d = {}                          # empty dict
d = {"name": "Alok", "age": 20}
d = dict(name="Alok", age=20)   # keyword form
d = dict([("a", 1), ("b", 2)])  # from a list of pairs

3. Keys must be hashable. This connects directly to what you just learned about tuples:

d = {(0, 0): "origin"}   # fine — tuple of ints is hashable
d = {[0, 0]: "origin"}   # TypeError — lists are NOT hashable, can't be keys

Values can be anything — lists, other dicts, functions.

4. Accessing values

d = {"name": "Alok", "age": 20}

d["name"]            # "Alok" — KeyError if "name" doesn't exist
d.get("name")         # "Alok" — returns None if missing, no crash
d.get("city", "N/A")  # "N/A" — custom default if missing
"name" in d           # True — checks KEYS only, not values

d["key"] vs d.get("key") is a real decision: use [] when the key must exist and a missing one is a bug worth crashing on; use .get() when missing is a normal, expected case.

5. Adding and changing

d["city"] = "Nagpur"     # adds if new, overwrites if it exists — same syntax for both
d.update({"age": 21, "job": "dev"})   # merge in multiple pairs at once

6. Removing

del d["city"]            # KeyError if missing
d.pop("age")              # removes AND returns the value; KeyError if missing
d.pop("age", None)        # safe version — returns None instead of crashing
d.popitem()                # removes and returns the LAST inserted pair
d.clear()                   # empty the whole dict

7. Looping — three ways, and this matters

for key in d:              # loops over KEYS only (default behavior)
    print(key)

for key in d.keys():        # same as above, more explicit
    print(key)

for value in d.values():     # loops over VALUES only
    print(value)

for key, value in d.items():  # BOTH at once — this is the one you'll use most
    print(key, value)

8. .keys(), .values(), .items() are "views," not lists. They stay live-linked to the dictionary — if the dict changes, the view reflects it immediately. Wrap in list() if you need an actual, frozen list: list(d.keys()).

9. The trap you already know, applied here: never add or remove keys while looping over the dict directly — RuntimeError: dictionary changed size during iteration. Loop over list(d.keys()) instead if you need to modify while iterating.

10. Dictionary comprehensions (preview — full comprehension topic comes later)

squares = {n: n*n for n in range(5)}   # {0:0, 1:1, 2:4, 3:9, 4:16}

11. Nesting — dicts inside dicts, the realistic shape of real-world data (think JSON, which you'll meet in web dev):

students = {
    "Asha": {"age": 20, "marks": [82, 90]},
    "Rohit": {"age": 21, "marks": [55, 60]}
}
students["Asha"]["marks"].append(95)   # reach in, step by step

12. Merging dicts (Python 3.9+)

merged = dict_a | dict_b         # new dict; dict_b's values win on key clashes
dict_a |= dict_b                  # merge into dict_a in place

13. Default values without crashing — setdefault

d.setdefault("tags", []).append("python")
# if "tags" doesn't exist yet, creates it as [] first, THEN appends.
# Saves writing: if "tags" not in d: d["tags"] = []

14. Counting pattern — this directly replaces your word-counter code:

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

One line, same job as your two parallel lists plus .index(). This is why dictionaries exist — "find by name" problems collapse from many lines to one.

15. Equality and copying — same shallow-copy trap as lists:

a = {"x": [1, 2]}
b = a.copy()          # shallow copy
b["x"].append(3)       # a["x"] is ALSO changed — inner list is shared!
import copy
b = copy.deepcopy(a)   # fully independent

16. Dict vs list — when to use which. List: order matters, you access by position, or duplicates are meaningful. Dict: you look things up by a meaningful name/ID, and each key should be unique.

17. Common errors: KeyError (missing key with [] or del), TypeError: unhashable type: 'list' (using a list as a key).
