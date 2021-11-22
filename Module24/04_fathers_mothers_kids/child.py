class Child:

    def __init__(self, name, age, state_calm, state_hunger):
        self.name = name
        self.age = age
        self.state_calm = state_calm
        self.state_hunger = state_hunger

    def print_info(self):
        print(f'Меня зовут {self.name},\n'
              f'мне {self.age} лет')
        if self.state_calm:
            print('Я сейчас спокоен')
        else:
            print('Я плачу')
        if not self.state_hunger:
            print('Я сейчас сытый')
        else:
            print('Я голодный')

    def calm(self, parent):
        if not self.state_calm:
            parent.check_calm_down(self)

    def hunger(self, parent):
        if self.state_hunger:
            parent.check_feed(self)
