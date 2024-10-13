import re

def remove_citations(text):
    return re.sub(r'\[\d+\]', '', text)  # Example pattern for square bracketed citations




def get_text_input():
    return input("Enter the text to clean: ")