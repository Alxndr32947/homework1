def generate_password(n):
    if not (3 <= n <= 20):
        return "Число должно быть в диапазоне от 3 до 20."

    result = ""  # Здесь будет формироваться пароль
    for i in range(1, n):  # Перебираем первую часть пары
        for j in range(i + 1, n):  # Перебираем вторую часть пары (j > i)
            if n % (i + j) == 0:  # Проверяем кратность суммы пары
                result += f"{i}{j}"  # Добавляем пару в пароль

    return result


# Пример использования:
n = int(input("Введите число (от 3 до 20): "))
result = generate_password(n)
print(f"Нужный пароль для числа {n}: {result}")




