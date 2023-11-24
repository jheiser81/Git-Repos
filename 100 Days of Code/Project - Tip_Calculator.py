#If the bill was $150.00, split between 5 people, with a 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = $33.60
#Tip: There are two ways to round a number. 

#Write your code below this line:
print("Welcome to the Tip Calculator.")
bill = float(input("What is the bill total? \n$"))
# This should be a float because bills are usually decimal numbers

tip = int(input("What tip would you like to give? \n"))
# This could be either a float or an int because it's a percentage. I chose int to make it easier to read for the user

people = int(input("How many people are splitting the bill? \n"))
# This should be an int because you can't have a fraction of a person lol

total_with_tip = bill * (1 + (tip / 100))
# This is the total bill with the tip included. The calculation is the bill multiplied by 1 + the tip percentage divided by 100, which gives the decimal value of the tip percentage

print(f"\nThe total bill with tip is: ${round(total_with_tip, 2)}")
 
total_per_person = total_with_tip / people
print(f"The total for each person is: ${round(total_per_person, 2)}\n")
# This is the total bill with tip included, divided by the number of people splitting the bill, rounded to 2 decimal places for user readability

# Using the original exmample numbers will give the correct answers for both the total with tip, and the total per person. However, because we are using the round function, it will display as $168.0 and $33.6, instead of $168.00 and $33.60. This is a formatting issue and not a calculation issue. To fix this, we can use the format function instead of the round function.

total_with_tip = "{:.2f}".format(total_with_tip)
print(f"The total bill with tip is: ${total_with_tip}.")

total_per_person = "{:.2f}".format(total_per_person)
print(f"The total for each person is: ${total_per_person}.\n")

# This will display the correct formatting for the total with tip and the total per person. The drawback is that it's a bit harder to read, and it requires more lines of code. In most cases, using the round function is sufficient, but it's good to know how to use the format function as well.

# Say that I wanted to have a portable version of this code that I could use on my phone. I could upload this project onto a website like Repl.it, and then use the website on my phone to run the code. However, it would be much easier to use an app. I could use an app like Pydroid 3, which is a Python IDE for Android. I could also use an app like Pyto, which is a Python IDE for iOS. I could then copy and paste the code into either app, save the project, and run it on my phone.