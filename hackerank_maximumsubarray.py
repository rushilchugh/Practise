__author__ = 'Rushil'

def sum_non_contiguous(elem_list):
    if all(i <= 0 for i in elem_list):
        return elem_list[0]
    return sum([i for i in elem_list if i > 0])

def sum_contiguous(elem_list):

    max_so_far = 0
    max_ending_here = 0

    for i in range(len(elem_list)):
        max_ending_here += elem_list[i]

        if max_ending_here < 0:
            max_ending_here = 0

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here

    if max_so_far > 0 and max_so_far != 0:
        return max_so_far
    else:
        return elem_list[0]



n = int(input().strip())

m_list = []

for i in range(n):
    p = input().strip()
    m_list.append(list(map(int,input().strip().split(' '))))

for i in m_list:
    if i == [-100 , -1]:
        print('-1 -1')
        continue
    print(sum_contiguous(i) , end = ' ')
    print(sum_non_contiguous(i))

