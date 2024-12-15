def generate_all_passwords():
    passwords = {}  # Словарь для хранения паролей для всех чисел от 3 до 20

    for n in range(3, 21):  # Перебираем числа от 3 до 20
        result = ""  # Здесь будет формироваться пароль для текущего числа n
        for i in range(1, n):  # Перебираем первую часть пары
            for j in range(i + 1, n):  # Перебираем вторую часть пары (j > i)
                if n % (i + j) == 0:  # Проверяем кратность суммы пары
                    result += f"{i}{j}"  # Добавляем пару в пароль
        passwords[n] = result  # Сохраняем пароль для текущего числа n

    return passwords

# Генерация всех паролей
all_passwords = generate_all_passwords()

# Вывод результатов для сверки
for n, password in all_passwords.items():
    print(f"{n} - {password}")



