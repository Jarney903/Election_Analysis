## Assign a variable for the file to load and the path.
#file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file.

##Direct Path #1 Method
        #file_to_load = 'Resources/election_results.csv'
        #election_data = open(file_to_load, 'r')
        ## To do: perform analysis.
        ## Close the file.
        #election_data.close()

##Direct Path #2 Method
        #file_to_load = 'Resources/election_results.csv'
        #with open(file_to_load) as election_data:
        ## To do: perform analysis.
            #print(election_data)

##Indirect Path Method
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Print the file object.
     print(election_data)

##Write Data to a File in analysis folder

###Write to file using direct path
# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the open() function with the "w" mode we will write data to the file.
# # Name open fuction file as outfile variable
# outfile = open(file_to_save, "w")
# #Write some Data to the file
# outfile.write("Hellow World")
# # Close the file
# outfile.close()

###Write to file using indirect path
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
    ## \n The newline escape sequence will create a newline, like pressing "return" when it is read. Everything after the \n will be on the next line.
     txt_file.write("Counties in the Election\n")
     txt_file.write("-------------------------\n")
     txt_file.write("Arapahoe\n")
     txt_file.write("Denver\n")
     txt_file.write("Jefferson\n")



# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of condidates who recieved votes
# 3. The percentage of votes each candodate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

