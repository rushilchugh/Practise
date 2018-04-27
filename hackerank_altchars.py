__author__ = 'Rushil'

import itertools

def do_stuff(str):
    n_del = 0
    for i, j in itertools.groupby(str):
        len_list = len(list(j))
        if len_list > 1:
            n_del += len_list - 1
    return n_del

n = int(input().strip())

str_list = []
for i in range(n):  str_list.append(input())

for i in str_list:
    print(do_stuff(i))
