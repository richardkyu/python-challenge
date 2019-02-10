#Section 1: Import necessary libraries
import os #optional one, depends on locality of csv file you want to work with.
import csv

#######################

#Section 2: access csv file, using the with block.
with open("budget_data.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')


#######################

#Section 3: Create dictionary object to hold and manipulate csv file.
#Note: I am aware you could have done all of this without a dictionary in with the csv.reader
    bankDict = {}

#iterate through the csv file and put it into the previous dictionary object.
    for row in csvreader:
        #Syntax here is dict['key'] = value
        #Analogously, it's bankDict['month'] = price
        bankDict[row[0]] = row[1]

#variables for interfacing with (for...in) loop type issues... strings..
    totalMonths = -1 #to account for the fact that the first row is a header.
    totalProfit,monthsList =[],[] #two arrays to contain each csv column.

#iterate and check if values work, separate profits/losses column into another list.
    for key in bankDict:
        totalMonths+=1
        monthsList.append(key)
        totalProfit.append(bankDict[key])
        #print(key,bankDict[key])

#get rid of header, which will create issues when performing mathematical operations.
totalProfit.pop(0) 
monthsList.pop(0)


#######################

#Section 4: Numerical Operations

#set variables to iterate, since the (for .. in) statement uses str and not int type.
counter = 0
sumProfit =0

#important for average change tracking.
numericalProfit = []

#sum and typecasting for addition in the above totalProfit array.
for index in totalProfit:
    sumProfit = sumProfit + int(totalProfit[counter])
    numericalProfit.append(int(totalProfit[counter]))
    counter+=1

#set up reversed dictionary for data manipulation, and to find month related to min/max profit.
#Don't ask me why I thought this was the most optimal solution.
counterB=0
avgDict = {}

#Find average change each month
avgChange =[]

#Create reverse dictionary to perform lookups. 
#counter here, in comparison to counterB will be the number of months, since it was iterated through that many times.
while (counterB<counter):
    avgDict[numericalProfit[counterB]]= monthsList[counterB] 
    counterB+=1
    
    #this gets the differences between monthly profits starting from feb-jan
    if(counterB<counter):
        avgChange.append(numericalProfit[counterB]-numericalProfit[counterB-1])

#average change per month
aChange = sum(avgChange) / counter
aChange= round(aChange,2)

# this below is me realizing the difference between a float and an integer.
# print(aChange,type(aChange))

#remember, numericalProfit is an array.
maxProfit = max(numericalProfit)
minProfit = min(numericalProfit)

monthMax = avgDict[maxProfit]
monthMin = avgDict[minProfit]

#######################

#Section 5: Putting it all together for output to terminal
#Final Output will read:
print(f'''Financial Analysis  
----------------------------  
Total Months: {totalMonths} 
Total Profit: ${sumProfit}   
Average Change: ${aChange}  
Greatest Increase in Profits: {monthMax}, (${maxProfit})  
Greatest Decrease in Profits: {monthMin}, (${minProfit})''')

#######################

#Section 6: exporting to text file.
#this with block should generate a text file called "financial_analysis.txt with the same terminal output when executing."
with open("financial_analysis.txt", "w+") as out:
    out.write(f'''Financial Analysis  
----------------------------  
Total Months: {totalMonths} 
Total Profit: ${sumProfit}   
Average Change: ${aChange}  
Greatest Increase in Profits: {monthMax}, (${maxProfit})  
Greatest Decrease in Profits: {monthMin}, (${minProfit})''')


#######################

#Some testing outputs I put at the end for readability. Irrelevant to results.
'''
print(aChange) 
print("\n")
print(avgDict)
print(totalProfit)
print(numericalProfit)print(monthMax,maxProfit)
print(monthMin,minProfit)
print(sumProfit)
print(totalMonths)
print(bankDict)'''
