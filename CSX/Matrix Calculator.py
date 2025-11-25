class Matrix:
    def __init__(self, data):
        # Find Rows and Colum number, data is just the full matrix
        self.data = data
        self.rows =  len(data)
        self.columns = len(data[0])


    def print_matrix(self):
        # Prints matrix in proper format
        for row in self.data: 
            print(row)


    def scalar_multiply(self, k):
        # Takes an int; Multiplies a matrix by the int 
        final = []

        for i in range(self.rows):
            new_row = []
            for j in range(self.columns):
                new_row.append((self.data[i][j]) * k)
            final.append(new_row)
        return final


    def add(self, M2):
        # takes another matrix as input; adds two matrices together
        final = []
        # Bc the matrices have to be the same size, self.rows and self.columns is used for both matrices
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

        



M1 = Matrix([[200000, 3],
             [1, 1], 
             [5, -2]])

M2 = Matrix([[4, 5],
             [2, 2]])


M1.print_matrix()
# (Matrix(M2.scalar_multiply(2))).print_matrix()