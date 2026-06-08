from math import cos, sin

def f(x):
    return (0.2 * x) ** 3 - cos(x)

def f_derivative(x):
    return 0.024 * x**2 + sin(x)

# Начальное приближение (из графического метода: корень около 1.5)
x0 = float(input('Введите начальное приближение x0: '))
eps = float(input('Введите точность eps: '))

print(f"\n{'n':^4} | {'x_n':^12} | {'f(x_n)':^14} | {'f\'(x_n)':^14} | {'x_{n+1}':^12}")
print("-" * 65)

n = 0
x_prev = x0

while True:
    fx = f(x_prev)
    fpx = f_derivative(x_prev)
    
    x_next = x_prev - fx / fpx
    
    print(f"{n:^4} | {x_prev:12.6f} | {fx:14.6e} | {fpx:14.6f} | {x_next:12.6f}")
    
    if abs(x_next - x_prev) < eps:
        print("-" * 65)
        print(f"\nКорень уравнения: {x_next:.6f}")
        print(f"Значение функции в корне: {f(x_next):.6e}")
        print(f"Количество итераций: {n + 1}")
        break
    
    x_prev = x_next
    n += 1