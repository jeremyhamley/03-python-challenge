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
voter_count = []
candidates = []

#open and read data in csv file
with open(csvpath,'r') as election_data:
    read_election_data = csv.reader(election_data, delimiter = ',')
    #read header
    election_header = next(read_election_data)

    #read election data to collect candidates and total votes
    for vote in read_election_data:
        voter_count.append(vote[0])
        if vote[2] not in candidates:
            candidates.append(vote[2])
    
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

cand1_percentage = round((cand1_count * 100)/ len(voter_count),3)
cand2_percentage = round((cand2_count * 100)/ len(voter_count),3)
cand3_percentage = round((cand3_count * 100)/ len(voter_count),3)
cand4_percentage = round((cand4_count * 100)/ len(voter_count),3)

if cand1_percentage > cand2_percentage and cand3_percentage and cand4_percentage:
    winner = cand1
if cand2_percentage > cand1_percentage and cand3_percentage and cand4_percentage:
    winner = cand2
if cand3_percentage > cand1_percentage and cand2_percentage and cand4_percentage:
    winner = cand3
if cand4_percentage > cand1_percentage and cand2_percentage and cand3_percentage:
    winner = cand4


print("""
Election Results
----------------------------""")
print(f'Total Votes: {len(voter_count)}')
print('----------------------------')
print(f'{cand1}: {cand1_percentage}% ({cand1_count})')
print(f'{cand2}: {cand2_percentage}% ({cand2_count}) ')
print(f'{cand3}: {cand3_percentage}% ({cand3_count}) ')
print(f'{cand4}: {cand4_percentage}% ({cand4_count}) ')
print('----------------------------')
print(f'Winner: {winner}')
print('----------------------------')
print(" ")
