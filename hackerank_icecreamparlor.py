__author__ = 'Rushil'

#Test Cases - 2
#Money - 4
#No of Flavors - 5
#Cost of each Flavor - 1 4 5 3 2
#Money - 4
#No of Flavors - 4
#Cost of each Flavor - 2 2 4 3

def get_flav_index(m , n , flav_list):

    for i in range(n):
        for j in range(i,n):
            if flav_list[i] + flav_list[j] == m and i != j:
                return i+1 , j+1



tc = int(input().strip())

mast_array = []

for i in range(tc):
    money = int(input().strip())
    flav_no = int(input().strip())
    flav_lists =[int(i) for i in input().strip().split(' ')]
    mast_array.append([money , flav_no , flav_lists])

for i in mast_array:
    print(get_flav_index(i[0] , i[1] , i[2])[0] , get_flav_index(i[0] , i[1] , i[2])[1])