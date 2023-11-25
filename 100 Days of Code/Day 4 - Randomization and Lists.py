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


# random.choice(list) - returns a random item from the list specified, such as a random item from a list of colors: red, blue, green

random_color = random.choice(["red", "blue", "green"])
print(random_color)
# Step 1: Create a variable to store the random item in
# Step 2: Call the random.choice function, and pass in the list as a parameter
# Step 3: Print the variable to the console

# random.shuffle(list) - shuffles the list specified, such as shuffling a deck of cards

# There are many other random functions. Documentatinon can be found at: https://askpython.com/python-modules/python-random-module-generate-random-numbers-sequences/

# ================================================
# Python Modules
# ================================================

# Python modules are files that contain a set of functions that can be used in other Python files. They are used to organize code, and to make it more reusable. They are also used to avoid name collisions, which is when two functions have the same name.
# Modules can be built-in, such as the random module, or they can be user-defined, such as the Example_module.py file in this folder.

print(Example_module.pi)
# This will call the pi variable from the Example_module.py file, and print it to the console.