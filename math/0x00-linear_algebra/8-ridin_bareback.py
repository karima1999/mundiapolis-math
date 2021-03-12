#!/usr/bin/env python3

mat_mul = __import__('8-ridin_bareback').mat_mul


def mat_mul(mat1, mat2):

    result = []
    if len(mat1[0]) == len(mat2):
        for i in range(len(mat1)):
            aux = []
            for a in range(len(mat2[0])):
                num = 0
                for j in range(len(mat1[i])):
                    num += mat1[i][j] * mat2[j][a]
                aux.append(num)
            result.append(aux)
        return result
    return None

