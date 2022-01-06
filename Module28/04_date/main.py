from abc import ABC, abstractmethod


class Date(ABC):
    """ Абстрактный базовый клас проверки даты """
    day = 0
    mount = 0
    year = 0

    @classmethod
    @abstractmethod
    def from_string(cls, date_str: str) -> str:
        cls.day, cls.mount, cls.year = map(int, date_str.split('-'))
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
