# Task 4(Сортировка списка пузырьком)
n = 6
mas = [ 5,2,9,1,5,6]
count = 0
for run in range(n-1):
    for i in range(n-1):
        if mas[i] > mas[i+1]:
            count += 1
            mas[i], mas[i+1] = mas[i+1], mas[i]
print(mas)
print(count)

# Task 5(Максимальное число в списке двумя способами)
import time
import random
def find_max_simple(lst):
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num
def main():
    size = 10**6
    lst = [random.randint(1, 10**6) for _ in range(size)]

    start_time = time.time()
    max_simple = find_max_simple(lst)
    simple_time = time.time() - start_time
    print(f"Максимум: {max_simple}, время: {simple_time:.6f} секунд")

    start_time = time.time()
    max_builtin = max(lst)
    builtin_time = time.time() - start_time
    print(f"Максимум: {max_builtin}, время {builtin_time:.6f} секунд")
if __name__ == "__main__":
    main()

# Task 9(Расчёт факториала через функцию)
number = int(input("Число для факториала: "))
def factorial(n):
    if n < 0:
        return
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
print(factorial(number))

# Task 10(Функция с замыканием)
def multi(fact):
    def multi_by(x):
        return x * fact
    return multi_by
double = multi(2)
triple = multi(3)
print(double(4))
print(triple(4))

# Task 11(Атд: стек)
a = input("Введите строку: ")
stack = []
Verify = True

for lt in a:
    if lt in "([{":
        stack.append(lt)
    elif lt in ")]}":
        if len(stack) == 0:
            Verify = False
            break

        br = stack.pop()
        if br == "(" or lt == ")":
            continue
        if br == "[" or lt == "]":
            continue
        if br == "{" or lt == "{":
            continue

        Verify = False
        break
if Verify and len(stack) == 0:
    print("Yes")
else:
    print("No")