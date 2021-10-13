count_country = int(input('Кол-во стран: '))
dict_county = {}
for i in range(1, count_country + 1):
    lst_country = input(f' {i} страна: ').split()
    for j in lst_country[1:]:
        dict_county[j] = lst_country[0]

for i_city in range(1, 4):
    city = input(f'\n {i_city} город: ')
    if city in dict_county:
        print(f'Город {city} расположен в стране {dict_county[city]}.')
    else:
        print(f'По городу {city} данных нет.')
