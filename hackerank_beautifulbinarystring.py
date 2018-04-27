__author__ = 'Rushil'


#text = '0100101010'
#
#occ_in_str = exp.finditer(text)
#
#for i in occ_in_str:
#    print(text[i.start() : i.end()] , i.start() , i.end()-1)
#
#occ_in_str = exp.finditer(text)
#print('Total - ' , sum(1 for _ in occ_in_str))
#
import re

n = int(input().strip())
B = input().strip()

exp = re.compile(r'010')
print(len(exp.findall(B)))