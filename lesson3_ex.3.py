"""

В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

"""

import random


def list_nums():
    numbers = range(1, 100)
    return random.sample(numbers, 25)


def min_max(nums):
    print(f'Изначальный рандомный список: \n{nums}\n')
    max_ = nums[0]
    min_ = nums[0]
    for i in range(len(nums)):
        if max_ < nums[i]:
            max_ = nums[i]
        if min_ > nums[i]:
            min_ = nums[i]
    max_index = nums.index(max_)
    min_index = nums.index(min_)
    nums[max_index], nums[min_index] = nums[min_index], nums[max_index]
    return print(f'Изменённый рандомный список: \n{nums}\n\nМаксимальное число: {max_}\nМинимальное число: {min_}')


min_max(list_nums())
