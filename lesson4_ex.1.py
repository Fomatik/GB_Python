import random
import timeit
import cProfile
import numpy as np

"""

Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.

Примечание. Идеальным решением будет:

● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),

● написать 3 варианта кода (один у вас уже есть),

● проанализировать 3 варианта и выбрать оптимальный,

● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),

● написать общий вывод: какой из трёх вариантов лучше и почему.

"""

"""

Я выбрал 9 задание из 3 урока: найти максимальный элемент среди минимальных элементов столбцов матрицы.

С оценокой сложности алгоритмов пока не всё до конца понимаю, но предполагаю что сложность этого
алгоритма O(n).

"""

# Вариант 1.


def list_nums(len_lst, len_arr):
    numbers = range(0, 200)
    return [random.choices(numbers, k=len_lst) for len_ in range(len_arr)]


def min_in_lst(lst):
    min_lst = []
    for i in range(len(lst)):
        min_ = lst[0][i]
        for j in range(len(lst[i])):
            if lst[j][i] < min_:
                min_ = lst[j][i]
        min_lst.append(min_)
    # print(f'Минимальные элементы столбцов матрицы: \n{min_lst}')
    return min_lst


def max_in_min(min_lst):
    max_min = min_lst[0]
    for n in range(len(min_lst)):
        if min_lst[n] > max_min:
            max_min = min_lst[n]
    # print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: \n{max_min}')
    return max_min


for m in range(5):
    print(timeit.timeit(f'max_in_min(min_in_lst(list_nums({5**m}, {5**m})))', number=100, globals=globals()))

cProfile.run('max_in_min(min_in_lst(list_nums(900, 900)))')

"""
0.00031650000000005285
0.0015100000000001224
0.021043899999999782
0.4951798999999999
12.518390799999999
         814509 function calls in 0.534 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.003    0.003    0.534    0.534 <string>:1(<module>)
        1    0.000    0.000    0.407    0.407 lesson4_ex.1.py:36(list_nums)
        1    0.004    0.004    0.407    0.407 lesson4_ex.1.py:38(<listcomp>)
        1    0.122    0.122    0.123    0.123 lesson4_ex.1.py:41(min_in_lst)
        1    0.000    0.000    0.000    0.000 lesson4_ex.1.py:53(max_in_min)
      900    0.005    0.000    0.403    0.000 random.py:386(choices)
      900    0.319    0.000    0.398    0.000 random.py:399(<listcomp>)
        1    0.000    0.000    0.534    0.534 {built-in method builtins.exec}
     1802    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      900    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   810000    0.079    0.000    0.079    0.000 {method 'random' of '_random.Random' objects}
"""

# Вариант 2


def list_nums(len_lst, len_arr):
    return np.random.random_integers(1, 1000, (len_arr, len_lst))


def min_in_lst(lst):
    min_lst = []
    for i in range(len(lst)):
        min_lst.append(min(lst[i]))
    # print(f'Минимальные элементы столбцов матрицы: \n{min_lst}')
    return min_lst


def max_in_min(min_lst):
    max_min = 0
    for n in range(len(min_lst)):
        max_min = max(min_lst)
    # print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: \n{max_min}')
    return max_min


for m in range(5):
    print(timeit.timeit(f'max_in_min(min_in_lst(list_nums({5**m}, {5**m})))', number=100, globals=globals()))

cProfile.run('max_in_min(min_in_lst(list_nums(900, 900)))')

"""
0.0027999000000000773
0.00364169999999997
0.010139200000000015
0.1395010000000001
2.9943558
         2718 function calls in 0.060 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <__array_function__ internals>:2(prod)
        1    0.000    0.000    0.060    0.060 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:2928(_prod_dispatcher)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:2933(prod)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:69(_wrapreduction)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:70(<dictcomp>)
        1    0.001    0.001    0.041    0.041 lesson4_ex.1.py:102(min_in_lst)
        1    0.000    0.000    0.015    0.015 lesson4_ex.1.py:110(max_in_min)
        1    0.000    0.000    0.004    0.004 lesson4_ex.1.py:98(list_nums)
        1    0.000    0.000    0.060    0.060 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      900    0.014    0.000    0.014    0.000 {built-in method builtins.max}
      900    0.041    0.000    0.041    0.000 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
      900    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        1    0.004    0.004    0.004    0.004 {method 'random_integers' of 'numpy.random.mtrand.RandomState' objects}
        1    0.000    0.000    0.000    0.000 {method 'reduce' of 'numpy.ufunc' objects}
"""

# Вариант 3


def list_nums(len_lst, len_arr):
    return np.random.random_integers(1, 1000, (len_arr, len_lst))


def max_in_min(lst, max_min=None):
    if max_min is None:
        max_min = []
    if len(lst) > 0:
        max_min.append(min(lst[-1]))
        max_in_min(lst[0:-1])

    else:
        return max(max_min)


# max_in_min(list_nums(900, 900))

for m in range(5):
    print(timeit.timeit(f'max_in_min(list_nums({5**m}, {5**m}))', number=100, globals=globals()))

cProfile.run('max_in_min(list_nums(900, 900))')

"""
0.0025681999999997984
0.0032376000000000626
0.013904899999999998
0.13274410000000003
2.6920203
         3617 function calls (2717 primitive calls) in 0.050 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <__array_function__ internals>:2(prod)
        1    0.000    0.000    0.050    0.050 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:2928(_prod_dispatcher)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:2933(prod)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:69(_wrapreduction)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:70(<dictcomp>)
        1    0.000    0.000    0.004    0.004 lesson4_ex.1.py:161(list_nums)
    901/1    0.002    0.000    0.046    0.046 lesson4_ex.1.py:165(max_in_min)
        1    0.000    0.000    0.050    0.050 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
      901    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.001    0.001    0.001    0.001 {built-in method builtins.max}
      900    0.042    0.000    0.042    0.000 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
      900    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        1    0.004    0.004    0.004    0.004 {method 'random_integers' of 'numpy.random.mtrand.RandomState' objects}
        1    0.000    0.000    0.000    0.000 {method 'reduce' of 'numpy.ufunc' objects}
"""


"""

Общее описание:

Я выбрал 9 задание из 3 урока: найти максимальный элемент среди минимальных элементов столбцов матрицы.

С оценокой сложности алгоритмов пока не всё до конца понимаю, но предполагаю что сложность этого
алгоритма O(n).

timeit(N) = (5**m, 5**m) for m in range(5)
cProfile(N) = 900*900 (по причине использования рекурсии ограничился цифрой 900)

В первом варианте использовал для создания матрицы random, что оказалось достаточно медленно.
В дальнейших случая использовал Numpy. Это повлияло на уменьшение времени выполнения кода, а так же на меншее количество
вызовов функций.

Первый вариант: использование циклов и сравнения.
Второй вариант: использование встроенных функций min и max.
Третий вариант: использование рекурсии.

Выбор:

По производительности второй и третий варианты похожи, но так как у рекурсии имеется ограничения, то лучший вариант
будет второй.

"""