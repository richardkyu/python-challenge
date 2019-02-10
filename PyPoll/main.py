#Cool note: no dictionaries used (at least directly) to complete this exercise!!

#Section 1: Imports and Clean election_result.txt
import os
# for accessing csv files
import csv

#import Counter method to simplify tracking counts of objects in lists.
#please see: https://docs.python.org/3/library/collections.html#collections.Counter for documentation
from collections import Counter

##############

#clear the results of the previous election 
#opening and closing a text file in write mode deletes its existing contents
#convenient for multiple test runs
open('election_results.txt', 'w').close()

listCandidates =[] #self explanatory

##############

#Section 2: Open and read the csv file using with block, due to the convenience of csv reader's delimiter.
with open("election_data.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')

##############


#Section 3: Iterate to get all of the candidates into a list.
    for row in csvreader:
        #row 2 is the only relevant row, as county and voter ID don't
        #provide any information relevant to the output we want.
        listCandidates.append(row[2])
#remove header
listCandidates.pop(0)

##############

#Section 4: Get total vote count, sort the candidates in the listCandidates array using Counter method.
#cont. get other relevant numbers and declare other relevant lists.

voteC=len(listCandidates) #total number of votes

#setting most common to voteC ensures that all possible candidates are displayed.
#please read: https://docs.python.org/3/library/collections.html#collections.Counter.most_common for documentation
sortedVotes = Counter(listCandidates).most_common(voteC)

#store candidates
resultsC = []
#store votes for each candidate respectively.
resultsB = []

##############

#Section 5: Printing to the terminal
#print desired output to the terminal, f-string feels like cheating.

print(f'''
Election Results
-------------------------
Total Votes: {voteC}
-------------------------''')
winner = Counter(listCandidates).most_common(1)

#iterate through sortedVotes (which already has the candidates ranked in descending order.)
for value, count in sortedVotes:
        resultsC.append(value) #I need this later to write to the file.
        resultsB.append(count) #I need this later to write to the fil
        raw = float(count/voteC) # Needed for percentages
        percent = round(raw*100,3) 
        print(f"{value}: {percent}% ({int(raw*voteC)})")
        

print(
f'''-------------------------
Winner: {resultsC[0]}''') #print the winner.

#end of output to terminal

##############


#Section 6: write to the election_results.txt file.
#there are three parts to this write 
'''1. The election results and total votes heading.
2. The list of candidates.
3. The displaying of the winner. So, I open, write, and close to the file three times'''

#first file write, for header.
out = open("election_results.txt", "a")
out.write(
f'''Election Results
-------------------------
Total Votes: {voteC}
-------------------------\n''')
out.close()


#newCount allows for us not to hardcode writing the results.
newCount = -1
while newCount<len(resultsC)-1:

#iterate the output for all candidates who received votes, so it is not hard coded
#done via the new variable newCount - suggested by Ram.

#second file write, to allow for iteration and avoid hardcording.
   out = open("election_results.txt", "a")
   newCount+=1
   out.write(f'''{resultsC[newCount]}: {round((resultsB[newCount]/voteC*100),3)}% ({resultsB[newCount]})\n''')
   out.close()


#third time writing file, for winner.
out = open("election_results.txt", "a")
out.write(f'''-------------------------
Winner: {resultsC[0]}''')
out.close()
#end of writing results close code.

