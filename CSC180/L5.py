'''
Created on 2013-10-21

@author: Joel
'''

def matrix_scale(mat, num):
    """(matrix, int)
    Updates mat by multiplying each of its elements by num.
    """

    for row in range(len(mat)):
        for cell in range(len(mat[0])):
            mat[row][cell] *= num
    return

def matrix_sum(mat1, mat2):
    """(matrix, matrix) --> matrix or None
    Returns a matrix that is the sum of the argument matrices.
    If the matrices do not have matching dimensions, None is returned.
    """

    rows = range(len(mat1))
    cols = range(len(mat1[0]))
    
    if rows == range(len(mat2)) and cols == range(len(mat2[0])):
        return [[mat1[row][cell] + mat2[row][cell] for cell in cols] for row in rows]

    return None

def matrix_sym(mat):
    """(matrix) --> bool or None
    Returns True if mat is symmetrical.
    Returns False if symmetry can be evaluated, but is false.
    Returns None if mat is not a square matrix.
    """
    
    rows = len(mat)
    cols = len(mat[0])
    
    if rows == cols:
        for row in range(rows):
            # checks only cells to the right of the diagonal from [0][0] to [max][max]
            for cell in range(row + 1, rows):
                if not mat[row][cell] == mat[cell][row]:
                    return False
                
        return True
    
    return None

def matrix_mul(mat1, mat2):
    """(matrix, matrix) --> matrix or None
    Returns a matrix that is the matrix product of mat1*mat2.
    Returns None if the inner dimensions of the arguments do not match.
    """
    
    cols1 = len(mat1[0])
    rows2 = len(mat2)
    
    if cols1 == rows2:
        rows1 = range(len(mat1))
        cols2 = range(len(mat2[0]))
        
        # make a matrix of 0's according to outer dimensions of arguments
        output = [[0 for x in cols2] for x in rows1]
        
        for row in rows1:
            for col in cols2:
                for i in range(cols1):
                    output[row][col] += mat1[row][i] * mat2[i][col]
        return output
    return None

def column_sum_square(mat):
    """(matrix) --> array
    Returns an array whose nth element is equal to the
    sum of the squares of the nth column in mat
    """
    
    rows = range(len(mat))
    cols = range(len(mat[0]))
    
    # make an array of 0's as long as mat has columns
    output = [0 for x in cols]
    
    for row in rows:
        for cell in cols:
            output[cell] += mat[row][cell] ** 2
    return output
