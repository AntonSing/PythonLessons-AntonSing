#Task 1

# Создание объекта Series из списка:
import pandas as pd
data_list = [10, 20, 30, 40, 50]
series_from_list = pd.Series(data_list)
print("Series из списка:")
print(series_from_list)

# Создание объекта Series из массива NumPy:
import numpy as np
data_array = np.array([100, 200, 300, 400, 500])
series_from_array = pd.Series(data_array)
print("\nSeries из массива NumPy:")
print(series_from_array)

# Создание объекта Series из словаря:
data_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
series_from_dict = pd.Series(data_dict)
print("\nSeries из словаря:")
print(series_from_dict)

#Task 2
import pandas as pd
series1 = pd.Series([1, 2, 3, 4, 5])
series2 = pd.Series([4, 5, 6, 7, 8])
unique_elements = pd.Series(list(set(series1) ^ set(series2)))
print("Непересекающиеся элементы:")
print(unique_elements)

#Task 3
import pandas as pd
import matplotlib.pyplot as plt
data = pd.Series(['apple', 'banana', 'apple', 'orange', 'banana', 'banana', 'orange', 'apple', 'grape'])
frequency = data.value_counts()
plt.figure(figsize=(8, 6))
plt.bar(frequency.index, frequency.values)
plt.title("Частота уникальных элементов")
plt.xlabel("Элементы")
plt.ylabel("Частота")
plt.show()