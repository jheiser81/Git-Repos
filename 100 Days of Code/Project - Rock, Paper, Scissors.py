import random

def get_choices():
    player_choice = input("Choose rock, paper, or scissors: ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    game_choices = {"player": player_choice, "computer": computer_choice}
    return game_choices

game_result = get_choices()
# Need to implement logic to determine the winner, and print the results.
print(game_result)

# Step 1: Include the random module
# Step 2: Create a function to hold the logic of the game. 
# Step 3: Create a variable to store the user's choice, and then prompt the user to enter their choice in the console.
# Step 4: Create a list of options for rock, paper, and scissors. A list is a collection of items stored in a variable, and is defined by using square brackets, and separating the items with commas. Referred to as arrays in other languages.
# Step 5: Create a variable to store the computer's choice, and then use the random.choice function to randomly select an option from the previously created list.
# Step 6: Create a dictionary to store the player and computer choices. A dictionary is a collection of key value pairs stored in a variable. In this case, the keys are "player" and "computer", and the values are the choices made by the player and computer. It is defined by using curly braces, and separating the key value pairs with a colon. The key value pairs are separated by commas.
# Step 7: Return the game_choices dictionary. This will close the function, as well as return the game_choices dictionary to the function call. 
# Step 8: Create a variable called game_result, and pass in the get_choices function. This will call the get_choices function, and store the response in the game_result variable.
# Step 9: Print the game_result variable to the console. This will print the game_choices dictionary to the console.