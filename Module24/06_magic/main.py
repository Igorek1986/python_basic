class Water:

    def __str__(self):
        return self.name

    def __init__(self):
        self.name = 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        return None


class Air:

    def __str__(self):
        return self.name

    def __init__(self):
        self.name = 'Воздух'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        if isinstance(other, Earth):
            return Dust()
        return None


class Fire:

    def __str__(self):
        return self.name

    def __init__(self):
        self.name = 'Огонь'

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        return None


class Earth:

    def __str__(self):
        return self.name

    def __init__(self):
        self.name = 'Земля'

    def __add__(self, other):
        return None


class Storm:

    def __str__(self):
        return self.name

    def __init__(self):
        self.name = 'Шторм'

    def __add__(self, other):
        return None


class Steam:

    def __str__(self):
        return self.name

    def __init__(self):
        self.name = 'Пар'

    def __add__(self, other):
        return None


class Dirt:

    def __str__(self):
        return self.name

    def __init__(self):
        self.name = 'Грязь'

    def __add__(self, other):
        return None


class Lightning:

    def __str__(self):
        return self.name

    def __init__(self):
        self.name = 'Молния'

    def __add__(self, other):
        return None


class Dust:

    def __str__(self):
        return self.name

    def __init__(self):
        self.name = 'Пыль'

    def __add__(self, other):
        return None


class Lava:

    def __str__(self):
        return self.name

    def __init__(self):
        self.name = 'Лава'

    def __add__(self, other):
        return None


print(Dust() + Lava())

# зачёт!
