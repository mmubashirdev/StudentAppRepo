# StudentApp

A simple Python project that calculates a student’s grade based on marks and includes full unit testing plus custom exception handling.

---

## 📁 Project Structure

```

StudentApp/
│
├── grades.py
├── marks_calculator.py
├── test_grades.py
└── hello.py

````

---

## 🧩 Features

### ✅ `grades.py`
- Contains the `calculate_grade()` function  
- Validates input type (must be number)  
- Raises custom exceptions:
  - `NegativeValue` → marks < 0  
  - `OutOfRange` → marks > 100  
- Returns grade based on range:
  - 90–100 → **A**
  - 80–89 → **B**
  - 70–79 → **C**
  - 60–69 → **D**
  - Below 60 → **F**

---

### 🚨 Custom Exceptions

```py
class NegativeValue(Exception):
    pass

class OutOfRange(Exception):
    pass
````

---

## 🧪 Unit Testing (`test_grades.py`)

The project uses Python’s built-in `unittest` module.

Tests include:

* All grade ranges (A–F)
* Edge cases (0, 59, 60, 100)
* Exception tests:

  * Negative values
  * Out-of-range values
  * Invalid type (string input)

Run the tests using:

```sh
python -m unittest test_grades.py
```

---

## ▶️ Running the App

To manually calculate a grade:

```sh
python grades.py
```

Example:

```
Enter your marks: 80
B grade
```

---

## 🛠️ marks_calculator.py

A separate script demonstrating:

* Custom exceptions (`NegativeMarkError`, `AboveRangeError`)
* Error messages for strings, negative input, and values >100
* `finally:` block for cleanup message

---

## 🌱 Requirements

No external libraries needed.

You only need Python 3 installed.

---

## 📌 Version Control (Git)

Sample commands used:

```sh
git add .
git commit -m "files uploaded"
git push
```

---

## 👨‍💻 Author

**Muhammad Mubashir**
Software Engineering Student
