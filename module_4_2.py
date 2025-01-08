def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

# Вызов test_function
test_function()

# Попытка вызова inner_function вне области видимости
try:
    inner_function()
except NameError as e:
    if str(e) == "name 'inner_function' is not defined":
        print("inner_function больше не существует, её пределы ограничены только выполнением test_function")

