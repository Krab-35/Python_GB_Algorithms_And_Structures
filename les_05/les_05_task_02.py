from collections import deque, Counter

hex_arr = Counter(
        {
            '0': 1, '1': 2, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7, '7': 8, '8': 9,
            '9': 10, 'A': 11, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16
        }
    )
halo_arr = deque(hex_arr.keys())

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

    while take_a != halo_arr[0]:
        take_num = halo_arr.pop()
        halo_arr.appendleft(take_num)

    if one_step == 1:
        take_step = halo_arr.popleft()
        halo_arr.append(take_step)
        one_step = 0

    if pos_a + pos_b >= 17:
        one_step = 1

    if pos_a >= 11 and pos_b >= 11:
        pos_b -= 1

    for el in range(pos_b - 1):
        take_number = halo_arr.popleft()
        halo_arr.append(take_number)

    result_out.appendleft(halo_arr[0])

    if len_a == 0:
        while True:
            take_b = input_b.pop()
            len_b -= 1

            if one_step == 1:
                while take_b != halo_arr[0]:
                    take_num_b = halo_arr.pop()
                    halo_arr.appendleft(take_num_b)

                take_step = halo_arr.popleft()
                halo_arr.append(take_step)
                one_step = 0
                result_out.appendleft(halo_arr[0])
            else:
                result_out.appendleft(take_b)
            if len_b == 0:
                break
        break
    if len_b == 0:
        while True:
            take_a = input_a.pop()
            len_a -= 1

            if one_step == 1:
                while take_a != halo_arr[0]:
                    take_num_a = halo_arr.pop()
                    halo_arr.appendleft(take_num_a)

                take_step = halo_arr.popleft()
                halo_arr.append(take_step)
                one_step = 0
                result_out.appendleft(halo_arr[0])
            else:
                result_out.appendleft(take_a)
            if len_b == 0:
                break
        break


print(f'Результат сложения двух чисел: {result_out}')
