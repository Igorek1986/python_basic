class House:
    total_money = 0
    total_fur_coat = 0
    total_eat = 0

    def __init__(self, fridge_eat=50, money=100, eat_cat=30, dirt=0):
        self.fridge_eat = fridge_eat
        self.money = money
        self.eat_cat = eat_cat
        self.dirt = dirt

    def __str__(self):
        return f'\nВсего заработали денег: {self.total_money}\n' \
               f'Съели еды: {self.total_eat}\n' \
               f'Купили шуб: {self.total_fur_coat}'
