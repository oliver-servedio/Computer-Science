'''
Author: Oliver Servedio
Date: 5/3/24
Description: A program that stores passwords on a txt file. You have various functions that you can also
execute through this program
Bugs: none  
Challenges: All of the challenges on the password keeper doc as well as a password to get into the program
and also the use of functions to make organized code
Instructions: Enter the password 'Shepiscool123' to start the program then use the instructions in the code
Sources: W3Schools - Samatha Marciano
'''

import random                                                               #Imports the random library

websites = []
usernames = []
passwords = []
#Creates 3 empty lists

f = open(r"passwordkeeperdoc.txt", 'r') #Opens the document with this domain in read mode
save = f.read().split('\n')                                                                   #Reads the document and separates it by lines
for i in save:
    site, name, pswrd = i.split(',')                                                          #For each line separate their elements by ',' labeling them by site, name, and pswrd
    websites.append(site)
    usernames.append(name)
    passwords.append(pswrd)
    #For each element add each of them to their respective list

def return_all_website_values():
    for i in range(len(websites)):
        print(websites[i], usernames[i], passwords[i])
    #Makes i = each index of the websites list and uses that index to print the i index in each of the other lists

def return_specific_website_values():
    access = input('Enter the name of the website you want the username and password for. ' )
    if access in websites:
        print(f'''Username = {usernames[websites.index(access)]} 
Password = {passwords[websites.index(access)]}
              ''')
    else:
        print('website not found')

def password_checker(password):
    non_alphabetical_charecters = ['1','2','3','4','5','6','7','8','9','0','!','@','$','%','^','&','*','(',')','#','_','-','+','=','{','[','}',']','|',',',':',';','~','?','/','>','.','<','}']
    check = 0
    if len(password) < 8:
        print('The password is to short')
    #Checks if the length of the password is longer than 8 characters to see if it is strong enough
    for location in password:
        for charecter in non_alphabetical_charecters:
            if location == charecter:
                check += 1
    #Checks the amount of non alphabet characters in the password
    if check < 2 :
        print('This password needs more non alphabet characters' )
    else:
        print('this password is good' )
    #If there are fewer than two non alphabet characters says the password is insecure else it says it's good
def password_generator():
    strong_password = ''
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    numberlist = list('1234567890!@#$%^&*()[]_+-=:;<>,.?/|~')
    #Creates two lists: one for Alphabet characters and one for non alphabet characters
    length_letters = random.randrange(8,13)
    length_numbers = random.randrange(3,7)
    #Takes two random numbers from there respective ranges one for letters and one for numbers
   
    for i in range(length_letters):
        strong_password += random.choice(alphabet)
    for i in range(length_numbers):
        strong_password += random.choice(numberlist)
    print(strong_password)
    #Prints random alphabet and numeric letters based on the previously randomly generated numbers
def add_entry():
    user_input = input('What is the name of your website, username, and password all separated by spaces and in that order? ').split(' ')
    #takes the input for the name username and password of a website
    websites.append(user_input[0])
    usernames.append(user_input[1])
    passwords.append(user_input[2])
    #adds the new values to the end of the 3 lists created at the start

def remove_entry():
    delete_target = input('Put the name of the website you want to remove ')
    if delete_target in websites:
        index = websites.index(delete_target)
        websites.pop(index)
        usernames.pop(index)
        passwords.pop(index)
        print('Done')
    else:
        print('That input is not in the list ')
    #if the website inputted is the websites list finds the index of the item and then removes that index from all of the other lists

def main():
    
    
    if input('Enter the password to acces the code ') == '123456789':
        while True:
            choice = input(f'''
    1 = Generate a random strong password
    2 = Check if a password is strong
    3 = Enter a new password
    4 = Print all of the websites, usernames and passwords
    5 = Access the password of a website
    6 = Remove a website
    7 = End the code
    Which option would you like --> ''')
            print('')    

            if choice == '1':
                password_generator()

            elif choice == '2':
                password_checker(input('What is the password you want to check '))

            elif choice == '3':
                add_entry()

            elif choice == '4':
                return_all_website_values()

            elif choice == '5':
                return_specific_website_values()

            elif choice == '6':
                remove_entry()

            elif choice == '7':
                break

    f = open(r"passwordkeeperdoc.txt", 'w+') #Opens the document with this name in write mode
    for i in range(len(websites)):
        f.write(websites[i])
        f.write(',')
        f.write(usernames[i])
        f.write(',')
        f.write(passwords[i])
        #Writes each of the values of the index i of each list with a comma in between
        if i + 1 != len(websites):
            f.write('\n')
        #makes a new line if it is not after that last item in the list
main()