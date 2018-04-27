#!/bin/python3

import sys

m_list = []

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n = int(n)
    k = int(k)
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    m_list.append([n,k,a])



def deck(total,min_num,t_list):
    att = []
    ab = []
    for i in t_list:
        if i <= 0:
            att.append(i)
        if i > 0:
            ab.append(i)

    if len(att) < min_num:
        return 'YES'
    else:
        return 'NO'



for i in m_list:
    print(deck(i[0],i[1],i[2]))

#print(deck(4,2,[0,-1,2,1]))