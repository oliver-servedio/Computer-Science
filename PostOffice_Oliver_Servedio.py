'''
Name: Oliver Servedio
Description: This code takes in information about mailing a package and returns the price to mail
Bugs: None
Features: None
Sources: Mr. Campbell, W3Schools
Log: 1.0 initial version 
'''

def package_type(length, height, width):
    '''
    Determines the type of mail based on the length, height and width

    Args:
        (float): The length, width and height of the mail
    Returns:
        (float): The cost of mailing the packages and the prices per zone
    Raises:
        (str): If the packages dimensions do not match any of the requirements
    '''
    
    # Post Card
    if 3.5 <= length <= 4.5 and 3.5 <= height <= 6.0 and .007 <= width <= .016:
        return [.20, .03]

    # Large Post Card    
    elif 4.25 <= length <= 6 and 6 <= height <= 11.5 and .007 <= width <= .015:
        return [.37, .03]
    
    # Envelope
    elif 3.5 <= length <= 6.125 and 5 <= height <= 11.5 and .016 <= width <= .25:
        return [.37, .04]  
             
    # Large Envelope
    elif 6.125 <= length <= 25.0 and 11 <= height <= 18 and .25 <= width <= .5:
        return [.6, .05]  
              
    # Package 
    elif 36.0 <= (length + (2*height) + (2*width)) <= 84.0:
        return [2.95, .25]          
    
    # Large Package
    elif 84.0 < (length + (2*height) + (2*width)) <= 130.0:
        return [3.95, .35]          
    
    else:
        print('Unmailable')
        exit()


def find_zone(zip):
    '''
    Determines the zone from a zip

    Args:
        (int): The location of where the mail starts and where the mail ends
    Returns:
        (int): The zone number
    Raises:
        (str): if the zone does not exist
    '''
    
    if 1 <= zip <= 6999:
        return 1
    elif 7000 <= zip <= 19999:
        return 2
    elif 20000 <= zip <= 35999:
        return 3
    elif 36000 <= zip <= 62999:
        return 4
    elif 63000 <= zip <= 84999:
        return 5
    elif 85000 <= zip <= 99999:
        return 6
    else:
        print('Zone does not exist')
        exit()

def main():

    '''
    Determines the price to mail the package based on the data received: length, height, width, starting zip, ending zip

    Args:
        (list): The package data that is imputed by the user in the order of length, height, width, starting zip, ending zip
    Returns:
        (str): The cost to mail the package
    Raises:
        (Value Error): if the user inputs the wrong data type or the wrong amount of data gives the user an error message and prompts them to try again
    '''

    package_data = input('length, height, width, starting zip, ending zip ').split(',')

    # Checks if the user entered five points of data and if they did not then give them an error message and exit the program
    if len(package_data) != 5:
        print('Make sure you only put 5 values in. Run the program again. ')
        exit()

    # Try's to call functions and change data type of str
    try:
        package_costs = package_type(float(package_data[0]), float(package_data[1]), float(package_data[2]))         # Set a variable equal to the package_type function with the float of the first 3 values of package_data
        distance = abs(find_zone(int(package_data[3])) - find_zone(int(package_data[4])))                         # 
    # If the code in the try does not work runs the code in the except
    except: 
        print('Make sure you are only entering in integers or floats. Also check that your package and zones are within the requirements to mail. Run the program again')
        exit()

    # determines the final cost of the package, removes the zero off the front if there is one and then split the final cost into a list by the decimal
    final_cost = ((str(package_costs[0] + (package_costs[1])*(distance))).strip('0')).split('.')
    
    # Continuously checks if the length of numbers after the decimal are <= 1 and if they are add a zero to the end of the cost
    while len(final_cost[1]) <= 1:
        final_cost[1] += "0"
    
    # Joins the final_cost list into one str using a decimal to join them
    final_cost = ".".join(final_cost)
    print(final_cost)

main()
