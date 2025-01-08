def get_matrix(n, m, value):
    # Создаем пустой список для хранения строк матрицы
    matrix = []

    # Проверяем, что размеры матрицы положительные
    if n <= 0 or m <= 0:
        return matrix

    # Внешний цикл: создание строк матрицы
    for _ in range(n):
        # Создаем строку, состоящую из значений `value`
        row = []
        for _ in range(m):
            row.append(value)
        # Добавляем строку в матрицу
        matrix.append(row)

    # Возвращаем готовую матрицу
    return matrix


# Проверяем работу функции
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

# Вывод результатов
print(result1)
print(result2)
print(result3)