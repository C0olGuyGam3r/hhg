import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# --- Логика конвертации (твои функции) ---
def to_si(value, system, quantity):
    if quantity == "force":
        if system == "SI": return value
        elif system == "CGS": return value / 100000
        elif system == "TECH": return value * 9.81
    elif quantity == "length":
        if system == "SI": return value
        elif system == "CGS": return value / 100
        elif system == "TECH": return value
    elif quantity == "mass":
        if system == "SI": return value
        elif system == "CGS": return value / 1000
        elif system == "TECH": return value
    return value

def from_si(value, system, quantity):
    if quantity == "force":
        if system == "SI": return value
        elif system == "CGS": return value * 100000
        elif system == "TECH": return value / 9.81
    elif quantity == "length":
        if system == "SI": return value
        elif system == "CGS": return value * 100
        elif system == "TECH": return value
    elif quantity == "mass":
        if system == "SI": return value
        elif system == "CGS": return value * 1000
        elif system == "TECH": return value
    return value

# --- Функция, которая срабатывает при нажатии на кнопку ---
def convert():
    try:
        # Получаем значение из поля ввода
        val = float(entry_value.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректное число!")
        return

    # Определяем выбранную величину
    quantity_rus = combo_quantity.get()
    if quantity_rus == "Сила":
        quantity = "force"
    elif quantity_rus == "Длина":
        quantity = "length"
    elif quantity_rus == "Масса":
        quantity = "mass"
    else:
        messagebox.showerror("Ошибка", "Выберите величину!")
        return

    from_sys = combo_from.get()
    to_sys = combo_to.get()

    # Перевод
    si_val = to_si(val, from_sys, quantity)
    result = from_si(si_val, to_sys, quantity)

    # Выводим результат в метку
    label_result.config(text=f"Результат: {result:.4f}")

# --- Создание окна Tkinter ---
root = tk.Tk()
root.title("Конвертер физических величин")
root.geometry("400x350")
root.resizable(False, False)

# Стили для красивого отступа
pad_x = 10
pad_y = 5

# 1. Выбор величины
label_q = tk.Label(root, text="Выберите величину:", font=("Arial", 10, "bold"))
label_q.pack(anchor="w", padx=pad_x, pady=pad_y)

combo_quantity = ttk.Combobox(root, values=["Сила", "Длина", "Масса"], state="readonly")
combo_quantity.current(0)  # По умолчанию выберем "Сила"
combo_quantity.pack(fill="x", padx=pad_x, pady=pad_y)

# 2. Ввод значения
label_v = tk.Label(root, text="Введите значение:", font=("Arial", 10, "bold"))
label_v.pack(anchor="w", padx=pad_x, pady=pad_y)

entry_value = tk.Entry(root)
entry_value.pack(fill="x", padx=pad_x, pady=pad_y)

# 3. Выбор исходной системы
label_f = tk.Label(root, text="Из какой системы:", font=("Arial", 10))
label_f.pack(anchor="w", padx=pad_x, pady=pad_y)

combo_from = ttk.Combobox(root, values=["SI", "CGS", "TECH"], state="readonly")
combo_from.current(0)
combo_from.pack(fill="x", padx=pad_x, pady=pad_y)

# 4. Выбор целевой системы
label_t = tk.Label(root, text="В какую систему:", font=("Arial", 10))
label_t.pack(anchor="w", padx=pad_x, pady=pad_y)

combo_to = ttk.Combobox(root, values=["SI", "CGS", "TECH"], state="readonly")
combo_to.current(1)
combo_to.pack(fill="x", padx=pad_x, pady=pad_y)

# Разделитель для красоты
ttk.Separator(root, orient="horizontal").pack(fill="x", padx=pad_x, pady=10)

# 5. Кнопка конвертации
btn_convert = tk.Button(root, text="Конвертировать", command=convert, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
btn_convert.pack(fill="x", padx=pad_x, pady=pad_y)

# 6. Поле вывода результата
label_result = tk.Label(root, text="Результат: -", font=("Arial", 12, "bold"), fg="blue")
label_result.pack(pady=10)

# Запуск главного цикла программы
root.mainloop()