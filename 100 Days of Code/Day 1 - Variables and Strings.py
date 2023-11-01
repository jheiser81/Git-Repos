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

input("What is your name?")
# the input() function will prompt the user for input and return the value as a string.

print("Hello " + input("What is your name?"))
# In this example, the input is passed as an argument to the print function which is then concatenated with the string
# "Hello " and printed to the console as a single string value "Hello <name>".
# This is an example of nested function calls, since we are calling the print function with the input function inside

num1 = int(input())
num2 = int(input())
print(num1 * num2)
# In this example, the input is passed to the int() function, which converts the string value to an integer.
# The resulting integer values are then multiplied together and printed to the console.

# Write a program that prints the number of characters in a user's name
print(len(input("What is your name?")))
# The len() function returns the number of characters in a string. In this example, the len function is called with the
# input function as an argument. The input function prompts the user for input and returns the value as a string.
# The len function then returns the number of characters in the string and prints it to the console.

name = input("What is your name? ")
print(len(name))
# In this example, I have assigned the input value to a variable called 'name'. Everything else is the same as above.
