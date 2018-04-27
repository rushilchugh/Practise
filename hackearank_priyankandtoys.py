__author__ = 'Rushil'

n = input().strip()
p_list = sorted(list(map(int , input().strip().split())))
p_list_2 = [list(i) for i in list(zip(p_list , [True]*len(p_list)))]

sorted(p_list_2)

n = 0

for i in range(len(p_list_2)):

    if p_list_2[i][1]:

        n += 1

        for j in range(i+1,len(p_list_2)):

            if p_list_2[j][0] in range(p_list_2[i][0] , p_list_2[i][0] + 5):
                p_list_2[j][1] = False
            else:
                break

print(n)