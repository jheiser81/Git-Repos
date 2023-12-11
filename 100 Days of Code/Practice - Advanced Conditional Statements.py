# # These are some practice problems for more advanced conditional statements. They will help you get more comfortable with the syntax and structure of conditional statements, and will also help you practice your problem solving skills.

# # 1) Write a program that checks if a number is a multiple of both 5 and 3.
mult_5_or_3 = int(input("Enter a number to check if it is divisible by both 5 and 3: "))
if mult_5_or_3 % 5 == 0 and mult_5_or_3 % 3 != 0: 
    print(f"The number {mult_5_or_3} is divisible by 5, but not divisible by 3.")
elif mult_5_or_3 % 5 != 0 and mult_5_or_3 % 3 == 0:
    print(f"The number {mult_5_or_3} is divisible by 3 but not divisible by 5.")
elif mult_5_or_3 % 5 != 0 and mult_5_or_3 % 3 != 0:
    print(f"The number {mult_5_or_3} is not divisible by either 5 or 3.")
else:
    print(f"The number {mult_5_or_3} is divisible by both 5 and by 3.")
    
# # 2) Write a program that determines if a year is a leap year (you've done this, but repeating it will help reinforce your understanding).
year = int(input("Enter a year to check: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a Leap Year.")
        else:
            print(f"{year} is not a Leap Year.")
    else: # This else statement needed to be indented one more level to be in line with the if statement above it. It was originally indented to be part of the first if statement.
        print(f"{year} is a Leap Year.")
        
# 3) Write a program that takes two numbers as input and prints the larger number.
num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a second number: "))
if num_1 > num_2:
    print(f"The first number ({num_1}) is greater than the second number ({num_2}).")
elif num_2 > num_1:
    print(f"The second number ({num_2}) is greater than the first number ({num_1}).")
else:
    print("Both numbers are equal.")
    
# Write a program that takes an age as input and prints whether the person is an infant (age 0-1), a child (age 2-12), a teenager (age 13-19), an adult (age 20-64), or a senior (age 65+).
age = int(input("Enter your age: "))
if age <= 1:
    print("You are an infant.")
elif age >= 2 and age <= 12:
    print("You are a child.")
elif age >= 13 and age <= 19:
    print("You are a teenager.")
elif age >= 20 and age <= 64:
    print("You are an adult.")
# elif age >= 65:
else:
    print("You are a senior.")
# use >= or <= to check for a range. Using == will only be true if an age is **exactly** what is specified.

# Write a program that takes a single letter as input and determines if it's a vowel or a consonant.
# Write a program that takes a temperature as input and determines if water at that temperature would be solid (below 0 degrees Celsius), liquid (between 0 and 100 degrees Celsius), or gas (above 100 degrees Celsius).
# Write a program that takes a score as input and determines the corresponding letter grade (A for 90-100, B for 80-89, C for 70-79, D for 60-69, F for below 60).

# ==============================================================================
# Advanced problems that require loops. Come back to these later
# ==============================================================================

# 1) Write a program that determines if a number is a prime number (a number that has no divisors other than itself and 1).

# 2) Write a program that checks if a string is a palindrome (a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run).

# 3) Write a program that determines the type of a triangle based on the lengths of its sides (equilateral, isosceles, or scalene). Not sure how to do this one yet.