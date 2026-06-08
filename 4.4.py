from math import *

a = float(input("Введите a: "))
b = float(input("Введите b: "))
h = float(input("Введите h: "))

print("x F(x)")

x = a

while x <= b:
    f = sin(x) + tan(x)
    print(round(x, 2), round(f, 2))
    x = x + h