__author__ = 'Rushil'

def mult(n,m):
    if m == 1:
        return n
    else:
        return n + mult(n,m-1)

print(mult(5,5))
