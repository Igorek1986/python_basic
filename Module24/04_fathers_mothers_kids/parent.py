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

    def add_child(self, child):
        if not child.age + 16 >= self.age:
            self.child.append(child.name)

    @staticmethod
    def check_calm_down(child):
        if not child.state_calm:
            print('Успокойся мой малыш.')
            child.state_calm = True

    @staticmethod
    def check_feed(child):
        if child.state_hunger:
            print('Кушай!')
            child.state_hunger = False
