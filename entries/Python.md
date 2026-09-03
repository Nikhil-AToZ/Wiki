# Python
---
## Introduction

Python is a high-level, general-purpose programming language known for its simple syntax and readability. It is widely used in web development, automation, data analysis, data science, artificial intelligence, machine learning, and scientific computing.

Python allows developers to write programs using relatively simple and readable code, making it popular among both beginners and experienced developers.



## History

Python was created by Guido van Rossum and was first released in 1991. The language was designed with an emphasis on readability and simplicity.

Python has had two major versions:

- Python 2
- Python 3

Python 2 was officially discontinued in 2020, so modern Python development uses Python 3.

## Features of Python

### Simple and Readable Syntax

Python uses a relatively simple syntax that makes programs easier to read and understand.

```python
name = "Nikhil"

if name:
    print("Hello", name)
```

### Dynamically Typed

Python does not require variables to be explicitly declared with a data type.

```python
x = 10
x = "Hello"
```

The type of the value is determined at runtime.

### Object-Oriented

Python supports object-oriented programming using classes and objects.

```python
class Student:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)


student = Student("Nikhil")
student.introduce()
```

### Cross-Platform

Python can run on operating systems such as:

- Windows
- Linux
- macOS

## Basic Data Types

Python provides several built-in data types.

### Integer

Used for whole numbers.

```python
age = 18
```

### Float

Used for decimal numbers.

```python
price = 99.99
```

### String

Used to store text.

```python
name = "Nikhil"
```

### Boolean

Represents either `True` or `False`.

```python
is_student = True
```

### List

A list is an ordered and mutable collection.

```python
numbers = [1, 2, 3, 4, 5]
```

### Tuple

A tuple is an ordered collection that is generally immutable.

```python
coordinates = (10, 20)
```

### Set

A set contains unique values.

```python
numbers = {1, 2, 3, 4}
```

### Dictionary

A dictionary stores data as key-value pairs.

```python
student = {
    "name": "Nikhil",
    "age": 18
}
```

## Conditional Statements

Python uses `if`, `elif`, and `else` to make decisions.

```python
marks = 85

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
else:
    print("C")
```

## Loops

Loops are used to execute code repeatedly.

### For Loop

```python
for number in range(5):
    print(number)
```

### While Loop

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

Python also provides `break` and `continue` for controlling loops.

## Functions

Functions are reusable blocks of code.

```python
def add(a, b):
    return a + b


result = add(10, 20)
print(result)
```

Functions help divide programs into smaller and reusable parts.

## Modules and Packages

Python allows code to be organized into modules and packages.

For example:

```python
import math

print(math.sqrt(25))
```

Python also has a large ecosystem of external packages that can be installed using `pip`.

```bash
pip install requests
```

## Exception Handling

Python provides exception handling using `try` and `except`.

```python
try:
    number = int(input("Enter a number: "))
    print(10 / number)

except ValueError:
    print("Invalid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

Exception handling allows programs to deal with unexpected situations without immediately crashing.

## File Handling

Python can read and write files.

```python
with open("data.txt", "r") as file:
    content = file.read()

print(content)
```

The `with` statement automatically handles closing the file.

## Applications of Python

Python is used in many different areas.

- Web development
- Data science
- Machine learning
- Artificial intelligence
- Automation
- Scientific computing
- Data analysis
- Scripting
- Software development

Popular Python technologies include:

- Django
- Flask
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- PyTorch

## Advantages

- Easy-to-read syntax
- Large ecosystem of libraries
- Large developer community
- Cross-platform
- Useful in many different fields
- Good language for learning programming

## Limitations

- Generally slower than languages such as C or C++
- Can use more memory for some tasks
- Dynamic typing can allow some errors to appear at runtime
- Not usually the first choice for native mobile application development

## Python in Data Science

Python is especially important in data science because of its large collection of data-related libraries.

For example:

```python
import pandas as pd
import numpy as np
```

Pandas can be used for data manipulation, NumPy for numerical computing, and libraries such as Matplotlib and Scikit-learn can be used for visualization and machine learning.

## Conclusion

Python is a versatile programming language that can be used for everything from simple scripts to large applications.

Its readable syntax and extensive ecosystem make it particularly useful for learning programming, web development, automation, data science, and machine learning.
