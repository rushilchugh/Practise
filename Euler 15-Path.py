__author__ = 'Rushil'

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

x = fact(40)
y = fact(20)

print(x/y**2)
