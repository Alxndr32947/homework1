# module_5_1
class House:
    def __init__(self, name, number_of_floors):
        """
        Инициализация объекта класса House.
        :param name: Название здания.
        :param number_of_floors: Количество этажей.
        """
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        """
        Метод для перехода на указанный этаж.
        :param new_floor: Этаж, на который нужно перейти.
        """
        if 1 <= new_floor <= self.number_of_floors:
            print(*range(1, new_floor + 1), sep="\n")
        else:
            print("Такого этажа не существует")


# Примеры использования
if __name__ == "__main__":
    h1 = House('ЖК Горский', 18)
    h2 = House('Домик в деревне', 2)

    h1.go_to(5)
    h2.go_to(10)