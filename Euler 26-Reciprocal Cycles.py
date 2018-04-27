__author__ = 'Rushil'

def sieve(n):

    num_list = [True] * n

    num_list[0] = num_list[1] = False

    for i,j in enumerate(num_list):

        if j:
            yield i
            for num in range(i*i , n , i):
                num_list[num] = False
m_list = []
max_num = 0
f_key = ''
for i in sieve(1001):
    dec_late = str(1/i).split('.')[1]

    if len(dec_late) > 1 and i != 3:
        if dec_late[0] == dec_late[1]:
            m_key = dec_late[0] + dec_late[1]
        else:
            m_key = dec_late[0]
        m_list = dec_late.split(m_key)[1:]
        f_key = m_key
        print(i,dec_late,m_key,m_list)

    #if len(m_list) > 1:
    #
    #    for j in range(len(m_list)):
    #        try:
    #            if m_list[j] == m_list[j+1]:
    #                    print('--'*60)
    #                    print(i,dec_late,m_list)
    #
    #                    if len(m_list[0])+len(f_key) > max_num:
    #                        max_num = i
    #
    #        except:
    #            pass

print(max_num)


