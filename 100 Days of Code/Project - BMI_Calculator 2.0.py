height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

BMI = float(weight) / float(height) ** 2
if BMI < 18.5:
   print(f"Your BMI is: {BMI}, you are underweight.")
elif BMI > 18.5 and BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI >= 25 and BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI >= 30 and BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
elif BMI >= 35:
    print(f"Your BMI is {BMI}, you are clinically obese.")
    
# Example input 1:
# 1.50
# 63
# Output: "Your BMI is 28.0, you are slightly overweight."

# Example input 2:
# 1.80
# 96
# Output: "Your BMI is 37.49999999999999, you are clinically obese.

# Example input 3:
# 1.71
# 73
# Output: "Your BMI is 24.96494647925858, you have a normal weight."

# I could have capped off the if statement, since that would have been a default condition if all the other conditions were false. However, I wanted to explicityly print the BMI result, so I left it as an elif statement.

# In order to round the results, I have to use the round() function with the BMI variable as an argument, and specify the number of decimal places. I could do this for each print statement, but it is more efficient to use it with the initial variable, since that way I only have to call the function once.

print("Using the round function:")
BMI = round(float(weight) / float(height) ** 2)
if BMI < 18.5:
   print(f"Your BMI is: {BMI}, you are underweight.")
elif BMI > 18.5 and BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI >= 25 and BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI >= 30 and BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
elif BMI >= 35:
    print(f"Your BMI is {BMI}, you are clinically obese.")