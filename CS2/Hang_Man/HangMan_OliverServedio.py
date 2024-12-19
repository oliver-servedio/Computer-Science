'''
Name: Oliver Servedio
Date: 12/19/2024
Description: A game of hangman that can either be chosen from a random list of words or from a word of the users choice
Bugs: None
Features: 1 and 2 players - red error messages - Clearing Terminal
Sources: Geeks for Geeks(For making text red and for os.('cls'))
Log: 1.0 initial version 
'''

board = ['''
   +---+
    |  |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']

import os
import random

# The reason for the long list is so no external file is needed
possible_words = ('''able about account acid across addition adjustment advertisement after again against agreement almost among amount amusement angle angry animal answer apparatus apple approval arch argument attack attempt attention attraction authority automatic awake baby back balance ball band base basin basket bath beautiful because before behavior belief bell bent berry between bird birth bite bitter black blade blood blow blue board boat body boiling bone book boot bottle brain brake branch brass bread breath brick bridge bright broken brother brown brush bucket building bulb burn burst business butter button cake camera canvas card care carriage cart cause certain chain chalk chance change cheap cheese chemical chest chief chin church circle clean clear clock cloth cloud coal coat cold collar color comb come comfort committee common company comparison competition complete complex condition connection conscious control cook copper copy cord cork cotton cough country cover crack credit crime cruel crush current curtain curve cushion damage danger dark daughter dead dear death debt decision deep degree delicate dependent design desire destruction detail development different digestion direction dirty discovery discussion disease disgust distance distribution division door doubt down drain drawer dress drink driving drop dust early earth east edge education effect elastic electric engine enough equal error even event ever every example exchange existence expansion experience expert face fact fall false family farm father fear feather feeble feeling female fertile fiction field fight finger fire first fish fixed flag flame flat flight floor flower fold food foolish foot force fork form forward fowl frame free frequent friend from front fruit full future garden general girl give glass glove goat gold good government grain grass great green grey grip group growth guide hair hammer hand hanging happy harbour hard harmony hate have head healthy hear hearing heart heat help high history hole hollow hook hope horn horse hospital hour house humour idea important impulse increase industry insect instrument insurance interest invention iron island jelly jewel join journey judge jump keep kettle kick kind kiss knee knife knot knowledge land language last late laugh lead leaf learning leather left letter level library lift light like limit line linen liquid list little living lock long look loose loss loud love machine make male manager mark market married mass match material meal measure meat medical meeting memory metal middle military milk mind mine minute mist mixed money monkey month moon morning mother motion mountain mouth move much muscle music nail name narrow nation natural near necessary neck need needle nerve news night noise normal north nose note number observation offer office only open operation opinion opposite orange order organization ornament other oven over owner page pain paint paper parallel parcel part past paste payment peace pencil person physical picture pipe place plane plant plate play please pleasure plough pocket point poison polish political poor porter position possible potato powder power present price print prison private probable process produce profit property prose protest public pull pump punishment purpose push quality question quick quiet quite rail rain range rate reaction reading ready reason receipt record regret regular relation religion representative request respect responsible rest reward rhythm rice right ring river road roll roof room root rough round rule safe sail salt same sand scale school science scissors screw seat second secret secretary seed seem selection self send sense separate serious servant shade shake shame sharp sheep shelf ship shirt shock shoe short shut side sign silk silver simple sister size skin skirt sleep slip slope slow small smash smell smile smoke smooth snake sneeze snow soap society sock soft solid some song sort sound soup south space spade special sponge spoon spring square stage stamp star start statement station steam steel stem step stick sticky stiff still stitch stocking stomach stone stop store story straight strange street stretch strong structure substance such sudden sugar suggestion summer support surprise sweet swim system table tail take talk tall taste teaching tendency test than that then theory there thick thin thing this thought thread throat through through thumb thunder ticket tight till time tired together tomorrow tongue tooth touch town trade train transport tray tree trick trouble trousers true turn twist umbrella under unit value verse very vessel view violent voice waiting walk wall warm wash waste watch water wave weather week weight well west wheel when where while whip whistle white wide will wind window wine wing winter wire wise with woman wood wool word work worm wound writing wrong year yellow yesterday young Android''').split(' ')

loop = True
while loop:
    choice = input ('1 or 2 players: answer w/ 1 or 2 ')
    if choice == ('2'):
        # Uses loop instead of while true so I can break both loops at once
        while loop:
            word = input('What is the word you want to use ')
            if word.isalpha() == True:
                word = list(word.upper())
                os.system('cls')                                        # Clears the terminal - is the reason for the os library
                loop = False                                            # Breaks Both loops
            else: print('\033[31mYour input is incorrect you must use all alphabetical characters\033[0m')      # Weird Characters are to make str red
    elif choice == ('1'):
        word = list((random.choice(possible_words)).upper())
        break
    else: print('\033[31mYour input was wrong. You must enter 1 or 2\033[0m ')


# Setting up variables
guess_list = 'Guess list: '
empty_word = list('_' * len(word))
lives = 6
alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

while lives > 0:
    print(board[-lives -1])
    print(f'''{''.join(empty_word)} Lives = {lives} ''')
    while True:
        try:
            guess = (input('What is your one letter guess ')).upper()
            if len(guess) != 1 and guess in alphabet:                   # Checks to make sure the guess is one letter, is in the alphabet, and has not been guessed
                raise InterruptedError
            alphabet.remove(guess)
            break
        except:
            print('\033[31mYour input was not correct make sure it is a original one letter guess\033[0m')
    
    # Check if the guess is valid
    if guess in word:
        loc = 0                                                         # var for the index of the guess in word
        for letter in word:
            if letter == guess:
                empty_word[loc] = guess
            loc += 1
    else: lives -= 1

    
    # Checks for win by seeing if there is no more empty spaces in empty word
    if '_' not in empty_word:
        print(f'''{''.join(empty_word)} You had {lives} lives left''')
        print('You Win!')
        exit()

    guess_list = guess_list + guess + ' '
    print(guess_list)


# Needs the if lives = 0 because of faulty exit()
if lives == 0:
    print(board[-lives -1])
    print(f'''Lives = {lives}
    You ran out of lives! YOU LOSE!
    The word was {''.join(word)} ''')