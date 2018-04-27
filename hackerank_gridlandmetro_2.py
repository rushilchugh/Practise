__author__ = 'Rushil'

m,n,k = list(map(int,input().strip().split()))
m_list = []

for i in range(k):
    m_list.append(list(map(int,input().strip().split())))

m_array = [[1 for _ in range(n)] for _ in range(m)]
#print(m_array)

for j in m_list:
    row_np = j[0]-1
    col_st = j[1]-1
    col_en = j[2]-1

    for index in range(col_st,col_en+1):
        m_array[row_np][index] = 0


#print(m_array)

f_list = [item for sublist in m_array for item in sublist if item == 1]
print(sum(f_list))
