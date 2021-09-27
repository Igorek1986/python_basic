def selection_sort(shop_list, detail):
    for i_detal in shop_list:
        if i_detal[0] == detail:
            shop_sort.extend(i_detal)


# TODO, предлагаю решить задание всего за один цикл for без использования range + len.
#  один вложенный список, это одна деталь. По идее метод count, в решении будет лишним.
#  таким образом, мы сократим количество функций и циклов в решении. =)

# def selection_price(shop_list, detail):
#     summ_price = 0
#     for i_detal in range(len(shop_list)):
#         if shop_list[i_detal].count(detail):
#             summ_price += shop_list[i_detal][1]
#     return summ_price


shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]
shop_sort = []

title_detail = input('Название детали: ')

total_count = selection_sort(shop, title_detail)

# total_summ = selection_sort(shop, title_detail)

print('\nКол-во деталей -', shop_sort.count(title_detail))
# print('Общая стоимость -', total_summ)
