#!/usr/bin/env python3
import numpy as np
def np_slice(matrix, axes={}):
    slices = []
    for i in range(len(matrix.shape)):
        if i in axes.keys():
            slices.append(slice(*axes[i]))
        else:
            slices.append(slice(None, None, None))
    return matrix[tuple(slices)]


