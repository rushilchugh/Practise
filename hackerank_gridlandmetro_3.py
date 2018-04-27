__author__ = 'Rushil'

from collections import defaultdict

n,m,k = list(map(int,input().strip().split()))
m_list = []
m_dict = defaultdict(list)

for i_1 in range(k):
    m_list.append(list(map(int,input().strip().split())))

for v1,v2,v3 in m_list:
    m_dict[v1].append((v2,v3))

for val_1,val_2 in m_dict.items():
    print(val_1,sorted(val_2))

