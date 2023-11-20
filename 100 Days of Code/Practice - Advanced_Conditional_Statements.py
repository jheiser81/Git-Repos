# These are some practice problems for more advanced conditional statements. They will help you get more comfortable with the syntax and structure of conditional statements, and will also help you practice your problem solving skills.

# 1) Write a program that checks if a number is a multiple of both 5 and 3.
mult_5_or_3 = int(input("Enter a number to check if it is divisible by both 5 and 3: "))
if mult_5_or_3 % 5 == 0 and mult_5_or_3 % 3 != 0: 
    print(f"The number {mult_5_or_3} is divisible by 5, but not divisible by 3.")
elif mult_5_or_3 % 5 != 0 and mult_5_or_3 % 3 == 0:
    print(f"The number {mult_5_or_3} is divisible by 3 but not divisible by 5.")
elif mult_5_or_3 % 5 != 0 and mult_5_or_3 % 3 != 0:
    print(f"The number {mult_5_or_3} is not divisible by either 5 or 3.")
else:
    print(f"The number {mult_5_or_3} is divisible by both 5 and by 3.")
    
# 2) Write a program that determines if a year is a leap year (you've done this, but repeating it will help reinforce your understanding).
year = int(input("Enter a year to check: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a Leap Year.")
        else:
            print(f"{year} is not a Leap Year.")
    else: # This else statement needed to be indented one more level to be in line with the if statement above it. It was originally indented to be part of the first if statement.
        print(f"{year} is a Leap Year.")

# ==============================================================================
# Advanced problems that require loops. Come back to these later
# ==============================================================================

# 1) Write a program that determines if a number is a prime number (a number that has no divisors other than itself and 1).

# 2) Write a program that checks if a string is a palindrome (a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run).

# 3) Write a program that determines the type of a triangle based on the lengths of its sides (equilateral, isosceles, or scalene). Not sure how to do this one yet.