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
            print("Leap Year.") # If the year is divisible by 4, 100, and 400, it is a Leap Year.
        else:
            print("Not a Leap Year.") # If the year is divisible by 4 and 100, but not 400, not a Leap Year.
    else:
        print("Leap Year.") # If the year is divisible by 4, but not 100, it is a Leap Year.
        
            
    
    
        