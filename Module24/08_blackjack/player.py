class Player:
    lst_card = []

    def __init__(self, name):
        self.name = name

    def add_card_player(self, card):
        self.lst_card.append(card)

    def count_card(self):
        pass
