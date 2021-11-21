import random
from player import Player
from desk import Desk


class Dealer:
    lst_card = []

    def __init__(self, name):
        self.name = name

    def add_card(self, card):
        self.lst_card.append(card)

    @staticmethod
    def question_card(player):
        answer = input('Будем брать еще одну карту? (да или нет) ').lower()
        if answer == 'да':
            player.add_card_player(Desk().random_card())

    def question_card_dealer(self):
        answer = random.randint(1, 2)
        if answer == 1:
            self.lst_card.append(Desk().random_card())
