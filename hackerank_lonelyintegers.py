__author__ = 'Rushil'

from collections import defaultdict

count_implt = defaultdict(int)

n = int(input().strip())

num_array = input().strip()

for i in num_array.split(' '):
    count_implt[i] += 1

for i,j in count_implt.items():
    if j == 1:
        print(i)
