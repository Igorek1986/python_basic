count_country = int(input('Кол-во стран: '))
dict_county = {}
for i in range(1, count_country + 1):
    lst_country = (input(str(i) + ' страна: ').split())
    country = lst_country[0]
    dict_county[country] = lst_country[1:]
    # TODO, предлагаю перевернуть словарь =)
    #  Ключами сделать города, а значениями - страны.
    #  В таком случае, проверить наличие города (ключа) в словаре, мы сможем при помощи in.
    #  Для создания такого словаря, стоит реализовать цикл по списку городов lst_country[1:].


for i_city in range(1, 4):
    city = input(str(i_city) + ' город: ')
    if city in [x for name_city in dict_county.values() for x in name_city]:
        print('Город ' + city + ' расположен в стране' + '.')
    else:
        print('По городу', city, 'данных нет.')


