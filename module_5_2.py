# module_5_2
from module_5_1 import House

def extend_house(cls):
    """
    Расширяет класс House магическими методами __len__ и __str__.
    """
    def house_len(self):
        return self.number_of_floors

    def house_str(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    cls.__len__ = house_len
    cls.__str__ = house_str

    return cls


# Расширяем класс House
extend_house(House)

# Примеры использования
if __name__ == "__main__":
    h1 = House('ЖК Эльбрус', 10)
    h2 = House('ЖК Акация', 20)

    # Использование __str__
    print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 10
    print(h2)  # Название: ЖК Акация, кол-во этажей: 20

    # Использование __len__
    print(len(h1))  # 10
    print(len(h2))  # 20