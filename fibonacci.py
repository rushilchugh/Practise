__author__ = 'Rushil'


fibdec = {1: 1, 2: 1}


def fib(n):

    global fibdec

    if n in fibdec.keys():
        return fibdec[n]
    else:
        fibdec[n] = fib(n - 1) + fib(n - 2)
        return fibdec[n]

print(fib(9))