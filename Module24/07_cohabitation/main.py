from human import Human
from house import House
import random

player_1 = Human('Артем')
house = House()
player_1.add_house(house)
player_1.work()
print(player_1.my_house.money)
player_1.eat()
# print(player_1.my_house.money())
