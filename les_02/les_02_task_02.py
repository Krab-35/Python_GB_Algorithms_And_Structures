"""
Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


def count_number(a: int, i=0, k=0):
    if a == 0:
        if i == 0 and k == 0:
            i = 1
        return f'Количество четных цифр: {i}, нечетных: {k}'
    if ((a % 10) % 2) == 0:
        i += 1
    else:
        k += 1
    return count_number((a // 10), i, k)


z = count_number(int(input('Введите натуральное число: ')))

print(z)