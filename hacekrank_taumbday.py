__author__ = 'Rushil'

t = int(input().strip())

m_list = []

for _ in range(t):
    b,w = list(map(int,input().strip().split(' ')))
    x,y,z = list(map(int,input().strip().split(' ')))
    m_list.append([b,w,x,y,z])

def do_stuff(n_b,n_w,c_b,c_w,z):

    if c_b <= z and c_w <= z:
        return n_b*c_b + n_w*c_w

    elif z < c_b and c_b > c_w:
        return (n_b+n_w)*c_w + n_b*z

    elif z < c_w and c_w > c_b:
        return (n_b+n_w)*c_b + n_w*z

    elif z < c_b and z < c_w:
        if c_b < c_w:
            return (n_b+n_w)*c_b + n_w*z

        elif c_w < c_b:
            return (n_b+n_w)*c_w + n_b*z

for i in m_list:
    print(do_stuff(*i))