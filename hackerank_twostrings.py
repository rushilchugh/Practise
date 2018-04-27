__author__ = 'Rushil'

n = int(input().strip())

m_list = []

for _ in range(n):
    str1 = input().strip()
    str2 = input().strip()
    m_list.append([str1,str2])

for i in m_list:
    if len(set(i[0]).intersection(i[1])) != 0:
        print('YES')
    else:
        print('NO')