"""

В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

"""

result = {}
for num in range(2, 10):
    result[num] = []
    for nums in range(2, 100):
        if nums % num == 0:
            result[num].append(nums)
    print(f'Числа кратные {num} - {len(result[num])}: {repr(result[num])}.')
