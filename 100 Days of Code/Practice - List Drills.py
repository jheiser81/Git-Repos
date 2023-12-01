# ================================================
# List Creation and Access
# ================================================

# Create a list of numbers or strings. Print the first, middle, and last items from the list.

# Steps:
# 1. Declare variable and create list
# 2. Make variables for the first, middle, and last items from the list, using the index positions to access the correct items
# 3. Using the same variable name as the original list, reassign the values of the list to the new variables. This will create a new list from the specified items
# 4. Print the new list using f-strings

list_of_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
_1st_num = list_of_nums[0]
mid_num = list_of_nums[4]
last_num = list_of_nums[-1]
list_of_nums = [_1st_num, mid_num, last_num]
print(f"1st num: {_1st_num}\nMiddle num: {mid_num}\nLast num: {last_num}\n")

list_of_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
_1st_day = list_of_days[0]
mid_day = list_of_days[2]
last_day = list_of_days[-1]
list_of_days = [_1st_day, mid_day, last_day]
print(f"First day: {_1st_day}\nMiddle day: {mid_day}\nLast day: {last_day}\n")

GGK_books = ["Tigana", "Lions of Al-Rassan", "Under Heaven", "The Last Light of the Sun", "River of Stars", "A Brightness Long Ago", "All the Seas of the World"]
first_book = GGK_books[0]
middle_book = GGK_books[3]
last_book = GGK_books[-1]
GGK_books = [first_book, middle_book, last_book]
print(f"First Book: {GGK_books[0]}\nMiddle Book: {GGK_books[1]}\nLast Book: {GGK_books[2]}\n")

# ================================================
# List Modificiation
# ================================================

# Create a new list. Add a new item to the end of the list, then replace the first item in the list with a new item. Print the updated list.

import random
rand_num_list = [random.randrange(1, 101), random.randrange(1, 101), random.randrange(1, 101)]
print(f"Original list: {rand_num_list}")

rand_num_list.append(random.randrange(1, 101))
print(f"Appended list: {rand_num_list}")

rand_num_list[0] = random.randrange(1, 101)
print(f"Final list: {rand_num_list}\n")

# Create a new list. Add a new item to the end of the list. Replace the first item in the list, remove the middle item in the list, and then print the updated list.

animal_list = ["Dogs", "Cats", "Zebras", "Koalas", "Bears"]
print(f"Original List: {animal_list}")

animal_list.append("Capybaras")
print(f"Appended List: {animal_list}")

# using pop() method. pop() removes specified item, and also returns it. pop() is a method so requires (). If no index is specified, it will remove the last item.
animal_list[0] = "Snakes"
removed_item = animal_list.pop(2)
print(f"Removed Item: {removed_item}")
print(f"Updated List: {animal_list}")

# using del, which removes an object and does not return anything. del is a statement, so uses [] 
del animal_list[-2]
print(f"Final List: {animal_list}\n")

# ================================================
# List Length
# ================================================

# Write a function that takes a list as an argument and returns the number of items in the list

import random

rand_num_list = [random.randrange(1, 101), random.randrange(1, 101), random.randrange(1, 101), random.randrange(1, 101), random.randrange(1, 101)]
def list_length(rand_num_list):
    return len(rand_num_list)
print(f"List Numbers: {rand_num_list}")
print(f"Number of items in list: {list_length(rand_num_list)}\n")