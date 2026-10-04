# Indexing, Slicing — Identical to lists

t = (10, 20, 30, 20, 40)

print(t[0])
print(t[-1])
print(t[1:3]) # all work exactly like lists

# t[0] = 99 Tuples are Immutable.

# But — important trap — if a tuple contains a mutable object, that inner object can still change:
t1 = ([1, 2], "fixed")
t1[0].append(3)        # legal! t is now ([1, 2, 3], "fixed")
# t[0] = [9, 9]          # illegal — this would replace what's AT position 0
print(t)

# Tuples Methods
t.count(20)   # how many times value appears
t.index(30)   # position of first match (ValueError if missing)
# No .append(), .sort(), .remove() — none of that exists for tuples.
