__author__ = 'Rushil'

"""
Merge Sort -

Recursively sort the 1st half of teh array
Recursively sort the 2nd half of teh array
Merge the sorted arrays

Base Case -
IF 0 or 1 elements in an array, they're already sorted and they're returned as is

Merge Subroutine -
C = Output array of size N
A - 1st sorted array
B - 2nd sorted array
i = 1
j = 1

for k = 1 to n
    if A[i] < B[j]
        C[k] = A[i]
        i++

    if B[j] < A[i]
        C[k] = A[i]
        j++

"""

import random


# noinspection PyPep8Naming
def SplittingTheArray(arr):

    if len(arr) == 1:
        return arr

    middle = int(len(arr) / 2)

    ar_1 = SplittingTheArray(arr[:middle])
    ar_2 = SplittingTheArray(arr[middle:])

    sr_array, i_1, i_2 = MergeSortedArrays(ar_1, ar_2)

    sr_array += ar_1[i_1:]
    sr_array += ar_2[i_2:]

    return sr_array

def MergeSortedArrays(arr_1, arr_2):

    i = 0
    j = 0

    aux_array = []

    while i < len(arr_1) and j < len(arr_2):

        if arr_1[i] < arr_2[j]:
            aux_array.append(arr_1[i])
            i += 1

        else:
            aux_array.append(arr_2[j])
            j += 1

    return aux_array, i, j

t_array = [random.randint(0, 100) for _ in range(10)]
t_array = [37, 56, 63, 80, 38, 56, 15, 67, 43, 10]
SplittingTheArray(t_array)
















