class Person:
    def __init__(self, name, surname, age):
        self.__set_name(name)
        self.__set_surname(surname)
        self.__set_age(age)

    def __set_name(self, name):
        self.__name = name

    def __set_surname(self, surname):
        self.__surname = surname

    def __set_age(self, age):
        self.__age = age
