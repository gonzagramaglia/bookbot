import sys

if len(sys.argv) > 1:
	arg = sys.argv[1]
else: 
	arg = False

with open('books/frankenstein.txt') as f:
	

	file_contents = f.read()
	words_list = file_contents.split()
	words_count = len(words_list)
	print(f"The file contains {words_count} words")
	
	letters = {}	
	for word in words_list:
		lowered_word = word.lower()
		for letter in lowered_word:
			if letter.isalpha():
				if letter in letters:
					letters[letter] += 1
				else:
					letters[letter] = 1
	
	if arg:
		for letter in letters:
			if letter == arg:
				print(f"The '{letter}' character was found {letters[letter]} times")
	else:
		print("Argument is missing. Please add a character to count")
	


		
