class Human:

    # TODO, т.к. аргумент является аргументом одного человека, а не нескольких, то стоит создавать его в методе __init__.
    my_house = None

    def __init__(self, name, energy=50):
        self.name = name
        self.energy = energy

    def add_house(self, obj):
        self.my_house = obj

    # TODO, как вариант, можно убрать из всех методов ниже параметры и увеличивать или уменьшать параметры на,
    #  всегда одни и теже цифры.

    def eat(self, energy, eat):
        # TODO, предлагаю добавить проверку. Если в доме нет еды, то поесть человек не может.
        self.energy += energy
        # TODO, стоит сокращать еду в "своём"."доме".
        self.eat -= eat

    def work(self, energy, money):
        # TODO, возможно аргумент money лишний.
        self.energy -= energy

    def game(self, energy):
        self.energy -= energy

    def shopping(self, eat, money):
        # TODO, предлагаю добавить проверку. Если в доме нет денег, то еды купить человек не сможет.
        #  Стоит сокращать количество денег в "своём"."доме".
        self.eat += eat
        money -= money
