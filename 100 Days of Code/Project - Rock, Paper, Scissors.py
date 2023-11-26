import random

def get_choices():
    player_choice = input("Choose rock, paper, or scissors: ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    game_choices = {"player": player_choice, "computer": computer_choice}
    return game_choices

player_wins = 0
computer_wins = 0
rounds = 0

while rounds < 3:
    rounds += 1     
    round_result = get_choices()
    if round_result["player"] == "rock" and round_result["computer"] == "scissors" or round_result["player"] == "paper" and round_result["computer"] == "rock" or round_result["player"] == "scissors" and round_result["computer"] == "paper":
        player_wins += 1
        print(f"Round Result: {round_result}\n Player wins this round.")
    elif round_result["player"] == "rock" and round_result["computer"] == "paper" or round_result["player"] == "paper" and round_result["computer"] == "scissors" or round_result["player"] == "scissors" and round_result["computer"] == "rock":
        computer_wins += 1
        print(f"Round result: {round_result}\n Computer wins this round.")
    else:
        print(f"Round Result: {round_result}\n Round is a draw.")
        
# If it's a tie after 3 rounds, play a tiebreaker round.
if player_wins == computer_wins:
    print("The game is a tie after 3 rounds. Playing a tiebreaker round.")
    round_choice = get_choices()
    if round_choice["player"] == "rock" and round_choice["computer"] == "scissors" or round_choice["player"] == "paper" and round_choice["computer"] == "rock" or round_choice["player"] == "scissors" and round_choice["computer"] == "paper":
        player_wins += 1
        print(f"Round Result: {round_choice}\n Player wins this round.")
    elif round_choice["player"] == "rock" and round_choice["computer"] == "paper" or round_choice["player"] == "paper" and round_choice["computer"] == "scissors" or round_choice["player"] == "scissors" and round_choice["computer"] == "rock":
        computer_wins += 1
        print(f"Round result: {round_choice}\n Computer wins this round.")

if player_wins > computer_wins:
    print(f"Final score: Player: {player_wins} Computer: {computer_wins}")
    print("Player wins the game!")
elif computer_wins > player_wins:
    print(f"Final score: Player: {player_wins} Computer: {computer_wins}")
    print("The computer won the game.")
else:
    print(f"Final score: Player: {player_wins} / Computer: {computer_wins}")
    print("The game was a draw.")
    
# This code works, but remember DRY: Don't Repeat Yourself.
# I should refactor this code to make it more efficient by eliminating repetition.

# Refactored code:

import random 

def get_choices():
    player_choice = input("Choose rock, paper, or scissors: ").lower()
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    game_choices = {"player": player_choice, "computer": computer_choice} 
    return game_choices

# Place the logic for determining the winner in a function, so that I can just call the function and avoid repeating code
def round_winner_check(round_choice):
    if round_choice["player"] == "rock" and round_choice["computer"] == "scissors" or round_choice["player"] == "paper" and round_choice["computer"] == "rock" or round_choice["player"] == "scissors" and round_choice["computer"] == "paper":
        return "player" # This will return the value of "player" to the variable winner, which is then used in the if/elif/else statements below 
    elif round_choice["player"] == "rock" and round_choice["computer"] == "paper" or round_choice["player"] == "paper" and round_choice["computer"] == "scissors" or round_choice["player"] == "scissors" and round_choice["computer"] == "rock":
        return "computer" # This will return the value of "computer" to the variable winner
    else:
        return "draw" 

# Create counter variables for player wins, computer wins, and rounds played  
player_wins = 0
computer_wins = 0
rounds = 0

# Create a while loop that will run for 3 rounds, and increment the rounds variable by 1 each time the loop runs
# If the player wins, increment the player_wins variable by 1, if the computer wins, increment the computer_wins variable by 1. Else, round is a draw.
while rounds < 3:
    rounds += 1
    round_result = get_choices() # Call the get_choices function and store the result in the variable round_result
    winner = round_winner_check(round_result) # Call the round_winner_check function and store the result in the variable winner
    if winner == "player":
        player_wins += 1 # Increment the player_wins variable by 1 if the player wins
        print(f"Round Result: {round_result}\nPlayer wins this round.\n")
    elif winner == "computer":
        computer_wins += 1 # Increment the computer_wins variable by 1 if the computer wins
        print(f"Round result: {round_result}\nComputer wins this round.\n")
    else: # If the round is a draw, print the round result and a message saying the round is a draw
        print(f"Round Result: {round_result}\nRound is a draw.\n")
        
# While loop to play a tiebreaker round if the game is a tie after 3 rounds. 
# This will run until the player or computer wins the tiebreaker round.
while player_wins == computer_wins:
    print("The game is a tie after 3 rounds. Playing a tiebreaker round.\n")
    tiebreaker = get_choices() # Call the get_choices function and store the result in the variable tiebreaker
    winner = round_winner_check(tiebreaker) # Call the round_winner_check function and store the result in the variable winner
    if winner == "player":
        player_wins += 1 # Increment the player_wins variable by 1 if the player wins
        print(f"Round Result: {tiebreaker}\nPlayer wins this round.\n")
    elif winner == "computer":
        computer_wins += 1 # Increment the computer_wins variable by 1 if the computer wins
        print(f"Round result: {tiebreaker}\nComputer wins this round.\n")
        
if player_wins > computer_wins:
    print(f"Final score: Player: {player_wins} Computer: {computer_wins}")
    print("Player wins the game!")
elif computer_wins > player_wins:
    print(f"Final score: Player: {player_wins} / Computer: {computer_wins}")
    print("The computer won the game.\n")
    





