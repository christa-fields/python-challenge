# Modules
import os
import csv

# Set path for cvs files
budget_data_1 = os.path.join("raw_data", "budget_data_1.csv")

# Open the CSV
	# CSV reader specifies delimiter and variable that holds contents
	
with open(budget_data_1, newline="") as csvfile_1:
	csvreader= csv.reader(csvfile_1, delimiter=",")

	print(csvreader)

	total_revenue = 0
	i = 0
	
	#  Each row is read as a row
	for row in csvreader:
		
		#print(row[0])

		if i > 0: #The total amount of revenue gained over the entire period
			total_revenue += int(row[1])
		i+= 1

	print(total_revenue)
		#print(row[1])


#The total number of months included in the dataset
    # Loop through looking for the video
		#for row in csvreader:
			#if row[0] == date:


#The average change in revenue between months over the entire period

#The greatest increase in revenue (date and amount) over the entire period

#The greatest decrease in revenue (date and amount) over the entire period