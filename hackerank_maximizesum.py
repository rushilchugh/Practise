__author__ = 'Rushil'

#3 3 9 9 5

from collections import defaultdict
from threading import Thread

n_t = int(input().strip())
m_list = []

m_dict = defaultdict(list)

for _ in range(n_t):
    (n,m) = tuple(map(int , input().strip().split(' ')))
    m_dict[m] = list(map(int,input().strip().split()))

def subsets(m_list,m):

    s = 0

    for i in range(len(m_list)):
        for j in range(i):
            temp_s = sum(m_list[j:i]) % m

            if temp_s > s:
                s = temp_s

    print(s)

def bitch():
    print('Hello')

for i,j in m_dict.items():
    Thread(target = subsets , args=(j,i,)).start()