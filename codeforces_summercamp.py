__author__ = 'Rushil'

req_num = ''.join(list(map(str,list(range(1,1001)))))

n = int(input().strip())
print(req_num[n-1])