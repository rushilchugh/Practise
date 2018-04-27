__author__ = 'Rushil'


def lcs_bad(a, b):
    if not a or not b:
        return 0
    elif a[-1] == b[-1]:
        return 1 + lcs_bad(a[:-1], b[:-1])
    else:
        t1 = lcs_bad(a, b[:-1])
        t2 = lcs_bad(a[:-1], b)
        return max(t1, t2)


mem_dict = {("", ""): 0}
al = ''

def lcs_m(a, b):

    global mem_dict, al

    if not a or not b:
        mem_dict[(a, b)] = 0
        return mem_dict[(a, b)]

    elif (a, b) in mem_dict:
        return mem_dict[(a, b)]

    elif a[-1] == b[-1]:

        mem_dict[(a, b)] = 1 + lcs_m(a[:-1], b[:-1])
        return mem_dict[(a, b)]

    else:
        mem_dict[(a, b[:-1])] = lcs_m(a, b[:-1])
        mem_dict[(a[:-1], b)] = lcs_m(a[:-1], b)
        return max(mem_dict[(a, b[:-1])], mem_dict[(a[:-1], b)])

print(lcs_m("AXYT", "AYZX"))
print(al)


