# 07_strings

Welcome to the **07_strings** module! This section covers character sequence processing in Python—including string indexing, positive and negative slicing, string immutability, iteration, formatting, and essential string transformation methods.

---

## 📖 Module Overview & Theory Summary

### 1. String Fundamentals & Immutability

* **Immutable Sequences**: Strings are ordered collections of characters. Once created, individual characters inside a string cannot be modified, replaced, or assigned in place. Any transformation method produces a brand-new string object rather than altering the original.


* **Creation & Escape Characters**: Strings can be declared using single, double, or triple quotes (for multi-line strings). Common escape sequences include `\n` for newlines and `\t` for horizontal tabs.



### 2. Indexing & Slicing Mechanics

* **Indexing**: Access individual characters via zero-based positive indexing (`string[0]`) or negative indexing from the end (`string[-1]`).


* **Slicing**: Extract substrings using `string[start:stop:step]`. The `stop` boundary is always exclusive. Negative index expressions evaluate internally as `len(string) - index`.



### 3. Built-In String Methods

* **Case Conversion**: `upper()`, `lower()`, `capitalize()`, `title()`, and `swapcase()` adjust letter casing across strings.


* **Trimming & Replacement**: `lstrip()` and `rstrip()` trim leading and trailing characters, while `replace(old, new)` substitutes target substrings.


* **Searching & Inspection**: `find()` returns index positions (or `-1` if missing), while methods like `startswith()`, `endswith()`, `isalpha()`, `isalnum()`, and `isnumeric()` evaluate character types and return boolean results.


* **Splitting**: `split(separator)` breaks strings apart into lists based on specified delimiters.



---

## 📂 File Index & Summaries

| File | Description | Key Concepts Learned |
| --- | --- | --- |
| **`019_strings.py`** | Basic string indexing and character iteration.

 | Index positioning (`string[i]`), iterating through characters using a `for` loop.

 |
| **`020_strings_02.py`** | String length calculation and slicing techniques.

 | Measuring length with `len()`, positive/negative index slicing, internal index offset math.

 |
| **`021_strings_03.py`** | Showcase of built-in string methods.

 | Case transformations, character stripping (`rstrip`, `lstrip`), splitting, formatted centering, string checks (`isalnum`, `isalpha`, `isspace`).

 |

---

## 🛠 Usage & Execution

To run any script in this folder, execute the following command in your terminal:

```bash
python <filename>.py

```

*Example:*

```bash
python 021_strings_03.py

```
