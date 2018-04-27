__author__ = 'Rushil'

n = int(input().strip())

m_list = [list(map(int , input().strip().split(' '))) for _ in range(n)]
#print(list(enumerate(m_list)))

other_list = []

for index,[i,j] in enumerate(m_list):
    other_list.append((index+1,i+j))

#print(other_list)
for i in (sorted(other_list , key = lambda l : l[1])):
    print(i[0] , end = ' ')