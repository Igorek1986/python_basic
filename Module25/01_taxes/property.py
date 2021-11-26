class Property:
    def __init__(self, name, worth):
        self.__set_worth(worth)
        self.__set_name(name)

    def __str__(self):
        return f'Объект: {self.__name}\n' \
               f'Стоимость имущества: {self.__worth}\n' \
               f'Налог к уплате: {self.tax_property()}\n'

    def get_worth(self):
        return self.__worth

    def __set_worth(self, worth):
        self.__worth = worth

    def __set_name(self, name):
        self.__name = name

    def tax_property(self):
        tax = self.get_worth() / 1000
        return tax


class Apartment(Property):
    def tax_property(self):
        tax = self.get_worth() / 1000
        return tax


class Car(Property):
    def tax_property(self):
        tax = self.get_worth() / 200
        return tax


class CountryHouse(Property):
    def tax_property(self):
        tax = self.get_worth() / 500
        return tax
