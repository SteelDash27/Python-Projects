# 🐍 Python Practice Projects

> A growing collection of Python exercises — general practice projects alongside Python re-implementations of problems I've solved in my [C++ course](https://github.com/SteelDash27/Educative-Learn-CPP-Course-For-Beginners).

---

## About

This repository serves two purposes:

**General Python Practice** — standalone projects and exercises that reinforce Python fundamentals, standard library usage, and Pythonic patterns.

**C++ → Python Parallels** — problems originally solved in C++ (from the Educative course *"Learn C++: The Complete Course for Beginners"*) re-implemented in Python to compare language paradigms, syntax, and idioms side by side.

---

## Repository Structure

```
learn-python/
├── general/
│   ├── 01-basics/
│   ├── 02-data-structures/
│   ├── 03-file-io/
│   ├── 04-oop/
│   └── ...
│
└── cpp-parallels/
    ├── 01-introduction/
    ├── 02-variables/
    ├── 03-data-types/
    ├── 04-operators/
    ├── 05-conditional-statements/
    ├── 06-loops/
    ├── 07-functions/
    ├── 08-recursion/
    ├── 09-lists/          # Python equivalent of C++ arrays
    ├── 10-references/     # Python equivalent of C++ pointers
    ├── 11-dynamic-memory/ # Python handles this automatically
    ├── 12-data-classes/   # Python equivalent of C++ structures
    └── 13-projects/
```

---

## C++ Parallels Progress

These mirror the problems solved in the C++ course. Each folder contains the Python solution alongside a short note on how the approach differs from C++.

| # | Topic | Problems | C++ Status | Python Status |
|---|-------|----------|------------|---------------|
| 01 | Introduction | Display Text, Right-Angle Triangle | ✅ Complete | ⬜ Not Started |
| 02 | Variables | Initialize & Overwrite, Swap Values | ✅ Complete | ⬜ Not Started |
| 03 | Data Types | Convert Double to Integer | ✅ Complete | ⬜ Not Started |
| 04 | Operators | Previous Alphabet, Hours/Minutes/Seconds, Area of Sphere | ✅ Complete | ⬜ Not Started |
| 05 | Conditional Statements | Highest Salary, Check Alphabet, Day of the Week | ✅ Complete | ⬜ Not Started |
| 06 | Loops | Power of Number, Prime Number, Decimal to Binary, Palindrome | ✅ Complete | ⬜ Not Started |
| 07 | Functions | Digits to Text, Smallest Number, Calculator | ✅ Complete | ⬜ Not Started |
| 08 | Recursion | Power Recursively, Count Digits, Fibonacci Number | 🔄 In Progress | ⬜ Not Started |
| 09 | Lists / Arrays | Average Marks, Left Rotate, Sort Descending, Diagonal Sum, Matrix Multiply | ⬜ Not Started | ⬜ Not Started |
| 10 | References / Pointers | Area of Rectangle, Sum & Absolute Difference | ⬜ Not Started | ⬜ Not Started |
| 11 | Memory Management | Odd Elements to -1, Delete at Index | ⬜ Not Started | ⬜ Not Started |
| 12 | Data Classes / Structures | Subtract Complex Numbers, Student Percentage, Customer Balance | ⬜ Not Started | ⬜ Not Started |
| 13 | Projects | Mini Project 1, Mini Project 2 | ⬜ Not Started | ⬜ Not Started |

**Legend:** ✅ Complete · 🔄 In Progress · ⬜ Not Started

---

## General Python Projects Progress

| # | Topic | Projects | Status |
|---|-------|----------|--------|
| 01 | Basics | | ⬜ Not Started |
| 02 | Data Structures | | ⬜ Not Started |
| 03 | File I/O | | ⬜ Not Started |
| 04 | OOP | | ⬜ Not Started |

---

## C++ vs Python: Key Differences

A running reference of paradigm differences encountered across problems.

| Concept | C++ | Python |
|---------|-----|--------|
| Variable declaration | Explicit type required (`int x = 5;`) | Dynamic typing (`x = 5`) |
| Pointers | Manual pointer arithmetic | No direct equivalent; use references/objects |
| Memory management | Manual (`new` / `delete`) | Automatic (garbage collected) |
| Arrays | Fixed-size, contiguous (`int arr[5]`) | Lists are dynamic and flexible |
| Structs | `struct` keyword, value type | `dataclass` or `class` |
| Pass by reference | `&` operator | All mutable objects passed by reference |

---

## How to Run

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/learn-python.git
cd learn-python

# Run any solution directly
python cpp-parallels/06-loops/palindrome.py

# Or from the general section
python general/02-data-structures/stack.py
```

No external dependencies are required unless noted within a specific project folder.

---

## Related Repository

🔗 **[learn-cpp-educative]([https://github.com/YOUR_USERNAME/learn-cpp-educative](https://github.com/SteelDash27/Educative-Learn-CPP-Course-For-Beginners))** — C++ solutions for every coding challenge in the Educative course *"Learn C++: The Complete Course for Beginners"*.

---

## Author

**Laone Makeketa** — learning Python through structured practice, using C++ as a reference point for understanding language design decisions.
