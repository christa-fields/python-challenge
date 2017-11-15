#Import a text file filled with a paragraph of your choosing.
import re 

# Store the file path associated with the file 
paragraph_1 = 'raw_data/paragraph_1.txt'

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(paragraph_1, 'r') as text_1:

	print(text_1)

	# Store all of the text inside a variable called "lines"
	#reades cvs file as string
	lines_1 = text_1.read()
	# Print the contents of the text file
	print(lines_1)


#Assess the passage for each of the following:
	print ("Paragraph Analysis")
	print("---------------------")

	#Approximate word count
	words = lines_1.split(" ")

	print ("Approximate word count:") 
	print(len(words))

	#Approximate sentence count
	sentence = lines_1.split(".")

	print ("Approximate sentence count:") 
	print(len(sentence))
	
	#Approximate letter count (per word)
	letter_count= sum(map(len, words))/ len(words)

	print ("Approximate letter count (per word):") 
	print(letter_count)

	#Average sentence length (in words)
	sentence_count= re.split(r"[/s]+", lines_1)
	print ("Approximate sentence length (in words):") 
	print(len(sentence_count))



	

