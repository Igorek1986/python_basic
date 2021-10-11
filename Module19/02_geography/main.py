count_country = int(input('Кол-во стран: '))
dict_county = {}
for i in range(1, count_country + 1):

    # TODO, Возможно, Вам тоже покажется удобным форматирование при помощи f-строк, вместо использования str в print и input =).
    #  https://python-scripts.com/f-strings
    lst_country = (input(str(i) + ' страна: ').split())

    # TODO, предлагаю уйти от использования конструкции len + range и тем самым,
    #  сократить количество вычислений элементов списка по индексам.
    #  Стоит взять по срезу все элементы списка кроме первого и идти по нему в цикле =)
    for j in range(1, len(lst_country)):
        dict_county[lst_country[j]] = lst_country[0]

for i_city in range(1, 4):
    city = input('\n' + str(i_city) + ' город: ')
    if city in dict_county:
        print('Город ' + city + ' расположен в стране ' + dict_county[city] + '.')
    else:
        print('По городу', city, 'данных нет.')
