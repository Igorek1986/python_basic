message = 'Это задание очень! простое.'.split()
# message = 'Хотя ,. возм:ожно и нет.'.split()

# message = message.split()
print(message)
test = ''
for i in range(len(message)):
    if message[i].isalpha():
        message[i] = message[i][::-1]
    else:
        for i2 in message[i]:
            # print(i2)
            message[i] = test
            if i2.isalpha():
                test = i2 + test
                # print(test)
            elif not i2.isalpha() and not ' ':
                test = test + i2
            else:
                test = ' '

print(message)
