#Task 2.2
import math
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
total_need = 0 # Необходимая подушка безопасности
for month in range(months):
    if month == 0:
        current_spend = spend
    else:
        current_spend *= 1 + increase
    difference = current_spend - salary
    if difference > 0:
        total_need += difference
total_need = math.ceil(total_need)
print(f"Подушка безопасности, что протянуть {months} месяцев без долгов: {total_need}")