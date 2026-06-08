n = int(input("Введите количество элементов: "))

p = 1

for i in range(n):
    a = float(input("Введите элемент: "))
    p = p * abs(a)

print("Произведение =", p)