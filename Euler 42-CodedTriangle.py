__author__ = 'Rushil'

import re

word_file = open('words.txt' , 'r').read()
print(word_file)


name_list = re.findall(r'"[A-Z]+"' , word_file)

def get_pos(ch):
    return ord(ch) - 96

s = 0

def gen_t_num(n):
    for i in range(1,n):
        yield int(i*(i+1))//2

t_num_list = list(gen_t_num(100))
print(t_num_list)
for i in name_list:
    print(list(i[1:-1].lower()))
    sum_let = sum(list(map(get_pos , list(i[1:-1].lower()))))
    if sum_let in t_num_list:
        print(i,sum_let)
        s += 1

print(s)
