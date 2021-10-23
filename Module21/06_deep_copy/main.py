import copy


def find_key(structure, key, k_value):

    for i_key, value in structure.items():
        if isinstance(value, dict):
            structure[i_key] = find_key(value, key, k_value)
    if key in structure:
        structure[key] = k_value
    return structure


def copy_site(structure, key_title, key_h2, count=0, n_site={}):
    for _ in range(count):
        name = input('Введите название продукта для нового сайта: ')
        if isinstance(structure, dict):
            # key = 'Сайт для ' + name
            key = 'site ='
            n_site[key] = copy.deepcopy(structure)
            find_key(n_site[key], key_title, k_value=f'Куплю/продам {name} недорого')
            find_key(n_site[key], key_h2, k_value=f'У нас самая низкая цена на {name}')
            print(f'Сайт для {name}:')

            # TODO, функцию structure_print стоит создать до создания функции copy_site.
            def structure_print(s):

                space = 0  # TODO, переменную стоит сделать значением по умолчанию, иначе, каждый вызов функции она обнуляется.
                for i_key, i_value in s.items():
                    if isinstance(i_value, dict):
                        print(' ' * space, f'{i_key}:')
                        space += 4
                        structure_print(i_value)  # TODO, новое значение space стоит передавать в функцию как параметр.
                    else:
                        print(' ' * space, f'{i_key}: {i_value}')
            structure_print(n_site)

    # def print_dict(struct, count_space=4):
    #     for k, v in struct.items():
    #         # print(k + ':')
    #         # print('site = {')
    #         if isinstance(v, dict):
    #             print(' ' * count_space, f'{v}')
    #             print_dict(v)
    #         else:
    #             print(' ' * count_space, f'{k}: {v}')
    #             # count_space += 4
    # print_dict(n_site, 4)
    # return n_site


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на телефон',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


count_site = int(input('Сколько сайтов: '))
copy_site(site, 'title', 'h2', count_site)


# TODO Для вывода структуры сайта, в функцию стоит написать ещё одну функцию.
#  И добавить в неё параметр «количество пробелов».
#  При помощи цикла необходимо идти по словарю и проверять, является ли следующее значение словарём.
#  Если нет, выводим значение текущего ключа при помощи print с текущим «количеством пробелов».
#  Если да, выводим ключ и его значением текущим «количеством пробелов»
#  и проваливаемся глубже, увеличивая «количество пробелов».
