__author__ = 'Rushil'

n = int(input().strip())

a = [input().strip() for _ in range(n)]

for i in a:
    print(int(i)+1)