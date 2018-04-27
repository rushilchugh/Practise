__author__ = 'Rushil'

import time
import numpy as np

def sieve_of_eratosthenes(n):

    all_nums = list(range(2, n+1))

    for num_1 in all_nums:
        for num_2 in range(num_1+ 1, n+1):
            if num_2 % num_1 == 0:
                try:
                    all_nums.remove(num_2)
                except:
                    pass

    return all_nums


def sieve_of_eratosthenes_2(n):
    a = [True] * n                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, n, i):     # Mark factors non-prime
                a[n] = False


def sieve_of_eratosthenes_3(n):

    all_nums = dict(list(enumerate(list(range(0,n+1))))[2:])
    print(all_nums)

    for i in all_nums:
        for j in list(all_nums.values())[i::i]:
            print(i,j)
            try:
                all_nums[j] = False
            except:
                pass
        print(all_nums)
        all_nums[i] = True
    return all_nums

t1 = time.time()
print(sieve_of_eratosthenes(100))
t2 = time.time()
print('In Time: ' ,  t2 - t1)

t1 = time.time()
print(list(sieve_of_eratosthenes_2(100)))
t2 = time.time()
print('In Time: ' ,  t2 - t1)

t1 = time.time()
print(list(sieve_of_eratosthenes_3(100)))
t2 = time.time()
print('In Time: ' ,  t2 - t1)
