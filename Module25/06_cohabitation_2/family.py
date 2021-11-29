class Person:
    def __init__(self, name, surname, age, energy=30, happy=100):
        self.name = name
        self.surname = surname
        self.age = age
        self.energy = energy
        self.happy = happy
        self.my_house = None

    def add_house(self, obj):
        self.my_house = obj

    def eat(self):
        if self.my_house.fridge_eat > 30:
            self.energy += 30
            self.my_house.fridge_eat -= 30
            self.my_house.total_eat += 30

    def pet_the_cat(self):
        self.happy += 5

    def action(self):
        if self.energy:
            if self.energy < 50:
                print('Приятного аппетита!')
                self.eat()
            elif self.energy < 50:
                print('Гладим кота!')
                self.pet_the_cat()
            elif self.energy < 0:
                print('Ты проиграл')


class Man(Person):
    # TODO, если метод не переопределяется, то создавать его не нужно!
    #  Его мы возьмём из родительского класса. =)
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def work(self):
        self.energy -= 10
        self.my_house.money += 150
        self.my_house.total_money += 150

    def game(self):
        if self.energy > 30:
            self.energy -= 10
            self.happy += 20


class Woman(Person):
    # TODO, если метод не переопределяется, то создавать его не нужно!
    #  Его мы возьмём из родительского класса. =)
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def shopping(self):
        if self.my_house.money > 10:
            self.my_house.fridge_eat += 10
            self.energy -= 10
            self.my_house.money -= 10

    def shopping_cat_eat(self):
        if self.my_house.money > 10:
            self.my_house.eat_cat += 20
            self.energy -= 10
            self.my_house.money -= 10

    def fur_coat(self):
        if self.my_house.money > 350:
            self.happy += 60
            self.energy -= 10
            self.my_house.money -= 350
            self.my_house.fur_coat += 1

    def cleaning(self):
        if self.my_house.dirt <= 100:
            self.my_house.dirt = 0
        else:
            self.my_house.dirt = self.my_house.dirt - 100
        self.energy -= 10


class Cat:

    def __init__(self, name, energy=30):
        self.name = name
        self.energy = energy
        self.my_house = None

    def add_house(self, obj):
        self.my_house = obj

    def eat(self):
        if self.my_house.fridge_eat > 10:
            self.energy += 20
            self.my_house.fridge_eat -= 10

    def sleep(self):
        self.energy -= 10

    def harm(self):
        self.my_house.dirt += 5
        self.energy -= 10
