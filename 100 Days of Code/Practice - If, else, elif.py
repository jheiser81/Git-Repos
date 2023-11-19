# 1) Write a program that asks the user for a number and then prints whether the number is positive, negative, or zero.

number = int(input("Please enter a number to check: ")) 
if number == 0:
    print("Cannot use zero. Please choose a different number.")
elif number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
# The check for zero had to be at the top of the code. I originally had the zero check at the bottom, so it would never trigger the check.
    
# 2) Write a program that asks the user for their age and then prints whether they are a child (under 13), a teenager (13 to 19), or an adult (20 and older).

age = int(input("Please enter your age: "))
if age < 13:
    print("You are a child.")
elif age >= 13 and age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")

# 3) Write a program that asks the user for two numbers and then prints whether the first number is greater than, less than, or equal to the second number.

first_number = float(input("Enter a number: "))
second_number = float(input("Enter a second number: "))
if first_number == second_number:
    print("The two numbers are equal.")
elif first_number > second_number:
    print("The second number is greater than the first number.")
elif first_number < second_number:
    print("The first number is less than the second number.")

# 4) Write a program that asks the user for a grade (0 to 100) and then prints whether the grade is an A (90 to 100), B (80 to 89), C (70 to 79), D (60 to 69), or F (below 60).

grade = int(input("Enter a grade from 0-100: "))
if grade < 60:
    print("You scored an F. This grade shows a lack of effort.")
elif grade >= 60 and grade < 70:
    print("You scored a D. This is a failing grade. Study hard to improve your grade!")
elif grade >= 70 and grade < 80:
    print("You scored a C. This is a passing mark, but you should try to improve.")
elif grade >= 80 and grade < 90:
    print("You scored a B. Well done!")
elif grade >= 90 and grade < 101:
    print("You scored an A! You know the material very well.")
else:
    print("Invalid number. The grade must be between 0-100.")

# 5) Write a program that asks the user for a number and then prints whether the number is even or odd. If the number is even, also check if it's divisible by 4 and print an additional message if it is.

new_number = int(input("Enter a number: "))
if new_number == 0:
    print("Cannot use zero, please choose another number.")
elif new_number % 2 == 0:
    print("The number is even.")
    if new_number % 4 == 0:
        print("The number is also divisible by 4.")
    if new_number % 4 != 0:
        print("The number is not divisible by 4.")
else:
    print("The number is odd.")

# Remember, the key to these exercises is to understand how to use if/else/elif statements to check different conditions and execute different code based on the results of those checks.