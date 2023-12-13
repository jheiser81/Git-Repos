# Create the classic game TicTacToe, using a 3x3 grid and two players. The program must include the following: 
# -a game board and way to display it (using lists)
# -user input to decide where to place their marker (must be able to determine if a move is valid)
# -a computer opponent that makes random moves (must be able to determine if a move is valid)
# -a way to determine if the player or computer has won
# -a way to determine if the game is a draw
# -a way to restart the game. 
# -use of functions, conditionals, loops, variables, and other concepts learned so far

import random
import time # this module is used to add a delay between print statements. It can be used to simulate a computer thinking or calculating.

# Setting up the game board grid
row1 = ["-", "-", "-"]
row2 = ["-", "-", "-"]
row3 = ["-", "-", "-"]
game_board = [row1, row2, row3]

# Print the game board
def print_board():
    print(f"{row1}\n{row2}\n{row3}\n")

# Determine if the user or the computer goes first
def turn_order():
    # using random.choice() to randomly select a value from a list, and using boolean values to represent the player and computer
    player_turn = random.choice([True, False]) 
    if player_turn == True:
        player_mark = "X"
        computer_mark = "O"
        print("Player goes first!")
    else:
        player_mark = "O"
        computer_mark = "X"
        print("Computer goes first!")
        computer_turn()
    return player_mark, computer_mark

'''Using random.randint() to randomly select from a range of integers. This requires subtracting 1 from the range to get the correct index.
    turn_result = random.randint(1, 2)
    if turn_result == 1:
        player = "X"
        computer = "O"
        print("Player goes first!")
    else:
        player = "O"
        computer = "X"
        print("Computer goes first!")
        computer_turn()
    return player, computer'''
    
'''Using random.randrange() to randomly select from a range. This eliminates the need to subtract 1 from the range.
    turn_result = random.randrange(1, 3)
    if turn_result == 1:
        player = "X"
        computer = "O"
        print("Player goes first!")
    else:
        player = "O"
        computer = "X"
        print("Computer goes first!")
        computer_turn()
    return player, computer'''

# Function for the computer's turn   
def computer_turn():
    # Choose a random row and column for the computer
    row = random.randint(0, 2)
    column = random.randint(0, 2)
    
    # Check if the computer's move is valid
    while game_board[row][column] != "-":
        
    # If the move is not valid, choose a new random row and column
        row = random.randint(0, 2)
        column = random.randint(0, 2)
        
    # Place computer's marker on the game board and print the board
    game_board[row][column] = computer_mark
    print_board()
    
# Function for the player's turn
def player_turn():
    print("Choose a position on the game board to place your marker in the format 'row, column'.")
    print("For example, if you want to place your marker in the top left corner, type '1, 1' to represent the first row and first column.\n")
    print_board()
    position = input("Enter your move: ")
    row = int(position[0]) - 1
    column = int(position[-1]) - 1
    
    while game_board[row][column] != "-":
        print("That position is already taken. Please choose another position.")
        position = input("Enter your move: ")
        row = int(position[0]) - 1
        column = int(position[-1]) - 1
        game_board[row][column] = player_mark
        print_board()
 
    

# Ask the user to input their move on the game board
print("Welcome to TicTacToe!")
print("First, let's determine who goes first...")
time.sleep(2) # .sleep() method takes a number as an argument and pauses the program for that many seconds.
player_mark, computer_mark = turn_order()
print(f"Player is {player_mark} and computer is {computer_mark}.\n")











    










