"""

Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

Разбил на несколько функций для читаемости.

"""

from collections import namedtuple


def enterprises():

    Enterprise = namedtuple('Year_profit', ['q1', 'q2', 'q3', 'q4'])
    company = {}
    num = int(input("Количество предприятий: "))

    for i in range(num):
        company_name = input(str(i+1) + '-е предприятие: ')
        profit_q1 = int(input('Прибыль за 1-й квартал $: '))
        profit_q2 = int(input('Прибыль за 2-й квартал $: '))
        profit_q3 = int(input('Прибыль за 3-й квартал $: '))
        profit_q4 = int(input('Прибыль за 4-й квартал $: '))
        company[company_name] = Enterprise(q1=profit_q1, q2=profit_q2, q3=profit_q3, q4=profit_q4)
    return company


def total(company):
    total_profit = {}
    for key, value in company.items():
        print(f'Предприятие {key}: прибыль за год - {sum(value)}$')
        total_profit[key] = sum(value)
    return total_profit


def avg_profit(profit):
    avg_profit_total = sum(profit.values()) / len(profit)
    print(f'Средняя прибыль за год для всех предприятий {avg_profit_total}$')
    return avg_profit_total


def low_avg_profit(profit, avg_prof):
    print('Предприятия, у которых прибыль ниже среднего:')

    for name, profit in profit.items():
        if profit < avg_prof:
            print(f'{name} - {profit}$')


def up_avg_profit(profit, avg_prof):
    print('Предприятия, у которых прибыль выше среднего:')

    for name, profit in profit.items():
        if profit > avg_prof:
            print(f'{name} - {profit}$')


enterprise = enterprises()
total = total(enterprise)
avg = avg_profit(total)
low_avg_profit(total, avg)
up_avg_profit(total, avg)
