import random

def get_choices (): #def is how you define a function in python
    player_choice = input("Enter a choice(rock, paper, or scissors: ")
    options = ["rock", "paper", "scissors"] # this is a list (aka array) of options, which is a collection of items stored in a variable
    computer_choice = random.choice(options) # this is calling the random.choice function, and passing in the options list as a parameter
    choices = {"player": player_choice, "computer": computer_choice} # this is a dictionary, which is a collection of key value pairs stored in a variable
    return choices
    #code that is indented indicates it is part of the function
    #call the get_choices function, and store the response in a variable called choices

choices = get_choices()
print (choices)

# dict = {"name": "Joel", "color": "blue"}
# this is an example of dictionaries, which are used to store data in key value pairs
# in this example, name and color are keys, and Joel and blue are the values
# in this example, the values are both strings, as they are enclosed by "". However, values can also be variables

# food = ["Fruit", "Chocolate", "Meat"]
# dinner = random.choice(food)
# this is creating a list, which is a collection of items stored in a variable
# lists in python are similar to arrays in other languages, but are more flexible
# in this example, we set a variable dinner, call the random.choice function, and pass in the food list as a parameter
