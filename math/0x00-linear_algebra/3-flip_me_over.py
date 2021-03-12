#!/usr/bin/env python3
matrix_transpose = __import__('3-flip_me_over').matrix_transpose
def matrix_transpose(matrix):
    matrix_t = []
    m = len(matrix)
    n = len(matrix[0])
    for x in range(0, n):
        row = []
        for y in range(0, m):
            row.append(matrix[y][x])
        matrix_t.append(row)
    return matrix_t

