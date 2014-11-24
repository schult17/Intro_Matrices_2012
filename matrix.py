def matrix_scale(mat,num):
    '''(matrix, int) -> matrix

    takes a matrix 'mat' and an integer 'num' and returns a new matrix

    of the elements of 'mat' multiplied by 'num'
    '''
    
    for i in range(len(mat)):

        for j in range(len(mat[i])):

            mat[i][j] = mat[i][j] * num
            
    return mat


def matrix_sum(mat1,mat2):
    ''' (matrix, matrix) -> matrix

    takes two matrices 'mat1' and 'mat2' and returns the sum of two matrices
    '''

    #conditional statement checking for matrices with same dimensions
    if (len(mat1) == len(mat2) and len(mat1[0]) == len(mat2[0])):
    
        mat_result = []

        for i in range(len(mat1)):

            #store each row in a temporary list
            row = []

            for j in range(len(mat2)):

                row.append(mat1[i][j] + mat2[i][j])

            #appends temporary list 'row' to final output
            mat_result.append(row)
            

        return mat_result

    else:

        return None


def matrix_sym(mat):
    '''(matrix) -> bool

    takes a matrix 'mat', and returns a bool variable: true if matrix

    is symmetrical or false if not symmetrical
    '''

    #conditional statement checking for a square (nxn) matrix (rows = columns)
    if len(mat) == len(mat[0]):

        #sends the matrix to the transpose() function
        #and checks if the transpose equal to the original
        if mat == transpose(mat):

            return True
        
        else:
            
            return False

    else:

        return None

   
def matrix_mul(mat1, mat2):
    '''(matrix, matrix) -> matrix

    takes two matrices, 'mat1' and 'mat2' and returns a new matrix

    which is the matrix multiplication of 'mat1' and 'mat2'
    '''

    #conditional statement checking for matrix multiplication compatibility.
    #inner dimensions must be equal (ie mxn nxm or nxm mxn) 
    if (len(mat1) == len(mat2[0]) or len(mat1[0]) == len(mat2)):

        #creates an empty list matrix with the same amount of
        #rows as mat2 and same number of columns as mat1
        result = [[0 for row in range(len(mat2[0]))] \
                  for col in range(len(mat1))]

        for i in range(len(mat1)):

            for j in range(len(mat2[0])):

                for k in range(len(mat1[0])):

                    result[i][j] += mat1[i][k] * mat2[k][j]

        return result

    else:

        return None


def column_sum_square(mat):
    '''(matrix) -> matrix

    takes a matrix 'mat' and returns a new matrix which is sum of the

    squares of each column in 'mat'
    '''
    
    #temporary list matrix to store data
    temp = []

    #square all terms in mat and store them to temp
    for i in range(len(mat)):

        row = []

        for j in range(len(mat[i])):

            row.append(mat[i][j] ** 2)

        temp.append(row)

    #transpose the temporary list to switch rows and columns
    trans_squares = transpose(temp)

    #create an output list to hold sum of squares with the same
    #amount of elements as rows in mat
    final = [0] * len(mat[0])

    #sums rows and stores them to output list final
    for i in range(len(trans_squares)):

        final[i] += sum(trans_squares[i])

    return final


def transpose(mat):
    '''(matrix) -> matrix

    takes a matrix 'mat' and returns the transpose of that matrix
    '''
    
    output = []
        
    for i in range(len(mat[0])):
        
        temp = []
        
        for j in range(len(mat)):
            
            temp.append(mat[j][i])
            
        output.append(temp)

    return output
