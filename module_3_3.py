def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Часть 1: Вызовы с разным количеством аргументов
print_params()
print_params(42)
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(10, 'Привет', False)

# Часть 2: Распаковка параметров
values_list = [99, 'пример', False]
values_dict = {'a': 3.14, 'b': 'текст', 'c': True}

print_params(*values_list)
print_params(**values_dict)

# Часть 3: Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)


