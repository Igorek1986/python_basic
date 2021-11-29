import random


class Person:
    def __init__(self, name, surname, age, energy=30, happy=100):
        self.name = name
        self.surname = surname
        self.age = age
        self.energy = energy
        self.happy = happy
        self.my_house = None

    def __str__(self):
        return f'Состояние {self.name}:\nЭнергия - {self.energy}\nУровень счастья - {self.happy}'

    def add_house(self, obj):
        self.my_house = obj

    def eat(self):
        if self.my_house.fridge_eat > 30:
            print(f'{self.name}: Я кушать!')
            self.energy += 30
            self.my_house.fridge_eat -= 30
            self.my_house.total_eat += 30
        else:
            print('Нет еды!')
            self.energy -= 10

    def pet_the_cat(self):
        print(f'{self.name}: глажу кота')
        self.happy += 5
        self.energy -= 10

    def one_day(self):
        pass


class Man(Person):

    def one_day(self):
        action = random.randint(1, 4)
        if self.energy and self.happy:
            # TODO, т.к. проверка на наличие грязи есть в каждом классе, предлагаю реализовать её в методе
            #  one_day родительского класса. А в этом методе, просто вызвать супер метод. =)
            if self.my_house.dirt > 90:
                self.energy -= 10
            if self.energy < 20:
                self.eat()
            elif action == 1:
                self.eat()
            elif action == 2:
                self.pet_the_cat()
            elif action == 3:
                self.work()
            elif action == 4:
                self.game()
        elif self.energy < 0 or self.happy < 0:
            print('Ты проиграл')

    def work(self):
        print(f'{self.name}: Пойдем денег заработаем!')
        self.energy -= 10
        self.my_house.money += 150
        self.my_house.total_money += 150

    def game(self):
        if self.energy > 30:
            print(f'{self.name}: Сегодня я играю!')
            self.energy -= 10
            self.happy += 20
        else:
            print('Сейчас не до игр. Нужно беречь энергию.')
            self.energy -= 10


class Woman(Person):

    def one_day(self):
        action = random.randint(1, 6)
        if self.energy and self.happy:
            if self.my_house.dirt > 90:
                self.energy -= 10
            if self.energy < 20:
                print(f'{self.name}: Я кушать!')
                self.eat()
            elif self.my_house.fridge_eat < 60:
                self.shopping()
            elif action == 1:
                self.eat()
            elif action == 2:
                self.pet_the_cat()
            elif action == 3:
                self.shopping()
            elif action == 4:
                self.shopping_cat_eat()
            elif action == 5:
                self.fur_coat()
            elif action == 6:
                self.cleaning()
        elif self.energy < 0 or self.happy < 0:
            print('Ты проиграл')

    def shopping(self):
        if self.my_house.money > 60:
            print(f'{self.name}: Иду за покупками!')
            self.my_house.fridge_eat += 60
            self.energy -= 10
            self.my_house.money -= 60

    def shopping_cat_eat(self):
        if self.my_house.money > 10:
            print(f'{self.name}: Покупаем еду для кота!')
            self.my_house.eat_cat += 20
            self.energy -= 10
            self.my_house.money -= 10

    def fur_coat(self):
        if self.my_house.money > 350:
            print(f'{self.name}: Сегодня я покупаю шубу!')
            self.happy += 60
            self.energy -= 10
            self.my_house.money -= 350
            self.my_house.total_fur_coat += 1

    def cleaning(self):
        print(f'{self.name}: Убираем дом!')
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

    def one_day_cat(self):
        action = random.randint(1, 3)
        if self.energy:
            if action == 1:
                self.eat_cat()
            elif action == 2:
                self.sleep()
            elif action == 3:
                self.harm()
        elif self.energy < 0:
            print('Ты проиграл')

    def add_house(self, obj):
        self.my_house = obj

    def eat_cat(self):
        if self.my_house.fridge_eat > 10:
            print(f'{self.name}: Пойду посплю!\n'
                  'А нет нужно поесть')
            self.energy += 20
            self.my_house.fridge_eat -= 10

    def sleep(self):
        print(f'{self.name}: Пойду посплю!')
        self.energy -= 10

    def harm(self):
        print(f'{self.name}: Точим когти')
        self.my_house.dirt += 5
        self.energy -= 10
