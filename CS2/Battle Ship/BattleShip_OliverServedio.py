'''
Name: Oliver Servedio
Date: 5/1/2025
Description: A two player battle ship game that allows for the players to place their ships and guess the other players ships
Bugs: If you place ships at the end of the board and try to go off the board it will not raise an error and will still try and place them
Features: Full ten by ten board, multi length ships, easy placement method, 
Testers: Jack Randall
Log: 1.0 initial version 
'''


import time
import os

player1_win_counter = 14
player2_win_counter = 14
# Counters for every time the corresponding player gets a hit


player1_board = list('----------------------------------------------------------------------------------------------------')
player1_guess_board = list('----------------------------------------------------------------------------------------------------')
player2_board = list('----------------------------------------------------------------------------------------------------')
player2_guess_board = list('----------------------------------------------------------------------------------------------------')

def print_board(board):
    '''
    Description: Prints the board in a formate that is easy to read

    Args:
        (): Does not take in anything
    Returns:
        (2d Array): The battle ship board cleaned (No brackets commas or quotes)
    '''
    print('  A B C D E F G H I J')
    board_list = []
    count = 0
    for pos in board:
        # Goes through each position in the list, board, and adds them to a list
        board_list.append(pos)
        if len(board_list) > 9:
            # if the list from before is 9 items than it will print the 3 items
            print(count, board_list[0], board_list[1], board_list[2], board_list[3], board_list[4], board_list[5], board_list[6], board_list[7], board_list[8], board_list[9])
            count += 1
            board_list = []

def get_place(player):
    '''
    Description: Gets the location of the ship from the user and formats it for the place_ship function

    Args:
        (int): Takes in the player that is moving (1 or 2)
    Returns:
        (func): Returns the function place_ship that continues the placing process
    '''
    for ship in range(1, 5):
        while True:
            user = ((input(f'Player {player} place your {6-ship} ship '))).split(' ')
            try:
                place = list(user[0].upper())
                direction = (user[1]).upper()
            except:
                print('Your input was incorrect. Make sure it is formatted LetterNumber Direction: Ex. A1 R ')
                continue
            if direction in ['L', 'R', 'D', 'U'] and place[0] in list('ABCDEFGHIJ') and place[1] in list('0123456789'):
                try:
                    if player == 1:
                        place_ship(place,    direction, 6-ship, player)
                    elif player == 2:
                        place_ship(place, direction, 6-ship, player)
                    break
                except ValueError:
                    print('Your input was incorrect. Make sure it is formatted LetterNumber Direction: Ex. A1 R ')
                    
            else:
                print('Your input was incorrect. Make sure it is formatted LetterNumber Direction: Ex. A1 R ')

def place_ship(place, direction, length, player):
    '''
    Description: Places the ship on the board in the correct location and direction

    Args:
        (list): Takes in the location of the ship [Letter, Number]
        (str): The direction of the ship (L, R, D, U)
        (int): The length of the ship
        (int): Player that is moving (1 or 2)
        
    Returns:
        (func): Returns the function place_ship_help that places the ship on the board
    '''
    for n in range(0, length):
        location = place.copy()
        if direction == 'L':
            location[0] = (chr(ord(location[0])-n)).upper()
            place_ship_help(''.join(location), player)
        elif direction == 'R':
            location[0] = (chr(ord(location[0])+n)).upper()
            place_ship_help(''.join(location), player)
        elif direction == 'D':
            location[1] = str(int(location[1]) + n)
            place_ship_help(''.join(location), player)
        elif direction == 'U':
            location[1] = str(int(location[1]) - n)
            place_ship_help(''.join(location), player)
    if player == 1:
        print_board(player1_board)
    elif player == 2:
        print_board(player2_board)


def place_ship_help(location, player):
    '''
    Description: Places the ship on the board

    Args:
        (str): Takes in the location of the ship [Letter, Number]
        (int): Player that is moving (1 or 2)
    Returns:
        Alters the game boards with the ships on them
        
    '''
    if player == 1:
        player1_board[find_guess(location)] = 'S'
    elif player == 2:
        player2_board[find_guess(location)] = 'S'
     

def find_guess(guess):
    '''
    Description: Finds the location of the guess on the board and formats it for the check_guess function

    Args:
        (str): Takes in the location of the guess [Letter, Number]
    Returns:
        (int): Returns the location of the guess on the board
    '''
    letters = list('ABCDEFGHIJ')
    letter_values = [1,2,3,4,5,6,7,8,9,10]

    num_value = [0,10,20,30,40,50,60,70,80,90]

    location = -1

    guess = list(guess)
 
    location = location + letter_values[letters.index(guess[0])]
    location = location + num_value[int(guess[1])]
    return location



def check_guess(location, player):
    '''
    Description: Checks the guess and determines if it is a hit or miss and changes the board accordingly

    Args:
        (int): Takes in the location of the guess [Letter, Number]
        (int): Player that is moving (1 or 2)
    Returns:
        Altered game board with the hits and misses on them
        (str): Returns a message if the player hits or misses
    '''
    global player1_win_counter
    global player2_win_counter
    if player == 1:
        if player2_board[location] == '-':
            player1_guess_board[location] = 'O'
            print('Miss')
        elif player2_board[location] == 'S':
            player1_board[location] = '-'
            player1_guess_board[location] = 'X'
            print('Hit')
            player1_win_counter -= 1
        else:
             return ValueError
    if player == 2:
        if player1_board[location] == '-':
            player2_guess_board[location] = 'O'
            print('Miss')
        elif player1_board[location] == 'S':
            player1_board[location] = '-'
            player2_guess_board[location] = 'X'
            print('Hit')
            player2_win_counter -= 1
        else:
             return ValueError

def check_win():
    '''
    Description: Checks if the game is over and if so, ends the game

    Returns:
        (str): Returns the winner of the game
    '''
    if player1_win_counter == 0:
        print('player 1 wins')
        exit()
    elif player2_win_counter == 0:
        print('player 1 wins')
        exit()

def main():
    '''
    Description: Main function that runs the game and calls all the other functions. It loops the code until the game is over

    Args:
        (): Does not take in anything
    Returns:
        (func): Returns the function that runs the game
    '''
    print_board(player1_board)
    get_place(1)
    time.sleep(1)                                   
    os.system('cls')                                   # Clears the terminal - is the reason for the os library
    print_board(player2_board)
    get_place(2)
    time.sleep(1)
    os.system('cls')

    while True:

        while True:
            try:
                print_board(player1_guess_board)
                guess = input('Player 1 What is your guess? ').upper()
                check_guess(find_guess(guess), 1)
                break
            except: print('Your input is incorrect. Make sure you have not guessed that spot and your guess is in the formal LetterNumber')
        check_win()


        while True:
            try:
                print_board(player2_guess_board)
                guess = input('Player 2 What is your guess? ').upper()
                check_guess(find_guess(guess), 2)
                break
            except: print('Your input is incorrect. Make sure you have not guessed that spot and your guess is in the formal LetterNumber')
        check_win()

main()