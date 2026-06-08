from math import cos, acos

# Уравнение: (0.2*x)^3 = cos(x)
# Приводим к виду x = phi(x)
# Выразим: cos(x) = (0.2*x)^3
#          x = arccos((0.2*x)^3)   (но это неявно)
# Лучше: x = ( (cos(x))^(1/3) ) / 0.2   — неудобно.
# Проще и надёжнее: x = arccos( (0.2*x)^3 )
# Однако это не сходится. В примере 2-го скриншота было x = acos(-0.3x/4)
# Для нашего случая: (0.2x)^3 = cos x => cos x = 0.008*x^3
# Тогда x = arccos(0.008*x^3) — этот оператор сжимающий на нужном интервале.

def phi(x):
    """Приведённое уравнение: x = arccos(0.008*x^3)"""
    return acos(0.008 * x**3)

# Начальное приближение из графического метода (корень около 2.2)
x_next = 2.2
x_prev = 0
count = 1
eps = 1e-3

print(f"0 --- {x_next}")

while abs(x_next - x_prev) > eps:
    x_prev = x_next
    x_next = round(phi(x_prev), 6)
    print(f"{count} --- {x_next}")
    count += 1
    if count > 100:  # защита от зацикливания
        print("Метод не сошёлся за 100 итераций")
        break

print(f"\nANSWER: {x_next}")