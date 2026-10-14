# 10_modules_and_packages

Welcome to the **10_modules_and_packages** module! This section covers importing code from Python's standard library modules—including manipulating dates and formatted timestamps using `time` and `datetime`, parsing log streams, sorting entries chronologically, calculating time intervals, and converting string data into datetime objects using `strptime()` and `strftime()`.

---

## 📖 Module Overview & Theory Summary

### 1. Modules & The Import System

* **Module Basics**: A module is a Python file containing reusable functions, classes, and variables. Importing code prevents duplication and organizes project structure.


* **Import Variants**: Code can be imported using `import module_name` or `from module_name import target`.



### 2. Time Manipulation (`time` & `datetime`)

* **Formatting Strings (`strftime()`)**: Converts `time` or `datetime` objects into formatted text strings using directives like `%Y` (year), `%m` (month), `%d` (day), `%H` (hour), `%M` (minute), and `%S` (second).


* **Parsing Strings (`strptime()`)**: Parses raw text representations into standard `datetime` objects for structured operations and comparisons.


* **Rule of Thumb**:
* `strptime()` = **Read** (String $\rightarrow$ Time Object)


* `strftime()` = **Write** (Time Object $\rightarrow$ String)





### 3. Chronological Analysis & Timestamp Math

* **Sorting Datetimes**: `datetime` objects support direct comparisons (`<`, `>`) and sorting via `list.sort()` or `sorted()`, making it straightforward to arrange log lines chronologically.


* **Time Deltas & Gaps**: Subtracting two `datetime` objects returns a `timedelta` object whose total seconds can be converted into human-readable formatted gaps (`Xh Ym Zs`) using integer floor division (`//`) and modulo operations (`%`).



---

## 📂 File Index & Summaries

| File | Description | Key Concepts Learned |
| --- | --- | --- |
| **`009_list_09.py`** | Advanced log file parser and chronological gap analyzer.

 | Importing `from datetime import datetime`, manual time text validation (`HH:MM:SS`), `strptime()` parsing, chronological sorting, `timedelta` second calculations, and formatted table rendering using f-string specifiers (`:<8`, `:>12`).

 |
| **`019_python_library_time.py`** | Guide to time directives and formatting methods.

 | Standard imports (`import time`, `from datetime import datetime`), comprehensive `strftime()` formatting directives (`%Y`, `%m`, `%d`, `%H`, `%M`, `%S`, `%f`, `%A`, `%B`, `%z`, `%Z`, `%G`, `%V`), and parsing strings using `strptime()`.

 |

---

## 🛠 Usage & Execution

To run any script in this folder, execute the following command in your terminal:

```bash
python <filename>.py

```

*Example:*

```bash
python 019_python_library_time.py

```
