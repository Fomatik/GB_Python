"""

Написать программу сложения и умножения двух положительных целых шестнадцатеричныйх чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Умножение пока не осилил(

"""
from collections import deque

# Сложение


def hex_sum(hex_1, hex_2):
    hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    rev_hex_dict = dict(map(reversed, hex_dict.items()))
    hex_1 = deque(hex_1)
    hex_2 = deque(hex_2)
    result = deque()

    if len(hex_1) < len(hex_2):
        hex_1, hex_2 = hex_2, hex_1
    hex_2.extendleft('0' * (len(hex_1) - len(hex_2)))

    rest = 0
    while hex_1:
        term_1 = hex_dict[hex_1.pop()]
        term_2 = hex_dict[hex_2.pop()]
        res_sum = term_1 + term_2 + rest

        if res_sum > len(hex_dict):
            rest = 1
            res_sum -= len(hex_dict)
        else:
            rest = 0
        result.appendleft(rev_hex_dict[res_sum])

    if rest == 1:
        result.appendleft('1')
    return ''.join(result)


print('Шестнадцатеричное сложение двух чисел\n')
num_1 = input('Первое шестнадцатеричное число: ').upper()
num_2 = input('Второе шестнадцатеричное число: ').upper()
print(f'{num_1} + {num_2} = {hex_sum(num_1, num_2)}')
