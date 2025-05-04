import matplotlib.pyplot as plt
import numpy as np
def f(x):
    return x ** 2
def g(x):
    return 2 * x + 3
x_values = np.arange(0, 6)
f_values = f(x_values)
g_values = g(x_values)
width = 0.4
x_indexes = np.arange(len(x_values))
plt.bar(x_indexes - width/2, f_values, width, label = "f(x) = x ^ 2", color = "green")
plt.bar(x_indexes + width/2, g_values, width, label = "g(x) = 2x + 3", color = "orange")
plt.xticks(x_indexes, x_values)
plt.xlabel("x")
plt.ylabel("f(x) и g(x)")
plt.title("Сравнение функций f(x) и g(x)")
plt.legend()
plt.show()