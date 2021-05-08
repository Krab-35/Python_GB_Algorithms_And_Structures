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

m = {
    'max_val': 0,  # максимальный элемент
    'max_pos': 0,  # позиция максимального элемента
    'min_val': float('inf'),  # минимальный элемент
    'min_pos': 0,  # позиция минимального элемента
    'step': 0   # шаг прохода по элементам массива array
}
for elem in array:
    if m.get('step') == 0:
        m.update({'max_val': elem})
    if elem > m.get('max_val'):
        m.update({'max_val': elem})
        m.update({'max_pos': m.get('step')})
    if elem < m.get('min_val'):
        m.update({'min_val': elem})
        m.update({'min_pos': m.get('step')})
    m.update({'step': m.get('step') + 1})

print(array)
array[m.get('max_pos')], array[m.get('min_pos')] = array[m.get('min_pos')], array[m.get('max_pos')]
print(array)

# занимаемый объем памяти
print(f'Выделенный размер памяти под переменные: {mem_size(locals())} байт')


# Выделенный размер памяти под переменные: 1281 байт
