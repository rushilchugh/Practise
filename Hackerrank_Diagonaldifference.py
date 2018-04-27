__author__ = 'Rushil'

n = int(input().strip())
a = []

for a_i in range(n):
   a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
   a.append(a_t)

def get_diag_a(a):
    d_1 = []
    for j in range(n):
        d_1.append(a[j][j])
    return d_1

def get_diag_b(a):
    d_2 = []
    for j in range(n):
        d_2.append(a[j][(n-1)-j])
    return d_2

d1 = get_diag_a(a)
d2 = get_diag_b(a)


print(abs(sum(d1) - sum(d2)))

