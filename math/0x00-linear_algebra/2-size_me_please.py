#!/bin/usr/env python3
def matrix_shape(matrix):
    res = []
    res.append(len(matrix))
    res.append(len(matrix[0]))
    if len(matrix[0]) > 2:
        res.append(len(matrix[0][0]))
    return (res)
