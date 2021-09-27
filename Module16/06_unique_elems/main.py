first_list = [1, 2, 3]
second_list = [2, 4, 6, 3, 3, 2, 1]


# first_list = []
# second_list = []
#
# for _ in range(3):
#     n = int(input('Введите первый список из 3 элементов: '))
#     first_list.append(n)
# for _ in range(7):
#     n = int(input('\nВведите второй список из 7 элементов: '))
#     second_list.append(n)


first_list.extend(second_list)
for i in first_list:
    # TODO Предлагаю попробовать заменить цикл while на for.
    #  Дело в том, что цикл for будет работать быстрее, т.к. формирует условие для своей работы только 1 раз, при создании.
    #  В то время, как цикл while проверяет условие своей работы каждую итерацию цикла.
    while first_list.count(i) > 1:
        first_list.remove(i)


print('Новый первый список с уникальными элементами:', first_list)
