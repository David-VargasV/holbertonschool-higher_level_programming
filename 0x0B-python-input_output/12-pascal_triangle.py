#!/usr/bin/python3
'''Pascal's Triangle'''


def pascal_triangle(n):
    ''' function that returns Pascal’s triangle'''
    if n <= 0:
        return []

    p_triangle = [[1]]

    for p in range(n - 1):
        row = [0] + p_triangle[-1] + [0]
        t = []
        for x in range(len(p_triangle[-1]) + 1):
            t.append(row[x] + row[x + 1])
        p_triangle.append(t)
    
    return p_triangle
