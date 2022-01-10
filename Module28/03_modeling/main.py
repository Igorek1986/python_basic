class Square:
    """" Базовый класс квадрата """

    def __init__(self, length: int) -> None:
        self._length = length

    def perimetr(self) -> int:
        return self._length * 4

    def area(self) -> int:
        return self._length ** 2

    @property
    def new_length(self) -> float:
        return self._length

    @new_length.setter
    def new_length(self, length: int):
        self._length = length


class Triangle:
    """ Базовый класс треугольника """

    def __init__(self, base: int, height: int) -> None:
        self._base = base
        self._height = height

    def perimetr(self) -> int:
        return 2 * self._height + self._base

    def area(self) -> float:
        return 1 / 2 * self._height * self._base

    @property
    def new_base(self) -> float:
        return self._height

    @new_base.setter
    def new_base(self, base: int):
        self._base = base

    @property
    def new_height(self) -> float:
        return self._height

    @new_height.setter
    def new_height(self, height: int):
        self._height = height


class SurfaceAreaMixin:

    def surface_area(self) -> float:
        surface_area = 0
        for surface in self.surfaces:
            surface_area += surface.area(self)

        return surface_area


class Cube(Square, SurfaceAreaMixin):
    """ Базовый класс Куба от класса Квадрат,
     Миксин расчета площади поверхности """

    def __init__(self, length: int) -> None:
        super().__init__(length)
        # TODO Список сторон должен состоять из объектов Класса(), но не из Класса. =)
        self.surfaces = [Square, Square, Square, Square, Square, Square]


class Pyramid(Triangle, SurfaceAreaMixin):
    """ Базовый класс Пирамиды от класса Треугольника,
     Миксин расчета площади поверхности """

    def __init__(self, base: int, height: int) -> None:
        super().__init__(base, height)
        self._length = base
        self._height = height
        self.surfaces = [Square, Triangle, Triangle, Triangle, Triangle]


cube = Cube(length=7)
print('Площадь поверхности куба:', cube.surface_area())
cube.new_length = 2
print('Площадь поверхности куба:', cube.surface_area())
pyramid = Pyramid(base=6, height=2)
print('Площадь поверхности пирамиды:', pyramid.surface_area())
pyramid.new_base = 2
print('Площадь поверхности пирамиды:', pyramid.surface_area())

# зачёт!
