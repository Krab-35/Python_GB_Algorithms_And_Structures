"""
Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""


def output_ten(i: int, k: int):
    if i + 10 <= k:
        for elem in range(i, (i + 10)):
            print(f'{elem}-{chr(elem)}', end=' ')
        i += 10
        print()
        return output_ten(i, k)
    if i == k:
        print(f'{i}-{chr(i)}', end=' ')
    else:
        for elem in range(i, k + 1):
            print(f'{elem}-{chr(elem)}', end=' ')
    return ''


z = output_ten(32, 127)
print(z)
