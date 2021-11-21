from human import Human
from house import House
import random

player_1 = Human('Артем')
player_2 = Human('Ольга')
house = House()
player_1.add_house(house)
player_2.add_house(house)
for day in range(1, 366):
    print(f'Сегодня {day}-й')
    action = random.randint(1, 6)
    player_1.status_human(action)
    player_2.status_human(action)
    if player_1.energy == 0:
        print('умер')
        break

# зачёт!
