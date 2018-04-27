__author__ = 'Rushil'

def f_pow(n):
    s = 0
    num_list = list(map(int , list(str(n))))
    for i in num_list:
        s += i**5
    return s

n = 10

s = 0

while True:
    if n == f_pow(n):
        s += n
        print(n)
    n += 1


print(n)