import hashlib  # Импортируем модуль для хэширования паролей.
import time  # Импортируем модуль для добавления задержек при воспроизведении видео.

class User:
    """
    Класс User представляет пользователя платформы UrTube.

    Атрибуты:
    - nickname (str): Имя пользователя.
    - password (int): Хэшированный пароль пользователя.
    - age (int): Возраст пользователя.
    """

    def __init__(self, nickname: str, password: str, age: int):
        """
        Конструктор для создания нового пользователя.

        Аргументы:
        - nickname (str): Имя пользователя.
        - password (str): Пароль в виде строки, который будет хэшироваться.
        - age (int): Возраст пользователя.
        """
        self.nickname = nickname  # Сохраняем имя пользователя.
        self.password = self._hash_password(password)  # Хэшируем пароль и сохраняем его.
        self.age = age  # Сохраняем возраст пользователя.

    def _hash_password(self, password: str) -> int:
        """
        Приватный метод для хэширования пароля пользователя.

        Аргументы:
        - password (str): Пароль в виде строки.

        Возвращает:
        - int: Хэш пароля.
        """
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)  # Используем SHA-256 для хэширования строки.

    def check_password(self, password: str) -> bool:
        """
        Проверяет, совпадает ли хэш введенного пароля с хранимым хэшем.

        Аргументы:
        - password (str): Пароль в виде строки.

        Возвращает:
        - bool: True, если пароли совпадают, иначе False.
        """
        return self.password == self._hash_password(password)  # Сравниваем хэши паролей.

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта User.

        Возвращает:
        - str: Строка с именем пользователя.
        """
        return f"User: {self.nickname}"  # Упрощенный вывод объекта для пользователя.

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта для разработчика.

        Возвращает:
        - str: Полная информация о пользователе.
        """
        return f"User(nickname='{self.nickname}', age={self.age})"  # Отображаем подробную информацию о пользователе.

    def __eq__(self, other) -> bool:
        """
        Сравнивает двух пользователей по имени.

        Аргументы:
        - other (User): Другой пользователь.

        Возвращает:
        - bool: True, если имена совпадают, иначе False.
        """
        if isinstance(other, User):  # Проверяем, является ли другой объект экземпляром User.
            return self.nickname == other.nickname  # Сравниваем пользователей по nickname.
        return False  # Если другой объект не является User, возвращаем False.


class Video:
    """
    Класс Video представляет видео на платформе UrTube.

    Атрибуты:
    - title (str): Название видео.
    - duration (int): Длительность видео в секундах.
    - time_now (int): Текущая секунда просмотра видео (по умолчанию 0).
    - adult_mode (bool): Флаг возрастного ограничения (по умолчанию False).
    """

    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        """
        Конструктор для создания нового видео.

        Аргументы:
        - title (str): Название видео.
        - duration (int): Длительность видео в секундах.
        - adult_mode (bool, optional): Возрастное ограничение (по умолчанию False).
        """
        self.title = title  # Сохраняем название видео.
        self.duration = duration  # Сохраняем длительность видео.
        self.time_now = 0  # Устанавливаем начальную точку просмотра на 0.
        self.adult_mode = adult_mode  # Сохраняем информацию о возрастном ограничении.

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Video.

        Возвращает:
        - str: Строка с названием и длительностью видео.
        """
        return f"Video: {self.title} ({self.duration} sec)"  # Упрощенное представление видео.

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта для разработчика.

        Возвращает:
        - str: Полная информация о видео.
        """
        return f"Video(title='{self.title}', duration={self.duration}, adult_mode={self.adult_mode})"  # Подробная информация о видео.


class UrTube:
    """
    Класс UrTube представляет платформу для управления пользователями и видео.

    Атрибуты:
    - users (list[User]): Список зарегистрированных пользователей.
    - videos (list[Video]): Список загруженных видео.
    - current_user (User | None): Текущий вошедший пользователь (по умолчанию None).
    """

    def __init__(self):
        """
        Конструктор для создания экземпляра платформы UrTube.
        """
        self.users = []  # Инициализируем пустой список пользователей.
        self.videos = []  # Инициализируем пустой список видео.
        self.current_user = None  # Устанавливаем отсутствие текущего пользователя.

    def __contains__(self, video: Video) -> bool:
        """
        Проверяет, есть ли видео в списке загруженных видео.

        Аргументы:
        - video (Video): Видео для проверки.

        Возвращает:
        - bool: True, если видео уже загружено, иначе False.
        """
        return video.title in [v.title for v in self.videos]  # Проверяем, есть ли такое же название в списке видео.

    def log_in(self, nickname: str, password: str) -> None:
        """
        Метод для входа пользователя в систему.

        Аргументы:
        - nickname (str): Имя пользователя.
        - password (str): Пароль пользователя.

        Возвращает:
        - None
        """
        for user in self.users:  # Перебираем всех пользователей в списке.
            if user.nickname == nickname and user.check_password(password):  # Проверяем логин и пароль.
                self.current_user = user  # Устанавливаем текущего пользователя.
                return  # Выходим, если пользователь найден.

    def register(self, nickname: str, password: str, age: int) -> None:
        """
        Метод для регистрации нового пользователя.

        Аргументы:
        - nickname (str): Имя пользователя.
        - password (str): Пароль пользователя.
        - age (int): Возраст пользователя.

        Возвращает:
        - None
        """
        new_user = User(nickname, password, age)  # Создаем нового пользователя.
        if new_user in self.users:  # Проверяем, есть ли пользователь в списке (используем __eq__).
            print(f"Пользователь {nickname} уже существует")  # Сообщаем, если пользователь уже есть.
            return  # Прерываем выполнение метода.
        self.users.append(new_user)  # Добавляем нового пользователя в список.
        self.current_user = new_user  # Устанавливаем нового пользователя как текущего.

    def add(self, *videos: Video) -> None:
        """
        Метод для добавления одного или нескольких видео на платформу.

        Аргументы:
        - *videos (Video): Видео для добавления.

        Возвращает:
        - None
        """
        for video in videos:  # Перебираем все переданные видео.
            if video not in self:  # Проверяем, есть ли видео в списке (используем __contains__).
                self.videos.append(video)  # Если нет, добавляем его в список.

    def get_videos(self, keyword: str) -> list[str]:
        """
        Метод для поиска видео по ключевому слову.

        Аргументы:
        - keyword (str): Ключевое слово для поиска.

        Возвращает:
        - list[str]: Список названий видео, содержащих ключевое слово.
        """
        keyword = keyword.lower()  # Приводим ключевое слово к нижнему регистру.
        return [video.title for video in self.videos if keyword in video.title.lower()]  # Возвращаем список совпадений.

    def watch_video(self, title: str) -> None:
        """
        Метод для воспроизведения видео.

        Аргументы:
        - title (str): Название видео.

        Возвращает:
        - None
        """
        if not self.current_user:  # Проверяем, вошел ли пользователь в систему.
            print("Войдите в аккаунт, чтобы смотреть видео")  # Если нет, выводим сообщение.
            return

        video = next((v for v in self.videos if v.title == title), None)  # Ищем видео по названию.
        if not video:  # Если видео не найдено, ничего не делаем.
            return

        if video.adult_mode and self.current_user.age < 18:  # Если видео имеет ограничение, а пользователь младше 18.
            print("Вам нет 18 лет, пожалуйста покиньте страницу")  # Выводим сообщение об ограничении.
            return

        for second in range(video.time_now + 1, video.duration + 1):  # Имитируем просмотр видео.
            print(second, end=" ", flush=True)  # Выводим текущую секунду.
            time.sleep(0.1)  # Задержка для эффекта воспроизведения.
        print("Конец видео")  # Сообщаем, что просмотр окончен.
        video.time_now = 0  # Сбрасываем прогресс просмотра.

if __name__ == "__main__":
    """
    Основная часть программы для тестирования функциональности платформы UrTube.
    """
    ur = UrTube()  # Создаем экземпляр платформы.

    # Создаем два видео.
    v1 = Video('Лучший язык программирования 2024 года', 200)  # Видео без ограничений.
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)  # Видео с ограничением 18+.

    ur.add(v1, v2)  # Добавляем видео на платформу.

    print(ur.get_videos('лучший'))  # Поиск видео по слову "лучший".
    print(ur.get_videos('ПРОГ'))  # Поиск видео по слову "ПРОГ".

    ur.watch_video('Для чего девушкам парень программист?')  # Попытка просмотра без входа.

    ur.register('vasya_pupkin', 'lolkekcheburek', 13)  # Регистрация несовершеннолетнего пользователя.
    ur.watch_video('Для чего девушкам парень программист?')  # Попытка просмотра видео с ограничением 18+.

    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)  # Регистрация совершеннолетнего пользователя.
    ur.watch_video('Для чего девушкам парень программист?')  # Успешный просмотр видео с ограничением.

    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)  # Попытка зарегистрировать существующего пользователя.

    if ur.current_user:  # Проверяем, есть ли текущий пользователь.
        print(ur.current_user.nickname)  # Выводим имя текущего пользователя.