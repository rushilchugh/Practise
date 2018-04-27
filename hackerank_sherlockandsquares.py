__author__ = 'Rushil'

import math

n = int(input().strip())

m_list = []

for i in range(n):
    m_list.append(list(map(int,input().strip().split(' '))))

def do_stuff(a,b):
    s = 0
    r_a = math.ceil(math.sqrt(a))

    while r_a**2 <= b:
        s += 1
        r_a += 1

    return s

for i in m_list:
    print(do_stuff(*i))
