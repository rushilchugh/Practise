__author__ = 'Rushil'

import math

def trail_zeroes(n):

    i = 1
    s = 0
    while 5**i <= n:
        s += n // 5**i
        i += 1

    return s

def last_n_0(n):

    base_dict = {0:1 , 1:1 , 2:2 , 3:6 , 4:4 , 5:2 , 6:2 , 7:4 , 8:2 , 9:8 , 10:8}

    n_10 = (n // 10) % 10

    if n_10 % 2 != 0 and n > 10:
        return (4 * (last_n_0(math.ceil(n/5)))) * last_n_0(n % 10)

    elif n_10 % 2 == 0 and n > 10:
        return (6 * (last_n_0(math.ceil(n/5)))) * last_n_0(n % 10)

    else:
        return base_dict[n]


print(trail_zeroes(200))
print(last_n_0(50))