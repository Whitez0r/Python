"""
    1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
    Об окончании ввода данных свидетельствует пустая строка.
"""


new_file = open('example.txt', 'w')

string = input("Введите текст \n ")

while string:
    new_file.writelines(string)
    string = input("Введите текст \n ")
    if not string:
        break
new_file.close()