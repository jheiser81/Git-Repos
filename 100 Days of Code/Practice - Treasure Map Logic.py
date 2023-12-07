import random

# Setting up the lists
row1 = ["_","_","_"]
row2 = ["_","_","_"]
row3 = ["_","_","_"]
treasure_map = [row1, row2, row3]
    
def print_map():
    print(f"{row1}\n{row2}\n{row3}\n")

# Randomize the treasure location
def treasure_randomizer():
    global treasure_row, treasure_column # Make the variables global so they can be used outside of the function
    treasure_row = random.randint(0,2)
    treasure_column = random.randint(0,2)
    return treasure_row, treasure_column

def reset_map():
    global row1, row2, row3, treasure_map 
    # These variables need to be declared as global again so that modifications to them inside the function will be reflected outside of the function
    row1 = ["_","_","_"]
    row2 = ["_","_","_"]
    row3 = ["_","_","_"]
    treasure_map = [row1, row2, row3]
    return treasure_map

# Messages to the user
print("Welcome to the Treasure Map!")
print("You are on a deserted island and there is a treasure hidden somewhere.")
print("The treasure will be buried in a random location. You have to find the treasure within 5 attempts.")
print("Each place on the map is represented by a letter and a number, in the format of: A1, B3, C2, etc.")
print("Let's begin!\n")
print("Here is your map:\n")
treasure_randomizer()
print_map()

# User input
dig_count = 0 # Keep track of the number of digs
previous_digs = [] # Keep track of previous dig locations entered by the user

while dig_count < 5:
    dig_location = input("Enter the column letter and row number of where you want to dig: ")
    
    error_message = "Invalid input. Please enter a valid column letter and row number.\n"
    
    if len(dig_location) < 2:
        print(error_message)
        continue
    
    # First try/except block to check if the user entered a valid letter for the column location 
    # This doesn't seem to be working properly, the program terminates before the error message is printed 
    # Co-pilot keeps saying the same thing, and recommending the same fix that i've already tried
    try:
        column_letter = dig_location[0].upper()
        column_letters = ["A", "B", "C"]
        column_index = column_letters.index(column_letter)
        row_number = int(dig_location[1]) - 1
    except (ValueError, IndexError):
        continue
    finally:
        # This block will be executed regardless of whether an exception was caught or not
        if not (0 <= row_number <= 2 and 0 <= column_index <= 2):
            print(error_message)
            continue

    # Check if location was already selected
    if dig_location in previous_digs:
        print("\nYou have already searched here. Choose another location.\n")
        print_map()
        continue
    else:
        previous_digs.append(dig_location)
    
    # Check if treasure is found
    # If treasure is found, update the map with an X, and print the map
    if row_number == treasure_row and column_index == treasure_column:
        treasure_map[row_number][column_index] = "X"
        print(f"The treasure was buried at {column_letters[treasure_column]}{treasure_row + 1}.")
        print("You found the treasure! Congratulations!\n")
        print_map()
        break
    else:
        treasure_map[row_number][column_index] = "O"
        print("\nThe treasure isn't here. Select another location to search.\n")
        dig_count += 1
        print(f"You have {5 - dig_count} attempts left.\n")
        print_map()
    # If treasure is not found, update the map with an O, and print the map
       
if dig_count == 5:
    print("You have run out of attempts.")
    treasure_map[treasure_row][treasure_column] = "X"
    print(f"The treasure was buried at {column_letters[treasure_column]}{treasure_row + 1}.\n")
    print_map()
    print("Game Over.")
    
    print("Do you want to play again? (Y/N)")
    play_again = input().upper()
    if play_again == "Y":
        dig_count = 0 # Reset the dig count to 0
        previous_digs = [] # Reset the list of previous digs to an empty list
        reset_map()
        treasure_randomizer()
        print_map()
    else:
        print("Thanks for playing!")
        
# use functions to print map, DRY
# use while loop to repeat game?
# implement logic for when user enters invalid input, or enters the same location twice



















