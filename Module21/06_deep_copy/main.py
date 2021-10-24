import copy


def find_key(structure, key, k_value):
    for i_key, value in structure.items():
        if isinstance(value, dict):
            structure[i_key] = find_key(value, key, k_value)
    if key in structure:
        structure[key] = k_value
    return structure


def structure_print(s, space=0):
    for i_key, i_value in s.items():
        if isinstance(i_value, dict):
            print(' ' * space, f"'{i_key}': {{")
            structure_print(i_value, space + 4)
            print(' ' * space, "}")
        else:
            print(' ' * space, f"'{i_key}': '{i_value}',")


def copy_site(structure, key_title, key_h2, lst, count=0, n_site={}):
    for _ in range(count):
        name = input('Введите название продукта для нового сайта: ')
        if isinstance(structure, dict):
            key = 'Сайт для ' + name
            # key = 'site ='
            # key = ''
            # n_site = copy.deepcopy(structure)
            # find_key(n_site, key_title, k_value=f'Куплю/продам {name} недорого')
            # lst.append(find_key(n_site, key_h2, k_value=f'У нас самая низкая цена на {name}'))
            n_site[key] = copy.deepcopy(structure)
            find_key(n_site[key], key_title, k_value=f'Куплю/продам {name} недорого')
            lst.append(find_key(n_site[key], key_h2, k_value=f'У нас самая низкая цена на {name}'))
            # print(f'Сайт для {name}:')
            print('site = {')
            # print(lst)
            structure_print(n_site)


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

site_lst = []

count_site = int(input('Сколько сайтов: '))
copy_site(site, 'title', 'h2', site_lst, count_site)

# зачёт!
