print("Таблица сложения (hex):")
print("   ", end="")

for i in range(16):
    print(f"{i:X} ", end="")
print()

for i in range(16):
    print(f"{i:X} ", end=" ")
    for j in range(16):
        s = i + j
        print(f"{s:X} ", end="")
    print()

print("\n" + "-"*40)

print("Таблица умножения (hex):")
print("   ", end="")

for i in range(16):
    print(f"{i:X} ", end="")
print()

for i in range(16):
    print(f"{i:X} ", end=" ")
    for j in range(16):
        m = i * j
        print(f"{m:X} ", end="")
    print()