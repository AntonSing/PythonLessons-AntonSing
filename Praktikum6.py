#Task 1
import math
import matplotlib.pyplot as plt

class Derivative:
    def __init__(self, h=1e-5):
        self.h = h
        self.instance = None

    def __call__(self, func):
        def wrapper(x):
            return (func(x + self.h) - func(x - self.h)) / (2 * self.h)
        return wrapper

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self(instance)

class ExponentialFunction:
    def __init__(self, a):
        self.a = a
        self.derivative = Derivative()(self)

    def __call__(self, x):
        return self.a * math.exp(x)

    def plot(self):
        x_values = [x / 100 for x in range(-200, 201)]
        y_values = [self(x) for x in x_values]
        dy_values = [self.derivative(x) for x in x_values]

        plt.figure(figsize=(10, 6))
        plt.plot(x_values, y_values, label=f"f(x) = {self.a} * exp(x)")
        plt.plot(x_values, dy_values, label=f"f'(x) = {self.a} * exp(x)")
        plt.title("Графики функции и её производной")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.grid(True)
        plt.show()

# Пример:
exp_func = ExponentialFunction(a=2)
print(exp_func(0))          # 2.0
print(exp_func.derivative(0))  # 2.0 (производная 2e^x в x=0)

# Построение графиков
exp_func.plot()