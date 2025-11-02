"""
This file will capture code snippets and instructions
related to creating, accessing, importing, and managing Python packages and modules.
"""
# assign the name of this module to a variable e.g. corepython.py
module_name = __file__
parts = module_name.split("\\")
print(f"Module - single python file, {parts[-1]}")
print(f"Package - a folder containing multiple python files (modules) and an __init__.py file")
print("Function - a block of reusable code that performs a specific task")
print("Class - a blueprint for creating objects that encapsulate data and behavior")

# Use import statements to bring in modules and packages
import math  # standard library module
from math import sqrt  # importing specific function from a module

# Get current working directory using os module
import os
current_directory = os.getcwd()
parts = current_directory.split("\\")
print(f"Current Working Directory: {parts[-1]}")

# Example of creating a simple package structure
print("Example of creating a simple package structure:")
print("mypackage/")
print("├── __init__.py")
print("├── module1.py")
print("└── module2.py")
print()

print("In module1.py:")
print("def greet(name):")
print("    return f\"Hello, {name}!\"")
print()

print("In module2.py:")
print("def farewell(name):")
print("    return f\"Goodbye, {name}!\"")
print()

print("In __init__.py:")
print("from .module1 import greet")
print("from .module2 import farewell")
print()

print("Now you can import the package and use its functions:")
print("from mypackage import greet, farewell") 

import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print(df)

print("To install a specific version of a package, use:")
print("pip install package_name==version_number")

# Print statement to show importing multiple modules from a package
print("from mypackage import greet, farewell")


