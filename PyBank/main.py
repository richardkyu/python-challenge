

import os
import csv

#access csv file.


with open("budget_data.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')

#Create dictionary object to hold and manipulate csv file
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

#set up reversed dictionary for data manipulation.
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
aChange=round(aChange,2)

# this is me realizing the difference between a float and an integer.
# print(aChange,type(aChange))

#remember, numericalProfit is an array.
maxProfit = max(numericalProfit)
minProfit = min(numericalProfit)

monthMax = avgDict[maxProfit]
monthMin = avgDict[minProfit]


#Putting it all together
#Final Output will read:
print(f'''Financial Analysis  
----------------------------  
Total Months: {totalMonths} 
Total Profit: ${sumProfit}   
Average Change: ${aChange}  
Greatest Increase in Profits: {monthMax}, (${maxProfit})  
Greatest Decrease in Profits: {monthMin}, (${minProfit})''')

#exporting to text file.
#this with block should generate a text file called "financial_analysis.txt with the same terminal output when executing."
with open("financial_analysis.txt", "w+") as out:
    out.write(f'''Financial Analysis  
----------------------------  
Total Months: {totalMonths} 
Total Profit: ${sumProfit}   
Average Change: ${aChange}  
Greatest Increase in Profits: {monthMax}, (${maxProfit})  
Greatest Decrease in Profits: {monthMin}, (${minProfit})''')

#testing outputs
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
