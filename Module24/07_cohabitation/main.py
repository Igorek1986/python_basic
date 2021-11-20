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
    if action == 1:
        player_1.work()
    elif action == 2:
        player_1.eat()
