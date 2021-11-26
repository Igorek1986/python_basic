import random


class Karma:
    def __init__(self, carma_count):
        self.set_carma_count(carma_count)

    def get_carma_count(self):
        return self.__carma_count

    def set_carma_count(self, carma_count):
        self.__carma_count = carma_count

    @staticmethod
    def one_day():
        carma_day = random.randint(1, 7)
        return carma_day
