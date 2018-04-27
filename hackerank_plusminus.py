#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

p_list = []
m_list = []
z_list = []

for i in arr:
    if i > 0:
        p_list.append(i)
    if i < 0:
        m_list.append(i)
    if i == 0:
        z_list.append(i)

ma_list = m_list + p_list + z_list

print("%.5f" % (len(p_list)/len(ma_list)))
print("%.5f" % (len(m_list)/len(ma_list)))
print("%.5f" % (len(z_list)/len(ma_list)))

