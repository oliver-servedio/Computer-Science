"""
Authors: Oliver Servedio
Date: 11/6
Description: A lifelike simulation where you experience how your decisions affect you later in life and shows the boring repetition of life.
Bugs: Because of a delay you can write when you are not supposed to write
Challenges: While Loops - str.lower - Adding delays - Randomness - takes persons name and uses it thoughout the code - responsive input/alarmticker and hours - 
Sources: W3Schools
"""
import time #brings in the time library for reference
import random #brings in the time library for reference
name = input('whats your name? ')#Asks the user for there name and stores the name in the name varible to be use for later
while True: #runs the code indented under the wile True: untile it gets broke by the break command
    alarmticker = 0 #sets the varible alarmticker to 0
    hours = 0 #sets the varible hours to 0
    x = random.randrange(1,5) #makes the varible x a number 1,2,3,4 creating a 25% chance in the code
    while True: #runs the code indented under the wile True: untile it gets broke by the break command
        print(name+ ' your alarm goes off.')#prints the message in the parentheses
        time.sleep(1)#gives the code a 1 second delay
        snooze = str.lower(input(name+', do you want to snooze? '))#make the varible = to the users input and then changes the user input to all lower case charecters

        if snooze == 'no': #will perform the action in the indenten line below if the varible equals a certian value
            print('You wake up.')#prints the message in the parentheses
            time.sleep(1)#gives the code a 1 second delay
            break #breaks the while loop that it is in
        elif snooze == 'yes': #will perform the action in the indenten line below if the varible equals a certian value than will skip over the rest of the if and elif statements
            print('9 minutes go by.')#prints the message in the parentheses
            alarmticker += 1 #adds 1 to the value of the varible alarmticker
            time.sleep(1)#gives the code a 1 second delay
        else: #will perform the action in the indenten line below if all of the if and elif statements above were not true
            print('Your input is not avalible. The only acceptable inputs are ''no'' and ''yes''. Try again.')#prints the message in the parentheses
            time.sleep(1)#give the code a 1 second delay
    while True: #runs the code indented under the wile True: untile it gets broke by the break command
        changed = str.lower(input(name+', do you want to get changed? ')) #make the varible = to the users input and then changes the user input to all lower case charecters

        if changed == 'yes': #will perform the action in the indenten line below if the varible equals a certian value
            time.sleep(1)#gives the code a 1 second delay
            break#breaks the while loop that it is in
        elif changed == 'no': #will perform the action in the indenten line below if the varible equals a certian value than will skip over the rest of the if and elif statements
            print('You are weird '+name+', and your family shames you.')#prints the message in the parentheses
            time.sleep(1)#gives the code a 1 second delay
            break#breaks the while loop that it is in
        else: #will perform the action in the indenten line below if all of the if and elif statements above were not true
            print('Your input is not avalible. The only acceptable inputs are ''no'' and ''yes''. Try again.')#prints the message in the parentheses
            time.sleep(1)#gives the code a 1 second delay
    while True: #runs the code indented under the wile True: untile it gets broke by the break command
        hygene = str.lower(input('Do you want to do all of the hygiene stuff, like brushing your teeth? ')) #make the varible = to the users input and then changes the user input to all lower case charecters

        if hygene == 'yes': #will perform the action in the indenten line below if the varible equals a certian value
            print('Good job.')#prints the message in the parentheses
            time.sleep(1)#gives the code a 1 second delay
            break#breaks the while loop that it is in
        elif hygene == 'no': #will perform the action in the indenten line below if the varible equals a certian value than will skip over the rest of the if and elif statements
            print('You are gross and judged by everyone around you.')#prints the message in the parentheses
            time.sleep(1)#gives the code a 1 second delay
            break#breaks the while loop that it is in
        else: #will perform the action in the indenten line below if all of the if and elif statements above were not true
            print('Your input is not avalible. The only acceptable inputs are ''no'' and ''yes''. Try again.')#prints the message in the parentheses

    while True: #runs the code indented under the wile True: untile it gets broke by the break command
        bag = str.lower(input('Do you want to get your bag ready? ')) #make the varible = to the users input and then changes the user input to all lower case charecters

        if bag == 'yes': #will perform the action in the indenten line below if the varible equals a certian value
            print('Good job.')#prints the message in the parentheses
            time.sleep(1)#gives the code a 1 second delay
            break#breaks the while loop that it is in
        elif bag == 'no': #will perform the action in the indenten line below if the varible equals a certian value than will skip over the rest of the if and elif statements
            break#breaks the while loop that it is in
        else: #will perform the action in the indenten line below if all of the if and elif statements above were not true
            print('Your input is not avalible. The only acceptable inputs are ''no'' and ''yes''. Try again.')#prints the message in the parentheses
            
    print('You go to school.')#prints the message in the parentheses

    if alarmticker >= 2: #will perform the action in the indenten line below if the varible equals or is greater than a certian value
        print('You are late to school because you snoozed your alarm too much and got detention from your advisor.')#prints the message in the parentheses
        hours += 1 #adds 1 to the value of the varible hours
        time.sleep(1)#gives the code a 1 second delay
    elif alarmticker == 1: #will perform the action in the indenten line below if the varible equals a certian value than will skip over the rest of the if and elif statements
        print('You barely make it too school on time after you snoozed your alarm.')#prints the message in the parentheses
        time.sleep(1)#gives the code a 1 second delay
    else: #will perform the action in the indenten line below if all of the if and elif statements above were not true
        print('You make it to school with time to spare.')#prints the message in the parentheses
        print('You see Shepard O''Keeffe and out of anger smack him in his little face')#prints the message in the parentheses
        time.sleep(1)#gives the code a 1 second delay
        


    #if x == 1: #will perform the action in the indenten line below if the varible equals or is greater than a certian value
        #print('Your school burns down. Game over.')#prints the message in the parentheses
        #break#breaks the while loop that it is in
    if changed == 'no': #will perform the action in the indenten line below if the varible equals or is greater than a certian value
        print('You get embarrassed at school and get a detetion for indecency.')#prints the message in the parentheses
        hours += 1 #adds 1 to the value of the varible hours
        time.sleep(1)#gives the code a 1 second delay
    if hygene == 'no': #will perform the action in the indenten line below if the varible equals or is greater than a certian value
        print('Your friends make fun of you for having bad breath.')#prints the message in the parentheses
        time.sleep(1)#gives the code a 1 second delay
    if bag == 'no': #will perform the action in the indenten line below if the varible equals or is greater than a certian value
        print('you got two detetions for missing homework and for forgetting your bag')#prints the message in the parentheses
        hours += 2 #adds 2 to the value of the varible hours
        time.sleep(1)#gives the code a 1 second delay

    print("You have", hours ,'hours of detetion at the end of the day.')#prints the message in the parentheses
    time.sleep(1)#gives the code a 1 second delay
    print('The school day ends, and you finaly get home.')#prints the message in the parentheses
    time.sleep(1)#gives the code a 1 second delay
    print('You do your homework.')#prints the message in the parentheses
    time.sleep(1)#gives the code a 1 second delay
    print('You go to bed.')#prints the message in the parentheses
    time.sleep(1)#gives the code a 1 second delay
