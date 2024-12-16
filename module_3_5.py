def get_multiplied_digits(number):
    # Преобразуем число в строку
    str_number = str(number)

    # Берем первую цифру числа
    first = int(str_number[0])

    # Если длина строки больше 1, выполняем рекурсивное умножение
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        # Если осталась одна цифра, возвращаем её, что предотвращает бесконечную рекурсию.
        return first


# Примеры использования функции
result = get_multiplied_digits(40203)
print(result)  # Вывод: 24

result2 = get_multiplied_digits(402030)
print(result2)  # Вывод: 24
