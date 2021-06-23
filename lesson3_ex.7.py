"""

В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

"""

import random


def list_nums():
    numbers = range(0, 1000)
    return random.choices(numbers, k=50)


def min_nums(lst):
    print(lst)
    min_1 = 0
    min_2 = 1
    for i in lst:
        if i < lst[min_1] and lst.index(i) != min_1:
            min_2 = min_1
            min_1 = lst.index(i)
        elif i < lst[min_2] and lst.index(i) != min_1:
            min_2 = lst.index(i)
    return print(f'{lst[min_1]}, {lst[min_2]}')


min_nums(list_nums())
