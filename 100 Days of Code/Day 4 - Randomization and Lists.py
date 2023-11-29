import random
import Example_module

# ================================================
# Random Number Generation
# ================================================

# In order to perform many functions in programming, it is necessary to introduce a randomization element. This is done through the random module in Python, which is a built-in module that can be imported into your code. This is done by adding the line 'import random' to the top of your code page.

# There are many functions that can be used with the random module. The most common ones are:

# **random.randint(range)** - returns a random integer between the range specified, such as between 1 - 10

random_integer = random.randint(1, 10) 
print(random_integer) 
# Step 1: Create a variable to store the random integer in
# Step 2: Call the random.randint function, and pass in the range as a parameter. The range is separated by a comma.
# Step 3: Print the variable to the console

random_float = random.random() * 5
print(random_float)
# This will return a random float between 0 and 1, and then multiply it by 5. 

# **random.choice(list)** - returns a random item from the list specified, such as a random item from a list of colors: red, blue, green

random_color = random.choice(["red", "blue", "green"])
print(random_color)
# Step 1: Create a variable to store the random item in
# Step 2: Call the random.choice function, and pass in the list as a parameter
# Step 3: Print the variable to the console

# **random.shuffle(list)** - shuffles the list specified, such as shuffling a deck of cards

# There are many other random functions. Documentatinon can be found at: https://askpython.com/python-modules/python-random-module-generate-random-numbers-sequences/

# ================================================
# Python Modules
# ================================================

# Python modules are files that contain a set of functions that can be used in other Python files. They are used to organize code, and to make it more reusable. They are also used to avoid name collisions, which is when two functions have the same name.
# Modules can be built-in, such as the random module, or they can be user-defined, such as the Example_module.py file in this folder.

print(Example_module.pi)
# This will call the pi variable from the Example_module.py file, and print it to the console.

# ================================================
# Lists
# ================================================

# Lists, also known as arrays in other programming languages, are a data structure that can be used to store multiple values in a single variable. This is very useful anytime you are working with a range of values, such as a list of names, or a range of numbers. 
# List values usually have some kind of relationship to one another, which is why they are grouped.
# Lists are created using square brackets, and each item in the list is separated by a comma. Lists can contain any data type, mixed data types, or even other lists.
 
my_list = ["item1", "item2", "item3"]
num_list = [1, 2, 3]

# Lists are indexed, which means that each item in the list has a position. The first item in the list is at position 0, the second item is at position 1, and so on.
# When you want to access a particular item in a list, you can use the index position, such as my_list[0]. This will return the first item in the list.

print(my_list[0])
print(num_list[2])

# Unlike some other programming languages, lists in Python are mutable, which means that you can change the items in the list after it has been created. In other programming languages, lists (arrays) cannot be changed after they are created.

num_list = [4, 5, 6] # This changes the values in the list from 1, 2, 3 to 4, 5, 6

# You can also change a specific item in the list by using the index position

num_list[0] = 1 # This will change the first item in the list from 4 to 1

# You can also add items to a list using the append() function, which adds the item to the end of the list. This does no affect the other items in the list.

num_list.append(7) # this will add the number 7 to the end of the list

# Values can also be removed from a list using the remove() function, which removes the first instance of the value specified.

num_list.remove(7) # This will remove the number 7 from the list

# Another way to add an item to the end of a list is to use the += operator, which adds the item to the end of the list. This does not affect the other items in the list.

num_list += [8] # This will add the number 8 to the end of the list

# To add an item to a specific position in the list, use the insert() function, which takes two parameters: the index position, and the value to be inserted.

num_list.insert(0, 0) # This will insert the number 0 at index position 0, which will move the other items in the list down one position

# To remove an item from a specific position in the list, use the pop() function, which only needs the index position as a parameter.

num_list.pop(0) # This will remove the item at index position 0

# There are many other functions that be used with lists, and it is not necessary to memorize them all. Documentation can be found at: https://docs.python.org/3/tutorial/datastructures.html

# ================================================
# Index Errors
# ================================================

# Index errors are a common error that occurs when you try to access an item in a list at an index position that does not exist. This most often occurs in the form of an off-by-one error, which is when you try to access an item at an index position that is one more than the number of items in the list.
# For example, if you have a list with 3 items, and you try to access the item at index position 3, you will get an index error, because the last index position in a list is always 1 less than the number of items in the list. This is because the first index position in a list is always 0.

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

num_of_states = len(states_of_america) # This will return the number of items in the list, which is 50

print(states_of_america[50]) # This will return an index error, because there is no item at index position 50, since the index starts at 0 and ends at 49.

print(states_of_america[num_of_states]) # This will also return an index error, because the num_of_states variable is equal to 50, which is one more than the last index position in the list.

print(states_of_america[num_of_states - 1])
# This will correctly return the last item in the list, because the num_of_states variable is equal to 50, and the last index position in the list is 49, so subtracting 1 from the num_of_states variable will return the last item in the list.