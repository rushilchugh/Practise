__author__ = 'Rushil'

from collections import Counter

n = int(input())
n_list = list(map(int, input().strip().split()))
a = Counter(n_list)

for i in range(max(a.keys()) + 1):
    if i in a:
        print(a[i], end = ' ')
    else:
        print(0, end = ' ')
