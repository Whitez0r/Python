# 1. Создать список и заполнить его элементами различных типов данных.
#    Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
#    Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [1, "abc", True, None, {1: "one"}, ('a', 'b', 'c'), 1.5, [1, 3, 5, 7, 9]]

for i in my_list:
    print(f"{i} - {type(i)}")
