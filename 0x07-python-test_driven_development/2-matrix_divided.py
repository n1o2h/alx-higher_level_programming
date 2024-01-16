#!/usr/bin/python3
"""
This is a module documontation
"""

def matrix_divided(matrix, div):
    """
    Return a new matrix where each element has been divided by div.
    Args:
        matrix (list): list of lists integers or floats.
        div (int, float): the divider, >= 0.
    """

     mtrx_type_a = 'matrix must be a matrix (list of lists) of integers/floats'
    mtrx_len_a = 'Each row of the matrix must have the same size'
    div_type_a = 'div must be a number'
    div_zero_a = 'division by zero'

    row_len = 0
    if type(matrix) is not list:
        raise TypeError(mtrx_type_a)

    for row in matrix:
        if type(row) is not list:
            raise TypeError(mtrx_type_a)
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError(mtrx_type_a)
        if len(row) is not row_len and row_len is not 0:
            raise TypeError(mtrx_len_a)
        row_len = len(row)

    if type(div) not in [int, float]:
        raise TypeError(div_type_a)
    if div is 0:
        raise ZeroDivisionError(div_zero_a)

    return [[round(nb / div, 2) for nb in row] for row in matrix]
