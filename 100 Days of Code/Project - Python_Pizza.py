# Congratualations, you've got a job at Python Pizza. Your first task is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25\
# Add pepperoni for Small Pizza (Y/N): +$2
# Add pepperoni for Medium or Large Pizza (Y/N): +$3

# Example input: L, Y, N
# Example output: "Your final bill is: $28."

print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L? ").upper() 
add_pepperoni = input("Do you want to add pepperoni to your pizza? Y/N: ").upper() 
extra_cheese = input("Do you want to add extra cheese? Y/N: ").upper() 
bill = 0
if size == "S":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            