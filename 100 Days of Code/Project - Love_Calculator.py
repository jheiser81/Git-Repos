# The goal is to write a program that tests the compatibility between two people. To work out the love score between two people:
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
# 2. Then check for the number of times the letters in the word LOVE occurs.
# 3. Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is x, you go together like coke and mentos."

# For Love Scores between 40 and 50, the message should be:
# "Your score is y, you are alright together."

# Otherwise, the message will just be their score:
# "Your score is z."

print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ") 
name2 = input("What is their name? ")
combined_names = name1.lower() + name2.lower()
# combine the two name variables into a single variable, use the .lower() function to equalize the strings
true_count = combined_names.count("t") + combined_names.count("r") + combined_names.count("u") + combined_names.count("e")
love_count = combined_names.count("l") + combined_names.count("o") + combined_names.count("v") + combined_names.count("e")
# use the .count() function with the letters t, r, u, e and l,o,v,e as arguments to count the occurrences of each letter in the combined variable 
love_score = str(true_count) + str(love_count) 
# convert the int values to strings and concatenate them
love_score = int(love_score)    
# convert the concatenated string back to an int to get a 2 digit number for the score

if love_score < 10 or love_score > 90: 
    # use the < and > operators to check if the love_score is less than 10 or greater than 90, print message
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    # use the >= and <= operators to check if the love_score is between 40 and 50, print message
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
    # otherwise, just print the score
