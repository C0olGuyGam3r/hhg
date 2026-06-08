import math

def find_min_index(epsilon=8):
    """
    Находит наименьший номер n, для которого |a_n - a_{n-1}| < epsilon
    для последовательности a_n = (1/2) * tg(a_{n-1}), a_1 = 0.5
    """
    # Начальные значения
    a_prev = 0.5  # a_1
    n = 1
    
    # Список для хранения всех элементов
    elements = [a_prev]
    
    # Продолжаем, пока не найдём нужный номер
    while True:
        # Вычисляем следующий элемент
        a_current = 0.5 * math.tan(a_prev)
        n += 1
        
        # Добавляем в список
        elements.append(a_current)
        
        # Проверяем условие |a_n - a_{n-1}| < epsilon
        if abs(a_current - a_prev) < epsilon:
            break
        
        a_prev = a_current
    
    return n, elements

# Находим результат
epsilon = 8
n, elements = find_min_index(epsilon)

# Выводим результаты
print(f"Наименьший номер n = {n}")
print(f"Условие |a_{n} - a_{n-1}| < {epsilon} выполнено")
print(f"\nВсе элементы последовательности (i = 1, 2, ..., {n}):")
for i, value in enumerate(elements, start=1):
    print(f"a_{i} = {value}")
    
print(f"\nПроверка: |a_{n} - a_{n-1}| = {abs(elements[-1] - elements[-2])}")