__author__ = 'Rushil'

import math

div_num  = {1:1 , 2:2 , 3:2 , 4:3 , 5:2 , 6:4 , 7:2 , 8:4 , 9:3 , 10:4 , 11:2 , 12:6}

def triang_num(n):
    return int((n*(n+1))/2)

print(triang_num(5))

def main_1():
    n = 1
    while True:
        num = triang_num(n)
        s = 1

        for i in range(1,num//2 + 1):
            if num % i == 0:
                s += 1
        print(num , s)
        if s > 500:
            break
        n += 1

#(n)(n+1)/2                 (n+1)(n+2)/2

def gen_un_ser():

    for i in range(1,20):
        print('(%d)(%d)/2' % (i,i+1) , end = '\t')
        print(int((i *(i+1))/2))

gen_un_ser()

def get_factors(t_num_n):
    for i in range(1,2*t_num_n):
        if i*(i+1) == 2*t_num_n:
            n = i

    return n,n+1

print(get_factors(36))

def get_stuff(n):
    c_tnum = int((n *(n+1))/2)
    return factors() + get_stuff(n-1)
