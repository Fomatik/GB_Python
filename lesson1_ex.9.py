"""

https://drive.google.com/file/d/1mb-ntuxJivA7m_0DV2UJ8FItX86-M8K3/view?usp=sharing

Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

Начало
Вывод("Программа для определения среднего числа из трёх чисел.")
Вывод("Введите 3 целых числа:")
Ввод(num_1)
Ввод(num_2)
Ввод(num_3)
Если num_1 == num_2 или num_1 == num_3 или num_2 == num_3
То Вывод("Расчёт среднего числа не возможен, вы ввели два одинаковых числа.")
Иначе Если num_1 < num_2 < num_3 или num_3 < num_2 < num_1
То avg_num = num_2
Если num_2 < num_1 < num_3 или num_3 < num_1 < num_2
То avg_num = num_1
Иначе avg_num = num_3
Вывод(avg_num)
Конец
"""

print('Программа для определения среднего числа из трёх чисел.\n')

print('Введите 3 целых числа: ')
num_1 = int(input('Первое число: '))
num_2 = int(input('Второе число: '))
num_3 = int(input('Третье число: '))

if num_1 == num_2 or num_1 == num_3 or num_2 == num_3:
    print('Расчёт среднего числа не возможен, вы ввели два одинаковых числа.')
else:
    if num_1 < num_2 < num_3 or num_3 < num_2 < num_1:
        avg_num = num_2
    elif num_2 < num_1 < num_3 or num_3 < num_1 < num_2:
        avg_num = num_1
    else:
        avg_num = num_3
    print(f'\nСреднее число из {num_1}, {num_2}, {num_3}: {avg_num}')