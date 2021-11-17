class Human:
    my_house = None

    def __init__(self, name, energy=50):
        self.name = name
        self.energy = energy

    def add_house(self, obj):
        self.my_house = obj

    def eat(self, energy, eat):
        self.energy += energy
        self.eat -= eat

    def work(self, energy, money):
        self.energy -= energy

    def game(self, energy):
        self.energy -= energy

    def shopping(self, eat, money):
        self.eat += eat
        money -= money
