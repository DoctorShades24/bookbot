#!/usr/bin/env python3

def get_num_words(text):
	words = text.split()
	number_words = len(words)
	return number_words
	
def num_characters(text):
	lower_text = text.lower()
	char_counts = {}
	
	for char in lower_text:
		if char in char_counts:
			char_counts[char] += 1
		else:
			char_counts[char] = 1
	
	return char_counts

def pretty_printing(char_dict):
	chars_list = []
	for char, count in char_dict.items():
		chars_list.append({"char": char, "count": count})
	
	def sort_on(dict_item):
		return dict_item["count"]
	
	chars_list.sort(reverse=True, key=sort_on)
	
	return chars_list