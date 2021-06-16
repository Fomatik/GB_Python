"""

https://drive.google.com/file/d/1ztZ89NcSeth7PHt3kZY_ZfQJmTM1Q1Ky/view?usp=sharing

Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

"""


def odd_or_even(num, odd=0, even=0):
    if num < 1:
        return print(f'Сумма нечетных цифр: {odd}\nСумма чётных цифр: {even}')
    if ~(num % 10) & 1:
        return odd_or_even(num // 10, even=even+1, odd=odd)
    else:
        return odd_or_even(num // 10, odd=odd+1, even=even)


odd_or_even(int(input('Введите натуральное число: ')))