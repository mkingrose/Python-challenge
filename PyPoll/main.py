import os
import csv

csvpath = os.path.join("Resources/election_data.csv")
candidate_votes={}
total_votes= 0


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header= next(csvreader) 
    for row in csvreader:
        candidate = row[2]
        if candidate in candidate_votes.keys():
            candidate_votes[candidate] = candidate_votes[candidate]+1
        else:
            candidate_votes[candidate]=1
   
with open("elections", "w") as outfile:

    total_votes= sum(candidate_votes.values())
    print(f"total_votes {total_votes}")
    outfile.write((f"total_votes {total_votes}\n"))
                  
    percent=[]
    for i in candidate_votes:
        percent = round(candidate_votes[i]/total_votes*100,2)
        print(f"{i} {percent} {candidate_votes[i]}")
        outfile.write(f"{i} {percent} {candidate_votes[i]}\n")
    for key in candidate_votes.keys():
        if candidate_votes[key]==max(candidate_votes.values()):
            winner=key
    print(f"winner {winner}")
    outfile.write((f"winner {winner}\n"))


