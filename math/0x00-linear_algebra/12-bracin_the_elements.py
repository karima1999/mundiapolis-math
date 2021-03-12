#!/usr/bin/env python3
import numpy as np
def np_elementwise(mat1, mat2):
    return mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2
np_elementwise = __import__('12-bracin_the_elements').np_elementwise
