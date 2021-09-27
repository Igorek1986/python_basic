def selection_sort(song_list, song):
    time = 0
    for i_song in song_list:
        if i_song[0] == song:
            time += i_song[1]
    return time


violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

favorite_list = []


num_count = int(input('Сколько песен выбрать? '))


for i in range(num_count):
    title_song = input('Название ' + str(i + 1) + ' песни: ')
    favorite_list.append(selection_sort(violator_songs, title_song))


print('Общее время звучания песен:', round(sum(favorite_list), 2), 'минут')
