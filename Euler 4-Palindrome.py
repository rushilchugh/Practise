__author__ = 'Rushil'

palindromes = []

for i in range(1,999):
    for j in range(1,999):
        num = i*j
        if str(num) == str(num)[::-1]:
            palindromes.append(num)

print(max(palindromes))


