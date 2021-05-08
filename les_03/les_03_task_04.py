"""
Определить, какое число в массиве встречается чаще всего.
"""

from random import randint

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 7
array = [randint(MIN_ITEM, MAX_ITEM) for el in range(SIZE)]

m = []
for elem in array:
    k = 0
    for el in array:
        if el == elem:
            k += 1
    if len(m) == 0:
        m += [[elem, k]]
        continue
    if k > 0:
        i = 0
        flag = 0
        for el1 in m:
            if elem == el1[0]:
                flag = 1
                break
            i += 1
        if flag == 0:
            m += [[elem, k]]
        else:
            m[i][1] = k

result = m[1]
for n in m:
    if n[1] > result[1]:
        result = n

print(f'{array}\n{m}\n\nЧисло {result[0]} встречалось {result[1]} раз')
