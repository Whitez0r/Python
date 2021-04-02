"""
    1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
    В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
    Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""


from sys import argv

script_name, time, pay_per_hour, bonus = argv


def calc_salary(time, pay_per_hour, bonus):
    return time * pay_per_hour + bonus


salary = calc_salary(int(time), int(pay_per_hour), int(bonus))

print(f'Зарплата сотрудника = {salary}')
