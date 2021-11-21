from desk import Desk

class Card:

    def __init__(self, name):
        self.name = name
        # self.count = count

    # def name_card(self):
    #     return self.name

    def count_card(self):
        return Desk().value(self.name)
