violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}


my_song = {}
num = int(input('Сколько песен выбрать? '))
for i in range(1, num + 1):
    i_song = input('Название ' + str(i) + ' песни: ')
    my_song[i_song] = violator_songs[i_song]

total_time = round(sum(my_song.values()), 2)

print('Общее время звучания песен:', total_time, 'минут')

# TODO, стоит добавить проверку наличия ключа в словаре или воспользоваться методом словарей get с параметром по умолчанию.
#  Иначе, если ключа в словаре нет, получим ошибку.
#  Немного подробней про метод get словарей, можно почитать тут:
#  https://docs-python.ru/tutorial/operatsii-slovarjami-dict-python/metod-dict-get/
