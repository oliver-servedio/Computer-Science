'''
Name: Oliver Servedio
Date: 10/31/24
Description: Determines the top ten words in terms of appearance from a text 
Bugs: None
Features: Uses matplotlib
Sources: Mr. Campbell, W3Schools, stack overflow, Geeks for Geeks
Log: 1.0 initial version 
'''

# Imports the Library matplotlib and numpy
import matplotlib.pyplot as plt
import numpy as np

# Opens 3 files: One for Harris's speech, one for Trumps speech and one to write the output of the important_words function
harris = open('ElectionData\\kamala_new.txt')
trump = open('ElectionData\\trump_speech.txt')
speech_results = open('ElectionData\\speech_results', 'w')

def important_words(fhand, speech_results):

    '''
    Determines the top ten words in terms of appearance from a text 

    Args:
        (file): Takes in a file that is already cleaned (cleaned meaning no punctuation and words that you don't want to include removed)
    Returns:
        (int for value - str for key): The top words in the file
    '''
    counts = {}

    # Iterates through the file line by line and in each line goes through word by word
    for line in fhand:
        line = line.lower()
        words = line.split()
        # For every word that got iterated if it is not in the dict(counts) then its adds it to the dict with the value of one and if it is the value increases by one
        for word in words:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1

    sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True)) # Source Geeks for Geeks - Sorts the dict counts by highest value to lowest value

    loop = 0
    # For the first 15 words in the sorted dict combine there key and value then write those to a file
    for key in sorted_counts:
        if loop < 10:
            data = key + ' ' + str(sorted_counts[key])
            speech_results.write(data)
            speech_results.write('\n')
            loop += 1
    speech_results.write


important_words(trump, speech_results)
important_words(harris, speech_results)

speech_results.close()                                                                                      # This line was added so that speech results could open again as a read


speech_results = open('ElectionData\\speech_results', 'r')

# Creates empty list for trumps words and value
T_words = []
T_values = []
# Creates empty list for trumps words and value
K_words = []
K_values = []

loop = 0
# Goes line by line through the file with results and applies different effects based on how many lines it has gone through
for line in speech_results:
    # Splits lines by spaces and adds the first part of the new list to the words list and the second part to the values list
    if loop < 10:
        words_values = line.split()
        T_words.append(words_values[0])
        T_values.append(int(words_values[1]))
        loop += 1
    # Splits lines by spaces and adds the first part of the new list to the words list and the second part to the values list
    elif loop < 20:
        words_values = line.split()
        K_words.append(words_values[0])
        K_values.append(int(words_values[1]))
        loop += 1 


amount = np.array(T_values)                                                                                 # Makes the variable equal to an array of the values list
plt.title("Trump Speech")                                                                                   # Give the pie chart a title
plt.pie(amount, labels = T_words, autopct= lambda x: '{:.0f}'.format(x*amount.sum()/100), startangle=90)    # Makes the pie chart so that it has the amounts based on values, give the pie chart labels based on the words and gives the pie chart the number values as well
plt.show()                                                                                                  # Shows the pie chart


amount = np.array(K_values)                                                                                 # Makes the variable equal to an array of the values list
plt.title("Kamala Speech")                                                                                  # Give the pie chart a title
plt.pie(amount, labels = K_words, autopct= lambda x: '{:.0f}'.format(x*amount.sum()/100), startangle=90 )   # Makes the pie chart so that it has the amounts based on values, give the pie chart labels based on the words and gives the pie chart the number values as well
plt.show()                                                                                                  # Shows the pie chart