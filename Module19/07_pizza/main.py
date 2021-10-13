count_order = int(input('Введите кол-во заказов: '))
order_dict = dict()

for i_order in range(1, count_order + 1):
    order = input(f'{i_order} заказ: ').split()
    surname, pizza, summ_pizza = order[0], order[1], int(order[2])
    if surname in order_dict:
        if pizza in order_dict[surname]:
            summ_pizza += int(order_dict[surname][pizza])
            order_dict[surname][pizza] = summ_pizza
        else:
            order_dict[surname][pizza] = summ_pizza
    else:
        order_dict[surname] = {pizza: summ_pizza}

for surname in sorted(order_dict):
    print(f'{surname}:')
    for pizza in sorted(order_dict[surname]):
        print(f'\t    {pizza}: {order_dict[surname][pizza]}')

# зачёт!
