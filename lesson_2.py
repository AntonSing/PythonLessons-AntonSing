#Task 1
num_1 = int(input("Введите делимое: "))
num_2 = int(input("Введите делитель: "))
if num_2 != 0:
    num_3 = num_1 / num_2
    print(num_3)
else:
    print("На ноль делить нельзя")

#Task 2
sum = int(input("Введите сумму покупки: "))
if sum > 20:
    sum_1 = sum * 0.35
    print("Скидка: ", round(sum_1, 2))
    print("Итоговая стоимость: ", round(sum - sum_1, 2))
elif 1 <= sum <= 20:
    print('Скидки нет')
else:
    print('Ошибка')

#Task 3
data = int(input("Введите число от 1 до 12: "))
if data == 12 or data == 1 or data == 2:
    if data == 12:
        print("Месяц: Декабрь")
    if data == 1:
        print("Месяц: Январь")
    if data == 2:
        print("Месяц: Февраль")
    print("Время года: Зима")
elif data == 3 or data == 4 or data == 5:
    if data == 3:
        print("Месяц: Март")
    if data == 4:
        print("Месяц: Апрель")
    if data == 5:
        print("Месяц: Май")
    print("Время года: Весна")
elif data == 7 or data == 8 or data == 9:
    if data == 7:
        print("Месяц: Июнь")
    if data == 8:
        print("Месяц: Июль")
    if data == 9:
        print("Месяц: Август")
    print("Время года: Лето")
elif data == 9 or data == 10 or data == 11:
    if data == 9:
        print("Месяц: Сентябрь")
    if data == 10:
        print("Месяц: Октябрь")
    if data == 11:
        print("Месяц: Ноябрь")
    print("Время года: Осень")
else:
    print("Ошибка")