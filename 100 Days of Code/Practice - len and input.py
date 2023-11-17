# 1) Write a program that asks the user for their favorite color and then prints a greeting that includes their favorite color. Use the input() and print() functions.  

fav_color = input("What is your favourite color? ")
print(f"Great! Your favourite color is {fav_color} ")
# #Using variable and f-string
print(f"Great! Your favourite color is {input('What is your favourite color? ')}")
#This method doesn't use a variable, since the input method is nested inside the print function. This is less common though.

# 2) Write a program that asks the user for their age and then prints a message that includes their age. Use the input() and print() functions.  

print(f"Great! You are {input('How old are you? ')} years old ")
#Using nested input function

print("Enter your age: ")
age = input()
print(f"Great! You are {age} years old.")
#Using variable and f-string

# 3) Write a program that asks the user for their city of residence and then prints the number of characters in the city name. Use the input() and len() functions.
print(len(input("What city do you live in? ")))
# Examble using nested function calls

print("What city do you live in? ")
city = input()
city_length = (len(city))
print(f"You live in {city}.")
# This example uses variabes to store the user input, and requires the len() function to be used separately. Trying to use len() with just the one variable and nesting will give incorrect result

# 4) Write a program that asks the user for their favorite food and then prints the number of characters in the food name. Use the input() and len() functions.
# print(len(input("What is your favourite food? ")))
print("What is your favourite food? ")
fav_food = input()
fav_food_len = len(fav_food)
print(f"Your favourite food is {fav_food}, which has {fav_food_len} characters.")
# These examples follow the same structure as question 4

# 5) Write a program that asks the user for a sentence and then prints the number of characters in the sentence. Use the input() and len() functions.
print("Type a short sentence: ")
sentence = input()
sentence_length = len(sentence)
print(f"The sentence '{sentence}' is {sentence_length} characters long.")
print(len(input("Type a short sentence: ")))