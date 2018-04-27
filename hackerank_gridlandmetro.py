__author__ = 'Rushil'

import numpy as np

m,n,k = list(map(int,input().strip().split()))
m_list = []

for i in range(k):
    m_list.append(list(map(int,input().strip().split())))

print(m_list)

m_array = np.ones((m,n))

for j in m_list:
    row_np = j[0]-1
    col_st = j[1]-1
    col_en = j[2]-1
#    print(row_np , col_st , col_en)
    m_array[row_np , col_st:col_en+1] = 0

print(m_array)
print(int(m_array.sum()))
