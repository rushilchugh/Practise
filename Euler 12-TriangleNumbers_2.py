__author__ = 'Rushil'

import math

def divisors(n):
    num_factors = 0

    for i in range(1,int(math.ceil(math.sqrt(n)))):
        if n % i == 0:
            num_factors += 2
        if i*i == n:
            num_factors -= 1

    return num_factors


for i in range(1,1000000):
    t_num_i = int((i *(i+1))/2)
    num_of_divisors = divisors(t_num_i)
    #print(i,t_num_i,num_of_divisors)
    if num_of_divisors > 500:
        print(i,t_num_i,num_of_divisors)
        break

