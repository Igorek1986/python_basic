from abc import ABC, abstractmethod


class MyMath(ABC):
    """ Абстрактный базовый модуль нахождения математических вычислений """
    import math

    def __init__(self, rad: int) -> None:
        self.rad = rad

    @classmethod
    @abstractmethod
    def circle_len(cls, radius: int) -> float:
        return 2 * cls.math.pi * radius

    @classmethod
    @abstractmethod
    def circle_sq(cls, radius: int) -> float:
        return cls.math.pi * radius ** 2

    @classmethod
    @abstractmethod
    def cube_v(cls, len_edge_cube: int) -> float:
        return len_edge_cube ** 3

    @classmethod
    @abstractmethod
    def sfera_sq(cls, radius: int) -> float:
        return cls.math.pi * 4 * radius ** 2


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)


print(res_1)
print(res_2)


# Результат:
# 31.41592653589793
# 113.09733552923255
