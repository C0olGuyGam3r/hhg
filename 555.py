N = int(input("Введите N: "))
if N > 72:
    print(90000000)
elif N <= 1:
    print("нет")
else:
    count = 0
    # Исправлено: теперь тут ровно 100 000 000 (сто миллионов)
    for num in range(10000000, 100000000):
        digit_sum = sum(int(digit) for digit in str(num))
        
        if digit_sum < N:
            count += 1

    if count > 0:
        print(count)
    else:
        print("нет")