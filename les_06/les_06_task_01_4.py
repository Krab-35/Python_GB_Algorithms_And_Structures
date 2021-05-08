"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

from random import randint
from les_06_task_01_memory import mem_size


def max_min_changer(input_array: list, max_el=float('-inf'), max_pos=0,
                    min_el=float('inf'), min_pos=0, step=0, memo=None):
    """Рекурсивная функция замены максимального и минимальных значений массива,

    Для получения результата перестановки необходимо обратиться к 0-му элементу функции
    Для определния выделенной памяти под переменные функции необходимо обратиться к 1-му элементу массива
    Без учета самой переменной "memo" для отслеживания выделяемой памяти
    """
    if memo is None:
        memo = {}
    temp_array = locals()
    for elem in temp_array:
        if elem == 'memo':
            continue
        memo.update({f'{elem + str(step)}': temp_array.get(elem)})

    len_array = len(input_array)
    if step < len_array:
        if input_array[step] > max_el:
            max_el = input_array[step]
            max_pos = step
        if input_array[step] < min_el:
            min_el = input_array[step]
            min_pos = step
        step += 1
        return max_min_changer(input_array, max_el, max_pos, min_el, min_pos, step, memo)
    if step == len_array:
        input_array[max_pos], input_array[min_pos] = input_array[min_pos], input_array[max_pos]
        return [input_array, memo]


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [randint(MIN_ITEM, MAX_ITEM) for el in range(SIZE)]

print(array)
z = max_min_changer(array)
print(z[0])

# занимаемый объем памяти
print(f'Выделенный размер памяти под переменные: {mem_size(locals()) + mem_size(z[1])} байт')

# Выделенный размер памяти под переменные: 9748 байт

"""
Вывод: для решения данной задичи лучше всего использовать отдельные переменные под каждое значение. При использовании
рекурсивной функции выделяется большой объем памяти под переменные каждой следующей вызываемой функции.
Версия ОС: Windows 10 Home 64-bit
Версия Python: 64-bit
"""
