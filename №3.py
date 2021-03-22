# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
#    Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
#    Напишите решения через list и через dict.


month = int(input("Введите месяц в виде целого числа: "))
all_month_list = ["Зима", "Весна", "Лето", "Осень"]
all_month_dict = {
    1: "Зима",
    2: "Весна",
    3: "Лето",
    4: "Осень",
}

if month == 1 or month == 2 or month == 12:
    print(f"Решение через список: {month} - {all_month_list[0]}")
    print(f"Решение через словарь: {month} - {all_month_dict.get(1)}")

elif month == 3 or month == 4 or month == 5:
    print(f"Решение через список: {month} - {all_month_list[1]}")
    print(f"Решение через словарь: {month} - {all_month_dict.get(2)}")

elif month == 6 or month == 7 or month == 8:
    print(f"Решение через список: {month} - {all_month_list[2]}")
    print(f"Решение через словарь: {month} - {all_month_dict.get(3)}")

else:
    print(f"Решение через список: {month} - {all_month_list[3]}")
    print(f"Решение через словарь: {month} - {all_month_dict.get(4)}")