__author__ = 'Rushil'

def mult_3(n):
    if n == 1:
        return 3
    else:
        return 3*mult_3(n-1)

print(mult_3(5))