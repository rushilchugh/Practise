__author__ = 'Rushil'

n1 = int(input().strip())
n2 = int(input().strip())

max = 0

for i in range(n1,n2+1):
    for j in range(i,n2+1):
        if i^j > max:
            max = i^j

print(max)