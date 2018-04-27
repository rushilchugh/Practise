__author__ = 'Rushil'

from collections import defaultdict

def grid_input():
    n = int(input().strip())
    nt_dict = defaultdict(list)
    for _ in range(n):
        n_t = int(input().strip())
        nt_dict[n_t] = [input().strip() for _ in range(n_t)]
        #nt_dict[n_t].append([input().strip() for _ in range(n_t)])

    return nt_dict


def bub_sort(alphs):
    for _ in range(len(alphs)):
        for i,j in enumerate(alphs):
            try:
                if alphs[i] > alphs[i+1]:
                    alphs[i] , alphs[i+1] = alphs[i+1] , alphs[i]
            except:
                pass
    return alphs

input_entry = grid_input()
print(input_entry)

for num_elems,elem_list in input_entry.items():

    m_list = []
    m_list_2 = []

    for elem in elem_list:
        sort_elem = bub_sort(list(elem))
        m_list.append(sort_elem)
        #print(elem,''.join(sort_elem))

    m_list = [''.join(i) for i in m_list]

    for i in range(len(m_list[0])):
        m_list_2.append([item[i] for item in m_list])

    m_list_2 = [''.join(i) for i in m_list_2]

    #print(m_list)
    #print(m_list_2)

    flag = 1

    for i in m_list_2:
        if bub_sort(list(i)) != list(i):
            flag = 0

    if flag == 1:
        print('YES')
    else:
        print('NO')






