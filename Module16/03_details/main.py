def selection_sort(shop_list, detail):
    count = 0
    for i_detal in range(len(shop_list)):
        if shop_list[i_detal].count(detail):
            count += 1
    return count


def selection_price(shop_list, detail):
    summ_price = 0
    for i_detal in range(len(shop_list)):
        if shop_list[i_detal].count(detail):
            summ_price += shop_list[i_detal][1]
    return summ_price


shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

title_detail = input('Название детали: ')

total_count = selection_sort(shop, title_detail)
total_summ = selection_price(shop, title_detail)

print('\nКол-во деталей -', total_count)
print('Общая стоимость -', total_summ)
