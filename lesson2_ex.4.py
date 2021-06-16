"""

https://drive.google.com/file/d/1ztZ89NcSeth7PHt3kZY_ZfQJmTM1Q1Ky/view?usp=sharing

Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

"""


n = int(input('Введите длинну ряда: '))
sum_ = 0
num_ = 1
for i in range(n):
    sum_ += num_
    num_ /= -2
print(f'Сумма ряда чисел = {sum_}')