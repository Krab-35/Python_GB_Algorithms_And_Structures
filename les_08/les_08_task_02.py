"""
Закодируйте любую строку по алгоритму Хаффмана.
"""

from collections import Counter


def sort_fun(inp_array):
    # вспомогательная функция сортировки элементов массива бинарного дерева для функции haf_bin_tree
    flag = 0
    for elem in range(len(inp_array) - 1):
        if flag == 1:
            break
        if inp_array[elem][1] > inp_array[elem + 1][1]:
            inp_array[elem], inp_array[elem + 1] = inp_array[elem + 1], inp_array[elem]
        else:
            flag = 1
    return inp_array


def haf_bin_tree(input_array, start=0, result_array=None):
    # функция создания массива бинароного дерева по алгоритму Хаффмана
    if result_array is None:
        result_array = []
    if start == 0:
        start = 1
        result_array.append(input_array)
        haf_bin_tree(None, start, result_array)

    temp_array = []
    if len(result_array[start - 1]) > 1:
        temp_array.append(
            (
                ''.join([result_array[start - 1][0][0], result_array[start - 1][1][0]]),
                result_array[start - 1][0][1] + result_array[start - 1][1][1]
            )
        )
        for elements in result_array[start - 1][2:]:
            temp_array.append(elements)
        result_array.append(sort_fun(temp_array))
        start += 1
        haf_bin_tree(None, start, result_array)
    return result_array


def bin_elements(array: list, bin_tree: list):
    # функция прохода от корня до листьевев дерева с заполненение траектории движения по дереву для каждого листа
    dict_elements = {}

    for dict_elem in range(len(array)):
        #  берем каждый отдельный элемент начиная с большего значения количества встречи
        dict_letter = array[len(array) - 1 - dict_elem][0]  # вывод искомой буквы
        len_bin_value = 0  # размер звена
        temp_val_elem_in = ''  # переменная для записи промежуточных значений списка листов дерева
        bin_letter = ''  # бинарный код буквы

        for num_bin in range(1, len(bin_tree)):
            # проходжение от корня до интересующего листа
            bin_arr_elem = bin_tree[len(bin_tree) - 1 - num_bin]
            step = 0

            for elem_in_num_bin in bin_arr_elem:

                try:
                    elem_in_num_bin[0].index(dict_letter)
                except ValueError:
                    step += 1
                    continue

                if len_bin_value == 1:
                    break

                if len_bin_value == 0:
                    # первый проход от корня к листьям
                    temp_val_elem_in = elem_in_num_bin[0]
                    len_bin_value = len(elem_in_num_bin[0])
                    if step % 2 == 0:
                        bin_letter += '0'
                    else:
                        bin_letter += '1'
                    continue

                if len_bin_value == len(elem_in_num_bin[0]):
                    # попадание на узлы, которые уже встречались
                    break
                else:
                    len_bin_value = len(elem_in_num_bin[0])

                    if len_bin_value == 1:
                        # попадание на лист
                        if temp_val_elem_in.index(dict_letter) == 0:
                            bin_letter += '0'
                        else:
                            bin_letter += '1'
                        continue

                    if temp_val_elem_in.index(elem_in_num_bin[0]) == 0:
                        # движение в сторону узла содержащий требуемый лист
                        bin_letter += '0'
                        temp_val_elem_in = elem_in_num_bin[0]
                        continue
                    else:
                        bin_letter += '1'
                        temp_val_elem_in = elem_in_num_bin[0]
                        continue
        dict_elements.update({dict_letter: bin_letter})

    return dict_elements


def encoding_fun(i_array, key_array):
    # функция кодирования вводимого текста в соответствии полученного словара листьев с их траекторией проходения от
    # корня
    encoding_array = ''
    step = 0
    for el_i_array in i_array:
        encoding_array += key_array.get(el_i_array)
    result_encoding = ''
    for el_encoding in encoding_array:
        result_encoding += el_encoding
        step += 1
        if step == 4:
            result_encoding += ' '
            step = 0

    return result_encoding


def alg_haf():
    input_values = input('Введите строку для кодирования: ')
    inp_value = Counter(input_values)
    in_val = list(reversed(inp_value.most_common()))
    print(in_val)
    bin_arr = haf_bin_tree(in_val)
    dict_arr = bin_elements(in_val, bin_arr[:len(in_val)])
    for el in dict_arr:
        print(f'\'{el}\': {dict_arr.get(el)}')
    result_fun_value = encoding_fun(input_values, dict_arr)
    return result_fun_value


z = alg_haf()
print(z)
