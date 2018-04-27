__author__ = 'Rushil'

num = 0

def m_in_m(n,m):
    global num
    if n != m:
        num += 1
        return m_in_m(n/m , m)
    if n == m:
        return num+1

print(m_in_m(27,2))
