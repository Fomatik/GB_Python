"""

В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.

"""

import random


def list_nums():
    numbers = range(-100, 100)
    return random.sample(numbers, 25)


def max_of_min(nums):
    index = -1
    for i in range(len(nums)):
        if nums[i] < 0 and index == -1:
            index = i
        elif nums[index] < nums[i] < 0:
            index = i
    return print(f'{nums}\n{index + 1}: {nums[index]}')


max_of_min(list_nums())
