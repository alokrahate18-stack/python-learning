# 05_functions

Welcome to the **05_functions** module! This section covers reusable code blocks in Python—including function definitions, parameters, return values, docstrings, placeholder code using `pass`, modular program design, and recursion.

---

## 📖 Module Overview & Theory Summary

### 1. Function Basics & Execution Flow

* **Defining Functions (`def`)**: Functions are declared using the `def` keyword followed by the function name and parentheses.


* **Execution**: Defining a function merely creates the object; code inside executes only when called.


* **`pass` Statement**: Serves as a temporary placeholder inside empty function bodies to prevent syntax errors during development.



### 2. Parameters, Arguments & Return Values

* **Parameters vs. Arguments**: Parameters are variables defined in the function signature, while arguments are the concrete values passed during a call.


* **`print()` vs. `return**`: `print()` outputs data to the console but evaluates to `None`, whereas `return` passes a calculated value back to the caller for further processing or variable storage.


* **Early Exits**: Executing a `return` statement immediately terminates function execution.



### 3. Documentation (`__doc__`) & Docstrings

* **Docstrings**: String literals placed directly beneath a function definition to describe its behavior.


* **Inspection**: Accessible via the `.__doc__` attribute or Python's built-in `help()` function.



### 4. Recursion

* **Recursive Functions**: Functions that call themselves to solve smaller instances of a problem.


* **Essential Components**: Must include a **base case** to stop recursion and prevent `RecursionError` stack overflows, and a **recursive case** that advances toward the base case.



---

## 📂 File Index & Summaries

| File | Description | Key Concepts Learned |
| --- | --- | --- |
| **`001_functions_01.py`** | Conditional comparison and placeholder syntax.

 | Function definitions (`def`), argument passing, using `pass` for empty function stubs.

 |
| **`002_functions_02.py`** | Modular salary calculation pipeline.

 | Breaking complex logic into modular functions, returning values, passing intermediate results.

 |
| **`003_functions_03.py`** | Multi-branch loan approval logic.

 | Function-level conditional validation, returning status strings, early exits via `return`.

 |
| **`004_recursion_and_docstring_01.py`** | Recursive factorial calculator with documentation.

 | Recursive function calls, base cases, defining and inspecting docstrings (`__doc__`).

 |
| **`005_recursion_02.py`** | Iterative Fibonacci series generator.

 | Iterative sequence calculation within functions, state updates, sequence generation.

 |

---

## 🛠 Usage & Execution

To run any script in this folder, execute the following command in your terminal:

```bash
python <filename>.py

```

*Example:*

```bash
python 004_recursion_and_docstring_01.py

```
