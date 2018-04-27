__author__ = 'Rushil'

import itertools

a = tuple(itertools.permutations('0123456789'))
(b,c,d) = (''.join(a[1000000]) , ''.join(a[999999]) , ''.join(a[1000001]))
print(b,c,d)

