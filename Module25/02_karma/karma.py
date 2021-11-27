import random
from my_exception import KillError, DrunkError, CarCrashError, GluttonyError, DepressionError


class Karma:
    day = 0
    my_exception = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]

    def __init__(self, carma_count):
        self.carma_count = carma_count

    def one_day(self):
        self.day += 1
        if not random.randint(1, 10) == 10:
            carma_day = random.randint(1, 7)
            self.carma_count += carma_day
        else:
            # TODO, запись данных в файл в этом методе получилась лишней.
            #  Метод должен или увеличивать количество кармы, или вызывать одно из исключений при помощи raise.
            #  Сам метод стоит запускать внутри блоков try/except, таким образом, запись исключений в файл,
            #  мы сможем производить в блоке except.
            with open('karma.log', 'a', encoding='utf-8') as file:
                file.write(f'Исключение возникло на {self.day} день просвещения' +
                           str(random.choice(self.my_exception)) + '\n')
