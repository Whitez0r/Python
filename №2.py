"""
    2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
    имя, фамилия, год рождения, город проживания, email, телефон.
    Функция должна принимать параметры как именованные аргументы.
    Реализовать вывод данных о пользователе одной строкой.
"""


def my_func(name, surname, year, city, email, telephone) :
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(name='Ilya', surname='Mungalov', year='2001', city='Blagoveschensk', email='i_mungalov@mail.ru',
              telephone='+79143829543'))
