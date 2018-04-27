__author__ = 'Rushil'

import math

def MinCoins(array, n):

    if n == 0:
        return 0

    res = math.inf

    for i in range(len(array)):
        if array[i] <= n:
            min_coins = MinCoins(array, n - array[i])

            if min_coins + 1 < res:
                res = min_coins + 1

    return res


print(MinCoins([9, 6, 5, 1, 3], 12))