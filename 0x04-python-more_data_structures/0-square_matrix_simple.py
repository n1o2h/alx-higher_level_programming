#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq_matrix = matrix.copy()
    for x in range(len(matrix)):
        sq_matrix[x] = [n ** 2 for n in matrix[x]]
    return sq_matrix
