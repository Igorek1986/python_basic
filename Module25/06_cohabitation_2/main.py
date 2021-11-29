from family import Cat, Man, Woman
from house import House


player_1 = Man(name='Артем', surname='Иванов', age=25)
player_2 = Woman('Ольга', surname='Иванова', age=25)
cat = Cat(name='Барсик')
house = House()
player_1.add_house(house)
player_2.add_house(house)
cat.add_house(house)
for day in range(1, 366):
    print(f'Сегодня {day}-й\n')
    player_1.one_day()
    player_2.one_day()
    cat.one_day_cat()
    print('\n', player_1)
    print('\n', player_2, '\n')
    # TODO, возможно, стоит проверять аргумент energy класса жены и кота. =)
    if player_1.energy == 0 or player_2 == 0 or cat == 0:
        print('умер')
        break

print(player_1.my_house)
