import math


class Car:
    def __init__(self, angel, distance, x=0, y=0):
        self.x = x
        self.y = y
        self.angel = angel
        self.distance = distance

    def move(self, angel, distance):
        self.x = round(self.x + distance * math.sin(math.radians(angel)))
        self.y = round(self.y + distance * math.cos(math.radians(angel)))


class Bus(Car):
    def __init__(self, angel, distance):
        super().__init__(angel, distance)
        self.count_of_passengers = 0
        self.cash = 0

    def in_the_bus(self, count, ticket=100):
        self.count_of_passengers += count
        self.cash = count * ticket

    def from_the_bus(self, count):
        self.count_of_passengers -= count

    def move(self, angel, distance):
        super().move(angel, distance)

    def profit(self):
        pass

    def __str__(self):
        return f'Координата Х:{self.x}\nКоордината У:{self.y}'


bus = Bus(angel=0, distance=0)

print('Деньги', bus.cash)
bus.in_the_bus(count=5)
print('Пассажиры', bus.count_of_passengers)
bus.move(angel=30, distance=10)
print('Деньги', bus.cash)

