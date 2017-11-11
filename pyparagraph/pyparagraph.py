#Import a text file filled with a paragraph of your choosing.

# Store the file path associated with the file 
paragraph_1 = 'raw_data/paragraph_1.txt'

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(paragraph_1, 'r') as text_1:

	print(text_1)

	# Store all of the text inside a variable called "lines"
	lines_1 = text_1.read()
	# Print the contents of the text file
	print(lines_1)


#Assess the passage for each of the following:

	#Approximate word count
	words = lines_1.split(" ")

	print ("Approximate word count:") 
	print(len(words))

#Approximate sentence count
	sentence = lines_1.split(".")

	print ("Approximate sentence count:") 
	print(len(sentence))
	
	#Approximate letter count (per word)
	print ("Approximate letter count (per word):") 

	#Average sentence length (in words)
	print ("Approximate sentence length (in words):") 

