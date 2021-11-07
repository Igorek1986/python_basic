def calc_file(string):
    my_list = string.split()
    num_1 = int(my_list[0])
    num_2 = int(my_list[2])
    action = my_list[1]
    result = 0
    if action == '+':
        result = num_1 + num_2
    elif action == '/':
        result = num_1 / num_2
    elif action == '*':
        result = num_1 * num_2
    elif action == '-':
        result = num_1 - num_2
    elif action == '//':
        result = num_1 // num_2
    elif action == '%':
        result = num_1 % num_2
    return result


def check_calc_file(string):
    my_list = string.split()
    if not my_list[0].isdigit() or not my_list[2].isdigit():
        raise ValueError('ValueError')
    operand_1 = int(my_list[0])
    operation = my_list[1]
    if operation not in ('+', '-', '/', '*', '//', '%'):
        raise ArithmeticError('ArithmeticError')
    if operand_1 == 0 and operation == '/':
        raise ZeroDivisionError('ZeroDivisionError')
    return string


summ_num_file = 0
with open('calc.txt', 'r') as calc, open('temp.txt', 'w+') as temp:
    for line in calc.readlines():
        try:
            num = check_calc_file(line)
            temp.write(num)
            print(num)
        except (ValueError, ZeroDivisionError, ValueError) as err:
            print(f'{line.rstrip()} - {err}')
        except ArithmeticError:
            ask = input(f'Обнаружена ошибка в строке: {line} Хотите исправить? ')
            if ask == 'да':
                change = input('Введите исправленную строку: ')
                temp.write(change + '\n')
            else:
                pass
    temp.seek(0)
    for line in temp.readlines():
        summ_num_file += calc_file(line)


print('Сумма операций строк:', summ_num_file)
