__author__ = 'Rushil'

import inflect

eng = inflect.engine()

s_num = 0

for i in range(1,1001):
    word = eng.number_to_words(i)
    word = word.replace(' ' , '')
    word = word.replace('-' , '')
    s_num += len(word)

print(s_num)

