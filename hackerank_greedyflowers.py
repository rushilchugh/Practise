__author__ = 'Rushil'

(n, k) = tuple(map(int, input().split()))
f_cost = list(map(int, input().split()))

fl_by_customer = [0] * k
t_cost = 0

if n <= k:
    t_cost = sum(f_cost)
else:
    f_cost = sorted(f_cost, reverse=True)
    v = 0
    while f_cost:
        t_cost += sum(list(map(lambda x: (v + 1) * x, f_cost[:k])))
        f_cost = f_cost[k:]
        v += 1

print(t_cost)