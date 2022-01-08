from abc import ABC, abstractmethod


class Date(ABC):
    """ Абстрактный базовый клас проверки даты """
    # TODO, предлагаю добавить метод init в наш класс
    #  с параметрами из которых состоит дата => "День", "Месяц", "Год"
    day = 0
    mount = 0
    year = 0

    @classmethod
    @abstractmethod  # TODO Возможно этот метод получился лишним.
    def from_string(cls, date_str: str) -> str:
        cls.day, cls.mount, cls.year = map(int, date_str.split('-'))
        # TODO, Т.к. наш класс является Датой, из строки необходимо вернуть объект класса Дата.
        #  Т.к. аргумент cls ссылается на Дату, можно возвращать его.
        return f'День: {cls.day}\tМесяц: {cls.mount}\tГод: {cls.year}'

    @classmethod
    @abstractmethod
    def is_date_valid(cls, date_str: str) -> bool:
        cls.day, cls.mount, cls.year = map(int, date_str.split('-'))
        if (0 < cls.day <= 31) and (0 < cls.mount <= 12) and (0 < cls.year):
            return True
        return False


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))

# Результат:
# День: 10    Месяц: 12    Год: 2077
# True
# False
