def single_root_words(root_word, *other_words):
    # Приводим корневое слово к нижнему регистру
    root_word = root_word.lower()
    # Создаем пустой список для хранения подходящих слов
    same_words = []
    # Перебираем слова из *other_words
    for word in other_words:
        # Приводим текущее слово к нижнему регистру
        word_lower = word.lower()
        # Проверяем, входит ли root_word в word или наоборот
        if root_word in word_lower or word_lower in root_word:
            same_words.append(word)  # Добавляем слово в список, если условие выполнено
    # Возвращаем список подходящих слов
    return same_words

# Примеры вызова функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Выводим результаты на экран
print(result1)
print(result2)