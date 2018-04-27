__author__ = 'Rushil'

def make_part(str):
    str_len = len(str)

    if len(str)%2 == 0:
        return str[:str_len//2] , str[str_len//2:]

    else:
        return str[:str_len//2] , str[str_len//2+1:]

def fig(w1 , w2):

    n_opts = 0

    w2 = w2[::-1]

    for i in range(len(w1)):
        n_opts += abs(ord(w1[i]) - ord(w2[i]))

    return abs(n_opts)

n = int(input().strip())

str_list = []
for i in range(n):  str_list.append(input())

for i in str_list:
    tupl = make_part(i)
    print(fig(tupl[0] , tupl[1]))
