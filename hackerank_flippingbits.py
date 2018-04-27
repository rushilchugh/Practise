__author__ = 'Rushil'

def dec_to_bin(n):
    n = int(n)
    a_num = bin(n)[2:]
    return '0' * (32-len(a_num)) + a_num

def flip(bin_num):
    bin_num = list(bin_num)
    for i,j in enumerate(bin_num):
        if j == '0':
            bin_num[i] = '1'
        if j == '1':
            bin_num[i] = '0'
    return ''.join(bin_num)

def bin_to_dec(bin_num):
    return int(bin_num , 2)

#print(dec_to_bin('2147483647'))
#print(flip('01111111111111111111111111111111'))
#print(bin_to_dec(flip('01111111111111111111111111111111')))

n = int(input().strip())

m_list = [input() for _ in range(n)]
#print(m_list)

for i in m_list:
    print(bin_to_dec(flip(dec_to_bin(i))))