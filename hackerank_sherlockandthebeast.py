__author__ = 'Rushil'

def get_decent_num(n):

    num = n

    if n <= 2:
        return -1

    else:
        while n % 3 != 0:
            n -=5
        if n < 3 and n != 0:
            return -1

        return '5'*n + '3'*(num-n)

t = int(input().strip())

n = []

for a0 in range(t):
    n.append(int(input().strip()))

for i in n:
    print(get_decent_num(i))
