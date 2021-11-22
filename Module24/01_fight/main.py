import random
from unit import Unit

warrior_1 = Unit('Воин-1', 100)
warrior_2 = Unit('Воин-2', 100)

for _ in range(9):
    random_unit_kick = random.randint(0, 1)
    if warrior_1.health < 20 or warrior_2.health < 20:
        break
    elif random_unit_kick == 1:
        warrior_2.game(20)
        print(f'Атакует {warrior_1.name}, У {warrior_2.name} осталось {warrior_2.health} здоровья')
    else:
        warrior_1.game(20)
        print(f'Атакует {warrior_2.name}, У {warrior_1.name} осталось {warrior_1.health} здоровья')

if warrior_1.health > warrior_2.health:
    print(f'\nWinner {warrior_1.name}, Health: {warrior_1.health}')
else:
    print(f'\nWinner {warrior_2.name}, Health: {warrior_2.health}')

# зачёт!
