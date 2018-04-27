__author__ = 'Rushil'

import random

global arr

def InsertionSort(arr, elem):

    arr.append(elem)

    for i in range(len(arr) - 1, 0, -1):

        if arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]

        else:
            break

    return arr

arr = []

for i in range(100):
    num = random.randint(0, 100)
    InsertionSort(arr, num)
