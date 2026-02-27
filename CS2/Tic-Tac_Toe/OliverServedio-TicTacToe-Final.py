'''
Name: Oliver Servedio
Date: 12/2/24
Description: A game of tic tac toe either against a bot or player
Bugs: None
Features: uses a list instead of array for more efficient code
Sources: Mr. Campbell and W3Schools
Log: 1.0 initial version 
Note: I had trouble getting the exit function to work how I wanted because it was initially inside a function so I used the return 1's to get it to work
'''

import random
import sys
    
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def print_board():
    '''
    Prints the board in a formate that is easy to read

    Args:
        (): Does not take in anything
    Returns:
        (2d Array): The tic tac toe board cleaned (No brackets commas or quotes)
    '''
    board_list = []
    for pos in board:
        # Goes through each position in the list, board, and adds them to a list
        board_list.append(pos)
        if len(board_list) > 2:
            # if the list from before is 3 items than it will print the 3 items
            print(board_list[0], board_list[1], board_list[2])
            board_list = []


def player_move(move, turn):
    '''
    Makes the move for either the user or the computer

    Args:
        (Str - int): Takes in if player one or two is moving and the position of the move
    Returns:
        (list): The updated tic tac toe list
    '''
    # The reason for the X's and the O's being swapped is because the func is called before turn += 1
    player = 'X'                                            
    if (turn % 2) == 0: player = 'O'                        # If turn is even than it is O's turn
    # The % function divides the value and finds the remainder 

    board[move - 1] = player
    if check_win(player) == 1: return 1


def check_win(player):
    '''
    Checks over the position and sees if either player has won the game

    Args:
        (str) takes in which ever player is being checked
    Returns:
        (str): returns player wins if a player wins
    '''
#              Vertical Wins                  Horizontal Wins                   Diagonal Wins
    win_cons = [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5 ,7]   # A list of all of the possible winning positions
    for sec in win_cons:
        if board[sec[0]-1] == board[sec[1]-1] == board[sec[2]-1]:
            print_board()
            print(player + "'s Win")
            return 1


def main():
    # Determines if the user is playing against a bot or a human, if they are going first or second, and the move that need to be made

    order = 1
    while True:
        try:
            BoH = str.lower(input('Do you want to play against a bot or human answer with B or H '))
            if BoH == 'h' or BoH == 'b': 
                break
        except: 
            print('That was not a valid input try again')
    while BoH == 'b':
        try:
            order = int(input('Do you want to go first or second? Answer with 1 or 2 '))
            if order == 1 or order == 2: break 
            else: raise InterruptedError
        except: print('That was not a valid input try again')

    print_board()
    turn = order - 1                                               # It's used to find if there has been more than 9 moves and decide who's turn it is
    available_moves = [1,2,3,4,5,6,7,8,9]
    stop = 0
    
    
    while turn < 9:
        if BoH == 'h':
            if (turn % 2) == 0: player = '2'
            else: player = '1'
        else: player = '1'

        if BoH == 'h':
            while True:
                try:
                    move = int(input('Player '+ player +' what is your move? Answer with a number one the board --> '))
                    if not move in board:
                        raise InterruptedError                 # Just a error to trigger the try and except loop
                    available_moves.remove(move)
                    turn += 1
                    break
                except:
                    print('That is not a correct input. Go again ')
            if player_move(move, turn) == 1: sys.exit()
        
        elif BoH == 'b':
            while turn % 2 == 0:
                try:
                    move = int(input('Player '+ player +' what is your move? Answer with a number one the board --> '))
                    if not move in board:
                        raise InterruptedError                 # Just a error to trigger the try and except loop
                    available_moves.remove(move)
                    turn += 1
                    if player_move(move, turn) == 1:
                        stop = 1 
                        sys.exit()
                    break
                except:
                    if stop == 1: exit()
                    print('That is not a correct input. Go again ')
                    

            move = random.choice(available_moves)
            available_moves.remove(move)
            turn += 1
            if player_move(move, turn) == 1: sys.exit
                

        print_board()
    print('Draw')

main()