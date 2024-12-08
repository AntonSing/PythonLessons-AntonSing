#Task 1
import numpy as np
import matplotlib.pyplot as plt
def f(x, alpha, beta):
    return (x**beta + alpha**beta) / (x**beta)
x = np.linspace(0.1, 5, 500)
parameters = [(1, 1), (2, 1), (1, 2)]
plt.figure(figsize=(10, 6))
for alpha, beta in parameters:
    y = f(x, alpha, beta)
    plt.plot(x, y, label=f"α={alpha}, β={beta}")
plt.title("Графики функции f(x) при различных α и β")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.savefig("function_plot.svg")
plt.show()

#Task 2
import numpy as np
import matplotlib.pyplot as plt
def f(x, alpha, beta):
    return (x**beta + alpha**beta) / (x**beta)
x = np.linspace(0.1, 5, 500) 
small_x = np.linspace(0.1, 1, 500) 
large_x = np.linspace(3, 10, 500)
parameters = [(1, 1), (2, 1), (1, 2)]
fig, ax_main = plt.subplots(figsize=(12, 8))
for alpha, beta in parameters:
    y = f(x, alpha, beta)
    ax_main.plot(x, y, label=f"α={alpha}, β={beta}")
ax_main.set_title("Графики функции f(x) с врезками для малых и больших x")
ax_main.set_xlabel("x")
ax_main.set_ylabel("f(x)")
ax_main.legend()
ax_main.grid(True)
ax_inset_small = fig.add_axes([0.2, 0.6, 0.25, 0.25])
for alpha, beta in parameters:
    y_small = f(small_x, alpha, beta)
    ax_inset_small.plot(small_x, y_small, label=f"α={alpha}, β={beta}")
ax_inset_small.set_title("Малые x")
ax_inset_small.grid(True)
ax_inset_large = fig.add_axes([0.6, 0.2, 0.25, 0.25])
for alpha, beta in parameters:
    y_large = f(large_x, alpha, beta)
    ax_inset_large.plot(large_x, y_large, label=f"α={alpha}, β={beta}")
ax_inset_large.set_title("Большие x")
ax_inset_large.grid(True)
plt.savefig("function_plot_with_insets.svg")
plt.show()

#Task 3
import numpy as np
import matplotlib.pyplot as plt
def f(x, alpha, beta):
    return (x**beta + alpha**beta) / (x**beta)
x_neg = np.linspace(-5, -0.1, 500)
f_zero = np.zeros_like(x_neg)
x_neg_inset = np.linspace(-5, -1, 500)
fig, ax_main = plt.subplots(figsize=(12, 8))
for alpha, beta in [(1, 1), (2, 1), (1, 2)]:
    ax_main.plot(x_neg, f(x_neg, alpha, beta), label=f"α={alpha}, β={beta}")
    ax_main.plot(x_neg_inset, f(x_neg_inset, alpha, beta), label=f"α={alpha}, β={beta}", linestyle='dashed')
ax_main.plot(x_neg, f_zero, 'k--', label="f(x) = 0")
ax_main.set_title("Графики функции f(x) для x < 0 с врезкой")
ax_main.set_xlabel("x")
ax_main.set_ylabel("f(x)")
ax_main.legend()
ax_main.grid(True)
ax_inset = fig.add_axes([0.6, 0.6, 0.25, 0.25]) 
for alpha, beta in [(1, 1), (2, 1), (1, 2)]:
    ax_inset.plot(x_neg_inset, f(x_neg_inset, alpha, beta), label=f"α={alpha}, β={beta}")
    ax_inset.plot(x_neg_inset, f_zero[:len(x_neg_inset)], 'k--', label="f(x) = 0")
ax_inset.set_title("x → −∞")
ax_inset.grid(True)
plt.savefig("function_plot_neg_x_with_inset.svg")
plt.show()