# ======================================================== #
# ================= Functions and Modules ================ #
# ======================================================== #

'''*** Defining and Calling Functions ***
Functions are reusable blocks of code that perform a specific task. You can define a function to perform a task once, and then call that function whenever you need to perform the task. This saves you from having to write the same code multiple times. In Python, a function is defined using the 'def' keyword, followed by the function name and a set of parentheses. Inside the parentheses, you can specify any parameters that the function should take. Then, you use a colon to start the function's code block.'''

def greet(name):
    print(f"Hello, {name}!")

# Passing a parameter to the function
greet("Alice")

# Passing a variable to the function
name = "Bob"
greet(name)

'''*** Positional and Keyword Arguments *** 
Functions can take in parameters in two ways: positional and keyword arguments. 
Positional arguements are passed in the order they are defined.
Keyword arguments are passed using the arguement name.''' 

def describe_pet(name, animal_type):
    print(f"My {animal_type}'s name is {name}.")
    
# First function call, using positional arguements
describe_pet("Buddy", "dog") 
# Second function call, using keyword arguements
describe_pet(animal_type="cat", name="Whiskers")

'''*** Returning Values ***
Functions don't have to just perform tasks, they can also return values. To return a value from a fucntion, you use the return keyword followed by the value you want to return.'''

def square(x): 
    return x ** 2 
result = square(5) 
print(result)

def _sum(a, b):    
    return a + b
result = _sum(5, 10)
print(f"5 + 10 = {result}")

'''*** Multiple Return Values ***
Functions can return multiple values by separating them with commas after the return keyword.'''

def operations(x, y):
    sum = x + y
    difference = x - y
    product = x * y
    quotient = x / y
    modulo = x % y
    return sum, difference, product, quotient, modulo
result1, result2, result3, result4, result5 = operations(10, 3)
print(f"Sum: {result1}")
print(f"Difference: {result2}")
print(f"Product: {result3}")
print(f"Quotient: {result4}")
print(f"Modulo: {result5}")

'''*** Built-in Functions ***
Python comes with a wide range of built-in functions that you can use in your code. These functions are always available, so you don't have to define them yourself. Here's an overview of some commonly used built-in functions:
print(): Prints text to the console  
input(): Reads input from the user.  
len(): Returns the length of an object.
range(): Generates a sequence of numbers.  
sum(): Returns the sum of a list of numbers.  
max(): Returns the maximum value in a list of numbers.  
min(): Returns the minimum value in a list of numbers.  
str(): Converts an object to a string.  
int(): Converts a string or float to an integer.  
float(): Converts a string or integer to a float.  
bool(): Converts a value to a Boolean (True or False).  
type(): Returns the type of an object.  
help(): Displays documentation for an object.'''

'''*** Importing Modules ***
Python has a large standard library that provides a rich set of modules that you can use in your code. A module is a file containing Python code that defines functions, classes, and variables. You can use the import keyword to import a module.
'import math'

Some commonly used modules include:
    math: Provides functions for mathematical operations.
    random: Provides functions for generating random numbers.
    datetime: Provides classes for manipulating dates and times.
    json: Provides functions for working with JSON data.
    csv: Provides functions for working with CSV files.

Although the standard library contains many useful modules,there are also many third-party modules available that provide additional functionality. You can install third-party modules using the pip package manager. To install a module, you use the pip install command followed by the name of the module.
'pip install numpy'

Some of the most popular third-party modules include:
    NumPy: Provides support for large, multi-dimensional arrays and matrices.
    Pandas: Provides tools for data analysis and statistics.
    Matplotlib: Provides tools for creating data visualizations.
    Django: A web framework for building web apps and APIs.
    Flask: Another web framework for building web apps and APIs.
    Requests: Provides tools for making HTTP requests.
'''

'''*** Creating Custom Python Modules ***
In addition to using modules created by others, you can also create your own custom modules. To create a module, you simply create a new Python file with a .py extension. Then, you can import the module using the import keyword, just like you would with a standard library or third-party module.
# Create a python file named circle.py
# Define the code for the external module
# Import the module in your main program.'''

'''*** Using a Custom Module ***
You can use a custom module by importing it into your code using the import keyword. When you import a module, you can access the functions and variables defined in the module using dot notation. Using modules allows you to organize your code into separate files, and then import the code you need into your main program.'''
import Circle
result = Circle.area(5)
print(result)









