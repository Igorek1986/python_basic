import random
from my_exception import KillError, DrunkError, CarCrashError, GluttonyError, DepressionError


class Karma:
    day = 0
    my_exception = [KillError('KillError'), DrunkError('DrunkError'), CarCrashError('CarCrashError'),
                    GluttonyError('GluttonyError'), DepressionError('DepressionError')]

    def __init__(self, carma_count):
        self.carma_count = carma_count

    def one_day(self):
        self.day += 1
        if not random.randint(1, 10) == 10:
            carma_day = random.randint(1, 7)
            self.carma_count += carma_day
        else:
            raise random.choice(self.my_exception)
