# Исходный список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Пустые списки для простых и не простых чисел
primes = []
not_primes = []

# Перебираем числа из списка numbers
for num in numbers:
    # Число 1 не является ни простым, ни составным
    if num == 1:
        continue

    # Флаг, обозначающий простоту числа
    is_prime = True

    # Проверяем делители числа от 2 до num-1
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            is_prime = False
            break  # Если найден делитель, число не простое, выходим из цикла

    # Добавляем число в соответствующий список
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)

# Вывод результатов
print("Primes:", primes)
print("Not Primes:", not_primes)
