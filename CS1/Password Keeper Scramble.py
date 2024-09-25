import random

def all_stuff():
    for i in range(len(website_list)):
        print(website_list[i], username_list[i], password_list[i])

def call_password():
    while True:
        access = input('Enter the name of the website you want the username and password for. ' )  #Asks for a website
        key = 0                                                                 #Sets the key varible to 0
        for i in website_list:                                                  #Iterates through the list websites until it finds the users input
            if i == access:                                                     #If the user input = a list value print the corresponding items in the parellel arays
                print('username = '+ username_list[key])
                print('password = '+ password_list[key])
            else:
                key += 1                                                        #Adds 1 to keys to track the point that you are in your list
        if input('Do you want to move on? ') == 'yes':
            break

def password_checker(password):
    numbers = ['1','2','3','4','5','6','7','8','9','0','!','@','$','%','^','&','*','(',')','#','_','-','+','=','{','[','}',']','|',',',':',';','~','?','/','>','.','<','}']
    check = 0
    if len(password) < 8: 
        print('The password is to short')
    for i in password:
        for x in numbers:
            if i == x:
                check += 1
    if check < 2 :
        print('This password needs more non alphebet charecters' )
    else:
        print('this password is good' )

def password_generator():
    strong_password = ''
    alphebet = list('abcdefghijklmnopqrstuvwxyz')
    numberlist = list('1234567890!@#$%^&*()[]_+-=:;<>,.?/|~')
    length_letters = random.randrange(8,13)
    length_numbers = random.randrange(3,7)
    
    for i in range(length_letters):
        strong_password += random.choice(alphebet)
    for i in range(length_numbers):
        strong_password += random.choice(numberlist)
    print(strong_password)                

password_generator()
website_list = []
username_list = []
password_list = []
#Creates 3 empty lists
f = open(r"C:\Users\oservedio27\Desktop\CS\Passwordkeeperforlder\passwordkeeperdoc.txt", 'r')
save = f.read().split('\n')
for i in save:
    site, name, pswrd = i.split(',')
    website_list.append(site)
    username_list.append(name)
    password_list.append(pswrd)

while True:
    while True:
        if input('Do you want check a passwords security? ') == 'yes':
            password = input('What is your password you want to check? ')
            password_checker(password)
        if input('Do you want to change one of your website usernames and passwords? ') == 'yes':
            name_to_change = input('Put the name of the website you want to remove ')
            if name_to_change in website_list:
                index = website_list.index(name_to_change)
                website_list.pop(index)
                username_list.pop(index)
                password_list.pop(index)
            else:
                print('That input is not in the list ')

        if input('Do you want to enter a new password? ') == 'no':
            break
            
        user_input = input('What the name of your website, username, and password all separtated by spaces and in that order? ').split(' ')
        #takes the imput for the name username and password of a website
        website_list.append(user_input[0])
        username_list.append(user_input[1])
        password_list.append(user_input[2])
        #adds the new values to the end of the 3 list created at the start
        if input(' Do you want to enter another password? ') == 'no':           #Asks the user if they want to move on - if yes continue the loop else break the loop
            break                           #Prints the list of the websites, usernames, and passwords

    all_stuff()
    call_password()
    if input('Are you done? ') == 'yes':
        break

f = open(r"C:\Users\oservedio27\Desktop\CS\Passwordkeeperforlder\passwordkeeperdoc.txt", 'w+')
for i in range(len(website_list)):
    f.write(website_list[i]) 
    f.write(',')
    f.write(username_list[i])
    f.write(',')
    f.write(password_list[i])
    if i + 1 != len(website_list):
        f.write('\n')