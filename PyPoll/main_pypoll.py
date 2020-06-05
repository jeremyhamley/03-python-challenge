# This python script is designed for elctions with Four candidates.
# For elections with a number of candidates that is not Four, the script will need to be updated.
# For example: To add a fifth candidate- add the following variables:
#      example add:  cand5 = candidates[4] , cand5_count = 0 , cand5_percentage = round((cand5_count * 100)/ len(voter_count),3)

# import modules: os , csv
import os
import csv
#define the path to access the csv file with raw data
csvpath = os.path.join("Resources-PyPoll", "election_data.csv")

#create empty lists: voter count , candidates
voter_count = 0
candidates = []

#open and read data in csv file
with open(csvpath,'r') as election_data:
    read_election_data = csv.reader(election_data, delimiter = ',')
    #read header
    election_header = next(read_election_data)

    #read election data to collect candidates and total votes
    for vote in read_election_data:
        voter_count += 1
        if vote[2] not in candidates:
            candidates.append(vote[2])
    #assign candidates to variables and set vote count to zero
    cand1 = candidates[0]
    cand1_count = 0
    cand2 = candidates[1]
    cand2_count = 0
    cand3 = candidates[2]
    cand3_count = 0
    cand4 = candidates[3]
    cand4_count = 0

with open(csvpath,'r') as election_data:
    read_election_data = csv.reader(election_data, delimiter = ',')
    #read header
    election_header = next(read_election_data)    
    
    for choice in read_election_data:
        if choice[2] == cand1:
            cand1_count += 1
        elif choice[2] == cand2:
            cand2_count += 1
        elif choice[2] == cand3:
            cand3_count += 1
        elif choice[2] == cand4:
            cand4_count += 1

cand1_percentage = round((cand1_count * 100)/ (voter_count),3)
cand2_percentage = round((cand2_count * 100)/ (voter_count),3)
cand3_percentage = round((cand3_count * 100)/ (voter_count),3)
cand4_percentage = round((cand4_count * 100)/ (voter_count),3)

if cand1_percentage > cand2_percentage and cand3_percentage and cand4_percentage:
    winner = cand1
if cand2_percentage > cand1_percentage and cand3_percentage and cand4_percentage:
    winner = cand2
if cand3_percentage > cand1_percentage and cand2_percentage and cand4_percentage:
    winner = cand3
if cand4_percentage > cand1_percentage and cand2_percentage and cand3_percentage:
    winner = cand4
#open txt file and save the analysis of the Poll data
pypoll_analysis = os.path.join("Analysis-PyPoll", "PyPoll_analysis.txt")
with open(pypoll_analysis,"w") as text_file:
    text_file.write(f'''
        Election Results
        ----------------------------
        Total Votes: {voter_count}
        ----------------------------
        {cand1}: {cand1_percentage}% ({cand1_count})
        {cand2}: {cand2_percentage}% ({cand2_count})
        {cand3}: {cand3_percentage}% ({cand3_count})
        {cand4}: {cand4_percentage}% ({cand4_count})
        ----------------------------
        Winner: {winner}
        ----------------------------
        ''')
    text_file.close()
#print the analysis of the Poll data in the terminal
print(f'''
    Election Results
    ----------------------------
    Total Votes: {voter_count}
    ----------------------------
    {cand1}: {cand1_percentage}% ({cand1_count})
    {cand2}: {cand2_percentage}% ({cand2_count})
    {cand3}: {cand3_percentage}% ({cand3_count})
    {cand4}: {cand4_percentage}% ({cand4_count})
    ----------------------------
    Winner: {winner}
    ----------------------------
    ''')
