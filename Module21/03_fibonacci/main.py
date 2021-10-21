def fibonacci(num):
    if num in (1, 2):
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


number_row = int(input('Введите позицию числа в ряде Фибоначчи: '))
print('Число:', fibonacci(number_row))
