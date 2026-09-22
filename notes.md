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

    uxz • key= takes a function that maps each item to what you sort by: sorted(words, key=len) or key=str.lower.

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

10.  Lists and functions

    • A function receives a reference to the same list, so items.append(1) inside a function changes the caller's list.

    • items = items + [1] inside a function creates a new list and leaves the caller's list alone.

    • Mutable default argument trap: def f(x, box=[]) creates the list once, when the function is defined, and every call without box shares it. The fix is box=None and then if box is None: box = [].

11. Strings ↔ lists.

    "a,b,c".split(",") gives a list, and "-".join(["a", "b"]) gives a string. The items must all be strings. list("abc") splits a string into characters.

12. Speed (rough idea):

    append, pop() and indexing are fast. insert(0, x), pop(0), remove, in and count scan the list, so they get slower as the list grows.

13.  Common errors:

   IndexError (bad position), ValueError (remove or index of a missing item), TypeError (mixed-type sort, or joining non-strings), and None from x = x.sort().
