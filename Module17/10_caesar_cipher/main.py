alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


message = input("Введите сообщение: ")
shift = int(input('Введите сдвиг: '))
cipher = ''


cipher_list = [alphabet[(alphabet.index(i) + shift) % 33] if i != ' ' else ' ' for i in message]


for i in range(len(cipher_list)):
    cipher += cipher_list[i]
print('Зашифрованное сообщение:', cipher)

# зачёт!