import random #imports the random library

#creats a vissual set of indicators for the Hang Man game
HANGMAN_PICS = ['''
   +---+
    |
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
words = ['jazz', 'abrupt', 'abyss', ]                   #possible words to choose from for the player to guess
secret = random.choice(words)                           #chooses a secret word randomly from the list of possible words of the player to try and guess
                                    
guesses = 0                                             #varible to keep track of how many incorrect guesses the player has made; starts at zero
hidden = []                                             #creates an empty list to be used as a way for players to keep track of their guesses
secret_list = list(secret)                              #convert the secret word into a list by splicing the characters
#adds to the hidden list such that the characters in the secret list line up with dashes to indicate the length etc of the word to the player
for character in secret_list:                           #literate through every eleement (charecters) in the list of the secret word's characters
    hidden.append("_ ")                                 #add two spaces to the hidden list to demonstrate that there are multiple words
print(''.join(hidden))                                  #converts the hidden list to a string, which is displayed, by joining each character in its list

while '_ ' in hidden and guesses < len(HANGMAN_PICS):   #runs the the code underneath the while loop as long as there are still leters that have to be guessed 
    print(HANGMAN_PICS[guesses])                        #
    guess = input('Enter a letter: ')                   #creates a varible that equals the users input
    
    if guess in secret:                                 #runs the following code if the input is in the list
        for index in range(len(secret)):
            if guess == secret_list[index]:
                hidden[index] = guess
        print(''.join(hidden))
    else:
        print('Letter not here!')
        guesses += 1

    print(HANGMAN_PICS[guesses]) #prints the hang man sprite based on how many guesses the player has done
