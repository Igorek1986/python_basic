# message = 'Это задание очень! простое.'.split()
message = 'Хотя ,. возм:ожно и нет.'.split()

# message = message.split()
print(message)
word = ''
for i in range(len(message)):
    if message[i].isalpha():
        message[i] = message[i][::-1]
    else:
        for i2 in message[i]:
            if i2.isalpha():
                word = i2 + word
            else:
                word = word + i2
        message[i] = word
        word = ''

print(message)
