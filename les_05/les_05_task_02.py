"""
Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел. При этом каждое число
представляется как коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить
их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque, Counter

hex_arr = Counter(
        {
            '0': 1, '1': 2, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7, '7': 8, '8': 9,
            '9': 10, 'A': 11, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16
        }
    )
halo_arr = deque(hex_arr.keys())


def rotation_fun_right():
    # движение очереди вправо
    take_number_right = halo_arr.pop()
    halo_arr.appendleft(take_number_right)


def rotation_fun_left():
    # Движение очереди влево
    take_number_left = halo_arr.popleft()
    halo_arr.append(take_number_left)


def halo_fun(inp_val):
    # вращение очереди пока нулевой элемент не станер равным требуемому значению
    while inp_val != halo_arr[0]:
        rotation_fun_right()


def last_move(inp_arr, inp_len):
    # запись результата при окончании цифр другого числа сложения
    global one_step
    temp_arr = deque()
    while True:
        take_val = inp_arr.pop()
        inp_len -= 1
        if one_step == 1:
            halo_fun(take_val)
            rotation_fun_left()
            one_step = 0
            temp_arr.append(halo_arr[0])
        else:
            temp_arr.append(take_val)
        if inp_len == 0:
            return temp_arr


input_a = deque(input('Введите первое hex-число: ').upper())
input_b = deque(input('Введите второе hex-число: ').upper())
result_out = deque()

len_a = len(input_a)
len_b = len(input_b)

one_step = 0
while True:
    take_a = input_a.pop()
    pos_a = hex_arr[take_a]
    len_a -= 1
    take_b = input_b.pop()
    pos_b = hex_arr[take_b]
    len_b -= 1

    halo_fun(take_a)

    if one_step == 1:
        rotation_fun_left()
        pos_a = hex_arr[halo_arr[0]]
        if halo_arr[0] == '0':
            one_step = 1
        else:
            one_step = 0

    if pos_a + pos_b > 17:
        one_step = 1

    for el in range(pos_b - 1):
        rotation_fun_left()

    result_out.appendleft(halo_arr[0])

    if len_a == 0 and len_b == 0:
        if one_step == 1:
            result_out.appendleft('1')
            one_step = 0
        break

    if len_a == 0:
        result_out.extendleft(last_move(input_b, len_b))
        break

    if len_b == 0:
        result_out.extendleft(last_move(input_a, len_a))
        break

print(f'Результат сложения двух чисел: {result_out}')
