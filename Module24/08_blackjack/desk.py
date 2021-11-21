import random
card_name = ''
card_value = 0


class Desk:
    def __init__(self):
        self.desk_card = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                          '9': 9, '10': 10, 'валет': 10, 'дама': 10, 'король': 10, 'туз': 11}

    def random_card(self):
        return random.choice(list(self.desk_card.keys()))

    def value(self, key):
        return self.desk_card[key]

    def info(self):
        for key, value in self.desk_card.items():
            print(key, value)
