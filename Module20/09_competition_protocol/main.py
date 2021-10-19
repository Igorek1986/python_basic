def winner_sort(scores, num):
    test = num * 100000000 - scores
    return test


# count_protocol = int(input('Сколько записей вносится в протокол? '))
# games = {}
#
# print('Записи (результат и имя): ')
# for i_protocol in range(count_protocol):
#     protocol = input(f'{i_protocol + 1} запись: ').split()
#     name, score = protocol[1], int(protocol[0])
#     if name in games:
#         if games[name][0] < score:
#             games[name] = [score, i_protocol + 1]
#     else:
#         games[name] = [score, i_protocol + 1]
games = {'Jack': [95715, 6], 'qwerty': [197128, 5], 'Alex': [95715, 3], 'M': [95715, 9]}
winner = {}

for i, v in games.items():
    i_score = v[0]
    i_num = v[1]
    sorted(games[i], key=winner_sort(i_score, i_num))
print(winner)

# TODO, необходимо произвести сортировку исходя из "количества очков" и "номера записи".
#  Для этого, в key функции sorted необходимо передать функцию, которая будет принимать на вход
#  "количества очков" и "номера записи", и возвращать какое-то число, исходя из которого можно произвести сортировку.
#  Если позицию, к примеру 2, умножить на 100 000 000 и вычесть 95715, получим 199904285
#  Если позицию, к примеру 3, умножить на 100 000 000 и вычесть 95715, получим 299904285
#  Для того, чтобы победил тот, кто первый набрал большее количество очков, сортировку стоит делать от меньшего к большему.





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

# TODO, предлагаю реализовать задание за 2 отдельных цикла.
#  Один потребуется для запроса данных и заполнения словаря с данными.
#  Второй для вывода данных.
#  Словарь с данными стоит реализовать следующим образом
#  "Ключ" (Имя): "Значение" (список ["Счёт", "Номер записи"]).
#  Нам необходимы только записи с максимальным счётом у игрока.
