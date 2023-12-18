# Create the classic game TicTacToe, using a 3x3 grid and two players. The program must include the following: 
# -a game board and way to display it (using lists)
# -user input to decide where to place their marker (must be able to determine if a move is valid)
# -a computer opponent that makes random moves (must be able to determine if a move is valid)
# -a way to determine if the player or computer has won
# -a way to determine if the game is a draw
# -a way to restart the game. 
# -use of functions, conditionals, loops, variables, and other concepts learned so far

import random
import time 
'''the time() module is used to add a delay between code executions. 
The module takes a float or integer value as an argument, which represents the number of seconds to delay. It can be used to simulate a computer thinking or calculating'''

'''Initialize the player and computer markers as global variables so they can be accessed anywhere in the code.
The markers will be assigned a value later in the code, this is just to initialize them as empty strings.'''
player_mark = ""
computer_mark = ""

'''Sets up the game board, which is a 3x3 grid
The board is comprised of 3 rows and 3 columns. Each row is a list, and the board is a list of lists, also referred to as a matrix or multi-dimensional list.
The board is initialized with "-" to represent cells that are empty and have not been marked by either player.
Will also handle clearing/resetting the board by setting all cells back to "-".'''
def create_board():
    global row1, row2, row3, game_board # set to global so these variables can be used outside the function
    row1 = ["-", "-", "-"]
    row2 = ["-", "-", "-"]
    row3 = ["-", "-", "-"]
    game_board = [row1, row2, row3]

'''Print the game board
The main purpose of this function is to print the board after each player's turn, so that the user can see the progress of the game'''
def print_board():
    print(f"{row1}\n{row2}\n{row3}\n")

'''Determine if the user or the computer goes first using the random.choice() function.
The function is taking a list of boolean values as an argument, and randomly selecting one of the values from the list. Based on the result, one of two messages will be printed.'''
def turn_order():
    is_player_turn = random.choice([True, False]) # randomly selected from list of boolean values
    
    if is_player_turn:
        print("Player goes first!")
    else:
        print("Computer goes first!")
    return is_player_turn

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

'''Function for the player's turn
-The player is prompted to enter a position on the game board to place their marker in the row, column format.

-A While True loop is used to ensure the player makes a valid move. The loop will continue until the player chooses makes a valid cell, which is a position on the board that is not already marked.

-The Try block is used to attempt to convert the player's input to integers. If the input is not valid, the except block will execute and the player will be prompted to enter a valid move.

-The row and column variables are initialized as integers, and the player's input is converted to integers using the int() function. The int(position[0] gets the first character from the user's input, which is the row number. The int(position[-1]) gets the last character from the user's input, which is the column number. 1 is subtracted from each of these values to get the correct index.

-If the player enters a position that is already taken (if the cell position is NOT = '-'), the if statement will execute and the player will be prompted to enter a valid move. Otherwise, the break statement will execute and the loop will end. The break is necessary to prevent the loop from continuing if the player enters a valid move.

-The except block will catch any errors that occur when the player enters their move. If the player enters an invalid move, the except block will execute and the player will be prompted to enter a valid move.

-Once a valid move is made, the game_board variable takes the row and column variables (the user's input converted to integers) as arguments, and uses them to access the correct cell on the board. The player's marker is then placed in the cell, and the print_board() function is called to display the updated board.
'''
def player_turn():
    print("Choose a position on the game board to place your marker in the format 'row, column'.")
    print("For example, if you want to place your marker in the top left corner, type '1, 1' to represent the first row and first column.\n")
    
    while True:
        position = input("Enter your move: ")
        try:
            row = int(position[0]) - 1
            column = int(position[-1]) - 1
            
            if game_board[row][column] != "-":
                print("That position is already taken. Please choose another position.")
            else:
                break
        except (IndexError, ValueError):
            print("Invalid input. Please enter your move in the format 'row,column'.") 
                
    game_board[row][column] = player_mark
    print_board()
        
# Function for the computer's turn   
def computer_turn():
    print("Computer is comtemplating its move...")
    time.sleep(1.5)
    
    # Choose a random row and column for the computer
    row = random.randint(0, 2)
    column = random.randint(0, 2)
    
    # Check if the computer's move is valid
    while game_board[row][column] != "-":
        
    # If the move is not valid, choose a new random row and column
        row = random.randint(0, 2)
        column = random.randint(0, 2)
    
    # Display the computer's move
    print(f"Computer places {computer_mark} on row {row+1}, column {column+1}.\n")    
    # Place computer's marker on the game board and print the board
    game_board[row][column] = computer_mark
    print_board()
    
# Function to determine if the game is over.
# Checks if any of the rows, columns, or diagonals are filled with the same marker. 
def win_check(mark):
    # win_detected = False
    
    # Check horizontal rows
    if (game_board[0][0] == mark and game_board[0][1] == mark and game_board[0][2] == mark) or \
        (game_board[1][0] == mark and game_board[1][1] == mark and game_board[1][2] == mark) or \
        (game_board[2][0] == mark and game_board[2][1] == mark and game_board[2][2] == mark):
        return True
        # print(f"Player ({mark}) wins!")
        # win_detected = True
        
    # Check vertical columns 
    if (game_board[0][0] == mark and game_board[1][0] == mark and game_board[2][0] == mark) or \
        (game_board[0][1] == mark and game_board[1][1] == mark and game_board[2][1] == mark) or \
        (game_board[0][2] == mark and game_board[1][2] == mark and game_board[2][2] == mark):
        return True
        # print(f"Player ({mark}) wins!")
        # win_detected = True
        
    # Check diagonals
    if (game_board[0][0] == mark and game_board[1][1] == mark and game_board[2][2] == mark) or \
        (game_board[0][2] == mark and game_board[1][1] == mark and game_board[2][0] == mark):
        return True
        # print(f"Player ({mark}) wins!")
        # win_detected = True
        
    return False 

# Function to determine if the game is a draw
def draw_check():
    draw_detected = False
    if "-" not in game_board[0] and "-" not in game_board[1] and "-" not in game_board[2]:
        print("The game is a draw.")
        draw_detected = True
    return draw_detected

# Main game loop
def game_loop():
    global player_mark, computer_mark
    
    # Assign player and computer markers
    player_mark = "X"
    computer_mark = "O"
    
    print("Rolling to see who goes first...\n")
    time.sleep(2) # 2 second delay
    is_player_turn = turn_order()
    print(f"Player is {player_mark} and computer is {computer_mark}.\n")
    
    while True:
        # If player goes first
        if is_player_turn:
            player_turn()
            
            # Check if player has won  
            if win_check(player_mark): 
                print(f"Player ({player_mark}) wins!")
                break
            
            # Check if game is a draw
            elif draw_check(): 
                print("The game is a draw.")
                break
            
            # Computer's turn
            computer_turn()
            if win_check(computer_mark):
                print(f"Computer ({computer_mark}) wins :(")
                break
            elif draw_check():
                print("The game is a draw.")
                break
            
        # If computer goes first
        else:
            computer_turn()
            
            # Check if computer has won
            if win_check(computer_mark):
                print(f"Computer ({computer_mark}) wins :(")
                break
            
            # Check if game is a draw
            elif draw_check():
                print("The game is a draw.")
                break
            
            player_turn()
            if win_check(player_mark):
                print(f"Player ({player_mark}) wins!")
                break
            elif draw_check():
                print("The game is a draw.")
                break
                  
# Welcome message and game start
print("Welcome to TicTacToe!")
print("The game board is a 3x3 grid. Each player takes turns placing their marker on the board.")
print("The first player to get three of their markers in a row (horizontally, vertically, or diagonally) wins.")
print("If neither player can get three in a row, the game is a draw.\n")
print("Let's begin!\n")

while True:
    create_board()
    game_loop()
    print_board()
    
    # Ask the player if they want to play again
    # If yes, reset the game board. If no, thank the player and end the game.
    play_again = input("Do you want to play again? Y/N: ").upper()
    if play_again != "Y":
        break















    










