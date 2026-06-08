def to_si(value, system, quantity):
    #Сила
    if quantity == "force":
        if system == "SI":
            return value
        elif system == "CGS":
            return value / 100000
        elif system == "TECH":
            return value * 9.81

    #Длина
    elif quantity == "length":
        if system == "SI":
            return value
        elif system == "CGS":
            return value / 100  # см → м
        elif system == "TECH":
            return value  # там тоже метры

    #Масса
    elif quantity == "mass":
        if system == "SI":
            return value
        elif system == "CGS":
            return value / 1000  # г → кг
        elif system == "TECH":
            return value  # кг


def from_si(value, system, quantity):
    #Сила
    if quantity == "force":
        if system == "SI":
            return value
        elif system == "CGS":
            return value * 100000
        elif system == "TECH":
            return value / 9.81

    #Длина
    elif quantity == "length":
        if system == "SI":
            return value
        elif system == "CGS":
            return value * 100  # м → см
        elif system == "TECH":
            return value

    #Масса
    elif quantity == "mass":
        if system == "SI":
            return value
        elif system == "CGS":
            return value * 1000  # кг → г
        elif system == "TECH":
            return value


#Выбор

print("Конвертер физических величин")
print("Выберите величину:")
print("1 — Сила")
print("2 — Длина")
print("3 — Масса")

choice = input("Ваш выбор: ")

if choice == "1":
    quantity = "force"
elif choice == "2":
    quantity = "length"
elif choice == "3":
    quantity = "mass"
else:
    print("Ошибка выбора!")
    exit()

value = float(input("Введите значение: "))

print("Системы: SI / CGS / TECH")
from_sys = input("Из системы: ").upper()
to_sys = input("В систему: ").upper()

#Проверка
if from_sys not in ["SI", "CGS", "TECH"] or to_sys not in ["SI", "CGS", "TECH"]:
    print("Ошибка: неправильная система!")
    exit()

#Перевод
si = to_si(value, from_sys, quantity)
result = from_si(si, to_sys, quantity)

print(f"Результат: {result:.2f}")