__author__ = 'Rushil'

def count7(n):
    if n == 0:
        return 0
    if n%10 == 7:
        return 1 + count7(n//10)
    else:
        return count7(n//10)


print(count7(77177))