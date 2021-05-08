"""
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
"""
import timeit
import cProfile


def sum_n_v1(a: int, i=1.0, b=1.0):
    if a == 0:
        return f'Сумма из ноль элементов равна неопределенности'
    elif a == 1:
        return f'Сумма ряда чисел равна: {b}'
    i *= -0.5
    b += i
    a -= 1
    return sum_n_v1(a, i, b)


print(timeit.timeit('sum_n_v1(3)', number=1000, globals=globals()))    # 0.0016584000000000043
print(timeit.timeit('sum_n_v1(6)', number=1000, globals=globals()))    # 0.002711200000000011
print(timeit.timeit('sum_n_v1(9)', number=1000, globals=globals()))    # 0.004016500000000006
print(timeit.timeit('sum_n_v1(12)', number=1000, globals=globals()))   # 0.005481100000000003
print(timeit.timeit('sum_n_v1(15)', number=1000, globals=globals()))   # 0.006078
print(timeit.timeit('sum_n_v1(18)', number=1000, globals=globals()))   # 0.008009299999999997
print(timeit.timeit('sum_n_v1(21)', number=1000, globals=globals()))   # 0.008757700000000007
print(timeit.timeit('sum_n_v1(24)', number=1000, globals=globals()))   # 0.009849399999999994
print(timeit.timeit('sum_n_v1(27)', number=1000, globals=globals()))   # 0.0106522
print(timeit.timeit('sum_n_v1(30)', number=1000, globals=globals()))   # 0.011282100000000017
print(timeit.timeit('sum_n_v1(60)', number=1000, globals=globals()))   # 0.026477400000000012
print(timeit.timeit('sum_n_v1(90)', number=1000, globals=globals()))   # 0.03469420000000001
print(timeit.timeit('sum_n_v1(120)', number=1000, globals=globals()))  # 0.042930899999999994
print(timeit.timeit('sum_n_v1(150)', number=1000, globals=globals()))  # 0.07705480000000003
print(timeit.timeit('sum_n_v1(180)', number=1000, globals=globals()))  # 0.07950849999999998
print(timeit.timeit('sum_n_v1(210)', number=1000, globals=globals()))  # 0.10202799999999995
print(timeit.timeit('sum_n_v1(240)', number=1000, globals=globals()))  # 0.11235090000000003
print(timeit.timeit('sum_n_v1(270)', number=1000, globals=globals()))  # 0.13777210000000006
print(timeit.timeit('sum_n_v1(300)', number=1000, globals=globals()))  # 0.14455780000000007

cProfile.run('sum_n_v1(989)')
#         992 function calls (4 primitive calls) in 0.004 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#    989/1    0.004    0.000    0.004    0.004 les_04_task_01.py:8(sum_n_v1)
#        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


def sum_n_v2(input_count: int):
    if input_count == 0:
        return f'Сумма из ноль элементов равна неопределенности'
    num_sum = 1
    next_num = 1
    for el in range(input_count - 1):
        next_num *= -0.5
        num_sum += next_num
    return f'Сумма ряда чисел равна: {num_sum}'


print(timeit.timeit('sum_n_v2(3)', number=1000, globals=globals()))    # 0.0015104999999999702
print(timeit.timeit('sum_n_v2(6)', number=1000, globals=globals()))    # 0.0018992999999998261
print(timeit.timeit('sum_n_v2(9)', number=1000, globals=globals()))    # 0.0023406999999999734
print(timeit.timeit('sum_n_v2(12)', number=1000, globals=globals()))   # 0.0027466000000000435
print(timeit.timeit('sum_n_v2(15)', number=1000, globals=globals()))   # 0.0031745999999999164
print(timeit.timeit('sum_n_v2(18)', number=1000, globals=globals()))   # 0.003549999999999942
print(timeit.timeit('sum_n_v2(21)', number=1000, globals=globals()))   # 0.0037394000000001704
print(timeit.timeit('sum_n_v2(24)', number=1000, globals=globals()))   # 0.00408009999999992
print(timeit.timeit('sum_n_v2(27)', number=1000, globals=globals()))   # 0.004343100000000044
print(timeit.timeit('sum_n_v2(30)', number=1000, globals=globals()))   # 0.0052779000000000575
print(timeit.timeit('sum_n_v2(60)', number=1000, globals=globals()))   # 0.007797199999999949
print(timeit.timeit('sum_n_v2(90)', number=1000, globals=globals()))   # 0.010623100000000107
print(timeit.timeit('sum_n_v2(120)', number=1000, globals=globals()))  # 0.013684400000000041
print(timeit.timeit('sum_n_v2(150)', number=1000, globals=globals()))  # 0.01669760000000009
print(timeit.timeit('sum_n_v2(180)', number=1000, globals=globals()))  # 0.019507799999999964
print(timeit.timeit('sum_n_v2(210)', number=1000, globals=globals()))  # 0.02142640000000018
print(timeit.timeit('sum_n_v2(240)', number=1000, globals=globals()))  # 0.032030400000000014
print(timeit.timeit('sum_n_v2(270)', number=1000, globals=globals()))  # 0.03567620000000016
print(timeit.timeit('sum_n_v2(300)', number=1000, globals=globals()))  # 0.036035199999999934

cProfile.run('sum_n_v2(10_000_000)')
#         4 function calls in 1.263 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    1.263    1.263 <string>:1(<module>)
#        1    1.263    1.263    1.263    1.263 les_04_task_01.py:51(sum_n_v2)
#        1    0.000    0.000    1.263    1.263 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


def sum_n_v3(input_count: int):
    if input_count == 0:
        return f'Сумма из ноль элементов равна неопределенности'
    num_sum = 1
    next_num = 1
    while input_count > 1:
        next_num *= -0.5
        num_sum += next_num
        input_count -= 1
    return f'Сумма ряда чисел равна: {num_sum}'


print(timeit.timeit('sum_n_v3(3)', number=1000, globals=globals()))  # 0.0012555999999999123
print(timeit.timeit('sum_n_v3(6)', number=1000, globals=globals()))  # 0.0018591999999997277
print(timeit.timeit('sum_n_v3(9)', number=1000, globals=globals()))  # 0.0024614999999998943
print(timeit.timeit('sum_n_v3(12)', number=1000, globals=globals()))  # 0.0030498999999997167
print(timeit.timeit('sum_n_v3(15)', number=1000, globals=globals()))  # 0.003710299999999833
print(timeit.timeit('sum_n_v3(18)', number=1000, globals=globals()))  # 0.004419500000000021
print(timeit.timeit('sum_n_v3(21)', number=1000, globals=globals()))  # 0.004662500000000236
print(timeit.timeit('sum_n_v3(24)', number=1000, globals=globals()))  # 0.005136499999999877
print(timeit.timeit('sum_n_v3(27)', number=1000, globals=globals()))  # 0.005780100000000399
print(timeit.timeit('sum_n_v3(30)', number=1000, globals=globals()))  # 0.006043100000000301
print(timeit.timeit('sum_n_v3(60)', number=1000, globals=globals()))  # 0.01115939999999993
print(timeit.timeit('sum_n_v3(90)', number=1000, globals=globals()))  # 0.015989400000000042
print(timeit.timeit('sum_n_v3(120)', number=1000, globals=globals()))  # 0.021528499999999617
print(timeit.timeit('sum_n_v3(150)', number=1000, globals=globals()))  # 0.03271770000000007
print(timeit.timeit('sum_n_v3(180)', number=1000, globals=globals()))  # 0.04164449999999986
print(timeit.timeit('sum_n_v3(210)', number=1000, globals=globals()))  # 0.042269100000000004
print(timeit.timeit('sum_n_v3(240)', number=1000, globals=globals()))  # 0.04648089999999999
print(timeit.timeit('sum_n_v3(270)', number=1000, globals=globals()))  # 0.047139299999999995
print(timeit.timeit('sum_n_v3(300)', number=1000, globals=globals()))  # 0.05973240000000002

cProfile.run('sum_n_v3(10_000_000)')
#         4 function calls in 2.122 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    2.122    2.122 <string>:1(<module>)
#        1    2.122    2.122    2.122    2.122 les_04_task_01.py:94(sum_n_v3)
#        1    0.000    0.000    2.122    2.122 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Вывод: сравнивая 3 варианта реализации подсчета суммы лучший вариант sum_n_v2, т.к. в нем используется цикл for
# и с увеличением количества суммируемых элементов скорость выполнения расчета происходит быстрее
