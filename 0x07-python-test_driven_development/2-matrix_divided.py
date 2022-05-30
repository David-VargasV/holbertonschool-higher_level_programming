#!/usr/bin/python3

"""Temporal"""


def matrix_divided(matrix, div):
    """"Temporal"""
    
    """Error Messages"""
    Type_error1 = "matrix must be a matrix (list of lists) of integers/floats"
    Type_error2 = "Each row of the matrix must have the same size"
    Type_error3 = "div must be a number"
    Zero_div = "division by zero"

    if type(matrix) != list:
        raise TypeError(Type_error1)
    if type(matrix[0]) != list:
        raise TypeError(Type_error1)
    if not matrix:
        raise TypeError(Type_error1)
    if type(div) != int and type(div) != float:
        raise TypeError(Type_error3)
    if div == 0:
        raise ZeroDivisionError(Zero_div)

    row = len(matrix[0])
    new = []

    for x in matrix:
        if type(x) != list:
            raise TypeError(Type_error1)
        if len(x) != row:
            raise TypeError(Type_error2)
        n_row = []
        for y in x:
            if type(y) != int and type(y) != float:
                raise TypeError(Type_error1)
            n_row.append(round(y/div, 2))
        new.append(n_row)
    return new
