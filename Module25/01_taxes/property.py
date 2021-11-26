class Property:
    def __init__(self, name, worth):
        # TODO, пожалуйста, обратите внимание, метод __init__ по своей сути, простой список аргументов.
        #  Предлагаю убрать вызовы остальных методов из этого класса и оставить только создание аргументов. =)
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
    # TODO, пожалуйста, обратите внимание
    #  "Каждый дочерний класс должен иметь конструктор с одним параметром, передающий свой параметр конструктору базового класса."
    #  Предлагаю добавить в методы __init__ наших классов, аргумент "процент стоимости"
    #  и использовать его в методе с расчётом налога, вместо чисел 1000, 500 и 200.
    #  В таком случае, если число в дальнейшем нужно будет поменять, мы всегда легко найдём его
    #  в методе __init__.

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
