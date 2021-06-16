"""

https://drive.google.com/file/d/1ztZ89NcSeth7PHt3kZY_ZfQJmTM1Q1Ky/view?usp=sharing

Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

"""


def symbols(start, end, column=1):
    if start == end:
        return f'{end}: {chr(end)}'
    if column % 10 == 0:
        return f'{start}: {chr(start)}\n{symbols(start + 1, end, column + 1)}'
    else:
        return f'{start}: {chr(start)}\t{symbols(start + 1, end, column + 1)}'


z = symbols(32, 127)
print(z)



