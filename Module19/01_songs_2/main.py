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
    my_song[i_song] = violator_songs.get(i_song, 0)

total_time = round(sum(my_song.values()), 2)

print('Общее время звучания песен:', total_time, 'минут')

# зачёт!
