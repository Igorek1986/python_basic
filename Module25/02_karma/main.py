from karma import Karma


human = Karma(0)

while True:
    if not human.carma_count > 500:
        human.one_day()
    else:
        print('Карма достигнута за', human.day, 'день\nУровень кармы:', human.carma_count)
        break
