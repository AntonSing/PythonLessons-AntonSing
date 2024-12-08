#Task 1
import math
radius = int(input("Введите радиус:"))
print("Длина окружности: ", round(2 * math.pi * radius, 2))
print("Площадь круга: ", round(math.pi * radius ** 2, 2))

#Task 2
x, y = 10, 55
print('x =', x)
print('y =', y)
x, y = y, x
print('Замена:', x, y)

#Task 3
import math
length = int(input("Введите длину маятника: "))
g = 9.81
period = 2 * math.pi * math.sqrt(length / g)
print(round(period, 2))