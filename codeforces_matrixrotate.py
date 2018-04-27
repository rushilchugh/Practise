__author__ = 'Rushil'

import numpy as np

init_mat = '''1 2 3
4 5 6
7 8 9
'''

main_matrix = []

for j in [i.split(' ') for i in init_mat.strip().split('\n')]:  main_matrix.append(list(map(int , j)))

print(np.rot90(np.array(main_matrix)))





