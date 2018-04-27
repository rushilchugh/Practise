__author__ = 'Rushil'

def get_diag_elements(n):
    if n == 0:
        return 1,0,0,0
    side_l = 2*n
    main_elem = (2*n + 1)**2
    return main_elem , main_elem - side_l , main_elem - 2*side_l , main_elem - 3*side_l

s = 0

for i in range(501):
    diag_list = list(get_diag_elements(i))
    print(diag_list)
    s += sum(diag_list)

print(s)