class Property:
    def __init__(self, name, worth):
        self.worth = worth
        self.name = name


class Apartment(Property):
    def __init__(self, name, worth):
        super().__init__(name, worth)
        self.count_percent = 1 / 1000

    def tax_property(self):
        tax = self.worth * self.count_percent
        return tax

    def __str__(self):
        return f'Объект: {self.name}\n' \
               f'Стоимость имущества: {self.worth}\n' \
               f'Налог к уплате: {self.tax_property()}\n'


class Car(Property):
    def __init__(self, name, worth):
        super().__init__(name, worth)
        self.count_percent = 1 / 200

    def tax_property(self):
        tax = self.worth * self.count_percent
        return tax

    def __str__(self):
        return f'Объект: {self.name}\n' \
               f'Стоимость имущества: {self.worth}\n' \
               f'Налог к уплате: {self.tax_property()}\n'


class CountryHouse(Property):
    def __init__(self, name, worth):
        super().__init__(name, worth)
        self.count_percent = 1 / 500

    def tax_property(self):
        tax = self.worth * self.count_percent
        return tax

    def __str__(self):
        return f'Объект: {self.name}\n' \
               f'Стоимость имущества: {self.worth}\n' \
               f'Налог к уплате: {self.tax_property()}\n'
