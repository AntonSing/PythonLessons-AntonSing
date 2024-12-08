#Task 1
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('path_to_file.csv')

# 1. Средняя доходность женщин
avg_income_female = df[df['sex'] == 'female']['income'].mean()
print(f"Средняя доходность женщин: {avg_income_female}")

# 2. Определяем у обеих полов людей с большими расходами
median_expenses = df['expenses'].median()

high_expenses_men = df[(df['sex'] == 'male') & (df['expenses'] > median_expenses)]
high_expenses_women = df[(df['sex'] == 'female') & (df['expenses'] > median_expenses)]

print(f"Количество мужчин с большими расходами: {high_expenses_men.shape[0]}")
print(f"Количество женщин с большими расходами: {high_expenses_women.shape[0]}")

# 3. График зависимости доходов от возраста для мужчин
df_men = df[df['sex'] == 'male']
plt.figure(figsize=(8, 6))
plt.scatter(df_men['age'], df_men['income'], color='blue', alpha=0.6)
plt.title('Зависимость доходов от возраста для мужчин')
plt.xlabel('Возраст')
plt.ylabel('Доход')
plt.grid(True)
plt.show()

# 4. Столбчатый график для мужчин и женщин, распределение расходов в зависимости от доходов
plt.figure(figsize=(10, 6))

sns.histplot(data=df[df['sex'] == 'male'], x='income', y='expenses', color='blue', kde=False, label='Мужчины')

sns.histplot(data=df[df['sex'] == 'female'], x='income', y='expenses', color='pink', kde=False, label='Женщины')
plt.title('Распределение расходов в зависимости от доходов')
plt.xlabel('Доход')
plt.ylabel('Расходы')
plt.legend()
plt.grid(True)
plt.show()