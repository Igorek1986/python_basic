class Human:

    def __init__(self, name, energy=50):
        self.name = name
        self.energy = energy
        self.my_house = None

    def add_house(self, obj):
        self.my_house = obj

    def eat(self):
        if self.my_house.fridge_eat > 20:
            self.energy += 50
            self.my_house.fridge_eat -= 20
        else:
            print('Нет еды, пойду в магазин.')

    def work(self):
        self.energy -= 20
        self.my_house.money += 50

    def game(self):
        if self.energy > 25:
            self.energy -= 20
        else:
            print('Нельзя сейчас играть. Береги энергию для работы!')

    def shopping(self):
        if self.my_house.money > 5:
            self.my_house.fridge_eat += 50
            self.my_house.money -= 5
        else:
            print('Нет денег, нужно работать!')

    def status_human(self, num):

        if not self.energy == 0:  # TODO, или просто "if self.energy"
            # TODO, пожалуйста, обратите внимание, по итогам года люди должны выжить.
            #  Предлагаю попробовать есть заранее, к примеру, если энергии меньше 50.
            #  Идти в магазин стоит так же заранее, если еды в меньше 50.
            if self.energy < 20:
                print('Приятного аппетита!')
                self.eat()
            elif self.my_house.fridge_eat < 10:
                print('Пошли в магазин!')
                self.shopping()
            elif self.my_house.money < 50:
                print('Пошли работать!')
                self.work()
            elif num == 1:
                print('Пошли работать!')
                self.work()
            elif num == 2:
                print('Приятного аппетита!')
                self.eat()
            elif self.energy < 0:
                print('Ты проиграл')
            else:
                print('Играем!')
                self.game()
