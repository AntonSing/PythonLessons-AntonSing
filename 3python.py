#Task 1
n = int(input('Введите число:'))
s = 0
if n >= 100:
    print('Ошибка')
else:
    for i in range(1, n + 1):
        s += i**3
print(s)

#Task 2
for i in range(1,10):
    for j in range(1,10):
        print(f'{i * j: 3}', end=' ')
    print()