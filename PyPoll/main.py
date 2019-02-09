import os
import csv

#import Counter method to simplify tracking counts of objects in lists.
from collections import Counter
#access csv file.


with open("election_data.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')

    listCandidates =[]

#get all of the candidates into a list.
    for row in csvreader:
        listCandidates.append(row[2])


#remove header
listCandidates.pop(0)

#get total vote count.
voteC=len(listCandidates)

#setting most common to voteC ensures that all possible candidates are displayed.
sortedVotes = Counter(listCandidates).most_common(voteC)

#store winner
resultsC = []
resultsB = []

#print desired output
print(f'''Election Results
-------------------------
Total Votes: {voteC}
-------------------------''')
winner = Counter(listCandidates).most_common(1)

for value, count in sortedVotes:
        resultsC.append(value)
        resultsB.append(count)
        raw = float(count/voteC)
        percent = round(raw*100,3)
        print(f"{value}: {percent}% ({int(raw*voteC)})")
        

print(f'''-------------------------
Winner: {resultsC[0]}''')


with open("election_results.txt", "a") as out:
    out.write(f'''  Election Results
    -------------------------
    Total Votes: {voteC}
    -------------------------
    
    {resultsC[0]}: {round((resultsB[0]/voteC*100),3)}% ({resultsB[0]})
    {resultsC[1]}: {round((resultsB[1]/voteC*100),3)}% ({resultsB[1]})
    {resultsC[2]}: {round((resultsB[2]/voteC*100),3)}% ({resultsB[2]})
    {resultsC[3]}: {round((resultsB[3]/voteC*100),3)}% ({resultsB[3]})

    -------------------------
    Winner: {resultsC[0]}''')
out.close()

