k = int(input("Остаток при делении на 3: "))
m = int(input("Остаток при делении на 5: "))
n = int(input("Остаток при делении на 7: "))

for x in range(100):
    if x % 3 == k and x % 5 == m and x % 7 == n:
        print("x =", x)