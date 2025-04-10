#!/usr/bin/env python3

from stats import get_num_words, num_characters, pretty_printing	
import sys

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)
	
path_to_book = sys.argv[1]

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

def main():
	filepath = path_to_book
	text = get_book_text(filepath)
	word_count = get_num_words(text)
	char_counts = num_characters(text)
	pretty = pretty_printing(char_counts)
	
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {filepath}...")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")
	
	for char_dict in pretty:
		if char_dict["char"].isalpha():
			print(f"{char_dict['char']}: {char_dict['count']}")
	
	print("============= END ===============")
	
main()