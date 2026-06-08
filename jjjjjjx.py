import math

# Ввод данных
a = float(input("Введите a: "))
b = float(input("Введите b: "))
h = float(input("Введите шаг h: "))

print("\nТаблица значений:")
print(f"{'x':>10} | {'F(x)':>15}")
print("-" * 28)

x = a
while x <= b:
    try:
        # Проверка, чтобы не делить на 0
        if math.sin(x / 3) == 0:
            fx = "не определено"
        else:
            fx = (math.cos(x / 3) / math.sin(x / 3)) + 0.5 * math.sin(x)
            fx = round(fx, 6)

        print(f"{round(x, 6):>10} | {fx:>15}")
    except:
        print(f"{round(x, 6):>10} | ошибка")

    x += h