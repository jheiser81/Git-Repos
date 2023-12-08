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
    treasure_row = random.randint(0,2) # this randomizes the row location of the treasure
    treasure_column = random.randint(0,2) # this randomizes the column location of the treasure
    return treasure_row, treasure_column

def reset_map():
    global row1, row2, row3, treasure_map 
    # These variables need to be declared as global again so that modifications to them inside the function will be reflected outside of the function
    row1 = ["_","_","_"]
    row2 = ["_","_","_"] # Resets the map to the original state
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

# Tracking
dig_count = 0 # Keeps track of the number of digs
previous_digs = [] # Keeps track of previous dig locations entered by the user

# Main game logic, start of while loop block
while dig_count < 5: # The game will continue (loop) until the user has used up all 5 attempts (dig_count = 5
    dig_location = input("Enter the column letter and row number of where you want to dig: ")
    
    error_message = "Invalid input. Please enter a valid column letter and row number.\n"
    
    if len(dig_location) < 2: # Use len() to get the length of the user's input. If the length is less than 2, it means the user entered a single character
        print(error_message)
        continue # The program will then continue to the next iteration of the while loop
    
    # Error handling
    try: # This block will try to execute the code inside it. If an error occurs, the program will jump to the except block
        column_letter = dig_location[0].upper() # Extracts the first character of the user's input and converts it to uppercase
        column_letters = ["A", "B", "C"] # List of valid column letters
        column_index = column_letters.index(column_letter) 
        # index() is used to find the index of the column letter the user entered in the list (column_letters), and assigns it to column_index
        # Basically, this converts the column letter to a number (the index), so that it can be used to access the correct column in the treasure_map list
        row_number = int(dig_location[1]) - 1 
        # Extracts the second character from the user's input, converts it to an integer, and subtracts 1. This is because the user will enter a number from 1 to 3, but the treasure_map list uses 0 to 2
        # Basically, converts the second character from a string to a number, and subtracts 1 so that it can be used to access the correct row in the treasure_map list
      
    except (ValueError, IndexError): # If the user enters an invalid column letter or row number, the program will catch the error and print an error message
        continue # The program will then continue to the next iteration of the while loop
    
    finally: # This block will be executed regardless of whether an exception was caught or not. This was necessary because otherwise the program would terminate if invalid input was entered, and the error message would not be printed
        row_num_out_of_range = row_number < 0 or row_number > 2 # Checks if the row number is out of range
        column_index_out_of_range = column_index < 0 or column_index > 2 # Checks if the column index is out of range
        if row_num_out_of_range or column_index_out_of_range: # If either of the above conditions are true, the program will print an error message 
            print(error_message)
            continue # Next iteration 
        
    # Check if location was already selected
    if dig_location in previous_digs: # uses the in operator to check if the user's input is in the list of previous digs
        print("\nYou have already searched here. Choose another location.\n")
        print_map() # Prints the map again so that the user can see where they have already searched
        continue # Next iteration
    else: 
        previous_digs.append(dig_location) # If the user's input is not in the list of previous digs(so a valid location), it will be added to the list
        
    # Check if treasure is found
    if row_number == treasure_row and column_index == treasure_column: # Checks if the user's input (row and column) matches the location of the treasure
        treasure_map[row_number][column_index] = "X" # If the treasure is found, update the map with an X, and print the map
        print(f"The treasure was buried at {column_letters[treasure_column]}{treasure_row + 1}.") # Prints the location of the treasure
        print("You found the treasure! Congratulations!\n")
        print_map() # Prints updated map
        break # Breaks out of the while loop and ends the game
    else:
        treasure_map[row_number][column_index] = "O" # If the treasure is not found, update the map with an O
        dig_count += 1 # Increment the dig count by 1
        print(f"You have {5 - dig_count} attempts left.\n") # Prints the number of dig attempts left
        print_map() # Prints updated map
# End of while loop block

# Handles loss condition     
if dig_count == 5: # If the user has used up all 5 attempts, the game will end. This is outside of the while loop because it will only be executed if the while loop ends naturally (i.e. the user did not find the treasure)
    print("You have run out of attempts.")
    treasure_map[treasure_row][treasure_column] = "X" # Updates the map with an X at the location of the treasure so that the user can see where it was
    print(f"The treasure was buried at {column_letters[treasure_column]}{treasure_row + 1}.\n")
    print_map()
    print("Game Over.")
    
# Ask user if they want to play again
    print("Do you want to play again? (Y/N)")
    play_again = input().upper()
    if play_again == "Y":
        dig_count = 0 # Reset the dig count to 0
        previous_digs = [] # Reset the list of previous digs to an empty list
        reset_map() # Resets the map to the original state
        treasure_randomizer() # Randomize the treasure location again
        print_map() # Prints a new blank map
    else:
        print("Thanks for playing!") # If the user does not want to play again, the program will end
        




















