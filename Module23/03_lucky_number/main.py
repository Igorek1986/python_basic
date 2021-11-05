import random

sum_num = 0
while True:
    num = int(input('Введите число: '))
    sum_num += num
    if sum_num >= 777:
        break
    try:
        x = random.randint(1, 13)
        if x == 1:
            raise ValueError
        else:
            with open('answer.txt', 'a') as file:
                file.write(str(num) + '\n')
    except ValueError:
        print('Сектор приз! Вас выбросило!')
        raise

# зачёт!
