import copy


def copy_site(structure, count=0, n_site={}):
    for _ in range(count):
        name = input('Введите название продукта для нового сайта: ')
        if isinstance(structure, dict):
            key = 'Сайт для ' + name
            n_site[key] = copy.deepcopy(structure)
            n_site[key]['html']['head']['title'] = 'Куплю/продам ' + name + ' недорого'
            n_site[key]['html']['body']['h2'] = 'У нас самая низкая цена на ' + name
            print(n_site)
    return n_site


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


count_site = int(input('Сколько сайтов: '))
copy_site(site, count_site)
