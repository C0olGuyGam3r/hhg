from math import *

e = float(input("Введите e: "))

s = 0
n = 1

while 2**n / factorial(n - 1) >= e:
    a = 2**n / factorial(n - 1)
    s = s + a
    n = n + 1

print("Сумма =", round(s, 2))