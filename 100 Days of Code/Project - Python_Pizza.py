# Congratualations, you've got a job at Python Pizza. Your first task is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25\
# Add pepperoni for Small Pizza (Y/N): +$2
# Add pepperoni for Medium or Large Pizza (Y/N): +$3
# Add extra cheese to any size pizza (Y/N): +$1

# Example input: L, Y, N
# Example output: "Your final bill is: $28."

print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L? ")
add_pepperoni = input("Do you want to add pepperoni to your pizza? Y/N: ")
extra_cheese = input("Do you want to add extra cheese? Y/N: ")
bill = 0

if size == "S" or size == "s":
    bill = 15
    if add_pepperoni == "Y" or add_pepperoni == "y":
        bill += 2
elif size == "M" or size == "m":
    bill = 20
    if add_pepperoni == "Y" or add_pepperoni == "y":
        bill += 3
elif size == "L" or size == "l":
    bill = 25
    if add_pepperoni == "Y" or add_pepperoni == "y":
        bill += 3
else:
    print("Invalid input. Please choose between S, M, or L.")
    bill = "Invalid"
    
if bill != "Invalid":
    if extra_cheese == "Y" or extra_cheese == "y":
        bill += 1
    print(f"Your final bill is ${bill}.")
    
code_attempt = input("Is your code working? Enter Working or Not working: ")
if code_attempt == "Working":
    print("Yay! Your code is working!")
    answer = input("Do you want to try a different approach? Y or N: ")
    if answer == "Y":
        print("Great! Try something new.")
    elif answer == "N":
        print("Okay, good job!")
elif code_attempt == "Not working":
    print("If at first you don't succeed...keep trying!")
    answer = input("Do you want to try a different approach? Y or N: ")
    if answer == "Y":
        print("Great! Keep trying!")
    else:
        print("Don't be discouraged. Come back to it later.")
        print("Remember that learning is incremental, that it takes time, and that the process is not linear.")
else:
    print("Invalid input. Please enter Working or Not working.")

        