k = int(input("Введите k: "))

print("m n a b c")

for m in range(2, k):
    for n in range(2, k):
        a = m**2 - n**2
        b = 2 * m * n
        c = m**2 + n**2

        print(m, n, a, b, c)