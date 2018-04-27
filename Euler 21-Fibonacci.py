__author__ = 'Rushil'

import time

import heapq

def fib(n):
    fib_dict = {1:1 , 2:1}
    if n == 2:
        return fib_dict[2]

    else:
        if n in fib_dict.keys():
            return fib_dict[n]

        else:
            fib_dict[n] = fib(n-1) + fib(n-2)
            return fib_dict[n]


a = 1
b = 0
n = 1
while len(str(a)) != 1000:
    a, b = a+b, a
    n += 1

print(a,n)

a = 1
b = 0
n = 1

while len(str(a)) != 1000:
    a,b = a+b,a
    n += 1

print(a,n)





