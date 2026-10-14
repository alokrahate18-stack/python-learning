# 03_pattern_matching

Welcome to the **03_pattern_matching** module! This section covers Python's structural pattern matching introduced in Python 3.10—using `match` and `case` statements for clean, readable branching, sequence destructuring, variable binding, wildcard patterns, and list unpacking.

---

## 📖 Module Overview & Theory Summary

### 1. Structural Pattern Matching (`match`...`case`)

* **Beyond `if-elif-else**`: While `match-case` replaces long chains of `if-elif-else` statements, its true power lies in evaluating structural patterns in data (such as tuples, lists, and primitives).


* **Top-to-Bottom Evaluation**: Python checks patterns sequentially from top to bottom and executes only the **first** matching case block.


* **Wildcard Operator (`_`)**: The underscore `_` acts as the default catch-all pattern (similar to `else` in conditional statements).



### 2. Destructuring & Unpacking Patterns

* **Tuple & Sequence Matching**: Extract values directly into variables within the pattern (e.g., matching coordinates `(0, y)` vs `(x, 0)` vs `(x, y)`).


* **Rest Patterns (`*rest`)**: Collect remaining elements of a sequence into a list using `*rest` or `*remaining` during matching.


* **Pattern Specificity**: Always structure `case` statements from most specific patterns down to general patterns.



---

## 📂 File Index & Summaries

| File | Description | Key Concepts Learned |
| --- | --- | --- |
| **`001_match_case_01.py`** | Basic game option menu selection.

 | `match-case` syntax, scalar matching, wildcard fallback operator (`_`).

 |
| **`002_match_case_02.py`** | Coordinate plane check and sequence unpacking.

 | Tuple destructuring, variable binding in patterns, list unpacking with `*rest`.

 |

---

## 🛠 Usage & Execution

To run any script in this folder, execute the following command in your terminal:

```bash
python <filename>.py

```

*Example:*

```bash
python 002_match_case_02.py

```
