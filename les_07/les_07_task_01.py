"""
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
[-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. Улучшенные версии
сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""

from random import randint

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 99
array = [randint(MIN_ITEM, MAX_ITEM) for el in range(SIZE)]


def wisp_sort(input_array: list):
    for n in range(1, len(input_array)):
        for i in range(len(input_array) - n):
            if input_array[i] < input_array[i + 1]:
                input_array[i], input_array[i + 1] = input_array[i + 1], input_array[i]
    return input_array


print(array)
z = wisp_sort(array)
print(z)
