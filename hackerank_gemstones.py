__author__ = 'Rushil'

n = int(input().strip())
set_list = [set(input().strip()) for _ in range(n)]

def do_stuff_final(set_list):
    a = set_list[0]
    for i in set_list:
        a = a.intersection(i)
    return len(a)

print(do_stuff_final(set_list))
