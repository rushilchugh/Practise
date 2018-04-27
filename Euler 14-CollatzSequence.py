__author__ = 'Rushil'



def collatz_seq(n):
    s = 0
    while n != 1:
        if n %2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        s += 1
    #print(s)
    return s

a_dict = {}

#max_num = 0
#j = 0
#for i in range(5,1000000):
#    elem = collatz_seq(i)
#    if elem > max_num:
#        j = i
#        max_num = elem
#
#    else:
#        pass
#
#print(j)

seq_dict = {1: 0, 2: 1 , 4: 2 , 8: 3}
s = 0

def coll_seq_2(n):
    global s
    while n != 1:
        if n in seq_dict:
            print(s,n , 'From if n in seq_dict:                  ' , seq_dict)
            return seq_dict[n] + s

        elif n %2 == 0 & n not in seq_dict:
            print(s,n , 'From elif n %2 == 0 & n not in seq_dict:' , seq_dict)
            s += 1
            seq_dict[n] = coll_seq_2(n//2)

            return seq_dict[n]

        elif n % 2 != 0 & n not in seq_dict:
            print(s,n , 'From elif n % 2 != 0 & n not in seq_dict:' , seq_dict)
            s += 1
            seq_dict[n] = coll_seq_2(3*n + 1)

            return seq_dict[n]

        print(s)

print(coll_seq_2(2065000))

