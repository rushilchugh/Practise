__author__ = 'Rushil'

import random

def SpecialNumbers(array):

    di = {}
    array.sort()

    for i in array:
        di[i] = False

    for index, i in enumerate(array):
        for j in array[index + 1:]:
            if j % i == 0:
                di[j] = True

    return di

print(SpecialNumbers([random.randint(1, 100000) for _ in range(100)]))