from math import cos

def f(x):
    """Исходное уравнение в виде f(x) = (0.2*x)^3 - cos(x) = 0"""
    return (0.2 * x) ** 3 - cos(x)

a = 2.0
b = 2.5
eps = 0.001

print("=" * 70)
print("Метод хорд для уравнения (0.2*x)^3 = cos(x)")
print("=" * 70)
print(f"{'Итерация':^8} | {'a':^8} | {'b':^8} | {'x_next':^10} | {'f(a)':^10} | {'f(b)':^10} | {'f(x_next)':^10}")
print("-" * 70)

for i in range(1, 20):
    x_next = a - f(a) * (b - a) / (f(b) - f(a))
    
    fa = f(a)
    fb = f(b)
    fx = f(x_next)
    
    print(f"{i:^8} | {a:8.5f} | {b:8.5f} | {x_next:10.6f} | {fa:10.6f} | {fb:10.6f} | {fx:10.6f}")
    
    if abs(fx) < eps or abs(b - a) < eps:
        print("-" * 70)
        print(f"\nКорень уравнения: {x_next:.6f}")
        print(f"Значение функции в корне: f({x_next:.6f}) = {fx:.6e}")
        print(f"Достигнутая точность: {eps}")
        print(f"Количество итераций: {i}")
        break
    
    if fa * fx < 0:
        b = x_next
    else:
        a = x_next
else:
    print("\nМетод не сошелся за максимальное число итераций")