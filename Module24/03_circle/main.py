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

    def crossing(self, cross_round):
        if isinstance(cross_round, Round):
            length_between_centers = math.sqrt((self.coordinate_x - cross_round.coordinate_x) ** 2
                                               + (self.coordinate_y - cross_round.coordinate_y) ** 2)
            sum_radius = self.radius + cross_round.radius
            if length_between_centers <= sum_radius:
                print('Окружности пересекаются')
                return True
            else:
                print('Окружности не пересекаются')
                return False
        else:
            print('Ошибка! Данные не являются кругом. Проверка не возможна.')


round_1 = Round(1, 1, 1)
round_2 = Round()


print(f'Площадь: {round_1.square_round()}')
print(f'Периметр: {round_1.perimeter()}')
print(f'Увеличиваем круг в {4} раза')
round_1.increase(4)
print('Параметры увеличенного круга:')
print(f'Площадь: {round_1.square_round()}')
print(f'Периметр: {round_1.perimeter()}')

round_1.crossing(round_2)
