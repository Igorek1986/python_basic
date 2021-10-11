count_country = int(input('Кол-во стран: '))
dict_county = {}
for i in range(1, count_country + 1):
    lst_country = (input(str(i) + ' страна: ').split())
    for j in range(1, len(lst_country)):
        dict_county[lst_country[j]] = lst_country[0]


for i_city in range(1, 4):
    city = input('\n' + str(i_city) + ' город: ')
    if city in dict_county:
        print('Город ' + city + ' расположен в стране ' + dict_county[city] + '.')
    else:
        print('По городу', city, 'данных нет.')
