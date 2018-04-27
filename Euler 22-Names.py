__author__ = 'Rushil'

a = open('names.txt' , 'r').read()

name_list = a.split(',')
print(len(name_list))

m_name_list = []

for i in name_list:
    m_name_list.append(i[1:-1])

m_name_list = sorted(m_name_list)

m_name_list = [i.lower() for i in m_name_list]

def get_ascii(char):
    return ord(char) - 96

ascii_list = []

for i in m_name_list:
    print(list(i))
    ascii_list.append(list(map(get_ascii , i)))

sum_list = []

for i in ascii_list:
    sum_list.append(sum(i))

final_list = list(zip(m_name_list , sum_list))

s = 0

print(final_list[937])

for i,j in enumerate(final_list):
    s += (i+1) * j[1]

print(s)