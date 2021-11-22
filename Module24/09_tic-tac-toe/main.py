from board import Board
from player import Player

count = 0
win = False
x_0 = Board(list(range(1, 10)))
player = Player('Иван')

while not win:
    x_0.print_info()
    x_0.input_sym(player.sym_x_0(count))
    count += 1
    if count > 4:
        winner = x_0.check_win()
        if winner:
            print(winner, 'выиграл!')
            win = True
            x_0.print_info()
            break
    elif count == 9:
        print('Ничья!')
        break

# зачёт!
