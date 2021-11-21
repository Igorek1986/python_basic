class Board:

    def __init__(self, board=[]):
        self.board = board

    def print_info(self):
        print('-' * 13)
        for i in range(3):
            print('|', self.board[0 + i * 3], '|',
                  self.board[1 + i * 3], '|',
                  self.board[2 + i * 3], '|')
            print('-' * 13)

    def input_sym(self, sym):
        flag = False
        while not flag:
            answer = int(input(f'Куда поставим {sym}? '))
            if 1 <= answer <= 9:
                if str(self.board[answer - 1]) not in 'XO':
                    self.board[answer - 1] = sym
                    flag = True
                else:
                    print('Эта клетка уже занята!')
            else:
                print('Некорректный  ввод. Введите от 1 до 9')

    def check_win(self):
        victory = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for sym in victory:
            if self.board[sym[0]] == self.board[sym[1]] == self.board[sym[2]]:
                return self.board[sym[0]]
        return False
