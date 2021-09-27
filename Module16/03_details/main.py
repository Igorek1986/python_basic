def selection_sort(shop_list, detail):
    count = 0
    summ_price = 0
    for i_detal in shop_list:
        if i_detal[0] == detail:
            count += 1
            summ_price += i_detal[1]
    return [count, summ_price]


shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]
shop_sort = []

title_detail = input('Название детали: ')

total_count, total_summ = selection_sort(shop, title_detail)


print('\nКол-во деталей -', total_count)
print('Общая стоимость -', total_summ)
