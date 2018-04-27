import itertools

a = '4433555555666666'

g_list = [''.join(j) for i,j in itertools.groupby(a)]

def make_groups(elem):
    a = [''.join(j) for i,j in itertools.groupby(elem)]
    return a

num_list = [1, 11, 21, 1211, 111221]

for i in range(0,len(num_list)):
    num_list[i] = str(num_list[i])

def get_next_elem(num):

    x = []
    
    for i in num:
        x.append(str(len(i)) + i)

    x = [''.join(x[::])]    
    return x[0]
