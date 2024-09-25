'''
Author: Oliver Servedio
Date: 4/16/24
Description: This code runs each of the functions from the function mashup assignment sheet
Instructions: enter a number 1-10 that corresponds to the function mashup sheet (skipping over the first challenge)
Sources: W3Schools - Samantha Marciano
'''


import random                                                   #imports the random library

def happy_birthday(name):                                       #Creates a function that takes the input of a name and outputs the code below
    print('Happy Birthday to you')
    print('Happy Birthday to you')
    print('Happy Birthday to',(name))
    print('Happy Birthday to you')
    print('')
    print('Happy Birthday to you')
    print('Happy Birthday to you')
    print('Happy Birthday to',(name))
    print('Happy Birthday to you')
    #Prints the happy birthday song using a variety of print statements

def add(num1, num2):                                            #Creates a function that takes two numbers and adds them together
    print(num1 + num2)
    #Prints the Sum of num1 and num2

def list_(list_to_print):                                       #Creates a function that takes a list and prints it vertically
    for i in list_to_print:
        print(i)
    #prints each item in a list vertically

def list_element(user_list, element):                           #Creates a function that takes a list and checks for a certain item
    if element in user_list: return True
    else: return False
    #checks if an element is in a list - if it is print true else print false

def int_checker(int_str):                                       #Creates a function that checks if something is an int
    if '-' in int_str:
        int_str = int_str.strip('-')
    int_str = int_str.isdigit()                                 #checks if int_str is an int then assigns the true value if it is or false if it is not
    return int_str                                              #prints int_str

def range_checker(num1, num2):                                  #Creates a function that gives the range of two inputted numbers
    print(random.randrange(num1, num2))                         #Prints and random number in between num1 and num2

def replace(body, led1, led2):                                  #Creates a function that replaces certain letters in text with other li
    new_body = ''
    
    for i in body:
        if i == led1:
            new_body += led2
        else:
            new_body += i
    return new_body

    #return body.replace(led1, led2)                             
#replaces every led1 in the text with led2 returns body to be used later than returns the result

def reverse(txt):                                               #Defines the reverse function that reverses text
    txt = txt[::-1]                                             #Reverses text
    print(txt)                                                  #Prints text

def palchecker(txt):                                            #Defines the palchecker function that checks for palindrome
    return txt[::-1] == txt                                     #if rtxt = txt returns true, else return false

def initials(name):                                             #Creates a function that returns the initials of a entered name
    initials = []
    for i in range(len(name)):
        initials.append((name[i])[0])
    print(''.join(initials))
#iterates through the name list and adds the first letter of each element of the list to the initials list. Then join the list into a Str

def main():        
    function_to_run = input('What Function should run? ')       #Asks the user what number function they want to run

    if function_to_run == '1':                                  #If the variable function_to_run = 1 then it runs the code below
        name = input('Enter a name ')                           #Asked the user for input that will be stored in the variable name
        happy_birthday(name)                                    #Runs the function HappyBDay1 using the name variable

    elif function_to_run == '2':                                #If the variable function_to_run = 2 then it runs the code below
        numbers = input('What two numbers do you want to add? ').split(' ')
        add(int(numbers[0]), int(numbers[1]))
        #Asks the user what numbers they want to add then splits them into a list and puts them into the add function while making them ints

    elif function_to_run == '3':                                #If the variable function_to_run = 3 then it runs the code below
        list_to_print = input('What is your list? Seperate each items with commas. ').split(',')
        list_(list_to_print)
        #ask for a list that has there items seperated by commas than runs the list_ function

    elif function_to_run == '4':                                #If the variable function_to_run = 4 then it runs the code below
        user_list = input('What is your list? Seperate each items with commas. ').split(',')
        element = input('What is you element? ')
        print(list_element(user_list, element))
        #asks the user for a list and an element than runs the list_element functionn

    elif function_to_run == '5':                                #If the variable function_to_run = 5 then it runs the code below
        int_str = input('Input an int or str to be checked. ')
        print(int_checker(int_str))
        #asks for an input to be check if it is an int than runs the int_checker function with int_str as its variable

    elif function_to_run == '6':                                #If the variable function_to_run = 6 then it runs the code below
        input_range = input('what are your two numbers?').split(' ')#Asks for two numbers than slits them into a list
        range_checker(int(input_range[0]), int(input_range[1])) #Runs the range_checker function with the first and second value of the input_range list
        
    elif function_to_run == '7':                                #If the variable function_to_run = 7 then it runs the code below
        body_text = input('What is your body text? ')           #asks the user for a body text
        letters = (input('what are your two letters? ')).split(' ')#takes two values than splits them
        print(replace(body_text, letters[0], letters[1]))       #runs the replace function

    elif function_to_run == '8':                                #If the variable function_to_run = 8 then it runs the code below
        txt = input('What is your string? ')                    #Asks for a string
        reverse(txt)                                            #Runs the reverse function

    elif function_to_run == '9':                                #If the variable function_to_run = 9 then it runs the code below
        txt = input('What is your string? ')                    #Asks for a string
        print(palchecker(txt))                                  #Prints the result of the palchecker function

    elif function_to_run == '10':                               #If the variable function_to_run = 8 then it runs the code below
        name = input('What is your full name? ').split(' ')      #Ask for a name then splits it up into a list by spaces
        initials(name)                                          #Runs initials function
        
    
        
while True:                                                     #runs the code underneath until false
    main()                                                      #runs the main function
