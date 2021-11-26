import math


class Car:
    def __init__(self, x, y, angel, distance):
        self.x = 0
        self.y = 0
        self.angel = angel
        self.distance = distance

    def move(self, distance, angel):
        self.x = round(self.x + distance * math.sin(math.radians(angel)))
        self.y = round(self.x + distance * math.cos(math.radians(angel)))


class Bus(Car):
    def __init__(self, x, y, angel, distance):
        super().__init__(x, y, angel, distance)
        self.count_of_passengers = 0
        self.cash = 0

    def in_the_bus(self, count):
        self.count_of_passengers += count

    def from_the_bus(self, count):
        self.count_of_passengers -= count

    def move(self, distance, angel):
        self.x = round(self.x + distance * math.sin(math.radians(angel)))
        self.y = round(self.x + distance * math.cos(math.radians(angel)))
