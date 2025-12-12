from matrix_class import Matrix

def input_matrix():
    '''
    Description: Takes user input to create a matrix of any size
    Args: None
    Returns(array): returns the matrix created by the user
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
        




M1 = Matrix([[0, 1, 0],
             [1, 2, 3], 
             [0, 0, 1]])

M2 = Matrix([[2, 1, 1],
            [-.5, -5, 0],
            [0, 0, 2]])

M3 = Matrix([[1, 0,],
            [0, .1],
            [2, 1]])

M1 = Matrix(input_matrix())

M2 = Matrix(input_matrix())

M1.print_matrix()

