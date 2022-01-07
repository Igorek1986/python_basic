from abc import ABC, abstractmethod


class Figure(ABC):

    """ Абстрактынй базовый класс фигуры"""

    @abstractmethod
    def __init__(self, side_1: int, side_2: int):
        self._side_1 = side_1
        self._side_2 = side_2

    @property
    def side_1(self):
        return self._side_1

    @side_1.setter
    def side_1(self, side_1):
        self._side_1 = side_1

    @property
    def side_2(self):
        return self._side_2

    @side_2.setter
    def side_2(self, side_2):
        self._side_2 = side_2


class Square(Figure):

    """" Дочерний класс квадрата от Фигуры """

    def __init__(self, side: int):
        super().__init__(side_1=side, side_2=side)
        self.side = side

    def perimetr(self) -> int:
        return self.side * 4

    def square(self) -> int:
        return self.side ** 2


class Triangle(Figure):

    """ Дочерний класс треугольника от Фигуры """

    def __init__(self, base: int, height: int):
        super().__init__(side_1=base, side_2=height)
        self.base = base
        self.height = height

    def perimetr(self) -> int:
        return 2 * self.height + self.base

    def square(self) -> float:
        return 1 / 2 * self.height * self.base


class Square3D(Square):

    pass

    # def __init__(self, side):
    #     super().__init__(side)
    #     self.side = self.side.append(Square)


class Triangle3D(Triangle):
    pass


a = Square(side=7)
a.side_1 = 8
print(a.square())
b = Triangle(base=6, height=2)
print(b.square())
