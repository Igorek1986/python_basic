from desk import Desk
from card import Card
from player import Player
from dealer import Dealer


sum_player = 0
sum_dealer = 0
player_1 = Player('Костя')
dealer = Dealer('Дилер')
for _ in range(2):
    player_1.add_card_player(Desk().random_card())
    dealer.add_card(Desk().random_card())

dealer.question_card(player_1)
dealer.question_card_dealer()


for key in player_1.lst_card:
    if key == 'туз' and sum_player >= 11:
        sum_player += 1
    else:
        sum_player += Card(key).count_card()
for key in dealer.lst_card:
    if key == 'туз' and sum_dealer >= 11:
        sum_player += 1
    else:
        sum_dealer += Card(key).count_card()


if sum_player >= 22:
    sum_player = 0
if sum_dealer >= 22:
    sum_dealer = 0

if sum_dealer < sum_player:
    print(f'Выиграл {player_1.name}!')
    print('Карты победителя:')
    for _ in player_1.lst_card:
        print(_)
elif sum_player < sum_dealer:
    print(f'Выиграл {dealer.name}!')
    print('Карты победителя:')
    for _ in dealer.lst_card:
        print(_)
else:
    print('Нет победителей.')
