__author__ = 'Rushil'

n_test = int(input())
points = []

def str_to_cood(str):
    return  [tuple(str.split(' ')[:2]) , tuple(str.split(' ')[2:])]

def get_sym_point(p_list):
    point_1 = p_list[0]
    point_2 = p_list[1]
    point_3_x = 2*int(point_2[0]) - int(point_1[0])
    point_3_y = 2*int(point_2[1]) - int(point_1[1])
    print(point_3_x , point_3_y)


while n_test:
    a = input().strip()
    a = str_to_cood(a)
    points.append(a)
    n_test -= 1

for i in points:   get_sym_point(i)



