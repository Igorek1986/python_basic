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


class Square3D(Square):

    pass

    # def __init__(self, side):
    #     super().__init__(side)
    #     self.side = self.side.append(Square)


class Triangle3D(Triangle):
    pass


a = Square(side=7)
print(a.square())
