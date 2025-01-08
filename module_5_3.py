# module_5_3
from module_5_2 import House

def extend_house(cls):
    """
    Расширяет класс House операторами сравнения и арифметики.
    """

    def house_eq(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return NotImplemented

    def house_lt(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return NotImplemented

    def house_le(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return NotImplemented

    def house_gt(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return NotImplemented

    def house_ge(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return NotImplemented

    def house_ne(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return NotImplemented

    def house_add(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
        if isinstance(value, House):
            return House(self.name, self.number_of_floors + value.number_of_floors)
        raise TypeError("Можно добавлять только целые числа или объект House.")

    def house_radd(self, value):
        return self.__add__(value)

    def house_iadd(self, value):
        return self.__add__(value)

    cls.__eq__ = house_eq
    cls.__lt__ = house_lt
    cls.__le__ = house_le
    cls.__gt__ = house_gt
    cls.__ge__ = house_ge
    cls.__ne__ = house_ne
    cls.__add__ = house_add
    cls.__radd__ = house_radd
    cls.__iadd__ = house_iadd

    return cls


# Расширяем класс House
extend_house(House)

# Примеры использования
if __name__ == "__main__":
    h1 = House("ЖК Эльбрус", 10)
    h2 = House("ЖК Акация", 20)

    # Использование __str__
    print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 10
    print(h2)  # Название: ЖК Акация, кол-во этажей: 20

    # Использование __len__
    print(len(h1))  # 10
    print(len(h2))  # 20

    # Сравнение __eq__
    print(h1 == h2)  # False

    # Увеличение этажей __add__
    h1 = h1 + 10
    print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 20
    print(h1 == h2)  # True

    # Увеличение этажей __iadd__
    h1 += 10
    print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 30

    # Обратное сложение __radd__
    h2 = 10 + h2
    print(h2)  # Название: ЖК Акация, кол-во этажей: 30

    # Сравнения
    print(h1 > h2)  # False
    print(h1 >= h2)  # True
    print(h1 < h2)  # False
    print(h1 <= h2)  # True
    print(h1 != h2)  # False