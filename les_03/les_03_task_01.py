"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

m = [0, 0, 0, 0, 0, 0, 0, 0]
i = 0
for el in range(2, 10):
    for elem in range(2, 100):
        if elem % el == 0:
            m[i] += 1
    print(f'{el} кратно {m[i]} элем.')
    i += 1