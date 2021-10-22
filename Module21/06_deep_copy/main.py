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
            key = 'Сайт для ' + name
            n_site[key] = copy.deepcopy(structure)
            find_key(n_site[key], key_title, k_value=f'Куплю/продам {name} недорого')
            find_key(n_site[key], key_h2, k_value=f'У нас самая низкая цена на {name}')
            print(n_site)
    return n_site


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
