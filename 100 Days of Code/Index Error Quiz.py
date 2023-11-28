# # Given the following list:
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# # Which line of code will give you "Apples" as the output?

# # Answer:
# print(fruits[-5])
# # This is a negative offset, which starts from the end of the list instead of the beginning. Accordingly, the order would be -1, -2, -3 etc, since lists always start at index position 0

# # Given the code below:
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# fruits[-1] = "Melons"
# fruits.append("Lemons")
# print(fruits)
# # What do you think will be printed?
# # Answer:
# # ['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Melons', 'Lemons']
# # This is because the negative offset -1 refers to the last item in the list, which is "Pears". The code then replaces "Pears" with "Melons", and then appends "Lemons" to the end of the list, which is why "Melons" is printed before "Lemons". Code is always executed in a hierarchical order, so the code is executed from top to bottom.

# Given the code below:
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])
# What do you think will be printed?    
# Answer:
# "Kale"
# The first index position refers to the fruits list, and the second index position refers to the vegetables list. The item at the second position (index position 1) in the vegetables list is "Kale".
# Breakdown:
# print(dirty_dozen) would print the full nested list, which contains both the fruits and vegetables lists
# print(dirty_dozen[0] would print the first item in the nested list, which is the fruits list)
# print(dirty_dozen[1] would print the second item in the nested list, which is the vegetables list)
# print(dirty_dozen[0][1]) would print the second item in the fruits list, which is "Nectarines"
# print(dirty_dozen[1][1]) would print the second item in the vegetables list, which is "Kale"