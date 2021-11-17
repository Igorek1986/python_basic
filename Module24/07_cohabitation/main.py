from human import Human
from house import House
import random

player_1 = Human('Артем')
house = House()
player_1.add_house(house)
print(player_1.my_house.money())
