#region ---BASIC PYTHON SYNTAX---

# -Python has a very simple syntax that is easy to read and understand. It is not necessary to do certain things common in other programming languages, such as ending lines with a semicolon or using curly braces to open and close blocks of code.
    
# -Python uses indentation to indicate blocks of code. Anything indented at the same level is considered to be in the same block of code. The number of spaces is up to you as long as it is consistent. Most people use 4 spaces.

# -Python is case sensitive. This means that "name" and "Name" are two different variables.

# -Python uses the hash symbol (#) to indicate a comment. Anything after the hash symbol on the same line is ignored by the interpreter. Comments are used to explain what the code does and are not executed. Comments can be placed on their own line, or you can make in-line comments.

#endregion

#region ---OPERATORS---

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

#endregion

#region ---VARIABLES---

# -Variables in python function the same as in other languages. They are essentially containers for storing data values. They consist of a name, a value, and the assignment operator (=).

# -Python has no command for declaring a variable, it is created the moment you first assign a value to it.

#-Variables do not need to be declared with any particular type and can even change type after they have been set. 

#-Variable names can contain letters, numbers, and underscores but cannot start with a number. Additionally, there are certain python keywords that cannot be used as variable names, such as "if", "for", "while", "sum", "print", etc. These keywords are reserved as they are used to define the syntax and structure of the language. There is no need to memorize the reserved keywords, as your IDE will highlight them for you if you try to use them as a variable name.

#endregion

#region ---DATA TYPES---

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

#region ---EXPRESSIONS AND STATEMENTS---

# -An expression is any type of code that return a value. For example, 5 + 5 is an expression that returns the value 10.

# -A statement performs an operation on a value. For example, print(Hello World) is a statement that prints "Hello World" to the console.

# -A program is formed from a sequence of expressions and statements.

# -Commonly, each statement is written on a separate line. However, multiple statements can be written on the same line by separating them with a semicolon (;). However, it is generally considered bad practice to do this as it makes the code harder to read.

#endregion