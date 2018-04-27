__author__ = 'Rushil'

(n,k) = tuple(map(int,input().strip().split()))
p_list = list(map(int,input().strip().split(' ')))

s = 0
n = 0

m_list = sorted(p_list)

for i in m_list:

    if s > k:
        n -= 1
        break

    s += i
    n += 1

print(n)