### Show Zeb this - 3.4


#The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Import the datetime class from the datetime module.
#import datetime
# Use the now() attribute on the datetime class to get the present time.
        #now = datetime.datetime.now()
    #now = dt.datetime.now()
# Print the present time.
#print("The time right now is ", now)

#file_variable = open('election_results.csv', 'r')

#with open('election_results.csv') as election_data:

#    print(election_data)

#file_variable.close()

#import csv
#import os
# Assign a variable for the file to load and the path.
#file_to_load = os.path.join("election_results.csv")
# Open the election results and read the file.
#with open(file_to_load) as election_data:

    # Print the file object.
     #print(election_data)

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("c:/Users/ccoelho/Desktop/Data Bootcamp/Module 3_pyPoll/analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("election_analysis.txt")

# Using the with statement open the file as a text file.
#outfile = open(file_to_save, "w")
# Write some data to the file.
#outfile.write("Arapahoe, ")
#outfile.write("Denver, ")
#outfile.write("Jefferson")

#outfile.write("Counties in the Election\n----------------------\nArapahoe\nDenver\nJefferson")

# Close the file
#outfile.close()

#adding dependencies
#import csv
#import os

#assigning a variable to load a file from a path
#file_to_load = os.path.join("election_results.csv")

#assigning a variable to save the file to a path
#file_to_save = os.path.join('election_analysis.txt')

#open the election results and read the file
#with open(file_to_load) as election_data:

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("election_analysis1.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

# Print each row in the CSV file.
  #  for row in file_reader:
   #     print(row)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)