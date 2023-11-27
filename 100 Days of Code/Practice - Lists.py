# The goal of this exercise is to write a program that will select a random name from a list of names. The person selected will pay for everybody's food bill.
# You are not allowed to use the choice() function.
# The first line splits the string names_string into individual names and puts them inside a list called names. For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name
# Example Input: Angela, Ben, Jenny, Michael, Chloe

# Hint 1: You might need the help of the len() function.
# Hint 2: Remember that Lists start at index 0!

# Solution:

# Create a variable to store the list of names as a string, separated by commas and a space
# Use a second variable with the split() function, which will split the string into a list of names, and store it in the variable 'names'
# name_string = input("Enter list of names separated by commas: ")
# names = name_string.split(", ")

# # import the random module
# import random 

# # use the len() function to get the number of items in the list, and store it in the variable num_item
# num_items = len(names) 

# # generate a random number between 0 and the number of items in the list
# random_choice = random.randint(0, num_items - 1) 
# # 0 is the first index position, and num_items - 1 is the last index position. We subtract 1 because the last index position is always 1 less than the number of items in the list, since the first index position in a list is always 0.

# # pick out random person from list of names using the random number
# person_who_will_pay = names[random_choice] 
# # this will return the name at the random index position

# print(f"{person_who_will_pay} is going to buy the meal today!")

# Simpler solution:

import random

names_string = input("Enter a list of names separated by commas and a space: ")
names = names_string.split(", ")
name_index = random.randrange(len(names))
random_name = names[name_index]

print(f"{random_name} is going to buy the meal today!")

# This is a simpler and more efficient solution, because it uses the randrange() function, which returns a random integer between 0 and the number of items in the list, and then uses that random integer as the index position to return the name at that index position. In this way, it avoids the need to use the randint() function and having to subtract 1 from the number of items in the list, since this is done automatically by the randrange() function.


