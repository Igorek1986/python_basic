alfavit = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

message = input("Введите сообщение: ")
shift = int(input('Введите сдвиг: '))
cipher = ''

for i in message:
    for i2 in alfavit:
        if i == i2:
            word = alfavit.index(i2) + shift - 33
            cipher += alfavit[word]
    if i == ' ':
        cipher += ' '
print(cipher)
