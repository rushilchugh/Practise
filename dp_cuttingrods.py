__author__ = 'Rushil'

from collections import defaultdict
import time

p = [0,1, 5, 8, 9, 10, 17, 17, 20, 24, 30] + [30, 30, 30, 30, 30, 30, 30, 30, 30, 30]

def cut_rods(p,n):                                                          #RECURSIVE
                                                                            #Problem is thought of as, after cutting at point i,
    if n == 0:                                                              #the rest of the rod of length (n-i) can be considered as
        return 0                                                            #another rod cutting problem

    q = -999

    for i in range(1,n+1):
        q = max(q , p[i] + cut_rods(p,n-i))

    return q

r = defaultdict(int)

for i in range(25):
    r[i] = -999

r[0] = 0

def cut_rods_2(p,n,r):                                                                  #MEMOIZATION

    if r[n] > 0:
        return r[n]

    if n == 0:
        q = 0

    else:
        q = -999

        for i in range(1,n+1):
            q = max(q , p[i] + cut_rods_2(p,n-i,r))

    r[n] = q
    return q


max_dict = defaultdict(int)


def cut_rods_3(p,n,max_dict):                                                       #MEMOZIATION_2

    if n in max_dict.keys():
        return max_dict[n]

    if n == 0:
        return 0
    else:
        q = -999
        for i in range(1,n+1):
            q = max(q , p[i] + cut_rods_3(p,n-i,max_dict))
        max_dict[n] = q

    return q

def cut_rods_4(p,n):                                                                   #BOTTOMS_UP_1

    #This over here means that problem of size i is smaller than that of j

    max_dict = defaultdict(int)
    max_dict[0] = 0

    for j in range(1,n+1):                                  #This loop and the next 2 lines solves a sub-problem of size j
        q = -999
        for i in range(1,j+1):                              #This emulates cutting the rod at distance i, note that there is
            q = max(q , p[i] + max_dict[j - i])             #no recursive call, and unlike in recursion, here, problems are
        max_dict[j] = q                                     #solved individually as opposed to sub-problems of original as
    return max_dict[j]                                      #in recursion


def cut_rods_5(p,n):                                                                    #BOTTOMS_UP_2

    max_dict = defaultdict(int)
    max_dict[0] = 0

    for i in range(1,n+1):
        q = -999
        for j in range(1,i+1):
            q = max(q , p[j] + max_dict[i - j])
        max_dict[i] = q
    return max_dict[i]

def cut_rods_6(p,n):

    max_dict = defaultdict(int)
    max_dict[0] = 0

    sol_list = defaultdict(list)
    sol_list[0] = [0]

    for i in range(1,n+1):
        q = -999
        for j in range(1,i+1):
            if q < p[j] + max_dict[i - j]:
                q = p[j] + max_dict[i - j]
                sol_list[i].append(j)

        max_dict[i] = q

    return max_dict , sol_list



#s = 0
#print('cut_rods_1')
#for i in range(1,20):
#    a = time.time()
#    c = cut_rods(p,i)
#    b = time.time()
#    print(i,c)
#    s += b-a
#print(s)

print('--'*60)

s = 0
print('cut_rods_2')
for i in range(1,20):
    a = time.time()
    c = cut_rods_2(p,i,r)
    b = time.time()
    print(i,c)
    s += b-a
print(s)

print('--'*60)

s = 0
print('cut_rods_3')
for i in range(1,20):
    a = time.time()
    c = cut_rods_3(p,i,r)
    b = time.time()
    print(i,c)
    s += b-a
print(s)
s = 0

print('--'*60)

s = 0
print('cut_rods_4')
for i in range(1,20):
    a = time.time()
    c = cut_rods_4(p,i)
    b = time.time()
    print(i,c)
    s += b-a
print(s)

print('--'*60)

s = 0
print('cut_rods_5')
for i in range(1,20):
    a = time.time()
    c = cut_rods_5(p,i)
    b = time.time()
    print(i,c)
    s += b-a
print(s)

print('--'*60)

s = 0
print('cut_rods_6')

#c,d = cut_rods_6(p,20)

for i in cut_rods_6(p,20):
    print(i.items())

#SINCE THE BOTTOMS UP APPROACH ALL I NEED TO D
#CONTAINS THE SOLUTION TO ALL THE PREVIOUS CASES