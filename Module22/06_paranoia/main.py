print('Содержимое файла text.txt:')


with open('text.txt', 'r') as file:
    key_cipher = 0
    for i_line in file:
        print(i_line, end='')
        key_cipher += 1
        for sym in i_line:
            if ord('A') <= ord(sym) <= ord('z'):
                new_sym = ord(sym) + key_cipher
                cipher = open('cipher_text.txt', 'a')
                cipher.write(chr(new_sym))
        cipher.write('\n')
    cipher.close()


print('\n\nСодержимое файла cipher_text.txt:')
with open('cipher_text.txt', 'r') as cipher:
    for i_line in cipher:
        print(i_line, end='')
