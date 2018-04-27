__author__ = 'Rushil'

n = int(input().strip())
test_str = input().strip()

m_str = test_str
count = 0

sub_str_list = []

for i in range(0,len(m_str)+1):
    for j in range(i,len(m_str)+1):
        sub_str = m_str[i:j]
        print(sub_str , end = ' ')
        if sub_str == sub_str[::-1] and len(sub_str) > 1 and sub_str not in sub_str_list:
            sub_str_list.append(sub_str)
            count += 1

print(count)


