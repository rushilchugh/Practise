__author__ = 'Rushil'

#0.123456789101112131415161718192021...

num_list = []
for i in range(1000000):
    num_list += str(i)

m_list = ''.join(num_list)[1:]
print(len(m_list))
print(m_list[1])
n = 1
prod = 1

while n != 1000000:
    prod *= int(m_list[n-1])
    print(int(m_list[n-1]) , n)
    n *= 10

print(prod)