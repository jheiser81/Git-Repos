# # **Primitive Data Types**

# # **Strings**

# # Strings are just a sequence of characters. In python, they can be enclosed in single or double quotes. 

# print("Hello"[0])
# # This will print the first character in the string "Hello", which is "H". This uses the subscript operator to access the character at the specified index. 
# # In python, the first character in a string always starts at index 0.

# street_name = "Abbey Road"
# print(street_name[4] + street_name[7])

# print("123" + "456")
# # Note that the "numbers" inside the quotes are not treated as actual numbers, but as characters in a string. This is because the computer reads anything inside quotes as a string, and so the result will simply concatenate the two strings together.

# # **Integers**

# # Integers are just whole numbers. They can be positive or negative. 
# # To get the computer to read the above example as numbers, you can simply remove the quotes. In python, numbers not enclosed in quotes are automatically treated as integers. In other languages, this may not be the case, and you may have to specify that the number is an integer first.

# print(123 + 456)

# # In normal usage, large integers are written with commas to separate them. In python, you can use underscores to accomplish the same separation. When the computer reads the number, it will ignore the underscores and treat the number as a single integer. The underscores are simply there to make the number easier to read for humans.

# print(123_456_789)

# # **Floats(Floating Point Numbers)**

# # Floating point numbers are simply numbers with a decimal point. They can be positive or negative.

# print(3.14159)

# # **Boolean**

# # Booleans are simply True or False values. They are used for checking conditions in code, and activating or ignoring certain parts of the code depending on the result of the check.

# bool = True
# bool = False

# # **Type Error, Type Checking and Type Conversion**

# # **Type Error**

# # A type error occurs when you try to combine two different data types in a way that is not supported. For example, you cannot add a string and an integer together.

# num_char = len(input("What is your name? "))
# # print("Your name has " + num_char + " characters.")

# # This will result in a type error, because you are trying to combine a string and an integer together. The len() function returns an integer, and the "+" operator is used to concatenate strings together. 

# # **Type Checking**

# # To check the data type of a variable, you can use the type() function.
# print(type(num_char))

# # **Type Conversion**

# # In addition to type checking, you can also perform type conversion or "type casting". This is when you convert one data type to another. For example, you can convert an integer to a string, or a string to an integer.

# num_char = len(input("What is your name? "))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")

# a = 123
# print(type(a))
# # This will print the data type of the variable a, which is an integer.

# a = str(123)
# print(type(a))
# This will print the data type of the variable a, which has been converted to a string.

# a = float(123)
# print(type(a))

# print(70 + float("100.5")) This will print the sum of 70 and 100.5, which is 170.5. The string "100.5" has been converted to a float, and the two numbers have been added together.

# print(str(70) + str(100))
# This will simply concatenate the two strings together, resulting in "70100".

# **Coding Exercise**
# In this exercise, the goal is to write a program that takes a two-digit number input, and then adds the two digits together.

# two_digit_number = input("Type a two digit number: ")
# # print(type(two_digit_number))
# first_digit = int(two_digit_number[0])
# second_digit = int(two_digit_number[1])
# two_digit_number = first_digit + second_digit
# print(two_digit_number)

# **Mathematical Operations in Python**
print(3 + 5)  # Addition
print(7 - 4)  # Subtraction
print(3 * 2)  # Multiplication
print(6 / 3)  # Division
# Note that in python, the "/" operator will always return a float, even if the result is a whole number. If you want to return a whole number, you can use the "//" operator instead.
print(2 ** 2)  # Exponent (power of)
print(3 % 2)  # Modulo (remainder of division)

# **Order of Operations**
# PEMDAS - Parentheses, Exponents, Multiplication, Division, Addition, Subtraction
# This is the order in which python will perform mathematical operations, which is the same as the order used in mathematics.
# Operations are also performed from left to right, so if there are multiple operations of the same type, or operations that have the same level of "priority", such as multiplication and division, the operations will be performed in the order that they appear from left to right.

print(3 * 3 + 3 / 3 - 3)
# This will print 7.0, because the multiplication and division operations have the same level of priority, and so are performed from left to right. To break this down, the first operation performed is 3 * 3, which is 9. Then 3 / 3 is performed, which is 1.0. Next, 9 + 1.0 is performed, which is 10.0. Finally, 10.0 - 3 is performed, which is 7.0.

# **Coding Exercise**
# In this exercise, the goal is to get the end result of 3 instead of 7. How would you do that?

print(3 * (3 + 3) / 3 - 3)
# This will give the result of 3. The reason for this is that the parentheses can be used to isolate parts of the code to give a low-priority operation a higher priority level. In this case, they are used to perform the addition of 3 + 3 first, then the multiplication of 3 * 6, then the division of 18 / 3, and finally the subtraction of 6 - 3.






