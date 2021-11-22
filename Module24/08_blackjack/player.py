from card import Card


class Player:

    def __init__(self, name, lst_card=[]):
        self.name = name
        self.lst_card = lst_card

    def add_card_player(self, card):
        self.lst_card.append(card)

    def count_player(self, sum_player=0):
        for key in self.lst_card:
            if key == 'туз' and sum_player >= 11:
                sum_player += 1
            else:
                sum_player += Card(key).count_card()
        return sum_player

    def cards_player(self):
        for _ in self.lst_card:
            print(_)
