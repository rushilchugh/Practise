__author__ = 'Rushil'

import math



for p in range(1000,10,-1):
    #print(p)
    sol_list = []
    for i in range(1,p//4):
        for j in range(i,(p-i)//2):
            k = math.sqrt(i**2 + j**2)
            if i+j > k:
                pass
            else:
                break
            if k.is_integer():
                if p == i + j + k:
                    sol_list.append((i,j,k))
            else:
                pass
    if len(sol_list) != 0:
        print(p,sol_list)
