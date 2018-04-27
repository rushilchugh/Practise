__author__ = 'Rushil'

s = 0
for i in range(1,1000000):
    bin_i = bin(i)[2:]
    str_i = str(i)
    if str_i[::-1] == str_i and bin_i[::-1] == bin_i:
        s += i

print(s)
