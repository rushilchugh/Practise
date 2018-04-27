__author__ = 'Rushil'

total , friends = list(map(int , input().strip().split()))
sleep_index = input().strip()
friend_index = [i-1 for i in list(map(int , input().strip().split()))]


for i in friend_index:
    if sleep_index[i] == '0':
        print('YES')
        exit()
print('NO')