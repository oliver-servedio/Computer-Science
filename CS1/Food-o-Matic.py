'''
Author: Oliver Servedio
Date: March 29, 2024
Description: The program will ask you for a number of insults. After you input your number, it will give you the number of random insults you asked for
out of around 150 random insult combinations with three unique parts.
Challenges: You can not break the code by inputting a non-int value because of try and except loops - the domain is changed to an insult generator - This code uses
three different lists, not two - after each of the insults, there is a rating assigned to it
How to play: Enter the number of insults you want
Sources: W3Schools - Samantha Marciano
'''

import random                                                                                                                                #imports the random library

#together these create insults
adj = ['a smelly', 'an ugly', 'a disgusting', 'a weird', 'a short', 'a hairy',]                                                              #adjectives
noun = ['pig', 'cow', 'snake', 'simpleton', 'moron', 'swine', ]                                                                              #nouns
hurt = ['no one loves you', 'people cross the road when they see you', 'children cry in your presence', 'your dad wants to leave you']       #mean comments

while True: 
    try:                                                                                                                                     #try's to run the code below
        num_insults = int(input('number of insults '))                                                                                       #ask the user for how many insults they want - to be used later in the code
        break                                                                                                                                #Breaks the try and exept loop
    except ValueError:                                                                                                                       #runs the code under if there is a value error
        print("Invalid input. Please enter an integer.")                                                                                     #prints the stuff in the ""
                                                                                                                                                            
for i in range(num_insults):                                                                                                                 #runs the code indented below the same numbers of times as the amount variable 
    #prints the text in between (f''' ''')
    print(f'''
    You look like {random.choice(adj)} {random.choice(noun)}, no wonder {random.choice(hurt)}!
    That was a {random.randrange(6,11)} out of 10 insult.
    ''')

    #{random.choice(varible)} this prints a random item from the varibles list

