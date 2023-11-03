# **String Manipulation**

print("Hello, World!\nHello, World!\nHello, World!")
print("Hello" + " " + "Joel")

# Fix the code below 👇
# print(Day 1 - String Manipulation")
# print("String Concatenation is done with the "+" sign.")
#   print('e.g. print("Hello " + "world")')
# print(("New lines can be created with a backslash and n.")

print("Day 1 - String Manipulation")
# Missing double quotes
print('String concatenation is done with "+" sign')
print("String Concatenation is done with the \"+\" sign.")
# + sign read as string, need to differentiate quotes, or escape string with \
print('e.g. print("Hello " + "world")')
# Unnecessary indent, in python this will cause an error
print("New lines can be created with a backslash and n.")
# Extra bracket causing error

# **Input Function**

input("What is your name?")
# the input() function will prompt the user for input and return the value as a string.

# **Print Function**

print("Hello, " + input("What is your name?"))
# In this example, the input is passed as an argument to the print function, which is then concatenated with the string
# "Hello " and printed to the console as a single string value "Hello, <name>".
# This is an example of nested function calls, since we are calling the print function within the input function call.

# **Len Function**

# Write a program that prints the number of characters in a user's name

print(len(input("What is your name? ")))
# The len() function returns the number of characters in a string. In this example, the len function is called with the input function as an argument.
# The input function prompts the user for input and returns the value as a string.
# The len function then returns the number of characters in the string and prints it to the console.

# **Variables**

name = input("What is your name? ")
print(name)
print(len(name))
# In this example, the input value is assigned to a variable called 'name'. The variable can then be used later in the program to access the value.

name = "Jack"
print(name)
name = "Angela"
print(name)
# In this example, the variable 'name' is assigned the value "Jack" and then printed to the console. The variable is then reassigned the value "Angela" and printed again.
# Variables can be reassigned as many times as needed, and the value can be changed. However, it is good practice to use one variable per value, and to use descriptive variable names to make the code easier to read.

name = input("What is your name? ")
length = len(name)
print(length)
# In this example, the input value is assigned to a variable called 'name'. The len function is then called with the variable 'name' as an argument.
# The result of the len function is assigned to a variable called 'length' and printed to the console.

# **Int Function**

# Write a program that takes two numbers as input and prints their product.
num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))
print(num1 * num2)

# In this example, two variables are created to hold the value of the user inputs.
# The input is then passed to the int() function, which converts the string value to an integer. The resulting integer values are then multiplied together and printed to the console.

print("The product of the two numbers is: " + str(num1 * num2))
# Here we have used the str() function to convert the integer value to a string so that it can be concatenated with the other string values.

print(f"The product of the two numbers is: {num1 * num2}")
# Here we have used an f-string to format the string value with the result of the multiplication. f-strings are a more modern way of formatting strings in Python. In other languages, this is referred to as string interpolation.

# Write a program that switches the values stored in the variables a and b.
a = input("Enter number for a: ")
b = input("Enter number for b: ")
# **Write your code below**
temp = a
a = b
b = temp
# **Don't change the code below here**
print("a: " + a)
print("b: " + b)
# In this example, a temporary variable is used to store the value of a before it is reassigned to b. The value of b is then reassigned to a and the value of the temporary variable is reassigned to b.
