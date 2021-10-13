count_order = 6 #int(input('Введите кол-во заказов: '))
order_dict = dict()


for i_order in range(1, count_order + 1):
    order = input(f'{i_order} заказ: ').split()
    if order[0] in order_dict:
        order_dict[order[0]][order[1]] = order[2]
    else:
        order_dict[order[0]] = {order[1]: order[2]}


print(order_dict)
