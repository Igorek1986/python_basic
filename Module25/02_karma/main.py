import random
from my_exception import KillError, DrunkError, CarCrashError, GluttonyError, DepressionError
from karma import Karma


human = Karma(0)
my_exception = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]
day = 0


while True:
    day += 1
    if not random.randint(1, 10) == 10:
        if not human.get_carma_count() > 500:
            human.set_carma_count(human.get_carma_count() + human.one_day())
        else:
            print('Карма достигнута за', day, 'день\nУровень кармы:', human.get_carma_count())
            break
    else:
        with open('karma.log', 'a', encoding='utf-8') as file:
            file.write(f'Исключение возникло на {day} день просвещения' + str(random.choice(my_exception)) + '\n')
