__author__ = 'Rushil'

import random

global arr
arr = []

"""
Instead of pairwise swaps I can also do a Binary Search on the array and do it O(N logN) complexity instead of O(N)
"""

def InsertionSort(arr, elem):

    arr.append(elem)

    for i in range(len(arr) - 1, 0, -1):

        if arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]             #Pairwise Swaps

        else:
            break

    return arr

for i in range(100):
    num = random.randint(0, 100)
    InsertionSort(arr, num)

