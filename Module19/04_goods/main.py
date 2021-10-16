goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for product in goods.keys():
    summ_goods = 0
    q_count = 0
    for quantity_price in store[goods[product]]:
        summ_goods += quantity_price['quantity'] * quantity_price['price']
        q_count += quantity_price['quantity']
    print(f'{product} - {q_count} шт, стоимость {summ_goods} руб')

# зачёт!
