class Player:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def sym_x_0(count):
        if count % 2 == 0:
            return 'X'
        else:
            return '0'
