__author__ = 'Rushil'

#SetCount(x) - Number of ones in an binary number x
#Johnny wants to find a binary number, D, that is the smallest binary number >B where setCount(B) = setCount(D)
#He then wants to compress D into an array of integers,C (in the same way that integer array A contains the compressed form of binary string B).
#Values in even represents consecutive 1
#Values in odd represents consecutive 0

from itertools import groupby
import re

#Given input 4 1 3 2 4

def get_bin_rep(num):

    inp_text = num.replace(' ','')
    f_str = ''

    for index,char in enumerate(inp_text):
        if index % 2 == 0:
            f_str += '1'*int(char)
        else:
            f_str += '0'*int(char)

    return f_str

def get_other_bin(bin_num):

    occ_0 = 0

    bin_num = list(bin_num)

    if bin_num[-1] == '0':
        f1_index = ''.join(bin_num).rfind('1')
        bin_num[-1] = '1'
        bin_num[f1_index] = '0'
        return ''.join(bin_num)

    for index,i in enumerate(bin_num):
        if i == '0':
            occ_0 = index

    bin_num[occ_0] = '1'
    bin_num[occ_0 + 1] = '0'

    return ''.join(bin_num)

def make_rep(bin_num):
    #11110111010111
    f_str = ''
    for i,j in groupby(bin_num):

        f_str += str(len(list(j)))
        f_str += ' '
    return f_str

#
#print(get_other_bin('11110111001111'))
#print(make_rep('11110111001111'))
#print(make_rep(get_other_bin(get_bin_rep('4 1 3 2 4'))))

n = int(input().strip())

m_list = []

for i in range(n):
    w_len = input().strip()
    m_word = input().strip()
    m_list.append(m_word)

for i in m_list:
    f_sol = make_rep(get_other_bin(get_bin_rep(i)))
    print(len(f_sol))
    print(f_sol)


