import sys


def input_type(input_data):
    size_input = 0
    if type(input_data) is list:
        size_input += sys.getsizeof(input_data)
        for elList in input_data:
            size_input += sys.getsizeof(elList)
    if type(input_data) is int:
        size_input += sys.getsizeof(input_data)
    if type(input_data) is float:
        size_input += sys.getsizeof(input_data)
    return size_input


def mem_size(input_array: dict):
    size = 0
    for elem in input_array:

        if type(input_array.get(elem)) is dict:
            temp_array = input_array.get(elem)
            size += sys.getsizeof(temp_array)
            for elements in temp_array:
                size += input_type(temp_array.get(elements))
                size += sys.getsizeof(elements)
            continue

        size += input_type(input_array.get(elem))

    return size
