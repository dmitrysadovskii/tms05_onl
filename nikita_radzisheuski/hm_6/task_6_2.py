"""HOMEWORK TASK NUMBER TWO
Примеры для проверки работоспособности:
"cccbba" == "c3b2a"
"abeehhhhhcccd" == "abe2h5c3ed"
"aaabbceedd" == "a3b2ce2d2"
"abcde" == "abcde"
"aaabbdefffff" == "a3b2def5"
"""

import collections
thestring = 'abeehhhhhcccd'
d = collections.defaultdict(int)
for i in thestring:
    d[i] += 1


def power(d):
    for i in d:
        if d[i] >= 2:
            print(str(i)+str(d[i]), end='')
        else:
            print(i, end='')


power(d)
