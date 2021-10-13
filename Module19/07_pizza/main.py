count_order = 6 #int(input('Введите кол-во заказов: '))
order_dict = dict()


for i_order in range(1, count_order + 1):
    order = input(f'{i_order} заказ: ').split()

    # TODO, для сокращения количества вычислений, предлагаю создать переменные
    #  order[0] ... и далее в цикле работать с ними =)

    if order[0] in order_dict:
        # TODO, Стоит так же проверить, есть ли "Пицца" во вложенном словаре.
        #  Если есть, то увеличить значение количества пицц, если нет, то добавить с тем количеством, которое указал пользователь.
        order_dict[order[0]][order[1]] = order[2]
    else:
        order_dict[order[0]] = {order[1]: order[2]}

# TODO, пожалуйста, реализуйте вывод как в примере. =)
print(order_dict)
