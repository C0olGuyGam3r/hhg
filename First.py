import numpy as np
import matplotlib.pyplot as plt
from math import cos

def f1_graph(x):
    return (0.2 * x) ** 3

def f2_graph(x):
    return cos(x)

def f_diff(x):
    """Разность функций: (0.2*x)^3 - cos(x) = 0"""
    return (0.2 * x) ** 3 - cos(x)

x_vals = np.linspace(-10, 10, 1000)
y_left = f1_graph(x_vals)
y_right = f2_graph(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_left, label='(0.2*x)^3', linewidth=2)
plt.plot(x_vals, y_right, label='cos(x)', linewidth=2)
plt.axhline(y=0, color='k', linestyle='--', linewidth=0.8)
plt.axvline(x=0, color='k', linestyle='--', linewidth=0.8)
plt.grid(True, alpha=0.3)
plt.title('Графическое отделение корней уравнения (0.2*x)^3 = cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

intervals = []
step = 0.5
x_start = -5
x_end = 5
x_test = np.arange(x_start, x_end, step)

for i in range(len(x_test) - 1):
    if f_diff(x_test[i]) * f_diff(x_test[i + 1]) < 0:
        intervals.append((x_test[i], x_test[i + 1]))

print("Интервалы, содержащие корни:")
if intervals:
    for idx, (a, b) in enumerate(intervals, 1):
        print(f"  Корень {idx}: x ∈ [{a:.2f}, {b:.2f}]")
else:
    print("  Корней не найдено на интервале [-5, 5]")