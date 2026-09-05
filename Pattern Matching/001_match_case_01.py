"""It is just like if - elif - else conditioning. But, it looks way cleaner.
Also, match-case can do more than simply compare numbers and strings.
Just like matching a Pattern.

First master if-elif-else, then learn match-case. After that, pattern matching with tuples, lists, and dictionaries becomes much easier.




The underscore(_) means:
"Anything else"
"""
choice = 3

match choice:
    case 1:
        print("Starting Game....")
    case 2:
        print("Loading Game...")
    case 3:
        print("Opening Settings...")
    case 4:
        print("Exiting Game...")
