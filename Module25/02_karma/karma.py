import random


class Karma:
    def __init__(self, carma_count):
        # TODO, пожалуйста, обратите внимание, метод __init__ по своей сути, простой список аргументов.
        #  Предлагаю убрать вызовы остальных методов из этого класса и оставить только создание аргументов.
        self.set_carma_count(carma_count)

    def get_carma_count(self):
        return self.__carma_count

    def set_carma_count(self, carma_count):
        self.__carma_count = carma_count

    @staticmethod
    def one_day():
        # TODO, Этот метод должен или возвращать количество кармы, или вызывать случайное исключение из списка. =)
        carma_day = random.randint(1, 7)
        return carma_day
