count_order = int(input('Введите кол-во заказов: '))
order_dict = dict()
pizza = []
pizza_dict = {}


for i_order in range(1, count_order + 1):
    order = input(f'{i_order} заказ: ').split()
    order_dict[order[0]] = {order[1]: order[2]}
    for j_order in order_dict:
        print(order_dict[j_order])
        if order_dict[j_order] in pizza_dict:
            pizza_dict[order_dict[j_order]].append(j_order)
        else:
            pizza_dict[order_dict[j_order]] = [j_order]




print(order_dict)
