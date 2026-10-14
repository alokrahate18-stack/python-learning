# 01_basics

Welcome to the **01_basics** module! This section covers foundational Python programming concepts—including variable assignment, data types, type casting, basic input/output operations, operators, memory references, and fundamental computational logic.

---

## 📖 Module Overview & Theory Summary

### 1. Program Execution & Basic I/O

* **Python Interpreter**: Python executes `.py` files line-by-line via the interpreter.


* **`print()` Function**: Output values to the terminal. Supports parameters like `sep` (separator) and `end` (line ending).


* **`input()` Function**: Receives input from standard input as a `str` type.



### 2. Variables & Dynamic Typing

* **Assignment (`=`)**: Binds a variable name to a value in memory.


* **Dynamic Typing**: Variable names do not have fixed types; they reference objects whose types can change.


* **Naming Rules**: Must begin with a letter or underscore (`_`), case-sensitive, and cannot override reserved keywords or built-ins (e.g., `list`, `type`, `id`).



### 3. Basic Data Types

* **`int`**: Whole numbers.


* **`float`**: Floating-point decimal numbers.


* **`str`**: Text strings wrapped in quotes.


* **`bool`**: Truth values (`True` / `False`). Note: Capitalization is strictly required.



### 4. Type Conversion & Casting

* Convert data between types explicitly using `int()`, `float()`, `str()`, and `bool()` constructors.


* String input from `input()` must be converted before performing mathematical operations.



### 5. Operators & Truthiness

* **Arithmetic**: `+`, `-`, `*`, `/` (float division), `//` (floor division), `%` (modulo), `**` (power).


* **Comparison**: `==`, `!=`, `>`, `<`, `>=`, `<=`.


* **Assignment**: `=`, `+=`, `-=`, `*=`, `/=`, etc.


* **Logical**: `and`, `or`, `not`.


* **Membership**: `in`, `not in`.


* **Identity (`is` vs `==`)**: `==` checks value equality; `is` checks memory address / identity equality. Python caches small integers (typically -5 to 256) and interns short strings.



---

## 📂 File Index & Summaries

| File | Description | Key Concepts Learned |
| --- | --- | --- |
| **`001_hello.py`** | Basic "Hello World" program.

 | `print()`, basic execution.

 |
| **`002_variables.py`** | Variable initialization and printing.

 | Variable assignment, memory references.

 |
| **`003_input.py`** | Reading user input.

 | `input()`, string concatenation.

 |
| **`004_calculator.py`** | Basic numeric calculator.

 | Type conversion (`int()`), basic arithmetic operators.

 |
| **`005_student_info.py`** | Formatting user profile output.

 | Multi-type input, output formatting (`\n`).

 |
| **`006_challenge_01.py`** | Interactive user profile script.

 | Standard input, multi-variable display.

 |
| **`007_data_types.py`** | Variable reassignment across primitives & collections.

 | Dynamic typing, checking data types using `type()`.

 |
| **`008_data_types_int.py`** | Demonstrating numbers and string concatenation.

 | Primitive data types (`int`, `float`, `str`), type inspection.

 |
| **`009_data_types_boolean.py`** | Boolean evaluation and syntax rules.

 | `bool` data type, strict capitalization requirements (`NameError`).

 |
| **`010_type_conversion.py`** | Mental model of the input-processing pipeline.

 | `input()` returning string, explicit type casting (`int()`).

 |
| **`011_challenge_02.py`** | Comprehensive user profile calculator.

 | Unit conversion (feet to cm), boolean conversion (`.strip().lower()`).

 |
| **`012_challenge_03.py`** | Product billing and discount calculator.

 | Percentage logic, conditional statements, formatted floats.

 |
| **`013_challenge_04.py`** | Net salary calculation breakdown.

 | Payroll arithmetic, deductions, gross vs net calculations.

 |
| **`015_operators.py`** | Complete showcase of Python operators.

 | Arithmetic, comparison, logical, bitwise, identity, walrus operator (`:=`).

 |
| **`016_challenge_06.py`** | Cross-type equality comparisons.

 | Difference between value comparison (`==`) and type equality.

 |
| **`017_id_and_is.py`** | Memory management and object identity.

 | `id()`, `is` operator, small integer caching, interning, copy vs deepcopy.

 |
| **`018_challenge_07.py`** | Multi-item invoice generation.

 | Tax calculation (18% GST), subtotaling, string formatting.

 |

---

## 🛠 Usage & Execution

To run any script in this folder, execute the following command in your terminal:

```bash
python <filename>.py

```

*Example:*

```bash
python 004_calculator.py

```
