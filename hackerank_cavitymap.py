__author__ = 'Rushil'

n = int(input().strip())
grid = []
grid_i = 0


for grid_i in range(n):
   grid_t = str(input().strip())
   grid.append(grid_t)

grid_2 = [[] for _ in range(n)]

def get_elem_list(a,x,y):
    return a[x-1][y] , a[x+1][y] , a[x][y-1] , a[x][y+1]


for i,num in enumerate(grid):
    for j,num_2 in enumerate(num):
        grid_2[i].append(grid[i][j])
        if 0 < i < len(grid) - 1 and 0 < j < len(num) - 1:
            if all(int(grid[i][j]) > int(elem) for elem in get_elem_list(grid , i ,j)):
                grid_2[i][j] = 'X'

for i in grid_2:
    print(''.join(i))

