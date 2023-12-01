# This is a difficult challenge. You are going to write a program that will mark a spot on a map with an X.
# In the starting code, you will find a variable called map.
# This map contains a nested list. When map is printed this is what the nested list looks like, notice the nesting: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# In the starting code, we have used new lines (\n) to format the three rows into a grid, each on a new line, like this: print(f"{row1}\n{row2}\n{row3}")
# This is to try and simulate the coordinates on a real map.
# Your job is to write a program that allows you to mark a square on a map using a letter-number system:
# 0  A | B | C
# 1 [ ] [ ] [ ]
# 2 [ ] [ ] [ ]
# 3 [ ] [ ] [ ]
# https://cdn.fs.teachablecdn.com/2vnboIYTFFruvl9FJ2w5
# So an input of A3 would mark the bottom left corner with an X.
# First your program must take the user input and convert it to a usable format.
# Next, you need to use it to update your nested list with an "X". 

# Example Input 1: B3

# Example Output 1:
# Hiding your treasure! X marks the spot.
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', 'X',  '⬜️']

# Hints:
# Remember that Lists start at index 0!
# See if this list method helps you: https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list, and this method: https://www.w3schools.com/python/ref_list_index.asp
# Remember that nested lists in python are accessed like this: list_name[row][column]. So if we want to access the 8 in this nested list: [[1, 2, 3], [4, 5, 6], [7, 8, 9]] we would do this: list_name[2][1]

# Solution:

line1 = ["⬜️", "⬜️", "⬜️"]
line2 = ["⬜️", "⬜️", "⬜️"]
line3 = ["⬜️", "⬜️", "⬜️"]
map = [line1, line2, line3] # nested list
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? ")
# Don't change the code above 👆
# Write your code below:
letter = position[0].upper() # extracts the first character of 'position' and converts it to uppercase.
abc = ["A", "B", "C"] # list of letters
letter_index = abc.index(letter) # calls the index() method on the 'abc' list and passes in the 'letter' variable. The index() method returns the index of the first element with the specified value.
number_index = int(position[1]) - 1 # sets 'number_index' to the second character of 'position' and subtracts 1 from it. This is because list indexes start at 0.
map[number_index][letter_index] = "X" # sets both number_index and letter_index to "X" in the 'map' list.
# Write your code above 👆
# Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}") # prints the 'map' list with the modified indexes.

# 1. SETUP THE MAP: 
# -The map is a 3x3 grid represented as a list of lists. Each inner list represents a row on the map. 
# -Initially, all the squares on the map are empty, represented by "⬜️".

#*****************************
# line1 = ["⬜️", "⬜️", "⬜️"]
# line2 = ["⬜️", "⬜️", "⬜️"]
# line3 = ["⬜️", "⬜️", "⬜️"]
# map = [line1, line2, line3] 
#*****************************

# 2. GET USER INPUT: 
# -The user is asked to enter the coordinates of the square where they want to place the treasure. 
# -The coordinates are expected to be in the format "LetterNumber", where the letter represents the column and the number represents the row.

#************************************************************
# position = input("Where do you want to put the treasure? ")
#************************************************************

# 3. PROCESS USER INPUT: 
# -The first character of the user's input is extracted and converted to uppercase. This is the column letter.
# -The second character of the user's input is extracted and converted to an integer, and 1 is subtracted from it (lists starts at 0) to get the row index.

#************************************
# letter = position[0].upper()
# number_index = int(position[1]) - 1
#************************************

# 4. FIND COLUMN INDEX:
# -Sets up a new list that contains the characters A, B, and C.
# -The index of the column letter in the 'abc' list is found using the index() method, stored in the 'letter_index' variable, with 'letter' passed in as an argument.
# This index is used as the colum index in the map list.

#*********************************
# abc = ["A", "B", "C"]
# letter_index = abc.index(letter)
#*********************************

# 5. UPDATE MAP:
# -The square at the given row and column indices in the map list is updated to contain an "X", which represents the treasure.
# -This is done by accessing the list at the given row index, and then accessing the item at the given column index in that list. Both indices are passed in as arguments to the map list, and the "X" is assigned to that item.

# 6. PRINT MAP:
# -The map is printed to the console, showing the location of the treasure.
