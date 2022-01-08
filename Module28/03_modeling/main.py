from abc import ABC, abstractmethod


# class Figure(ABC):
#
#     """ Абстрактный базовый класс фигуры"""
#
#     @abstractmethod
#     def __init__(self, side_1: int, side_2: int):
#         self._side_1 = side_1
#         self._side_2 = side_2
#
#     @property
#     def side_1(self):
#         return self._side_1
#
#     @side_1.setter
#     def side_1(self, side_1):
#         self._side_1 = side_1
#
#     @property
#     def side_2(self):
#         return self._side_2
#
#     @side_2.setter
#     def side_2(self, side_2):
#         self._side_2 = side_2


class Square:

    """" Базовый класс квадрата """

    def __init__(self, side: int):
        self.side = side

    def perimetr(self) -> int:
        return self.side * 4

    def square(self) -> int:
        return self.side ** 2


class Triangle:

    """ Базовый класс треугольника """

    def __init__(self, base: int, height: int):
        self.base = base
        self.height = height

    def perimetr(self) -> int:
        return 2 * self.height + self.base

    def square(self) -> float:
        return 1 / 2 * self.height * self.base


class SurfaceAreaMixin:
    pass


class Cube(Square, SurfaceAreaMixin):

    pass

    # def __init__(self, side):
    #     super().__init__(side)
    #     self.side = self.side.append(Square)


class Pyramid(Triangle, SurfaceAreaMixin):
    pass


a = Square(side=7)
print(a.square())
b = Triangle(base=6, height=2)
print(b.square())
