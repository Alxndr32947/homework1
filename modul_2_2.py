# Вводим три числа
first = int(input())
second = int(input())
third = int(input())

# Условная конструкция
if first == second == third:
    print(3)  # Все три числа равны
elif first == second or first == third or second == third:
    print(2)  # Есть ровно два равных числа
else:
    print(0)  # Все числа различны
