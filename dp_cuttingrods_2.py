__author__ = 'Rushil'

from collections import defaultdict

p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

def cut_rods(n,p):

    if n == 0:
        return 0

    q = -999

    for i in range(1,n+1):
        q = max(q , p[i] + cut_rods(n-i,p))

    return q

def cut_rods_2(p,n):                                                          #RECURSIVE
                                                                            #Problem is thought of as, after cutting at point i,
    if n == 0:                                                              #the rest of the rod of length (n-i) can be considered as
        return 0                                                            #another rod cutting problem

    q = -999

    for j in range(1,n+1):
        q = max(q , p[j] + cut_rods_2(p,n-j))

    return q

p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

def cut_rods_3(p,n):

    sol_list = defaultdict(list)
    sol_list[0] = [0]

    max_dict = defaultdict(int)
    max_dict[0] = 0

    for i in range(1,n+1):
        q = -999
        for j in range(1,i+1):
            if q < p[j] + max_dict[i-j]:
                q = p[j] + max_dict[i-j]
                sol_list[i].append(j)

        max_dict[i] = q

    return max_dict

def cut_rods_4(p,n):

    sol_list = defaultdict(list)
    sol_list[0] = [0]

    max_dict = defaultdict(int)
    max_dict[0] = 0

    for i in range(1,n+1):
        q = -999
        for j in range(1,i+1):
            if q < p[j] + max_dict[i-j]:
                q = p[j] + max_dict[i-j]
                sol_list[i].append(j)

        max_dict[i] = q

    return max_dict

print(cut_rods(7,p))
print(cut_rods_2(p,7))
print(cut_rods_3(p,7))
print(cut_rods_4(p,7))