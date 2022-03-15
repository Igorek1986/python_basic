import re


if __name__ == '__main__':
    text = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

    pattern_auto = re.findall(r'\b\w\d{3}\w{2}\d{2,3}', text)
    print('Список номеров частных автомобилей:', pattern_auto)

    pattern_taxi = re.findall(r'\b\w{2}\d{5,6}', text)
    print('Список номеров такси:', pattern_taxi)

# Результат:

# Список номеров частных автомобилей: ['А578ВЕ777', 'К901МН666']

# Список номеров такси: ['ОР233787', 'СТ46599']
