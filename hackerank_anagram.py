__author__ = 'Rushil'

from collections import defaultdict

def chk_anagram(str):

    n_count = 0

    str1 = sorted(list(str[:len(str)//2]))
    str2 = sorted(list(str[len(str)//2:]))

    dict_str1 = defaultdict(list)
    dict_str2 = defaultdict(list)

    if len(str1) !=  len(str2):
        return -1

    for i in range(1,26):
        dict_str1[i] = list()
        dict_str2[i] = list()

    for i in str1:
        dict_str1[ord(i) - 96].append(i)

    for i in str2:
        dict_str2[ord(i) - 96].append(i)

    print(dict_str1 , dict_str2 , sep = '\n')

    for i in range(1,26):
        len_a , len_b = len(dict_str1[i]) , len(dict_str2[i])
        if dict_str1[i] != dict_str2[i]:
            if len_a > len_b:
                n_count += len_a - len_b
            elif len_b > len_a:
                n_count += len_b - len_a
            elif len_a == len_b:
                n_count += len_a
        else:
            pass
    return n_count//2

#print(chk_anagram('xtnipeqhxvafqaggqoanvwkmthtfirwhmjrbphlmeluvoa'))

n = int(input().strip())
str_list = [input().strip() for i in range(n)]

for i in str_list:
    print(chk_anagram(i))