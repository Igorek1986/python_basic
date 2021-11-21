class Player:

    def __init__(self, name, lst_card=[]):
        self.name = name
        self.lst_card = lst_card

    def add_card_player(self, card):
        self.lst_card.append(card)
