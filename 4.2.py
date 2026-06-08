from math import *

n = int(input("Введите n: "))
x = float(input("Введите x: "))

s = 0

for i in range(1, n + 1):
    s = s + sin(x) ** i

print("Сумма =", round(s, 3))