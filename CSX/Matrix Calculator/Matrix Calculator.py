
from matrix_class import Matrix

def input_matrix():
    '''
    Description: Takes user input to create a matrix of any size
    Args: None
    Returns(array): returns the matrix created by the user

    To do: - non-numeric inputs
           - rows with different lengths
           - empty inputs
    '''
    
    row_num = int(input('how many rows would you like your matrix to be? '))

    print('Note: all of your rows need the same amount of points')
    matrix = []
    for i in range(row_num):
        row = input(f'For row {i+1} input your row numbers with the numbers separated by commas ')
        row = row.split(',')

        for item in row:
            if '/' in item: 
                equation = item.split('/')
                num = int(equation[0])/int(equation[1])
                row[row.index(i)] = num

        matrix.append(row)
    return matrix
        

def main():
    user = input(f'''What function would you like to run
            1: print_matrix
            2: scalar_multiply
            3: add
            4: matrix_multiply
            5: switch_rows
            6: liner_comb_reduce''')
    
    if user == '1':
        M1 = Matrix(input_matrix('What matrix do you want to print '))
    
    if user == '2':
        M1 = Matrix(input_matrix('What is your first matrix multiply '))
        scalar = input('what is your scalar input? ')
        row = input('what row do you want to multiply by ')
        M3 = M1.scalar_multiply(scalar, row)
    
    elif user == '3':
        M1 = Matrix(input_matrix('What is your first matrix to add '))
        M2 = Matrix(input_matrix('What is your second matrix to add: they have to be the same size '))
        M3 = Matrix(M1.add(M2))
        M3.print_matrix()
    
    elif user == '4':
        M1 = Matrix(input_matrix('What is your first matrix to multiply '))
        M2 = Matrix(input_matrix('What is your second matrix to multiply: size matters '))
        M3 = Matrix(M1.matrix_multiply(M2))






# M1 = Matrix(input_matrix())

M2 = Matrix([[1, 0, 0],
            [2, 1, 2],])

M3 = Matrix([[2, 1,],
            [0, -3]])

# MA = Matrix(input_matrix())

# MB = Matrix(input_matrix())

# MC = Matrix(input_matrix())


# MA.matrix_multiply(MB)

# MB.matrix_multiply(MA)


Matrix(M2.matrix_multiply(M3)).print_matrix()

Matrix(M3.matrix_multiply(M2)).print_matrix()




