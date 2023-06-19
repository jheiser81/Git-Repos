# --Variable manipulation--

#Create a simple program that swaps data between variables. This should include various data types, such as integers, floats, characters, and strings

a = 5
b = 10
print(f"Before swap: a = {a}, b = {b}")
a, b = b, a
print(f"After swap: a = {a}, b = {b}\n")

# --String Manipulation & Concatenation--

# Make a simple program that prints a string author and a string quote, and concatenates them together. Then, do the same thing using string interpolation.

author = "William Blake"
quote = "I must create a system, or be enslaved my another man's. I will not reason and compare: my business is to create."

#regular string concatenation
print(author + " once said: " + quote + "\n")

#string interpolation
print(f"{author} once said: {quote}\n")

# --Math Operators--

# Create a simple program that uses each of the math operators (+, -, *, /, %, **, //) with numbers between 1 and 10. Print the results of each operation.

x = 5
y = 5
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)

print(x + y * 3 -(100 / 5 - 5))
print("\n")

# --Conditional Statements--

# Explore conditional statements such as if, else if, else, and ternary operators. 

# if, else if, else
x = input("Enter a number for x:")
y = input("Enter a number for y:")
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")

print("\n")

# ternary operator, also known as a conditional expression

age = input("Enter your age:")
print("You are old enough to vote." if age >= 18 else "You are not old enough to vote.")




