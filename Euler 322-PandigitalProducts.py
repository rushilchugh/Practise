__author__ = 'Rushil'

pan_list = sorted('123456789')
print(pan_list)

s = 0
prod_set = set()
for i in range(1,100000):
    for j in range(1,i):
        prod = i*j
        s_i , s_j , s_p = str(i) , str(j) , str(prod)
        #print(s_i , s_j , s_p)
        if len(s_i + s_j + s_p) > 9:
            break

        m_list = sorted(s_i + s_j + s_p)

        if m_list == pan_list:

            prod_set.add(prod)
            print (i,j,prod)
            break

print(sum(prod_set))