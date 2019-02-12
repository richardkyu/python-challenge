#Section 1: Import modules and libraries needed to access I/O and writing for CSV
import os
import re
import csv
from datetime import datetime

#There should be a way to import this list of states. But I've just copy pasted it here.
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#Create lists for modification.
empID = []
splitNames = []
birthDates=[]
SSN = []
stateAbv = []

with open('employee_data.csv','r') as csvfile:
    csvreader= csv.reader(csvfile, delimiter =',')
    next(csvreader) # skip header line
    #csvreader.__next__() <--alternative that also works (Python 2 -> Python 3)
#Extract each piece of data from csv into lists.

    #Get the categories into their respective lists.
    for row in csvreader:
    #Get the ID which remains the same.
        empID.append(row[0])
    #Get first and last name as a list of lists.
        split = row[1].split(" ")
        splitNames.append(split)
    #Use datetime class to parse original string into a datetime object and then format back into a stron
        formatDate = datetime.strptime(row[2],'%Y-%m-%d').strftime('%m-%d-%Y')
        birthDates.append(formatDate.replace('-','/'))
        #print(formatDate.replace('-','/'))
        SSN.append(row[3])

    #Abbreviate all state names
        stateAbv.append(us_state_abbrev[row[4]])

    
#Get the first and last names into separate lists
firstName = []
for first in splitNames:
    firstName.append(first[0])

lastName = []
for last in splitNames:
    lastName.append(last[1])

hiddenSSN = []
#Hide digits using regex for [0-9] and leave remaining four digits unchanged in replacement.
for social in SSN:
    hiddenSSN.append(re.sub(r'^[0-9]$',social[0:7],f"***-**-{social[7:]}"))
    

#put everything together

newFormat = [empID,firstName,lastName,birthDates,hiddenSSN,stateAbv]

#Zip is the same thing as doing a transpose here.
newFormat = zip(*newFormat)

#declare new list to insert as a header.
newHeader= ["Emp ID","First Name","Last Name","DOB","SSN","State"]


#ouput the file with the newly formatted employee data as new_data.csv
with open('new_data.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',')
    employee_writer.writerow(newHeader)
    employee_writer.writerows(newFormat)