volleyball_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']

# TODO, Стоит добавить шаг в range, в таком случае, условный оператор получится лишний =)
for i in range(len(volleyball_list)):
    if i % 2 == 0 or i == 0:
        print(volleyball_list[i])


# это гугл))) Все как в цикле for. start, stop, step
# b = volleyball_list[::2]
# print(b)