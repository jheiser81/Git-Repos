# 1) List Creation and Access 
# Create a list of your favorite books. Print the first, middle, and last book from the list.
GGK_books = ["Tigana", "Lions of Al-Rassan", "Under Heaven", "The Last Light of the Sun", "River of Stars", "A Brightness Long Ago", "All the Seas of the World"]
first_book = GGK_books[0]
middle_book = GGK_books[3]
last_book = GGK_books[-1]
GGK_books = [first_book, middle_book, last_book]
print(f"First Book: {GGK_books[0]}\nMiddle Book: {GGK_books[1]}\nLast Book: {GGK_books[2]}")
    
# 2) List Modification 
# Add a new book to the end of the list. Now, replace the first book in the list with another book. Print the updated list.
GGK_books.append("Sailing to Sarantium")
GGK_books[0] = "The Summer Tree"
print(GGK_books)

# 3) List Length 
# Write a function that takes a list as an argument and returns the number of items in the list.
def list_length(new_list):
    return len(new_list)
print(list_length(["item1", "item2", "item3"]))

# 4) Nested Lists 
# Create a nested list where the first list contains your favorite movies, and the second list contains your favorite TV shows. Print the first movie and the last TV show.
fav_movies = ["La La Land", "Get Out", "Avengers: Endgame", "Parasite", "Dune Pt. 1"]
fav_shows = ["Wandavision", "Lucifer", "The Sandman", "Stranger Things", "Bodies"]
fav_media = [fav_movies, fav_shows]
print(f"First Movie: {fav_media[0][0]}\nLast Tv Show: {fav_media[1][-1]}")

# 5) Random Selection 
# Without using the choice() function, write a program that selects a random book from your list of favorite books and prints it.
import random

book_index = random.randrange(len(GGK_books))
rand_book = GGK_books[book_index]
print(f"The randomly selected GGK book is: {rand_book}")

# 6) List Slicing 
# Create a list of numbers from 1 to 10. Use slicing to print the first half and the second half of the list separately.
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first_half_list = num_list[:5]
second_half_list = num_list[5:]
print(f"First Half: {first_half_list}\nSecond Half: {second_half_list}")
# I had to look up list slicing, since I didn't know about it. The start position comes after a colon, and the end position comes after a second colon
letter_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
first_half = letter_list[:4]
second_half = letter_list[4:]
print(f"First half: {first_half}\nSecond Half: {second_half}")
# 7) List Comprehension 
# Use list comprehension to create a list of squares for numbers from 1 to 10.

# 8) Removing Items 
# Create a list of numbers from 1 to 5. Write a function that takes a number as an argument, removes that number from the list if it's present, and returns the updated list.

# 9) List Iteration 
# Write a function that takes a list of numbers as an argument and returns the sum of all the numbers in the list.

# 10) Sorting and Reversing 
# Create a list of numbers in random order. Sort the list in ascending order and print it. Then reverse the list and print it.