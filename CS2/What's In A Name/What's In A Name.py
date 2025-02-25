'''
Name: Oliver Servedio
Date: 3/1/2025
Description: A selection of different string functions made without using built in string functions
Bugs: None
Features: Bonus functions
Sources: 
Log: 1.0 initial version 
'''

from collections import Counter
import random as r

def reverse_and_display(string):
    '''
    Description: Reverses and displays a str
    Takes: A str
    Returns: the reversed str
    '''
    final_word = []
    word = list(string)
    for letter in word:
        final_word.insert(0, letter)
    final_word = ''.join(final_word)
    return final_word

def num_vowels(name):
    '''
    Description: returns the number of each vowel in a str
    Takes: str
    Returns: sorted dict
    '''
    name = lower_case(name)
    vowels = list('aeiouy')
    vowels_in_name = []
    for letter in name:
        if letter in vowels:
            vowels_in_name.append(letter)

    return Counter(vowels_in_name)

def num_consonants(name):
    '''
    Description: returns the number of each consonant in a str
    Takes: str
    Returns: sorted dict
    '''
    name = lower_case(name)
    consonants = list('bcdfghjklmnpqrstvwxz')
    consonants_in_name = []
    for letter in name:
        if letter in consonants:
            consonants_in_name.append(letter)
    return Counter(consonants_in_name)

def first_name(name):
    '''
    Description: Returns the first name of a name
    Takes: str - name
    Returns: str - first name
    '''
    name = title_remove(name)
    name = name.split(' ')
    return name[0]

def last_name(name):
    '''
    Description: Returns the last name of a name
    Takes: str - name
    Returns: str - last name
    '''
    name = title_remove(name)
    name = name.split(' ')
    return name[-1]

def middle_name(name):
    '''
    Description: Returns the middles name/names of a name
    Takes: str - name
    Returns: str - middle name/names
    '''
    name = title_remove(name)
    name = name.split(' ')
    if len(name) > 2:
        name.pop(-1) and name.pop(0)
        name = ' '.join(name)
        return name
    return 'no middle name'

def last_name_hyphen(name):
    '''
    Description: returns boolean depending on if last name has hyphen
    Takes: str - name
    Returns: boolean
    '''
    name = title_remove(name)
    name = name.split(' ')
    for i in name[-1]:
        if i == '-':
            return True
    return False

def upper_case(name):
    '''
    Description: Makes str upper case
    Takes: str
    Returns: str.upper
    '''
    lower_list = list('abcdefghijklmnopqrstuvwxyz')
    new_name = []
    for character in name:
        if character in lower_list:
            new_name.append(chr(ord(character)-32))
        else:
            new_name.append(character)
    return ''.join(new_name)

def lower_case(name):
    '''
    Description: makes a str lower case
    Takes: str
    Returns: str.lower
    '''
    upper_list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    new_name = []
    for character in name:
        if character in upper_list:
            new_name.append(chr(ord(character)+32))
        else:
            new_name.append(character)
    return ''.join(new_name)

def random_name(name):
    '''
    Description: Takes a str and randomly arranges the letters
    Takes: str
    Returns: str
    '''
    new_name = []
    name = list(name)
    while len(name) > 0:
        ran_num = r.randrange(-1,len(name))
        letter = name[ran_num]
        name.remove(letter)
        new_name.append(letter)
    return ''.join(new_name)

def palindrome(name):
    '''
    Description: Checks if the first name is a palindrome
    Takes: str - name
    Returns: boolean - True if it is a palindrome
    '''
    final_word = []
    word = list(first_name(name))
    for letter in word:
        final_word.insert(0, letter)
    final_word = ''.join(final_word)
    if lower_case(final_word) == lower_case(first_name(name)):
        return True
    return False

def sort_name(name):
    '''
    Description: Sorts a str alphabetically 
    Takes: str
    Returns: sorted str
    '''
    name_list = list(name)
    name_list.sort()
    return ''.join(name_list)

def initials(name):
    '''
    Description: Finds the addition in a name
    Takes: Str
    Returns: initials
    '''
    initials_list = []
    name = title_remove(name)
    for word in name.split(' '):
        initials_list.append(list(word)[0])
    return upper_case(''.join(initials_list))

def have_title(name):
    '''
    Description: Checks if name contains title
    Takes: str
    Returns: Boolean based off if has title
    '''
    name = name.split(' ')
    for i in name:
        if i in ['Dr.', 'Sir', 'Esq', 'Ph.D', 'Doctor', 'reverend', 'Sr', 'Senior', 'Prince', 'King', 'Professor','Private', 'Private second class', 'Private first class','Specialist', 'Corporal', 'Sergeant', ' Staff sergeant', 'Sergeant first class', 'Master sergeant','First sergeant',  'Sergeant major','Command sergeant major', 'Sergeant major', 'Second lieutenant', 'First lieutenant', 'Captain', 'Major','Lieutenant colonel', 'Colonel', 'Brigadier general', 'Major general']:
            return True
    return False

def title_remove(name):                             # Not a required function but used in other functions
    '''
    Description: removes titles
    Takes: Str
    Returns: initials
    '''
    name_list = name.split(' ')
    for i in ['Dr.', 'Sir', 'Esq', 'Ph.D', 'Doctor', 'reverend', 'Sr', 'Senior', 'Prince', 'King', 'Professor','Private', 'Private second class', 'Private first class','Specialist', 'Corporal', 'Sergeant', ' Staff sergeant', 'Sergeant first class', 'Master sergeant','First sergeant',  'Sergeant major','Command sergeant major', 'Sergeant major', 'Second lieutenant', 'First lieutenant', 'Captain', 'Major','Lieutenant colonel', 'Colonel', 'Brigadier general', 'Major general']:
        if i in name_list:
            name_list.remove(i)
    return ' '.join(name_list)

def swapcase(name):
    '''
    Description: Swaps the case of each letter
    Takes: Str
    Returns: Str
    '''                                 # Bonus Function
    upper_list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    lower_list = list('abcdefghijklmnopqrstuvwxyz')
    new_name = []
    for character in name:
        if character in upper_list:
            new_name.append(chr(ord(character)+32)) # Changes to ord than adds to change case then converts back
        elif character in lower_list:
            new_name.append(chr(ord(character)-32)) # Changes to ord than subtracts to change case then converts back
        else:
            new_name.append(character)
    return ''.join(new_name)


def main():
    '''
    Description: It is just a place to run each function
    Takes: Str - Your name and the number corresponding to what action you want to take
    Returns: the function that the user wants to call
    '''
    name = input('What is your name ')
    while True:
        choice = input(f'''
        Original Input = {name}
        1. Reverse and display
        2. Determine the number of vowels. You can prompt user for a particular vowel or
        create subtotals of each.
        3. Consonant frequency. Bonus: Subtotals of each consonant
        4. Return first name.
        5. Return last name.
        6. Return middle name(s)
        7. Return boolean if last name contains a hyphen
        8. Function to convert to lowercase
        9. Function to convert to uppercase
        10. Modify array to create a random name (mix up letters)
        11. Return boolean if first name is a palindrome
        12. Return full-name as a sorted array of characters (Bonus)
        13. Make initials from name
        14. Return boolean if name contains a title/distinction (“Dr.”, “Sir”, “Esq”, “Ph.d”)
        (Bonus)
        15. Change Case
        16. Secret Bonus ---See me
        17. Exit Code

        What do you want do do? Answer with a number. 
        ''')

        if choice == '1':
            print(reverse_and_display(name))
        elif choice == '2':
            print(num_vowels(name))
        elif choice == '3':
            print(num_consonants(name))
        elif choice == '4':
            print(first_name(name))
        elif choice == '5':
            print(last_name(name))
        elif choice == '6':
            print(middle_name(name))
        elif choice == '7':
            print(last_name_hyphen(name))
        elif choice == '8':
            print(lower_case(name))
        elif choice == '9':
            print(upper_case(name))
        elif choice == '10':
            print(random_name(name))
        elif choice == '11':
            print(palindrome(name))
        elif choice == '12':
            print(sort_name(name))
        elif choice == '13':
            print(initials(name))
        elif choice == '14':
            print(have_title(name))
        elif choice == '15':
            print(swapcase(name))
        # elif choice == '16':
            
        elif choice == '17':
            break
        else:
            print('Your input is incorrect ')
    

main()