run = input('Do you want to use the calulator ')     
while run == 'yes' or run == 'Yes':
    choice = input('Do you want to add, subtract, multiply or divide ')
   
    if choice == 'add':
        amount = input('how many nubers do you want to add 2, 3, or 4? ')
        if amount == '2':
             x = input('Give me your first number ' )
             y = input('Give me your second number ' )
             print(int(x)+int(y))
        elif amount == '3':
             x = input('Give me your first number ' )
             y = input('Give me your second number ' )
             z = input('Give me your third number ')
             print(int(x)+int(y)+int(z))
        elif amount == '4':
             x = input('Give me your first number ' )
             y = input('Give me your second number ' )
             z = input('Give me your third number ')
             a = input('Give me your fourth number ')
             print(int(x)+int(y)+int(z)+int(a))
    elif choice == 'subtract':
        amount = input('how many nubers do you want to add 2, 3, or 4? ')
        if choice == 2:
            print(int(x)-int(y))
        #elif choice == 3:

        #elif choice == 4:
            
    elif choice == 'multiply':
        print(int(x)*int(y))
    elif choice == 'divide':
        print(int(x)/int(y))
    run = input('Do you want to use the calulator ')
