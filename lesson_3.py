#Task 1
up_lim = int(input("Введите чило не превышающее 100: "))
m = 0
if up_lim > 100:
    print("Error")
else:
    for i in range(1, up_lim + 1):
        m += i ** 3
print(f"Сумма кубов от 1 до {up_lim} равна:", m)

#Task 2
for i in range(1,10):
    for j in range(1,10):
        print(f"{i * j: 3}", end=" ")
    print()