# ======================================================== #
# 1) Write a program that asks the user for their favorite color and then prints a greeting that includes their favorite color. Use the input() and print() functions.  #
# ======================================================== #
fav_color = input("What is your favourite color? ")
print(f"Great! Your favourite color is {fav_color} ")
# #Using variable and f-string
print(f"Great! Your favourite color is {input('What is your favourite color? ')}")
#This method doesn't use a variable, since the input method is nested inside the print function. This is less common though.

# ======================================================== #
# 2) Write a program that asks the user for their age and then prints a message that includes their age. Use the input() and print() functions.  #
# ======================================================== #
print(f"Great! You are {input('How old are you? ')} years old ")
#Using nested input function

print("Enter your age: ")
age = input()
print(f"Great! You are {age} years old.")
#Using variable and f-string

# 3) Write a program that asks the user for their city of residence and then prints the number of characters in the city name. Use the input() and len() functions.

# 4) Write a program that asks the user for their favorite food and then prints the number of characters in the food name. Use the input() and len() functions.

# 5) Write a program that asks the user for a sentence and then prints the number of characters in the sentence. Use the input() and len() functions.