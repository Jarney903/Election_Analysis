# Count Fruit Votes
## Using Indirect Method for Referenceing CSV File
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Python Practice", "Resources", "fruit_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Python Practice", "fruit_analysis", "fruit_analysis.txt")

total_votes = 0
fruit_list = [] #Find List of unique Friut
fruit_dict = {} #Add unique fruit as dict keys, total votes as values
winning_fruit = "" #Add winning fruid string
winning_votes = 0 #Add winning vote integer - will change to float later
winning_pct = 0 #Add winning vote percent integer - will change to float later 


#Make sure the correct file is open
with open(file_to_load) as fruit_data:
    # Read the file object with the reader function.
    fruit_reader = csv.reader(fruit_data)

    #Skip the header row in the CSV file.
    skip_headers = next(fruit_reader)

    #For-Loop #1 - Read through file rows assign fruit to list and fruit and votes to dictionary also count total votes
    for filerow in fruit_reader: #This is just: for Row in CSV File
        #Count rows as individual votes
        total_votes += 1
        #Grab Fruit Names in Collumn B
        fruit_name = filerow[1]
        #IF this is Unique add it to Fruit List and set votes to zero
        if fruit_name not in fruit_list:
            #Add unique fruit to list
            fruit_list.append(fruit_name)
            #Add list to dictionary and set first unique fruit to zero votes
            fruit_dict[fruit_name] = 0
        # Add one vote for each row we loop through as the value in the dictionary
        fruit_dict[fruit_name] +=1

    #For-Loop #2 - Find individual fruit votes and individual fuit vote %
    for fruit_name in fruit_dict: #This is just: for KEY in Dictionary
        votes = fruit_dict[fruit_name] #Grab dict_value by referencing dict_key
        vote_pct = float(votes) / float(total_votes) * 100 #Do basic math

        #Now the tricky part -> This IF is doing 2 things
        #Thing #1 -> Are votes and vote_pct > than winning_votes and winning_pct?
        if (votes > winning_votes) and (vote_pct > winning_pct):
        #Thing #2 -> Assign this first fruit's votes and vote_pct to winning_votes and winning_pct
        #Thing #2 works because as we iterate through the loop, the winning_votes and winning_pct will not be Zero anymore
            winning_votes = votes
            winning_pct = vote_pct
            winning_fruit = fruit_name

        # Print this.
        fruit_results = (f"{fruit_name}: {vote_pct:.1f}% ({votes:,})\n")
        #Try it both ways
        fruit_results_Winner = (f"{winning_fruit}: {winning_pct:.1f}% ({winning_votes:,})\n")

#print(fruit_results)
#print(fruit_results_Winner)

#Make it Fancy
winning_fruit_summary = (
        f"-------------------------\n"
        f"Winner: {winning_fruit}\n"
        f"Winning Vote Count: {winning_votes:,}\n"
        f"Of a total of: {total_votes:,} votes \n"
        f"Winning Percentage: {winning_pct:.1f}%\n"
        f"-------------------------\n")
print(winning_fruit_summary)
        # Save the winning candidate's name to the text file.

#Print Check
#print(total_votes)
#print(fruit_list)
#print(fruit_dict)