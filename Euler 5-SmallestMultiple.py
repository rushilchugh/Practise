def GCD(M, N):
    while (N != 0):
        M, N = N, M % N
    return M

LCM = 1
for X in range(1, 21):
    LCM = (X * LCM)/GCD(X, LCM)
print (LCM)