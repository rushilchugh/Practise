__author__ = 'Rushil'

n = int(input().strip())
m_list = []

for _ in range(n):
    (n,k) = tuple(map(int , input().strip().split(' ')))
    arr_1 = list(map(int , input().strip().split(' ')))
    arr_2 = list(map(int , input().strip().split(' ')))
    m_list.append(((n,k) , arr_1 , arr_2))

def do_stuff(k,arr_1,arr_2):
    arr_1 = sorted(arr_1)
    arr_2 = sorted(arr_2)[::-1]

    for i in range(len(arr_1)):
        if arr_1[i] + arr_2[i] < k:
            return 'NO'

    return 'YES'

for i in m_list:
    print(do_stuff(i[0][1] , i[1] , i[2]))

