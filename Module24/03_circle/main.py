import math


class Round:

    def __init__(self, coordinate_x=0, coordinate_y=0, radius=1):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.radius = radius

    def square_round(self):
        square = math.pi * self.radius ** 2
        return square

    def perimeter(self):
        perimeter = 2 * self.radius * math.pi
        return perimeter

    def increase(self, k):
        self.radius *= k

    def crossing(self, x2, y2, r2):
        # TODO,
        #  1. стоит передавать в этот метод класса второй круг, вместо параметров второго круга.
        #  2. а так же добавить проверку (при помощи функции isinstance), что элемент является объектом класса Круг.
        #  Ведь в противном случае, он может не иметь аргументов "x" и "y".

        length_between_centers = math.sqrt((self.coordinate_x - x2) ** 2 + (self.coordinate_y - y2) ** 2)
        sum_radius = self.radius + r2
        if length_between_centers <= sum_radius:
            print('Окружности пересекаются')
            return True
        else:
            print('Окружности не пересекаются')
            return False


round_1 = Round(1, 1, 1)
round_2 = Round()


print(f'Площадь: {round_1.square_round()}')
print(f'Периметр: {round_1.perimeter()}')
print(f'Увеличиваем круг в {4} раза')
round_1.increase(4)
print('Параметры увеличенного круга:')
print(f'Площадь: {round_1.square_round()}')
print(f'Периметр: {round_1.perimeter()}')

round_1.crossing(round_2.coordinate_x, round_2.coordinate_y, round_2.radius)
