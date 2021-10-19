def winner_sort(winner):
    return winner[1][0] * 100000000 - winner[1][1]


count_protocol = int(input('Сколько записей вносится в протокол? '))
games = {}


print('Записи (результат и имя): ')
for i_protocol in range(count_protocol):
    protocol = input(f'{i_protocol + 1} запись: ').split()
    name, score = protocol[1], int(protocol[0])
    if name in games:
        if games[name][0] < score:
            games[name] = [score, i_protocol + 1]
    else:
        games[name] = [score, i_protocol + 1]


games_lst = list(games.items())
games_lst.sort(key=winner_sort, reverse=True)


print('Итоги соревнований:')
for i_winner in range(3):
    name = games_lst[i_winner][0]
    score = games_lst[i_winner][1][0]
    print(f'{i_winner + 1} место {name} - {score}')


# 1 запись: 69485 Jack
# 2 запись: 95715 qwerty
# 3 запись: 95715 Alex
# 4 запись: 83647 M
# 5 запись: 197128 qwerty
# 6 запись: 95715 Jack
# 7 запись: 93289 Alex
# 8 запись: 95715 Alex
# 9 запись: 95715 M

# Итоги соревнований:
# 1 место. qwerty (197128)
# 2 место. Alex (95715)
# 3 место. Jack (95715)
