# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
#    Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.


n = input("Введите число n: ")
count_2 = n + n
count_2 = int(count_2)
count_3 = n + n + n
count_3 = int(count_3)
n = int(n)
print(n + count_2 + count_3)
