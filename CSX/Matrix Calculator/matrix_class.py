import copy

class Matrix:
    def __init__(self, data):
        '''
        description: Initialize the Matrix Class and defines the # of rows and columns of the matrix
        args(array): takes in the array data which should be a matrix of any size
        returns: None
        '''
        self.data = data
        self.rows =  len(data)
        self.columns = len(data[0])


    def print_matrix(self):
        '''
        description: Prints matrix in proper formate
        arg(Matrix): self
        output: formatted matrix

        to do: - align columns
        '''
        for row in self.data: 
            print(row)


    def scalar_multiply(self, k, row):
        '''
        description: Multiplies a specified row of a matrix by a scalar 
        args(Matrix, int, int): self, the scaler that the row is being multiplied by, the row that should to be multiplied
        returns(array): the final matrix with the added changes
        '''

        if k.isalpha() == True or row <= 0 or row > self.rows or row.isalpha() == True:
            print('Make sure your inputs are in range and have the correct formatting')
            return

        final = []
        row -= 1    

        for i in range(self.rows):
            new_row = []
            for j in range(self.columns):
                if i == row:
                    new_row.append((self.data[i][j]) * k)
                else:
                    new_row.append(self.data[i][j])
            final.append(new_row)
        return final


    def add(self, M2):
        '''
        description: Adds two objects in the class matrix together
        args(Matrix, Matrix): self, Another matrix of the same size
        returns(array): the final matrix with the added changes
        '''
        if self.rows != M2.rows or self.columns != M2.columns:
            print('Your input matrixes need to have the same number of rows and columns ')
            return

        final = []
        # Because the matrices have to be the same size, self.rows and self.columns is used for both matrices
        for i in range(self.rows):
            new_row = []
            for j in range(self.columns):
                new_row.append((self.data[i][j]) + M2.data[i][j])
            final.append(new_row)
        return final
    

    def matrix_multiply(self, M2):
        '''
        description: Multiplies two objects in the class matrix together
        args(Matrix, Matrix): self, Another matrix where the number of rows is equal to the number of columns of the first matrix
        returns(array): the final matrix with the added changes

        to do: - check if the rows and columns line up
               - 
        '''

        if self.columns != M2.rows or self.rows != M2.columns:
            print('Number of columns in first matrix must = number of rows in second matrix an vice versa ')
            return None

        final = []

        # Makes an empty matrix with the dimensions of the final matrix
        for i in range(self.rows):
            new_row = []
            for j in range(M2.columns):
                new_row.append(0)
            final.append(new_row)

        for i in range(self.rows):                                  # Iterates through rows of first matrix
            for j in range(M2.columns):                             # Iterates through columns of second matrix
                for k in range(M2.rows):                            # rows of second matrix = columns of first matrix
                    # The final matrix will have the number of rows of the first matrix and the number of columns of the second matrix
                    final[i][j] += self.data[i][k] * M2.data[k][j]

        return final


    def switch_rows(self, first, second):
        '''
        description: Switches two rows of a matrix
        args(Matrix, int, int): self, the first row to be switched, the second row to be switched
        returns(Matrix): the final matrix with the rows swapped
        '''
        first_row = copy.deepcopy(self.data[first-1])
        second_row = copy.deepcopy(self.data[second-1])

        for row in range(len(self.data[0])):
            self.data[first-1][row] = second_row[row]

        for row in range(len(self.data[0])):
            self.data[second-1][row] = first_row[row]
        
    
    def liner_comb_reduce(self, mult, first, second):
        '''
        description: Adds a multiple of one row to another row
        args(Matrix, int, int, int): self, the multiplier, the first row, the second row
        returns(Matrix): the final matrix with the added changes
        '''
        first_row = copy.deepcopy(self.data[first-1])
        second_row = self.data[second-1]

        final = []
        for i in first_row:
            new_row = (i * mult)
            final.append(new_row)

        for i in final:
            second_row[final.index(i)] = second_row[final.index(i)]+i





M1 = Matrix([[1, 2, 4],
             [3, 4, 6]])

M2= Matrix([[1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]])

M3 = Matrix([[1, 1, 1],
            [1, 1, 1]])

(Matrix(M1.liner_comb_reduce(3, 1, 2))).print_matrix()