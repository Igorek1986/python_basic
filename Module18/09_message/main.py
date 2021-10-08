# message = 'Это задание очень! простое.'.split()
message = 'Хотя ,. возм:ожно и нет.'.split()

print('Сообщение:', ' '.join(message))
test = ''
for i in range(len(message)):
    if message[i].isalpha():
        message[i] = message[i][::-1]
    else:
        for i2 in message[i]:
            if not i2.isalpha():
                message[i] = message[i][:message[i].index(i2):1][::-1] + i2 \
                             + message[i][1 + message[i].index(i2)::1][::-1]

print('Новое сообщение:', ' '.join(message))

# зачёт!
