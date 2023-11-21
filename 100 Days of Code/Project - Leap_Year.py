# The goal of this project is to write a program that determines whether a given year is a Leap Year or not. 
# A Leap Year is a year that is divisible by 4 with no remainder, *except* if the year is also divisible by 100, *unless* the year is also divisible by 400.

# Example: Year 2000
# 2000 / 4 = 500 (Leap Year)
# 2000 / 100 = 20 (Not a Leap Year)
# 2000 / 400 = 5 (Leap Year)
# So the year 2000 is a Leap Year.

year = int(input("Enter a year: "))
if year % 4 == 0: # First condition to check if the year is cleanly divisible by 4. If it is, it is a Leap Year.
    if year % 100 == 0: # Second condition to check if the year is also divisible by 100 (year % 4 == 0 and year % 100 == 0). If it is, it is not a Leap Year.
        if year % 400 == 0: # Third condition to check if the year is also divisible by 400 (year % 4 == 0 and year % 100 == 0 and year % 400 == 0). If it is, it is a Leap Year.
            print("Leap Year.") 
        else: # If the year is divisible by 4 and 100, but not 400, it is not a Leap Year.
            print("Not a Leap Year.") 
    else: # If the year is divisible by 4, but not 100, it is a Leap Year.
        print("Leap Year.") 
else:  # If the year is not divisible by 4, it is not a Leap Year. 
    print("Not a Leap Year.")
    
# Although this looks confusing, we are essentially using 3 nested if statements, which each have their own matching else statement. This is a good example of how to use nested if statements for checking multiple conditions.
# The first if statement checks if the year is divisible by 4. If it is, it is a Leap Year. If it is not, it is not a Leap Year, which corresponds to the else statement for the first if statement code block.
# The second if statement checks if the year is also divisible by 100. If it is, it is not a Leap Year. If it is not, it is a Leap Year, which corresponds to the else statement for the second if statement code block.
# The third if statement checks if the year is also divisible by 400. If it is, it is a Leap Year. If it is not, it is not a Leap Year, which corresponds to the else statement for the third if statement code block.

# A flow chart or a truth table would be a helpful way to visualize the logic of this program.


        
            
    
    
    