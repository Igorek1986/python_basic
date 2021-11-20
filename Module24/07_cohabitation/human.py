class Human:

    def __init__(self, name, energy=50):
        self.name = name
        self.energy = energy
        self.my_house = None

    def add_house(self, obj):
        self.my_house = obj

    def eat(self):
        if self.my_house.fridge_eat > 20:
            print('Приятного аппетита!')
            self.energy += 50
            self.my_house.fridge_eat -= 20
        else:
            print('Нет еды, пойду в магазин.')
            self.shopping()

    def work(self):
        self.energy -= 20
        self.my_house.money += 50

    def game(self):
        if self.energy > 50:
            self.energy -= 30
        else:
            print('Нельзя сейчас играть. Береги энергию для работы!')

    def shopping(self):
        if self.my_house.money > 15:
            self.my_house.fridge_eat += 30
            self.my_house.money -= 15
        else:
            print('Нет денег, нужно работать!')
            self.work()
