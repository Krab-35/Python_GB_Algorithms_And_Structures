"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
п.с.: тапкозакидательный вариант
"""

from random import randint
from les_06_task_01_memory import mem_size
import sys

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [randint(MIN_ITEM, MAX_ITEM) for el in range(SIZE)]

m = [
    0,  # максимальный элемент
    0,  # позиция максимального элемента
    float('inf'),  # минимальный элемент
    0,  # позиция минимального элемента
    0   # шаг прохода по элементам массива array
]
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

# занимаемый объем памяти
print(f'Выделенный размер памяти под переменные: {mem_size(locals())} байт')

# Выделенный размер памяти под переменные: 872 байт
