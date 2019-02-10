#Section 1: Import and declare variables

##Note, did not import os because I will just be reading the file locally.
import re

filename = ("raw_data/paragraph_1.txt")

#self-explanatory lists
wordList = []

#counter is equivalent to word count here
counter = 0

########################################

#Section 2: Read and iterate through the desired text file and add all words into a list.
with open(filename,'r') as f:
    for line in f: #for each sentence
        for word in line.split(): #in the sentence above, for each word.
           wordList.append(word)
           counter+=1 #count total words


########################################

#Section 3: Creating strings of letters and words in two lists, then create a list of sentences from the original text.
#Please read if you want to understand usage:
'''Here, I use the map function here on the list wordList I just created to create two strings.
These strings will be important since they allow me to print the results of the analysis easily by counting things like list length.

(1) letters: a string with all the letters that excludes spaces, due to how wordList had stored words from the text.
(2) words: a string as well. The differnce is that I use a ' ' delimiter to generate the string rather than the None delimiter('')

The way I conceputalize map is as a method that applies something (like a str typecast in this case) to all of the elements in a list, then
returns them as a string type.'''

#good examples to run through here: https://www.w3schools.com/python/ref_func_map.asp in official documentation it seems to be implied.

letters = ''.join(map(str, wordList))
words = ' '.join(map(str,wordList))

#print(len(letters)), Use check number of sentneces to see if map function did what I wanted it to do.

#Create a list of sentences.
listSentences = words.split(".")
#Get rid of empty indices in list, if any.
listSentences= list(filter(None, listSentences))

#print(listSentences) to check that the array actually has distinct sentences.

########################################

#Section 4: Output results to terminal
print(f'''Paragraph Analysis
-----------------
Approximate Word Count: {counter}
Approximate Sentence Count: {len(listSentences)}
Average Letter Count: {round((len(letters)/counter),1)}
Average Sentence Length: {round(len(wordList)/len(listSentences),1)}

Note: Checked for accuracy via Google Docs!''')


########################################


#Section 5: Analogous to Section 3, simply write a new file instead of printing.
#used w+ because I was too lazy to make a new file for output.

out = open("output.txt","w+")
out.write(f'''Paragraph Analysis
-----------------
Approximate Word Count: {counter}
Approximate Sentence Count: {len(listSentences)}
Average Letter Count: {round((len(letters)/counter),1)}
Average Sentence Length: {round(len(wordList)/len(listSentences),1)}''')
out.close()
#close file stream.