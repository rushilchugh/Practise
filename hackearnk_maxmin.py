__author__ = 'Rushil'

n = int(input().strip())
k = int(input().strip())

n_list = []

for _ in range(n):
    n_list.append(int(input().strip()))

min_init = 99999999999999

n_list.sort()

for i in range(n - k + 1):
    min_val = n_list[k + i - 1] - n_list[i]
    if min_val < min_init:
        min_init = min_val

print(min_init)