#!/usr/bin/env python3
add_arrays = __import__('4-line_up').add_arrays
def add_arrays(arr1, arr2):
    m = len(arr1)
    result = []
    if (len(arr1) == len(arr2)):
        for x in range(m):
            result.append(arr1[x] + arr2[x])
        return result
    return None

