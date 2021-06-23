"""

Найти максимальный элемент среди минимальных элементов столбцов матрицы.

"""

import random


def list_nums():
    numbers = range(0, 100)
    return [random.choices(numbers, k=5) for i in range(5)]


def max_in_min(lst):

    print(f'\nМатрица: \n{lst}')

    min_lst = []
    for i in range(len(lst)):
        min_ = lst[0][i]
        for j in range(len(lst[i])):
            if lst[j][i] < min_:
                min_ = lst[j][i]
        min_lst.append(min_)
    print(f'Минимальные элементы столбцов матрицы: \n{min_lst}')

    max_min = min_lst[0]
    for n in range(len(min_lst)):
        if min_lst[n] > max_min:
            max_min = min_lst[n]
    print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: \n{max_min}')


max_in_min(list_nums())
