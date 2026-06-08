n = int(input("Введите n: "))
S = 0
for k in range(1, n + 1):
    S += 1 / (2 * k + 1) ** 2
print("Сумма S =", round(S, 4))