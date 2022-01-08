class Date:
    """ Базовый клас проверки даты """

    day = 0
    mount = 0
    year = 0

    def __init__(self, date_str: str) -> None:
        self.day, self.mount, self.year = date_str.split('-')

    def __str__(self):
        return f'День: {self.day}\tМесяц: {self.mount}\tГод: {self.year}'

    @classmethod
    def from_string(cls, date_str: str) -> 'Date':
        return cls(date_str)

    @classmethod
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
