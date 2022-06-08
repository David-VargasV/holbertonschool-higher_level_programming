#!/usr/bin/python3
'''Pascal's Triangle'''


def pascal_triangle(n):
    ''' function that returns Pascal’s triangle'''
    if n <= 0:
        return []

    p_triangle = [[1]]

    for p in range(1, n):
        it = [1]
        for t in range(1, p):
            it.append(p_triangle[p-1][t-1] + p_triangle[p-1][t])
        it.append(1)
        p_triangle.append(it)
    return p_triangle
