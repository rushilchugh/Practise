__author__ = 'Rushil'

a0,a1,a2 = input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]

p_a = 0
p_b = 0

t_a = a0,a1,a2
t_b = b0,b1,b2

for i in range(len(t_a)):

    if t_a[i] > t_b[i]:
        p_a += 1

    elif t_a[i] < t_b[i]:
        p_b += 1

    elif t_a == t_b:
        pass

print(p_a , p_b)


