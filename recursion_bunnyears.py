__author__ = 'Rushil'

def BunnyEars(n):
    if n == 0:
        return 0
    else:
        return BunnyEars(n-1) + 2

print(BunnyEars(5))

