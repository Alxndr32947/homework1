def calculate_structure_sum(*args):
    total_sum = 0

    for item in args:
        if isinstance(item, (int, float)):  # Если это число
            total_sum += item
        elif isinstance(item, str):  # Если это строка
            total_sum += len(item)
        elif isinstance(item, (list, tuple, set)):  # Если это список, кортеж или множество
            total_sum += calculate_structure_sum(*item)
        elif isinstance(item, dict):  # Если это словарь
            total_sum += calculate_structure_sum(*item.keys(), *item.values())

    return total_sum


# Пример использования
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

# Распаковка внешнего списка
result = calculate_structure_sum(*data_structure)
print(result)


