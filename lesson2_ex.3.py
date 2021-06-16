"""

https://drive.google.com/file/d/1ztZ89NcSeth7PHt3kZY_ZfQJmTM1Q1Ky/view?usp=sharing

Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.

"""


def backward(num):
    if num == 0:
        return ''
    else:
        return f'{num % 10}{backward(num // 10)}'


print('Программа задом на перёд!')
z = backward(int(input('Введите число: ')))
print(f'Число наоборот: {z}')