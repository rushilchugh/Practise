__author__ = 'Rushil'

fact_dict = {0:0 , 1:1 , 2:2 , 3:6 , 4:24 , 5:120}

from math import factorial

def fact(n):
    if n in fact_dict:
        return fact_dict[n]

    else:
        fact_dict[n] = n * fact(n-1)
        return fact_dict[n]

def dee_fact(n):
    n_list = list(str(n))
    n_list = list(map(int , n_list))
    return n_list

n = 5


num_dict = {}

while True:

    s = sum(list(map(factorial , dee_fact(n))))
    #print(num_sum , n)
    if s == n:

        print('--'*60)
        print(n,s)
        print('--'*60)
    #else:
    #    print(n,s)
    n += 1

