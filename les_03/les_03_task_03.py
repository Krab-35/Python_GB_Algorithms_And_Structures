"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

from random import randint

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [randint(MIN_ITEM, MAX_ITEM) for el in range(SIZE)]

m = [0, 0, 0, 0, 0]
for elem in array:
    if m[4] == 0:
        m[2] = elem
    if elem > m[0]:
        m[0] = elem
        m[1] = m[4]
    if elem < m[2]:
        m[2] = elem
        m[3] = m[4]
    m[4] += 1

print(array)
array[m[1]], array[m[3]] = array[m[3]], array[m[1]]
print(array)
