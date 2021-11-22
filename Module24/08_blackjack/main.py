from desk import Desk
from player import Player
from dealer import Dealer

player_1 = Player('Костя')
dealer = Dealer('Дилер')
for _ in range(2):
    player_1.add_card_player(Desk().random_card())
    dealer.add_card(Desk().random_card())

while True:
    if not dealer.question_card(player_1):
        dealer.question_card_dealer()
    else:
        break

sum_player = player_1.count_player()
sum_dealer = dealer.count_dealer()
if sum_player >= 22:
    sum_player = 0
if sum_dealer >= 22:
    sum_dealer = 0

if sum_dealer < sum_player:
    print(f'Выиграл {player_1.name}!')
    print('Карты победителя:')
    player_1.cards_player()
elif sum_player < sum_dealer:
    print(f'Выиграл {dealer.name}!')
    print('Карты победителя:')
    dealer.cards_dealer()
else:
    print('Нет победителей.')
# зачёт!
