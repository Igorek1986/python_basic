from karma import Karma
from my_exception import KillError, DrunkError, CarCrashError, GluttonyError, DepressionError

human = Karma(0)

while True:
    if not human.carma_count > 500:
        try:
            human.one_day()
        except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as err:
            with open('karma.log', 'a', encoding='utf-8') as file:
                file.write(f'Исключение возникло на {human.day} день просвещения - Ошибка: {err}\n')
    else:
        print('Карма достигнута за', human.day, 'дней\nУровень кармы:', human.carma_count)
        break

# зачёт!
