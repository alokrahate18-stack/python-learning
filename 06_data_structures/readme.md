# 06_data_structures

Welcome to the **06_data_structures** module! This section covers Python's core collection types—including mutable lists, immutable tuples, indexing, slicing, list comprehensions, parallel data processing, custom algorithmic analysis, and complex CLI application design.

---

## 📖 Module Overview & Theory Summary

### 1. Lists (`list`) & Slicing Dynamics

* **Ordered & Mutable Sequences**: Lists hold heterogeneous data types whose items can be modified, appended, or removed in place.


* **Indexing**: Supports positive 0-based indexing and negative indexing starting from `-1`.


* **Slicing**: Structured as `list[start:stop:step]`. Slicing returns a new list and handles out-of-bounds bounds without raising an `IndexError`.



### 2. Reference Semantics, Shallow vs. Deep Copying

* **Aliasing Trap**: Direct variable assignment (`b = a`) creates a reference to the same memory object rather than cloning it.


* **Shallow Copy (`copy()`)**: Copies outer list structures; nested collections inside still share memory references.


* **Deep Copy (`deepcopy()`)**: Clones the outer collection and all nested objects recursively.



### 3. List Comprehensions & Advanced Operations

* **Comprehension Pattern**: Offers concise syntax to construct lists: `[expression for item in iterable if condition]`.


* **Iteration Utilities**: Uses `enumerate()` for simultaneous index-value tracking and `zip()` for parallel multi-list iteration.



### 4. Tuples (`tuple`) & Hashability

* **Immutable Collections**: Defined using commas (e.g., `(5,)`). Once instantiated, elements cannot be replaced, added, or removed.


* **Fixed Data Structure**: Useful for returning multiple function values, representing coordinates, and serving as set elements or dictionary keys when fully hashable.



---

## 📂 File Index & Summaries

| File | Description | Key Concepts Learned |
| --- | --- | --- |
| **`001_list_01.py`** | List instantiation and index slicing.

 | Positive/negative indexing, step jumping, sequence reversal via `[::-1]`.

 |
| **`002_list_02.py`** | Building lists via comprehensions.

 | Functional sequence filtering, transformation expressions, conditional ternaries inside comprehensions.

 |
| **`003_list_03.py`** | Core list mutation methods.

 | `append()`, `sort()`, `reverse()`, `insert()`, `extend()`, reference aliasing vs `.copy()`.

 |
| **`004_list_04.py`** | Advanced collection operations.

 | `min()`, `max()`, `sum()`, variable unpacking with `*`, `enumerate()`, `zip()`, shallow vs `deepcopy()`.

 |
| **`005_list_05.py`** | Manual list analysis without built-in functions.

 | Calculating highest, lowest, and average values manually using comparison loops.

 |
| **`006_list_06.py`** | Dictionary-free word frequency counter.

 | Parallel list tracking (`unique_words` and `counts`), string splitting, first-appearance retention.

 |
| **`007_list_07.py`** | Case-insensitive cart merging function.

 | Alternating list flattening, case-folding string comparison, preserving original input structures.

 |
| **`008_list_08.py`** | Interactive inventory shell CLI with undo system.

 | Pattern matching (`match-case`), `*rest` patterns, multi-level state history tracking, non-destructive sorting.

 |
| **`010_list_10.py`** | Identifying and fixing common Python list pitfalls.

 | Resolving mutable default argument traps, row replication bugs, and loop-mutation skips.

 |
| **`011_tuples_01.py`** | Tuple creation and single-element traps.

 | Trailing comma syntax `(5,)`, sequence conversions, implicit parenthesizing.

 |
| **`012_tuples_02.py`** | Tuple immutability and inner object mutability.

 | Immutable container constraints, tuple methods (`count()`, `index()`), modifying inner mutable lists.

 |

---

## 🛠 Usage & Execution

To run any script in this folder, execute the following command in your terminal:

```bash
python <filename>.py

```

*Example:*

```bash
python 008_list_08.py

```
