import timeit
import cProfile


def sieve(input_num: int):
    n = 1000  # количество элементов массива, не включая 1000
    sieve_arr = [i for i in range(n)]
    sieve_arr[1] = 0
    for i in range(2, n):
        if sieve_arr[i] != 0:
            j = i + i
            input_num -= 1
            while j < n:
                sieve_arr[j] = 0
                j += i
        if input_num == 0:
            return sieve_arr[i]


print(timeit.timeit('sieve(1)', number=1000, globals=globals()))    # 0.1225957
print(timeit.timeit('sieve(2)', number=1000, globals=globals()))    # 0.14306189999999996
print(timeit.timeit('sieve(3)', number=1000, globals=globals()))    # 0.17380420000000002
print(timeit.timeit('sieve(4)', number=1000, globals=globals()))    # 0.21530660000000007
print(timeit.timeit('sieve(5)', number=1000, globals=globals()))    # 0.22823339999999992
print(timeit.timeit('sieve(6)', number=1000, globals=globals()))    # 0.23672460000000006
print(timeit.timeit('sieve(7)', number=1000, globals=globals()))    # 0.23804420000000004
print(timeit.timeit('sieve(8)', number=1000, globals=globals()))    # 0.2500233999999999
print(timeit.timeit('sieve(9)', number=1000, globals=globals()))    # 0.251949
print(timeit.timeit('sieve(10)', number=1000, globals=globals()))   # 0.28080039999999995
print(timeit.timeit('sieve(20)', number=1000, globals=globals()))   # 0.30929980000000024
print(timeit.timeit('sieve(30)', number=1000, globals=globals()))   # 0.3341512
print(timeit.timeit('sieve(40)', number=1000, globals=globals()))   # 0.33846160000000003
print(timeit.timeit('sieve(50)', number=1000, globals=globals()))   # 0.30113119999999993
print(timeit.timeit('sieve(60)', number=1000, globals=globals()))   # 0.3422434999999999
print(timeit.timeit('sieve(70)', number=1000, globals=globals()))   # 0.42529919999999954
print(timeit.timeit('sieve(80)', number=1000, globals=globals()))   # 0.39043899999999976
print(timeit.timeit('sieve(90)', number=1000, globals=globals()))   # 0.4047800000000006
print(timeit.timeit('sieve(100)', number=1000, globals=globals()))  # 0.3926129999999999
cProfile.run('sieve(999)')
#         5 function calls in 0.001 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 les_04_tast_02.py:5(sieve)
#        1    0.000    0.000    0.000    0.000 les_04_tast_02.py:7(<listcomp>)
#        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


def prime(input_num: int):
    num_lim = 1000
    for el in range(2, num_lim):
        flag = 0
        for elem in range(2, num_lim):
            if el % elem == 0 and el != elem:
                flag = 1
                break
        if flag == 0:
            input_num -= 1
        if input_num == 0:
            return el


print(timeit.timeit('prime(1)', number=1000, globals=globals()))    # 0.08750329999999984
print(timeit.timeit('prime(2)', number=1000, globals=globals()))    # 0.15890730000000008
print(timeit.timeit('prime(3)', number=1000, globals=globals()))    # 0.2451774000000002
print(timeit.timeit('prime(4)', number=1000, globals=globals()))    # 0.34518179999999976
print(timeit.timeit('prime(5)', number=1000, globals=globals()))    # 0.42765269999999944
print(timeit.timeit('prime(6)', number=1000, globals=globals()))    # 0.4704315000000001
print(timeit.timeit('prime(7)', number=1000, globals=globals()))    # 0.5869682000000003
print(timeit.timeit('prime(8)', number=1000, globals=globals()))    # 0.6527509000000009
print(timeit.timeit('prime(9)', number=1000, globals=globals()))    # 0.6432850999999999
print(timeit.timeit('prime(10)', number=1000, globals=globals()))   # 0.7816863000000005
print(timeit.timeit('prime(20)', number=1000, globals=globals()))   # 1.5248834999999996
print(timeit.timeit('prime(30)', number=1000, globals=globals()))   # 2.3100398999999996
print(timeit.timeit('prime(40)', number=1000, globals=globals()))   # 3.1604116000000015
print(timeit.timeit('prime(50)', number=1000, globals=globals()))   # 4.1840796000000005
print(timeit.timeit('prime(60)', number=1000, globals=globals()))   # 4.941865200000002
print(timeit.timeit('prime(70)', number=1000, globals=globals()))   # 5.8049380000000035
print(timeit.timeit('prime(80)', number=1000, globals=globals()))   # 6.619371600000001
print(timeit.timeit('prime(90)', number=1000, globals=globals()))   # 7.5810995000000005
print(timeit.timeit('prime(100)', number=1000, globals=globals()))  # 8.495418199999996

cProfile.run('prime(999)')
#         4 function calls in 0.013 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.013    0.013 <string>:1(<module>)
#        1    0.013    0.013    0.013    0.013 les_04_tast_02.py:52(prime)
#        1    0.000    0.000    0.013    0.013 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

z = sieve(5)
print(z)
m = prime(5)
print(m)

# Вывод: алгоритм "Решето Эратосфена" работает более эффективнее, чем алгоритм поиска простых чисел по определению.
# При увеличении поиска элемента ближе к концу, нагрузка на поиск возрастает.
# Так же понял, что мой ноутбук в текущем состоянии не подходит для проведения лабораторных испытанию, т.к. пришлось
# делать очень много итераций, чтобы получить приблизительно правдивые результаты...
