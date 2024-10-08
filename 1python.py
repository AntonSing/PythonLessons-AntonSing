#Task 1
import math
r = int(input("Введите радиус:"))
a = (2*math.pi*r)
b = (math.pi*r**2)
print('Длина окружности: ', round (a, 2))
print('Площадь круга: ', round(b, 2))

#Task 2
x, y = 10, 55
print('x =', x)
print('y =', y)
x, y = y, x
print('Замена:', x, y)

#Task 3
import math
g = 9.81
l = int(input('Введите длину маятника в метрах: '))
b = l/g
T = (2*math.pi*math.sqrt(b))
print(round(T, 2))