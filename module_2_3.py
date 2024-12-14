# Исходный список
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

# Начальный индекс
index = 0

# Цикл while
while index < len(my_list):  # Условие: пока индекс меньше длины списка
    current_number = my_list[index]  # Текущее число

    if current_number < 0:  # Если число отрицательное
        break  # Завершаем цикл

    if current_number == 0:  # Если число равно нулю
        index += 1  # Увеличиваем индекс
        continue  # Переходим к следующей итерации

    print(current_number)  # Выводим положительное число
    index += 1  # Увеличиваем индекс
