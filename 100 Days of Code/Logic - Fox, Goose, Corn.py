# How to cross the river? 
# A farmer with a fox, a goose and a sack of corn need to cross a river. The farmer has a rowboat, but it can only carry him and one other thing. If the fox and the goose are left together, the fox will eat the goose. If the goose and the corn are left together, the goose will eat the corn. 
# How does the farmer get everything across the river safely?

# Key Constraints:
# 1. The farmer can only take one item at a time in the boat.
# 2. The fox and goose cannot be left alone on the same shore.
# 3. The goose and the corn cannot be left alone on the same shore.

# Operations:
# Row the boat from one shore to the other:
# if boat is empty, load item from the shore (fox, goose, corn)
# if boat is not empty, unload item from the boat
# if fox and goose are on the same shore, end program
# if goose and corn are on the same shore, end program

# Solution:
# 1. The starting shore (Shore1) has the farmer, the goose, the fox, and the corn.
# Shore1 [Farmer, Goose, Fox, Corn]
# Boat []

# 2. On the first trip, the farmer takes the goose across the river, leaving the fox and the corn together. The goose is unloaded to Shore2.
# Shore1 -> Boat [Farmer, Goose] -> Shore2
# Shore1 [Fox, Corn]
# Shore2 [Goose]
# Boat [Farmer]

# 3. The farmer returns to Shore1 alone.
# Boat [Farmer] -> Shore1
# Shore1 [Farmer, Fox, Corn]

# 4. The farmer loads the fox onto the boat and takes it across the river. The fox is unloaded to Shore2.
# Shore1 -> Boat [Farmer, Fox] -> Shore2
# Shore1 [Corn]
# Shore2 [Farmer, Goose, Fox]

# 5. The goose is loaded back onto the boat, and the farmer and goose head back to Shore1.
# Shore2 -> Boat [Farmer, Goose] -> Shore1
# Shore2 [Fox]
# Shore1 [Farmer, Goose, Corn]

# 6. The farmer unloads the goose onto Shore1, and loads the corn onto the boat. The farmer then takes the corn across the river and unloads it onto Shore2 with the fox.
# Boat [Farmer, Goose] -> Shore1
# Shore1 [Farmer, Goose, Corn]
# Boat [Farmer, Corn] -> Shore2
# Shore2 [Fox, Corn]

# 7. The farmer returns to Shore1 alone, and loads the goose onto the boat. The farmer takes the goose across the river and unloads it onto Shore2. Now all items are on Shore2.
# Shore1 -> Boat [Farmer, Goose] -> Shore2
# Shore1 []
# Shore2 [Farmer, Goose, Fox, Corn]


