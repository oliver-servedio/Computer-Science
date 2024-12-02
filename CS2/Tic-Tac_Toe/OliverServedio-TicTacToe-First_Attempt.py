import random

og_board = [                                                            # Creates a two dimensional array that will not change in the code
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

board = [                                                               # Creates a two dimensional array
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def print_board(): 
    '''
    Prints the board in a formate that is easy to read

    Args:
        (): Does not take in anything
    Returns:
        (2d Array): The tic tac toe board cleaned (No brackets commas or quotes)
    '''                                                     # Creates a function to print the tik tac toe board
    # Goes though each position in the parallel array and prints each position adding a new line after 3 outputs
    for row in range(len(board)):
        for column in range(len(board[row])):
            print(board[row][column], end=' ')
        print()


def player_move(player, move):
    '''
    Makes the move for either the user or the computer

    Args:
        (Str - int): Takes in if player one or two is moving and the position of the move
    Returns:
        (2d Array): The tic tac toe board with the updated board
    Raises:
        (input error): if the user inputs a move that is already taken returns skip and redoes the users move
    '''

    # Sets the player variable based of who is moving
    if player == 'player 1':
        value = 'X'
    elif player == 'player 2':
        value = 'O'
    
    if 0 > move or move > 9:
        print('That is not an available move, try again ')
        return 'skip' 


    for row in range(len(board)):
        for column in range(len(board[row])):
            if move == og_board[row][column]:
                if board[row][column] == og_board[row][column]:
                    board[row][column] = value

def check_win(player):
    '''
    Checks over the position and sees if either player has one the game

    Args:
        (str) takes in which ever player is being checked
    Returns:
        (str): returns player wins if a player wins
    '''
    
    if board[0][0] == board[0][1] == board[0][2]:
        print(player, 'wins! ')
        exit() 
    elif board[1][0] == board[1][1] == board[1][2]:
        print(player, 'wins! ')
        exit()
    elif board[2][0] == board[2][1] == board[2][2]:
        print(player, 'wins! ')
        exit()
    elif board[0][0] == board[1][0] == board[2][0]:
        print(player, 'wins! ')
        exit()
    elif board[0][1] == board[1][1] == board[2][1]:
        print(player, 'wins! ')
        exit()
    elif board[0][2] == board[1][2] == board[2][2]:
        print(player, 'wins! ')
        exit()
    elif board[2][0] == board[1][1] == board[0][2]:
        print(player, 'wins! ')
        exit()
    elif board[0][0] == board[1][1] == board[2][2]:
        print(player, 'wins! ')
        exit()
    

def main():
    while True:
        h_b = str.lower(input('Do you want to play a bot or human? Answer with b or h --> '))
        if h_b == 'h':
            break
        elif h_b == 'b':
            break
        else: 
            print('That was not a correct input try again')
    if h_b == 'h':
        counter = 0
        can_player_move = ''
        while counter < 9:
            if can_player_move != 'skip':
                print_board()
                check_win('player 2')
                try:
                    move = int(input('what is player ones move? Answer with a number one the board '))
                    can_player_move = player_move('player 1', move)
                except:
                    print('Your input has to be an int 1 - 9 --> Go again ')
                    can_player_move = 'skip'
                
                counter += 1
            else: 
                can_player_move = ''
                counter -= 1

            if counter >= 9:
                print('It is a draw')
                break


            if can_player_move != 'skip':
                print_board()
                check_win('player 1')
                try:
                    move = int(input('what is player twos move? Answer with a number one the board '))
                    can_player_move = player_move('player 2', move)
                except:
                    print('Your input has to be an int 1 - 9 --> Go again ')
                    can_player_move = 'skip'

                counter += 1
            else: 
                can_player_move = ''
                counter -= 1

            

    elif h_b == 'b':
        available_move = [1,2,3,4,5,6,7,8,9]
        order = input('Do you want to go first or second? Answer with 1 or 2 --> ')
        counter = 0
        can_player_move = ''
        while counter < 9:
            if can_player_move != 'skip' and order == '1':
                print_board()
                check_win('player 2')
                try:
                    move = int(input('what is player ones move? Answer with a number one the board '))
                    can_player_move = player_move('player 1', move)
                except:
                    print('Your input has to be an int 1 - 9 --> Go again ')
                    can_player_move = 'skip'
                if can_player_move != 'skip':
                    available_move.remove(move)
                
                counter += 1
            else: 
                can_player_move = ''
                counter -= 1

            if can_player_move != 'skip':
                order = '1'
                print_board()
                check_win('player 1')
                move_hold = random.randrange(len(available_move))
                move = available_move[move_hold]
                print('')
                can_player_move = player_move('player 2', move)
                if can_player_move != 'skip':
                    available_move.remove(move)
                
                counter += 1
            else:
                can_player_move = ''
                counter -= 1


main()