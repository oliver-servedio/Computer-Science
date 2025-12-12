class Matrix:
    def __init__(self, data):
        '''
        Description: Initialize the Matrix Class and defines the # of rows and columns of the matrix
        Args(array): takes in the array data which should be a matrix of any size
        '''
        self.data = data
        self.rows =  len(data)
        self.columns = len(data[0])


    def print_matrix(self):
        '''
        Description: Prints matrix in proper formate
        Arg(Matrix): self
        Output: formatted matrix
        '''
        for row in self.data: 
            print(row)


    def scalar_multiply(self, k, row):
        '''
        description: Multiplies a specified row of a matrix by a scalar 
        args(Matrix, int, int): self, the scaler that the row is being multiplied by, the row that should to be multiplied
        returns(array): the final matrix with the added changes
        '''
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
        args(Matrix, Matrix): self(the first matrix facilitating the function), Another matrix of the same size
        returns(array): the final matrix with the added changes
        '''
        final = []
        # Because the matrices have to be the same size, self.rows and self.columns is used for both matrices
        for i in range(self.rows):
            new_row = []
            for j in range(self.columns):
                new_row.append((self.data[i][j]) + M2.data[i][j])
            final.append(new_row)
        return final
    

    def matrix_multiply(self, M2):
        # takes another matrix as input; multiplies two matrices together
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
        first_row = self.data[first-1]

        print(first_row)
        second_row = self.data[second-1]

        for row in self.data[first-1]:
            test = first_row.index(row)
            print(first_row)
            self.data[first-1][test] = second_row[test]
        
        print(first_row)


        for row in self.data[second-1]:
            self.data[second-1][second_row.index(row)] = first_row[second_row.index(row)]
        
        print(self.data)




M1 = Matrix([[1, 2],
            [3, 4]])

M1.switch_rows(1, 2)