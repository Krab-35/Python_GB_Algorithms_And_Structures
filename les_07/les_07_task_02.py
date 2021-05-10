"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
[0; 50). Выведите на экран исходный и отсортированный массивы.
"""

from random import uniform


def atom_sort(input_array: list, temp_array=None):
    # Функция разбивающая список случайных вещественных чисел на массивы пар значений.
    # Рекурсивное деление списка надвое, до получения единичных размеров массивов.
    # Пример:
    # [12.869, 48.774, 41.558, 29.747, 29.16, 28.666, 12.039, 7.632, 6.114, 10.752] - исходный список
    # [[12.869, 48.774], [41.558], [29.16, 29.747], [12.039, 28.666], [7.632], [6.114, 10.752]] - результат работы ф-ции

    array_a = None
    array_b = None

    if temp_array is None:
        temp_array = []

    if len(input_array) > 1:
        array_a = input_array[:len(input_array) // 2]
        array_b = input_array[len(input_array) // 2:]

    if len(array_a) > 1:
        atom_sort(array_a, temp_array)

    if len(array_a) == 1 and len(array_b) == 2:
        temp_array.append(array_a)

    if len(array_b) > 1:
        atom_sort(array_b, temp_array)

    if (len(array_a) == 1 and len(array_b) == 1) and (array_a[0] > array_b[0]):
        temp_array.append([array_b[0], array_a[0]])
    if (len(array_a) == 1 and len(array_b) == 1) and (array_a[0] < array_b[0]):
        temp_array.append([array_a[0], array_b[0]])

    return temp_array


def next_sort(lr_array, result_sort=None):
    # Функция обратоки отсортированных пар значений массивов. На вход получает массив массивов.

    if result_sort is None:
        result_sort = []

    if len(lr_array) == 1:
        return lr_array[0]

    left_lr_ar = lr_array[0]
    right_lr_ar = lr_array[1]

    if len(lr_array) > 2:
        left_lr_ar = next_sort(lr_array[:len(lr_array) // 2])
        right_lr_ar = next_sort(lr_array[len(lr_array) // 2:])

    l_val = r_val = 0

    while l_val < len(left_lr_ar) + 1 and r_val < len(right_lr_ar) + 1:
        if l_val == len(left_lr_ar) and r_val == len(right_lr_ar):
            break

        if l_val == len(left_lr_ar):
            result_sort.append(right_lr_ar[r_val])
            r_val += 1
            continue

        if r_val == len(right_lr_ar):
            result_sort.append(left_lr_ar[l_val])
            l_val += 1
            continue

        if left_lr_ar[l_val] < right_lr_ar[r_val]:
            result_sort.append(left_lr_ar[l_val])
            l_val += 1
            continue
        if left_lr_ar[l_val] > right_lr_ar[r_val]:
            result_sort.append(right_lr_ar[r_val])
            r_val += 1
            continue

    return result_sort


def merger_sort(inp_array: list):
    result_array = atom_sort(inp_array)
    left_array = next_sort(result_array[:len(result_array) // 2])
    right_array = next_sort(result_array[len(result_array) // 2:])
    return next_sort([left_array, right_array])


SIZE = 13
MIN_ITEM = 0
MAX_ITEM = 50
array = [round(uniform(MIN_ITEM, MAX_ITEM), 3) for el in range(SIZE)]

print(array)
z = merger_sort(array)
print(z)
