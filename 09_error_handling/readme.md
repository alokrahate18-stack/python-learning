# 09_error_handling

Welcome to the **09_error_handling** module! This section covers exception handling in Python—including handling runtime errors, handling specific error types, user-friendly error recovery, and using the `finally` block to ensure execution regardless of exceptions or return statements.

---

## 📖 Module Overview & Theory Summary

### 1. Exceptions & Program Stability

* **Runtime Exceptions**: Errors occurring during program execution (such as `ValueError` or `IndexError`) halt code execution and crash the application if left unhandled.


* **`try...except` Blocks**: Intercept and resolve exceptions gracefully, preventing system crashes and ensuring smooth program continuation.



### 2. Specific vs. Catch-All Exception Handling

* **Specific Exceptions**: Catching precise errors like `except ValueError:` or `except IndexError:` allows custom recovery steps tailored to each error condition.


* **Generic / Catch-All**: Using `except Exception as e:` or a bare `except:` handles any unexpected error, preventing crashes but potentially hiding bugs if overused.



### 3. The `finally` Clause

* **Guaranteed Execution**: The `finally` block executes under all circumstances—whether the `try` block succeeds, encounters an exception, or hits an early `return` statement.


* **Resource Cleanup**: Useful for releasing system resources (such as closing file streams, ending database connections, or printing final status messages).



---

## 📂 File Index & Summaries

| File | Description | Key Concepts Learned |
| --- | --- | --- |
| **`013_exception_handling_01.py`** | Multiplication table generator with error reporting.

 | `try...except Exception as e` handling, printing standard exception objects.

 |
| **`014_exception_handling_02.py`** | Multiplication generator with user-friendly error messaging.

 | Bare `try...except` structure for graceful user error reporting.

 |
| **`015_exception_handling_03.py`** | Multi-branch specific exception handler.

 | Catching distinct error types (`ValueError`, `IndexError`) independently.

 |
| **`016_exception_handling_04.py`** | Index lookup with guaranteed `finally` execution.

 | Function error handling, return value propagation, guaranteed execution via `finally`.

 |

---

## 🛠 Usage & Execution

To run any script in this folder, execute the following command in your terminal:

```bash
python <filename>.py

```

*Example:*

```bash
python 016_exception_handling_04.py

```
