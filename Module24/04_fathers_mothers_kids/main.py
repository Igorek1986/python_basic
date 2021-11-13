class Parent:

    def __init__(self, name, age, child=[]):
        self.name = name
        self.age = age
        self.child = child

    def print_info(self):
        print(f'Меня зовут {self.name},\n'
              f'мне {self.age} лет')
        if self.child:
            print(f'У меня есть дети. Их зовут:')
            for i_child in self.child:
                print(i_child)
        else:
            print('У меня нет детей')

    def add_child(self, name):
        self.child.append(name)

    def check_calm_down(self):
        if not self:
            print('Успокойся мой малыш.')
            return True
        return False

    def check_feed(self):
        if not self:
            print('Кушай!')
            return True
        return False


class Child:

    def __init__(self, name, age, state_calm, state_hunger):
        self.name = name
        self.age = age
        self.state_calm = state_calm
        self.state_hunger = state_hunger

    def print_info(self):
        print(f'Меня зовут {self.name},\n'
              f'мне {self.age} лет')
        print(self.state_calm)
        print(self.state_hunger)

    def state_calm(self):
        if self.state_calm:
            self.state_calm.calm_down()


igor = Parent('Igor', 35)
dima = Child('Dima', 7, False, True)
# igor.add_child(dima.name)
# dima.print_info()
