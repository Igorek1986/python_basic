cell_list = []
unsuitable_list = []
n = int(input('Кол-во клеток: '))
for i in range(n):
    cell = int(input('Эффективность ' + str(i + 1) + ' клетки: '))
    if cell < i:
        unsuitable_list.append(cell)
print('\nНеподходящие значения:', unsuitable_list)
