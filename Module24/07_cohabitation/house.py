class House:
    def __init__(self, fridge_eat=50, money=0):
        self.fridge_eat = fridge_eat
        self.money = money

    # TODO, предлагаю, чтобы не путаться, убрать этот метод из решения.
    #  Методы и аргументы, должны иметь разные названия. =)
    def money(self, count):
        self.money += count
