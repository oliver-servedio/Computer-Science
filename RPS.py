'''
Author: Oliver Servedio
Date: 12/1
Description: A rock paper scissors program where you can choose to play against a highly skilled AI or against a friend of choice.
bugs: None that I found
Challegens: Scoreboard - Options to play a computer or another player - Rigged odds for the computer - while True loop - str.lower - error message built in
How to play = First, you are prompted answer the queston 'Do you want to play against the computer, best 2 out of 3?' if you choose yes, you
play against the computer. If you put no, you have the option to play against another player. You can play normally, and when you want to stop, you can write
stop as player1. If you want to check the score, just input 'score' as each player, and it will respond with the score.
Sources: W3Schools - Shep O'Keeffe
'''
import random #imports the random library
while True: #runs the code indented under the while True: until it gets broken by the break command
    play = str.lower(input('Do you want to play rock paper scissors, best two out of three, against the computer? '))#makes the variable = to the user's input and then changes the user input to all lowercase characters

    if play == 'yes':#will perform the action in the indented line below if the variable equals a certain value
        win_counter = 0 #creates a variable called win_counter to store information in the code
        loss_counter = 0 #creates a variable called loss_counter to store information in the code
        while True: #runs the code indented under the while True: until it gets broken by the break command
            if win_counter >= 2:#will perform the action in the indented line below if the variable equals a certain value
                print('you win')#prints the message in the parentheses
                break #breaks the while loop that it is in
            elif loss_counter >= 2:#will perform the action in the indented line below if the variable equals a certain value then will skip over the rest of the if and elif statements
                print('you lose')#prints the message in the parentheses
                break #breaks the while loop that it is in

            choice = str.lower(input('What do you want to throw: Rock, Paper, or Scissors '))#makes the variable = to the user's input and then changes the user input to all lowercase characters
            random_choice = random.randrange(1,11) #makes the variable random_choice = a random number with the limits (1,11)

            if choice == 'rock':#will perform the action in the indented line below if the variable equals a certain value
                if random_choice <= 2:#will perform the action in the indented line below if the variable equals a certain value
                    print('I throw scissors, you win this round')#prints the message in the parentheses
                    win_counter += 1 #increases the value of win_counter by 1
                elif random_choice == 3: print('I throw rock, we tie this round')#will perform the action in the indented line below if the variable equals a certain value then will skip over the rest of the if and elif statements
                elif random_choice > 3:#will perform the action in the indented line below if the variable equals a certain value then will skip over the rest of the if and elif statements
                    print('I throw paper, I win this round')#prints the message in the parentheses
                    loss_counter += 1 #increases the value of loss_counter by 1
            elif choice == 'paper':#will perform the action in the indented line below if the variable equals a certain value then will skip over the rest of the if and elif statements
                if random_choice <= 2:#will perform the action in the indented line below if the variable equals a certain value
                    print('I throw rock, you win this round')#prints the message in the parentheses
                    win_counter += 1 #increases the value of win_counter by 1
                elif random_choice == 3: print('I throw paper, we tie this round')#will perform the action in the indented line below if the variable equals a certain value then will skip over the rest of the if and elif statements
                elif random_choice > 3:#will perform the action in the indented line below if the variable equals a certain value then will skip over the rest of the if and elif statements
                    print('I throw scissors, I win this round')#prints the message in the parentheses
                    loss_counter += 1 #increases the value of loss_counter by 1
            elif choice == 'scissors':#will perform the action in the indented line below if the variable equals a certain value then will skip over the rest of the if and elif statements
                if random_choice <= 2:#will perform the action in the indented line below if the variable equals a certain value
                    print('I throw paper, you win this round')#prints the message in the parentheses
                    win_counter += 1 #increases the value of win_counter by 1
                elif random_choice == 3: print('I throw scissors, we tie this round')#will perform the action in the indented line below if the variable equals a certain value then will skip over the rest of the if and elif statements
                elif random_choice > 3:#will perform the action in the indented line below if the variable equals a certain value then will skip over the rest of the if and elif statements
                    print('I throw rock, I win this round')#prints the message in the parentheses
                    loss_counter += 1 #increases the value of loss_counter by 1
            else: #will perform the action in the indented line below if all of the if and elif statements above were not true
                print('you can only respond with rock paper or scissors')#prints the message in the parentheses
                
    elif play == 'no':#will perform the action in the indented line below if the variable equals a certain value then will skip over the rest of the if and elif statements
        print('OK')#prints the message in the parentheses
        real_person = str.lower(input('Do you want to play rock paper scissors agaist another player? '))#makes the variable = to the user's input and then changes the user input to all lowercase characters
        player_1_score = 0 #creates a variable called player_1_score to store information in the code
        player_2_score = 0 #creates a variable called player_2_score to store information in the code
        if real_person == 'yes':#will perform the action in the indented line below if the variable equals a certain value
            while True: #runs the code indented under the while True: until it gets broken by the break command
                limitation1 = 0 #creates a variable called limitation1 to store information in the code
                limitation2 = 0 #creates a variable called limitation2 to store information in the code
                player_1 = str.lower(input('Player one plays '))#makes the variable = to the user's input and then changes the user input to all lowercase characters
                while limitation1 < 100: #Runs the code indented below until the value of limitation1 exceeds 100
                    print()#prints the message in the parentheses
                    limitation1 += 1 #increases the value of limitation1 by 1
                if player_1 == 'stop':#will perform the action in the indented line below if the variable equals a certain value
                    break #breaks the while loop that it is in
                if player_1 == 'score':#will perform the action in the indented line below if the variable equals a certain value
                    print('player_1 =', player_1_score)
                player_2 = str.lower(input('Player two plays '))#makes the variable = to the user's input and then changes the user input to all lowercase characters
                while limitation2 < 100: #Runs the code indented below until the value of limitation2 exceeds 100
                    print()#prints the message in the parentheses
                    limitation2 += 1 #increases the value of limitation2 by 1
                if player_1 == 'score':#will perform the action in the indented line below if the variable equals a certain value
                    print('player_2 =', player_2_score)#prints the message in the parentheses
                elif player_1 == 'rock' and player_2 == 'paper':#will perform the action in the indented line below if the variable equals a certain value then will skip over the rest of the if and elif statements
                    print('player_2 wins')#prints the message in the parentheses
                    player_2_score += 1 #increases the value of player_2_score by 1
                elif player_1 == 'paper' and player_2 == 'rock':#will perform the action in the indented line below if the variable equals a certain value then will skip over the rest of the if and elif statements
                    print('player_1 wins')#prints the message in the parentheses
                    player_1_score += 1 #increases the value of player_1_score by 1
                elif player_1 == 'rock' and player_2 == 'scissors':#will perform the action in the indented line below if the variable equals a certain value then will skip over the rest of the if and elif statements
                    print('player_1 wins')#prints the message in the parentheses
                    player_1_score += 1 #increases the value of player_1_score by 1
                elif player_1 == 'scissors' and player_2 == 'rock':#will perform the action in the indented line below if the variable equals a certain value then will skip over the rest of the if and elif statements
                    print('player_2 wins')#prints the message in the parentheses
                    player_2_score += 1 #increases the value of player_2_score by 1
                elif player_1 == 'paper' and player_2 == 'scissors':#will perform the action in the indented line below if the variable equals a certain value then will skip over the rest of the if and elif statements
                    print('player_2 wins')#prints the message in the parentheses
                    player_2_score += 1 #increases the value of player_2_score by 1
                elif player_1 == player_2:#will perform the action in the indented line below if the variable equals a certain value then will skip over the rest of the if and elif statements
                    print('it is a tie')#prints the message in the parentheses
                else:#will perform the action in the indented line below if all of the if and elif statements above were not true
                    print('you can only respond with rock, paper, or scissors')#prints the message in the parentheses
        

    else:#will perform the action in the indented line below if all of the if and elif statements above were not true
        print('you can only respond with yes or no')#prints the message in the parentheses

