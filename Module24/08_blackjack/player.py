class Player:

    # TODO, если список карт относится к конкретному игроку, то его стоит создавать внутри метода __init__.
    lst_card = []

    def __init__(self, name):
        self.name = name

    def add_card_player(self, card):
        self.lst_card.append(card)

    # TODO, если метод получился пустым, то стоит просто убрать его из решения. =)
    def count_card(self):
        pass
