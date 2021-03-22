# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
#    У пользователя необходимо запрашивать новый элемент рейтинга.
#    Если в рейтинге существуют элементы с одинаковыми значениями,
#    то новый элемент с тем же значением должен разместиться после них.


my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг = {my_list}")
new_el = int(input("Введите число: "))
for i in range(len(my_list)):
    if my_list[i] == new_el:
        my_list.insert(i + 1, new_el)
        break
    elif my_list[0] < new_el:
        my_list.insert(0, new_el)
    elif my_list[-1] > new_el:
        my_list.append(new_el)
    elif my_list[i] > new_el > my_list[i + 1]:
        my_list.insert(i + 1, new_el)

print(f"Текущий список = {my_list}")

