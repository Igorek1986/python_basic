class Unit:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def print_info(self):
        print(f'Здоровье {self.name} - {self.health}')

    def game(self, kick=0):
        self.health -= kick
