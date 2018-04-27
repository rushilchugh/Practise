__author__ = 'Rushil'

n  = int(input().strip())

inp_list = [input().strip() for _ in range(n)]

#print(inp_list)

map_lst = []

for i in inp_list:
    map_lst.append(list(map(int,list(i))))

f_list = list(list(zip(inp_list , map_lst)))
#print(f_list)

for (num,num_list) in f_list:
#    print(num,num_list)
    s = 0
    for i in num_list:
        if i != 0 and int(num) % i == 0:
            s += 1
    print(s)
