'''
Author: Oliver Servedio
Date: 11/6
Description: A "magic 8-ball" where you ask a yes or no question and the code returns a random answer
Bugs: None
Challenges: while loop - a way to stop the loop
Sources: W3Schools, Shep O'Keeffe
'''

import random #imports the random library

while True: #runs the code indented under the while True: until it gets broken by the break command
    x = input()#makes x equal the text that the user inputs
    if x == 'stop': #will perform the action in the indented line below if the variable equals a certain value
        break #breaks the while loop that it is in
    print(random.choice(['yes', 'no', 'maybe', 'ask again later'])) #prints a random element of the list shown
    
