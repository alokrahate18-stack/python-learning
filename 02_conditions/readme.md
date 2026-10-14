# 02_conditions

Welcome to the **02_conditions** module! This section focuses on control flow and decision-making structures in Python—including conditional branching with `if`, `elif`, and `else` statements, logical conditions, boolean evaluation, and nested condition structures.

---

## 📖 Module Overview & Theory Summary

### 1. Conditional Logic (`if`, `elif`, `else`)

* **`if` Statement**: Evaluates a boolean expression; executes the code block only if the condition evaluates to `True`.


* **`elif` Statement**: Short for "else if". Allows testing multiple mutually exclusive conditions sequentially.


* **`else` Statement**: Acts as the catch-all fallback block when all preceding conditions evaluate to `False`.



### 2. Execution Order & Mutually Exclusive Conditions

* Python evaluates conditions sequentially from top to bottom.


* As soon as a condition evaluates to `True`, Python executes its associated code block and skips all remaining `elif` and `else` blocks in that chain.


* Order matters: place more specific or restrictive conditions before broader ones to avoid logic errors.



### 3. Nested Conditions & Complex Logic

* **Nested Branching**: An `if` statement placed inside another `if` block allows multi-step validation.


* **Combining Conditions**: Logical operators (`and`, `or`, `not`) can combine multiple checks into a single clean condition instead of using deep nesting.


* **Comparison Chaining**: Expressions like `18 <= age <= 60` are supported directly in Python as an equivalent to `age >= 18 and age <= 60`.



---

## 📂 File Index & Summaries

| File | Description | Key Concepts Learned |
| --- | --- | --- |
| **`014_challenge_05.py`** | Multi-factor entrance authorization checker.

 | Logical `and` operator combining age, ID, and permission checks.

 |
| **`022_if_elif_else.py`** | Banking transaction and withdrawal limit validator.

 | `if-elif-else` branching, string normalization (`.strip().lower()`), account balance checks.

 |
| **`023_if_elif_else_02.py`** | Multi-tiered loan eligibility assessment.

 | Nested conditional checks evaluating age, income, credit score, and existing debt status.

 |

---

## 🛠 Usage & Execution

To run any script in this folder, execute the following command in your terminal:

```bash
python <filename>.py

```

*Example:*

```bash
python 022_if_elif_else.py

```
