# 1. Create a greeting for your program.
# 2. Ask the user for the city that they grew up in.
# 3. Ask the user for the name of a pet.
# 4. Combine the name of their city and pet and show them their band name.

print("Welcome to the Band Name Generator.")
city = input("What's the name of the city or town you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + city + " " + pet)
# This uses normal string concatenation to print the band name

print("Welcome to the Band Name Generator.")
city = input("What's the name of the city or town you grew up in?\n")
pet = input("What's your pet's name?\n")
print(f"Your band name could be {city} {pet}")
# This uses f-strings to print the band name. f-strings can make code more readable and easier to debug, since it cuts down on the amount of characters you have to type, which reduces the chances of making an error.
