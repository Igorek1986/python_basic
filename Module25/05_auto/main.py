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
        self.ticket = 100

    def in_the_bus(self, count):
        self.count_of_passengers += count

    def from_the_bus(self, count):
        self.count_of_passengers -= count

    def move(self, angel, distance):
        super().move(angel, distance)
        road_distance = distance - self.distance
        if road_distance > 9:
            self.ticket = 100 * 1.5
        self.cash = self.count_of_passengers * self.ticket


bus = Bus(angel=0, distance=0)
print('Деньги', bus.cash)
bus.in_the_bus(count=5)
print('Пассажиры', bus.count_of_passengers)
bus.move(angel=30, distance=10)
print('Деньги', bus.cash)

# зачёт!
