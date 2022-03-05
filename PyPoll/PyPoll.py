
# Incorporated the csv module
import csv
import os

# Files to load and output (Remember to change these)
inputfile = os.path.join("../../../Python Resources", "election_data.csv")
outputfile = os.path.join("../../../Python Resources", "election_results_KS.txt")

# Total Vote Counter
total_votes = 0

# Candidate Options and Vote Counters
candidate_options = []
candidate_votes = {}
greatest_votes =["",0]
winning_candidate = ""
winning_count = 0


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(csvreader)

    # For each row...
    for row in csvreader:
        #get the total votes
        total_votes = total_votes + 1
        #create the conditional for adding candidate and votes 
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
             candidate_votes[candidate] = candidate_votes[candidate] + 1

        # Run the loader animation
        print(". ", end=""),

# Print the results and export the data to our text file
with open(outputfile, "w") as txfile"

    # Print the final vote count (to terminal)
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Determine the winner by looping through the counts
    for candidate in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # Print each candidate's voter count and percentage (to terminal)
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # Save each candidate's voter count and percentage to text file
        txt_file.write(voter_output)

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
    txt_file.write("Election results:")
    txt_file.write("\n")
    txt_file.write("--------------------------")
    txt_file.write("\n")
    txt_file.write("Total Votes:" + str(totalVotes))
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    for cv in candidateVotes:
        txt_file.write(cv + ": " + str(round(((candiateVotes[cv]/totalVotes*100),#))) + "&" + "("+ str(candiateVotes[cv] + ")")
        txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Winner is" + str(list(candiateVotes.keys())([list(candidateVotes.value()).index(max(listvotes))]))
    txt_file.write("\n")
    txt_file.write("--------------------------")
                 
    
