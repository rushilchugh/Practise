__author__ = 'Rushil'

from itertools import combinations

def get_m_string(str_inp):
    m_list = []
    for i in range(1,len(str_inp)+1):
        for j in combinations(str_inp,i):
            m_list.append(''.join(j))

    return set(sorted(m_list))

print(get_m_string('abcd'))