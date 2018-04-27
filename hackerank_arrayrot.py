__author__ = 'Rushil'

(n,k,q) = tuple(map(int , input().strip().split()))
array = list(map(int , input().strip().split()))
q_list = []

while q != 0:
    q_list.append(int(input()))
    q -= 1

def get_new_arr(array , k):

    for i in range(k):
        array.insert(0,array.pop())

    return array

array = get_new_arr(array , k)

for i in q_list:
    print(array[i])

    
