### Import Election Results Data
## Using Indirect Method for Referenceing CSV File
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

######################################
### 1. The total number of votes cast

## #1 Initialize a total vote counter
total_votes = 0

## #2.  Declare a new list with candidate names
candidate_options = []

## 3. Declare the empty dictionary to hold candidate votes.
# We are going to create Key = candidate Name  ->  Value = vote counter
candidate_votes = {}

# 5 Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:
    ### To do: read and analyze the data here.
    # Read the file object with the reader function.
    # The variable, file_reader, is referencing the file object, which is stored in memory. 
    file_reader = csv.reader(election_data)

    #Skip the header row in the CSV file.
    #Next goes to next item in the iterator file_reader
    headers = next(file_reader)
    
    #Go through rows in the CSV file 
    for row in file_reader:
        # Add to total vote count
        total_votes +=1
        #####################################
        # 2. A complete list of candidates who recieved votes
        # Look in index 2 -> column 3 for candidate names
        candidate_name = row[2]
        # Only grab unique candidate names
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Begin to track that candidate's vote count
            candidate_votes[candidate_name] = 0 ## we're setting each candidate's vote count to zero. Once we set it to zero, then we can start tallying the votes
        # Back-Indented so it is aligned with For-Loop -> This way it is out of the if statement
        # Add one vote to that candidate's count.
        candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:
        # Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)


        # Determine the percentage of votes for each candidate by looping through the counts.
        # 1. Iterate through the candidate list.
        for candidate_name in candidate_votes:
            # 2. Retrieve vote count of a candidate.
            votes = candidate_votes[candidate_name]
            # 3. Calculate the percentage of votes.
            # Ensure the variables are floating point numbers for division
            vote_percentage = float(votes) / float(total_votes) * 100
            
            # Determine winning vote count and candidate
            # 1. Determine if the votes are greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # 2. If true then set winning_count = votes and winning_percent =
                # vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
                # 3. Set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name

            # votes to the terminal.
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            # Print each candidate, their voter count, and percentage to the terminal.
            print(candidate_results)
            #  Save the candidate results to our text file.
            txt_file.write(candidate_results)

        #Pring the winning candidate summary save as variable to call when writting to textfile
        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
        print(winning_candidate_summary)
        # Save the winning candidate's name to the text file.
        txt_file.write(winning_candidate_summary)




### Print the total votes
#print(total_votes)
#print(candidate_options)
#print(candidate_votes)
#print(f"{candidate_name}: received {vote_percentage: .1f}% of the vote.")
#print(winning_candidate_summary)

# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of condidates who recieved votes
# 3. The percentage of votes each candodate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

### Publish to Git Hub
# Launch the terminal for macOS or GitBash for Windows.
# Navigate to the Election_Analysis folder using the necessary commands.
# Type git status and press Enter.
# Type git add . and press Enter.
# Check the status again with git status and then press Enter.
# Commit the files to be added to the repository by typing git commit -m "Adding the election analysis." and then press Enter.
# Type git push and press Enter to add the file to your repository.
# Refresh your GitHub page to see the repository changes.
