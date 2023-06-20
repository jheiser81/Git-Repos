
# # ​‌‍‌--𝗩𝗮𝗿𝗶𝗮𝗯𝗹𝗲 𝗺𝗮𝗻𝗶𝗽𝘂𝗹𝗮𝘁𝗶𝗼𝗻--​

# #Create a simple program that swaps data between variables. This should include various data types, such as integers, floats, characters, and strings

# a = 5
# b = 10
# print(f"Before swap: a = {a}, b = {b}")
# a, b = b, a
# print(f"After swap: a = {a}, b = {b}\n")

# # --String Manipulation & Concatenation--

# # Make a simple program that prints a string author and a string quote, and concatenates them together. Then, do the same thing using string interpolation.

# author = "William Blake"
# quote = "I must create a system, or be enslaved my another man's. I will not reason and compare: my business is to create."

# #regular string concatenation
# print(author + " once said: " + quote + "\n")

# #string interpolation
# print(f"{author} once said: {quote}\n")

# # ​‌‍‌--𝗠𝗮𝘁𝗵 𝗢𝗽𝗲𝗿𝗮𝘁𝗼𝗿𝘀--​

# # Create a simple program that uses each of the math operators (+, -, *, /, %, **, //) with numbers between 1 and 10. Print the results of each operation.

# num1 = 5 + 15 * 3
# num2 = 100 / 5 - 5
# num3 = num1 - num2
# print(num3)
# num3 = 15 % 4
# print(num3)

# print("\n")

# # ​‌‍‌--𝗖𝗼𝗻𝗱𝗶𝘁𝗶𝗼𝗻𝗮𝗹 𝗦𝘁𝗮𝘁𝗲𝗺𝗲𝗻𝘁𝘀--​

# # Explore conditional statements such as if, else if, else, and ternary operators. 

# # if, else if, else

# ifNum1 = int(input("Enter a number:"))
# if ifNum1 % 2 == 0:
#     print("The number is even.\n")
# else:
#     print("The number is odd.\n")

# x = input("Enter a number for x:")
# y = input("Enter a number for y:")
# if x > y:
#     print("x is greater than y")
# elif x < y:
#     print("x is less than y")
# else:
#     print("x is equal to y")

# print("\n")

# # ternary operator, also known as a conditional expression, is a way to check a condition and return a value based on that condition. It is similar to an if statement, but it is written as a single line of code.

# age = int(input("Enter your age:")) #have to convert input to int, otherwise it will be a string
# print("You are old enough to vote.\n" if age >= 18 else "You are not old enough to vote.\n")

# # ​‌‍‌‍--𝗟𝗼𝗼𝗽𝘀--​​

# # For Loop
# # DECLARE sum = 0
# # FOR i FROM 1 TO 100 DO
# #     sum = sum + i
# # END FOR
# # DISPLAY sum

# sum = 0
# for i in range(1, 101): #range is exclusive, so 101 is needed to get to 100
#     sum += i
# print(sum)

# print("\n")

# # WHILE password != correctPassword DO
# #     INPUT password
# # END WHILE

# correctPassword = "password123"
# password = ""

# while password != correctPassword:
#     password = input("Enter password: ")
# print("Access granted.\n")

# ​‌‍‌--𝗙𝘂𝗻𝗰𝘁𝗶𝗼𝗻𝘀--​

def addNum(a, b): #a and b are parameters
    return a + b
print("The sum of the two numbers is:", addNum(5, 10)) #5 and 10 are arguments that we pass into the fuction in order to define the value of the parameters

def subNum(a, b):
    return a - b
print("The difference of the two numbers is:", subNum(10, 5))

def multNum(a, b):
    return a * b
print("The product of the two numbers is:", multNum(5, 10))

def divNum(a, b):
    return a / b
print("The quotient of the two numbers is:", divNum(10, 5))
    
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)
print("The result of the power function is:", power(5, 3))




