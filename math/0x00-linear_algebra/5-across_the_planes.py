#!/usr/bin/env python3
add_matrices2D = __import__('5-across_the_planes').add_matrices2D
def add_matrices2D(mat1, mat2):
    result = []
    if (len(mat1) == len(mat2)) and (len(mat1[0]) == len(mat2[0])):
        for x in range(len(mat1)):
            row = []
            for y in range(len(mat1[0])):
                row.append(mat1[x][y] + mat2[x][y])
            result.append(row)
            return result
    return None
