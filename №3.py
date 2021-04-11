"""
    3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
    Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
    Выполнить подсчет средней величины дохода сотрудников.
"""

with open("example3.txt") as my_txt:
    content = my_txt.readlines()
    surname = []
    salary = []
    for i in content:
        content_list = (i.split())
        print(content_list)
        if int(content_list[1]) < 20000:
            surname.append(content_list[0])
        salary.append(int(content_list[1]))
print(f'Оклад меньше 20 тыс: {str(surname)}, Средняя величина дохода сотрудников = {sum(salary) / len(salary)}')
