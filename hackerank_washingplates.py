__author__ = 'Rushil'

#N is the number of dirty plates
#K is the number of plates with time to wash

(n,k) = tuple(map(int , input().strip().split()))

p_i , d_i = 1,1

pi_list = []
di_list = []

while p_i and d_i:
    (p_i , d_i) = tuple(map(int , input().strip().split()))
    pi_list.append(p_i)
    di_list.append(d_i)

print(n,k)
print(pi_list , di_list)

income = 0

def get_income(n,k):

    if k > n:
        return sum(pi_list)




    if income < 0:
        return 0

    return income
