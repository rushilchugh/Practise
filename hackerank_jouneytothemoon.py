__author__ = 'Rushil'

from itertools import combinations

(n, p) = tuple(list(map(int, input().strip().split())))

ast_group = []

for i in range(p):
    (a, b) = elem = tuple(list(map(int, input().strip().split())))
    ast_group.append(set(elem))

    for i in ast_group:
        pass


print(ast_group)

num_cases = sum([i[0] * i[1] for i in combinations(list(map(len, ast_group)), 2)])
print(num_cases)

