#region ​‌‍---𝗕𝗔𝗦𝗜𝗖 𝗣𝗬𝗧𝗛𝗢𝗡 𝗦𝗬𝗡𝗧𝗔𝗫---​

# -Python has a very simple syntax that is easy to read and understand. It is not necessary to do certain things common in other programming languages, such as ending lines with a semicolon or using curly braces to open and close blocks of code.
    
# -Python uses indentation to indicate blocks of code. Anything indented at the same level is considered to be in the same block of code. The number of spaces is up to you as long as it is consistent. Most people use 4 spaces.

# -Python is case sensitive. This means that "name" and "Name" are two different variables.

# -Python uses the hash symbol (#) to indicate a comment. Anything after the hash symbol on the same line is ignored by the interpreter. Comments are used to explain what the code does and are not executed. Comments can be placed on their own line, or you can make in-line comments.

#endregion

#region ---𝗜𝗡𝗣𝗨𝗧 𝗔𝗡𝗗 𝗢𝗨𝗧𝗣𝗨𝗧---

# -Python has a built-in function called ⁡⁢⁣⁣input()⁡ that will prompt the user to enter a value. The input() function can take a string as an argument that will be displayed to the user when the prompt appears. The input() function will return a string value, so if you want to use the input as a number, you will need to convert it to an integer or float. For example, ⁡⁢⁣⁣x = int(input("Enter a number: "))⁡ will prompt the user to enter a number and store it in the variable x as an integer. ⁡⁢⁣⁣name = input("Enter your name: ")⁡ will prompt the user to enter their name and store it in the variable name as a string.

# -Python has a built-in function called ⁡⁢⁣⁣print()⁡ that will output a value to the console. The print() function can take multiple arguments, separated by commas, and will print them to the console with a space between each value. The print() function will automatically add a new line at the end of the output. If you do not want a new line to be added, you can add an end argument to the print() function and set it to an empty string (""). For example, ⁡⁢⁣⁣print("Hello", end="")⁡ will print "Hello" to the console without adding a new line.

#-⁡⁢⁣⁣\n⁡ can be used to add a new line to a string. For example, ⁡⁢⁣⁣print("Hello\nWorld")⁡ will print "Hello" and "World" on separate lines.

#-The format() method can be used to insert values into a string. The format() method takes unlimited arguments, separated by commas, and inserts them into the string in the order they are given. The format() method can also take arguments with a number in curly braces ({}) to specify the order in which they are inserted. For example, print("Hello {}, my name is {}".format("World", "John")) will print "Hello World, my name is John" to the console.

#-The format() method can also take arguments with a colon (:) followed by a format specifier. For example, print("The number is {:.2f}".format(1.2345)) will print "The number is 1.23" to the console. The format specifier can be used to specify the number of decimal places, the number of digits, the type of number (integer, float, etc.), and more. In this case, the f denotes a float and the .2 denotes 2 decimal places.

#endregion

#region ---𝗢𝗣𝗘𝗥𝗔𝗧𝗢𝗥𝗦---

# -Arithmetic Operators:

# print(1 + 1) # Addition
# print(2 - 1) # Subtraction
# print(2 * 2) # Multiplication
# print(4 / 2) # Division
# print(5 % 2) # Modulus (returns the remainder of the division)
# print(2 ** 3) # Exponent (2 to the power of 3)
# print(5 // 2) # Floor Division (returns the largest integer less than or equal to the result of the division)

# -Assignment Operators: 

# x = 5 -Assigns a value to a variable
# x += 3 -Adds a value to a variable, same as x = x + 3
# x -= 3 -Subtracts a value from a variable, same as x = x - 3
# x *= 3 -Multiplies a variable by a value, same as x = x * 3
# x /= 3 -Divides a variable by a value, same as x = x / 3
# x %= 3 -Returns the remainder of a variable divided by a value, same as x = x % 3
# x //= 3 -Returns the floor division of a variable by a value, same as x = x // 3
# x **= 3 -Raises a variable to the power of a value, same as x = x ** 3

# -Comparison Operators: 

# print(5 == 5) # Equal to
# print(5 != 5) # Not equal to
# print(5 > 5) # Greater than
# print(5 < 5) # Less than
# print(5 >= 5) # Greater than or equal to
# print(5 <= 5) # Less than or equal to

# -Logical Operators: and, or, not 
# -In python, these are written as words instead of symbols. In most other programming languages, these are written as &&, ||, and ! respectively.

# -Identity Operators: is, is not
# -'is' returns true if both variables are the same object, not if they are equal. 
# -'is not' returns true if both variables are not the same object, not if they are not equal.

# -Membership Operators: in, not in
# -'in' returns true if a sequence with the specified value is present in the object. For example, 5 in [1, 2, 3, 4, 5] will return true.
# -'not in' returns true if a sequence with the specified value is not present in the object. For example, 6 not in [1, 2, 3, 4, 5] will return true.

# Ternary Operator:
# -The ternary operator is a shortcut for an if statement. It is written as follows:
# variable = value1 if condition else value2
# -If the condition is true, the variable will be assigned value1. If the condition is false, the variable will be assigned value2.
# -For example:
# x = 5
# y = 10
# z = x if x > y else y
# print(z) -This will print 10 to the console

#endregion

#region ---𝗩𝗔𝗥𝗜𝗔𝗕𝗟𝗘𝗦---

# -Variables in python function the same as in other languages. They are essentially containers for storing data values. They consist of a name, a value, and the assignment operator (=).

# -Python has no command for declaring a variable, it is created the moment you first assign a value to it.

#-Variables do not need to be declared with any particular type and can even change type after they have been set. 

#-To declare a variable, simply assign a value to it. For example:
# x = 5
# y = "Hello"
# z = 5.5

#-Variable names can contain letters, numbers, and underscores but cannot start with a number. Additionally, there are certain python keywords that cannot be used as variable names, such as "if", "for", "while", "sum", "print", etc. These keywords are reserved as they are used to define the syntax and structure of the language. There is no need to memorize the reserved keywords, as your IDE will highlight them for you if you try to use them as a variable name.

#endregion

#region ---𝗗𝗔𝗧𝗔 𝗧𝗬𝗣𝗘𝗦---

# -Python supports the following data types: 
# -Text Type: str (string) can be declared using either single or double quotes 
# -Numeric Types: int, float, complex 
# -Boolean Type: bool (true or false)
# -Sequence Types: list, tuple, range 
# -Mapping Type: dict (dictionary)
# -Set Types: set, frozenset 
# -Binary Types: bytes, bytearray, memoryview

# -You can check the data type of any object by using the type() function.
# For example:
# name = "John"
# print(type(name)) -This will print <class 'str'> to the console
# print(type(name) == str) -This will output True to the console
# print(isinstance(name, str)) -This will pass the name variable and the str data type to the isinstance() function and return True if the variable is of the specified type

# -While python has many data types, it is not necessary to declare the type of a variable when it is created. Python will automatically assign the correct data type based on the value assigned to the variable. If you type 5 for example, python will assign the integer data type, so 5 cannot be used as a string. 

# -While Python automatically detects data types, it is possible to use the class constructor functions to create variables of a specific data type. For example, you can use the str() constructor to create a string variable or the float() constructor to create a float variable. 

# -You can also convert between data types by using the int(), float(), and str() functions. For example, you can convert a string to an integer by using the int() function. If the string contains a decimal, the int() function will round down to the nearest integer. If the string contains a letter, the int() function will return an error. 

# -Variables can also be passed to the int(), float(), and str() functions to convert them to a different data type. For example, you can convert an integer to a string by passing it to the str() function. This is known as type casting.

#endregion

#region ​‌‍‌---𝗡𝗨𝗠𝗕𝗘𝗥𝗦---

# -Python supports two types of numbers: integers and floating point numbers. Integers are whole numbers, such as 5, 10, 15, etc. Floating point numbers are numbers with a decimal point, such as 5.5, 10.5, 15.5, etc.

# -Since Python is 100% object oriented, there is no reason to declare a variable before assigning a value to it. Python automatically detects the data type of the variable based on the value assigned to it. For example, if you assign the value 5 to a variable, Python will automatically assign the integer data type to that variable. If you assign the value 5.5 to a variable, Python will automatically assign the float data type to that variable. The only exception to this rule is if you are converting a variable to a different data type using the int(), float(), or str() functions. For example, myInt = 7 will be an integer, but myInt = 7.5 will be a float.

#endregion

#region ---𝗦𝗧𝗥𝗜𝗡𝗚𝗦---

# -Strings are used to store text data. They can be declared using either single or double quotes, but the quotes must match.

# -Strings can be indexed, meaning that each character in the string has a corresponding index number. The first character has an index of 0, the second character has an index of 1, and so on. You can access a specific character in a string by using the index number in square brackets. For example, name = "John" print(name[0]) will print "J" to the console.

# -You can also use negative indexing to access characters from the end of the string. The last character has an index of -1, the second to last character has an index of -2, and so on. For example, name = "John" print(name[-1]) will print "n" to the console.

# -You can also use a range of indexes to access a range of characters in a string. For example, name = "John" print(name[1:3]) will print "oh" to the console. Note that the range will start at the first index and end at the last index minus one.

# -You can also use the len() function to get the length of a string. For example, name = "John" print(len(name)) will print 4 to the console. This is the equivalent of the .length property in other languages.

# -You can concatenate two strings by using the + operator. For example, name = "John" print("Hello " + name) will print "Hello John" to the console. Note that you cannot concatenate a string and a number. You must first convert the number to a string by using the str() function. For example, name = "John" age = 25 print("Hello " + name + ". You are " + str(age) + " years old.") will print "Hello John. You are 25 years old." to the console.

# -You can also concatenate strings with variables that have been given a value. For example, name = "John" age = 25 print(f"Hello {name}. You are {age} years old.") will print "Hello John. You are 25 years old." to the console. Note that the f before the string indicates that it is a formatted string. This allows you to insert variables into the string by using curly braces.
# name = "John"
# age = 25
# print(f"Hello {name}. You are {age} years old.")

#Strings can be printed on multiple lines by using 3 sets of ""
#For example: 
print("""Joel is

42

years old
""")
#endregion

#region ---𝗦𝗧𝗥𝗜𝗡𝗚 𝗠𝗘𝗧𝗛𝗢𝗗𝗦---

# -Python has a set of built-in methods that can be used on strings. These methods are functions that can be called on a string to perform an operation on it. For example, name = "John" print(name.upper()) will print "JOHN" to the console. Note that the parentheses are required even if the method does not take any parameters.

# -The follows table lists some of the most commonly used string methods:

#  Method	             Description
# .capitalize()	        Converts the first character to upper case
# .toUpper()            Converts a string to upper case
# .toLower()            Converts a string to lower case
# .title()              Converts the first character of each word(string) to upper case 
# .strip()              Removes any whitespace from the beginning or the end of a string
# .replace()            Replaces a string with another string   
# .split()              Splits a string into a list
# .join()               Appends new string to the end of an existing string
# .format()             Formats specified values in a string
# .count()              Returns the number of times a specified value occurs in a string   
# .index()              Searches the string for a specified value and returns the position
# .find()               Returns the position of the first occurrence of a specified value
# .isalpha()            Returns True if a string contains only alphabetic characters
# .isalnum()            Returns True if a string contains only alphanumeric characters
# .isdecimal()          Returns True if a string contains only decimal characters
# .isdigit()            Returns True if a string contains only digits
# .islower()            Returns True if a string contains only lower case characters
# .isupper()            Returns True if a string contains only upper case characters
# .startswith()         Returns True if a string starts with a specified value
# .endswith()           Returns True if a string ends with a specified value
# len()                 Returns the length of a string

# -You can also us the in keyword to check if a string contains a specified value. For example, name = "John" print("J" in name) will print True to the console.

# -It is important to note that these methods do not modify the original string. Instead, they return a new string with the specified changes. For example, name = "John" print(name.upper()) will print "JOHN" to the console, but the value of name will still be "John".

# -There are many more string methods, and it is recommended that you look them up as you need them, rather than trying to memorize them all. A full list of string methods can be found at https://www.w3schools.com/python/python_ref_string.asp

#endregion

#region ---𝗘𝗫𝗣𝗥𝗘𝗦𝗦𝗜𝗢𝗡𝗦 𝗔𝗡𝗗 𝗦𝗧𝗔𝗧𝗘𝗠𝗘𝗡𝗧𝗦---

# -An expression is any type of code that return a value. For example, 5 + 5 is an expression that returns the value 10.

# -A statement performs an operation on a value. For example, print(Hello World) is a statement that prints "Hello World" to the console.

# -A program is formed from a sequence of expressions and statements.

# -Commonly, each statement is written on a separate line. However, multiple statements can be written on the same line by separating them with a semicolon (;). However, it is generally considered bad practice to do this as it makes the code harder to read.

#endregion

#region ---𝗖𝗢𝗡𝗗𝗜𝗧𝗜𝗢𝗡𝗔𝗟𝗦---

# -Condition statements, also known as if statements, are used to perform different actions based on a condition being either true or false. If true, do this. If false, do something else.

# -Note that the if statement condition must be followed by a colon (:). Python uses indentation to indicate which lines of code are part of the if statement. All indented lines of code will be executed if the condition is true. If the condition is false, the indented lines of code will be skipped. The code that will run if the condition is false does not have to be indented. 

# -In addition to the 'if' keyword, there are two other keywords that can be used in an if statement: 'elif' and 'else'. 'elif' is short for 'else if' and is used to check for additional conditions. 'else' is used to run code if none of the previous conditions are true. Note that 'else' does not have a condition. It is used to run code if none of the previous conditions are true.

beverage = input("What beverage would you like? ")
if beverage == "coffee":
    print("We have coffee")
elif beverage == "tea":
    print("We have tea")
elif beverage == "soda":
    print("We have soda")
else:
    print("We dont have that. You get water.")
    
# -In addition to regular if statements, there are also what are called conditional expressions. These are also known as ternary operators. They are used to assign a value to a variable based on a condition. The syntax for creating a conditional expression is: variable = value1 if condition else value2. If the condition is true, the variable will be assigned value1. If the condition is false, the variable will be assigned value2. For example, age = 25 if age >= 21 else 0 will assign 25 to the age variable if age is greater than or equal to 21. Otherwise, it will assign 0 to the age variable.

#endregion

#region ---𝗟𝗢𝗢𝗣𝗦---

# -Loops are used to repeat a block of code a specified number of times. There are two types of loops in Python: for loops and while loops.

    # -For Loops:⁡ Like in other languages, a for loop is primarily used to iterate over a sequence of values, like keeping track of a counter variable. When making a for loop in python, you must use the ⁡⁢⁣⁣range()⁡⁡ function. The range() function takes up to 3 parameters: start, stop, and step. The start parameter is the number that the loop will start at. The stop parameter is the number that the loop will stop at. The step parameter is the number that the loop will increment by. If the step parameter is not specified, it will default to 1. For example, ⁡⁢⁣⁣for i in range(1, 10, 2): print(i)⁡ ⁡⁡⁡will print the numbers 1, 3, 5, 7, and 9 to the console. It is not necessary to specify all 3 parameters. ⁡⁢⁣⁣for i in range(10): print(i)⁡⁡ will print the numbers 0 through 9 to the console. Keep in mind that range is exclusive of the stop parameter. This means that the loop will stop before reaching the stop parameter. If you wanted to print the numbers from 1 to 10, for example, you would have to make the range go to 11.
    
    # -While Loops: While loops are used to repeat a block of code while a condition is true, and will continue to run until the condition is no longer true. To declare a while loop in python, you use the following syntax: while condition: code. The code will continue to run as long as the condition is true. For example, ⁡⁢⁣⁣while i < 10: print(i) ⁡⁡will print the numbers 0 through 9 to the console. Keep in mind that if the condition is never false, the loop will run forever. This is called an infinite loop. For example, ⁡⁢⁣⁣while True: print("Hello World")⁡ ⁡⁡⁡will print "Hello World" to the console forever. To stop an infinite loop, you can press Ctrl + C on your keyboard.

#endregion

#region ---𝗙𝗨𝗡𝗖𝗧𝗜𝗢𝗡𝗦---

# -Functions are a way to make code modular and reusable. They are blocks of code that perform a specific task whenever they are 'called'. Functions can take parameters, which are values that are passed into the function. Functions can either return a value or not return a value. If a function does not return a value, it is called a procedure. To create a function in Python, you use the following syntax: ⁡⁢⁣⁣def function_name(parameters):code⁡. 

# The ⁡⁢⁣⁣def⁡ keyword is used to declare a function. The function name is the name of the function. The parameters are the values that are passed into the function. The code is the code that will run when the function is called. For example, ⁡⁢⁣⁣def add(x, y): return x + y⁡ will create a function called add that takes two parameters, x and y, and returns the sum of x and y. To call a function, you simply type the name of the function followed by parentheses. For example, add(5, 10) will call the add function and pass in the values 5 and 10 as the parameters. The function will then return the value 15.

#endregion