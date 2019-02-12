#Section 1: Import modules and libraries needed to access I/O and writing for CSV
import os
import re
import csv
from datetime import datetime

#There should be better a way to import this dictionary of states, for referencing.
#But I've just copy pasted it here below and shortened it using VS studio's display.
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

#Section 2: Create lists for modification.
empID = []
splitNames = []
birthDates=[]
SSN = []
stateAbv = []

#Section 3: Open the csv file and read it using the with block.
with open('employee_data.csv','r') as csvfile:
    csvreader= csv.reader(csvfile, delimiter =',')
    next(csvreader) # skip header line
    
    #csvreader.__next__() <--alternative that also works (Python 2 -> Python 3)

#Section 4: Extract each piece of data from csv into lists.
#4cont. : During extraction, also make sure that appropriate modifications are made. 
#This is the most complex part of the project.

    #Get all information from a row into their respective lists.
    for row in csvreader:
    #Get the ID which remains the same.
        empID.append(row[0])
    
    #Get first and last name as a list of lists.
        split = row[1].split(" ")
        splitNames.append(split)
    
    #Use datetime class to parse original string into a datetime object and then format back into a string
        formatDate = datetime.strptime(row[2],'%Y-%m-%d').strftime('%m-%d-%Y')
        #replace the dashes with slahes.
        birthDates.append(formatDate.replace('-','/'))
        
        #print(formatDate.replace('-','/'))
        SSN.append(row[3])

    #Abbreviate all state names while creating a list of those abbreviations.
        stateAbv.append(us_state_abbrev[row[4]])

    
#Get the first and last names into separate lists.
#Access the list of lists using a for loop, then access a specific element of a list..
#.. in this case either the first or last name, by its index.
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
    #Explanation: append() - append the newly formatted hidden SSN to the hiddenSSN list.
    #re.sub - regular expressions library, 
        #has usage re.sub(search for elements to delete, range to replace, return string form)
    #Regex expression used to search for numbers 0-9 for index of social between 0-7, and replace those with asterisks.
    #finally, just tack on the remaining part of the string with.
    

#Section 5: Put everything together into a list of lists again, but make it formattable for csv export.

#Create this list of lists from manipulated data in Section 4.
newFormat = [empID,firstName,lastName,birthDates,hiddenSSN,stateAbv]

#Zip is the same thing as doing a transposing a matrix here while creating a new zip object.
''' In math, this is how I conceptualize it:
[1,2,3]  T  [1,4,7]
[4,5,6] --> [2,5,8]
[7,8,9]     [3,6,9]
'''

#Use the zip format to transpose the newFormat list of lists so that the rows and columns are...
#...properly represented in the Zip object, zip creates tuples, which are immutable.
newFormat = zip(*newFormat)

#declare new list to insert as a header.
newHeader= ["Emp ID","First Name","Last Name","DOB","SSN","State"]


#Section 6: Output the file with the newly formatted employee data as new_data.csv
with open('new_data.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',')
    employee_writer.writerow(newHeader)
    employee_writer.writerows(newFormat)