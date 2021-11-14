class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def print_state(self):
        print(f'Картошка {self.index} сейчас {Potato.states[self.state]}')

    def is_ripe(self):
        if self.state == 3:
            return True
        return False


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает!')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка еще не созрела!\n')
        else:
            print('Вся картошка созрела. Можно собирать!\n')


class Gardener:

    def __init__(self, name, potato_garden): # TODO, potato_garden в этой строке кода получился лишним.
        self.name = name
        self.potato_garden = potato_garden  # TODO, т.к. Грядка это класс. Возможно, изначально стоит сделать его равным None.
        # TODO, для сбора урожая, можно создать ещё один аргумент у садовника - пустой список.
        #  Если Картошка созрела, то из списка картошек на грядке её стоит удалить, и добавить в список собранной картошки.
        #  В методе садовника по сбору урожая. =)

    def care(self, count):
        print('Сажаю картошку')
        self.potato_garden = PotatoGarden(count)

    def print_potato_garden(self):
        print(self.potato_garden)

    def check_potato(self):
        # TODO, стоит реализовать цикл по Грядке садовника с проверкой состояния Картошки на Грядке.
        pass

    @staticmethod
    def collect(garden):
        # TODO, По идее, декоратор staticmethod лишний.
        #  Т.к. у садовника есть "своя" грядка, с которой он работает.
        print('Собираем урожай')


my_garden = []
gardener = Gardener('Ivan', my_garden)
gardener.care(5)
gardener.print_potato_garden()
gardener.check_potato()
# print(my_garden)


# my_garden.are_all_ripe()
# for _ in range(3):
#     my_garden.grow_all()
#     my_garden.are_all_ripe()
# Gardener.collect(my_garden)
# print(my_garden)
