"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

from random import randint
from les_06_task_01_memory import mem_size

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [randint(MIN_ITEM, MAX_ITEM) for el in range(SIZE)]

maxElement = array[0]       # максимальный элемент
maxPos = 0                  # позиция максимального элемента
minElement = float("inf")   # минимальный элемент
minPos = 0                  # позиция минимального элемента

for elem in range(len(array) - 1):
    if array[elem] > maxElement:
        maxElement = array[elem]
        maxPos = elem
    if array[elem] < minElement:
        minElement = array[elem]
        minPos = elem

print(array)
array[maxPos], array[minPos] = array[minPos], array[maxPos]
print(array)

# занимаемый объем памяти
print(f'Выделенный размер памяти под переменные: {mem_size(locals())} байт')
# Выделенный размер памяти под переменные: 748 байт
