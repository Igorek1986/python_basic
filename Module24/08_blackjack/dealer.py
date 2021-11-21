import random
from desk import Desk
from card import Card


class Dealer:
    lst_card = []

    def __init__(self, name):
        self.name = name

    def add_card(self, card):
        self.lst_card.append(card)

    @staticmethod
    def question_card(player):
        print('Сумма очков:', player.count_player())
        answer = input('Будем брать еще одну карту? (да или нет) ').lower()
        if answer == 'да':
            player.add_card_player(Desk().random_card())
        else:
            return True

    def question_card_dealer(self):
        answer = random.randint(1, 2)
        if answer == 1:
            self.lst_card.append(Desk().random_card())

    def count_dealer(self, sum_dealer=0):
        for key in self.lst_card:
            if key == 'туз' and sum_dealer >= 11:
                sum_dealer += 1
            else:
                sum_dealer += Card(key).count_card()
        return sum_dealer

    def cards_dealer(self):
        for _ in self.lst_card:
            print(_)
