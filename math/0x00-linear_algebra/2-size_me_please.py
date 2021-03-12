#!/usr/bin/env python3
matrix_shape = __import__('2-size_me_please').matrix_shape
def matrix_shape(matrix):
   if type(matrix[0]) is not list:
        return [len(matrix)]
    else:
        return [len(matrix)] + matrix_shape(matrix[0])
