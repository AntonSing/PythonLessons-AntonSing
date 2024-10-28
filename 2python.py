#Task 1
num_1 = int(input("Введите делимое: "))
num_2 = int(input("Введите делитель: "))
if num_2 != 0:
    num_3 = num_1 / num_2
    print(num_3)
else:
    print("На ноль делить нельзя")

#Task 2
a = int(input('Введите сумму покупки: '))
if a > 20:
    b = a*0.35
    c = a - b
    print('Сумма со скидкой: ', round (c, 2))
    print('Размер скидки: ', b)
elif 1 <= a <= 20:
    print('Скидки нет')
else:
    print('Ошибка')

#Task 3
a = int(input('Введите число от 1 до 12: '))
if a == 12 or a == 1 or a == 2:
   if a == 12:
    print('Месяц: Декабрь')
   if a == 1:
    print('Месяц: Январь')
   if a == 2:
     print('Месяц: Февраль')
   print('Время года: Зима')
elif a == 3 or a == 4 or a == 5:
   if a == 3:
     print('Месяц: Март')
   if a == 4:
     print('Месяц: Апрель')
   if a == 5:
     print('Месяц: Май')
   print('Время года: Весна')
elif a == 6 or a == 7 or a == 8:
   if a == 6:
     print('Месяц: Июнь')
   if a == 7:
     print('Месяц: Июль')
   if a == 8:
     print('Месяц: Август')
   print('Время года: Лето')
elif a == 9 or a == 10 or a == 11:
   if a == 9:
     print('Месяц: Сентябрь')
   if a == 10:
     print('Месяц: Октябрь')
   if a == 11:
     print('Месяц: Ноябрь')
   print('Время года: Осень')
else:
  print('Ошибка')