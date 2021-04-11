"""
    2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
    выполнить подсчет количества строк, количества слов в каждой строке.
"""


with open("example2.txt") as string:
    content = string.readlines()
    n = 0
    for i in content:
        count_words = len(i.split())
        n += 1
        print(f"Количество слов в {n} строке = {count_words}")
    print(f"Количество строк = {n}")
