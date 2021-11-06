def calc_file(num_1, num_2, action):
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


def check_calc_file(string, count):
    my_list = string.split()
    if not my_list[0].isdigit() or not my_list[2].isdigit():
        raise ValueError('ValueError')
    operand_1 = int(my_list[0])
    operand_2 = int(my_list[2])
    operation = my_list[1]
    if operation not in ('+', '-', '/', '*', '//', '%'):
        change = input(f'Обнаружена ошибка в строке: {string} Хотите исправить? ')
        if change == 'да':
            change_string = input('Введите исправленную строку: ')
            with open('calc.txt', 'a') as calc_change:
                calc_change.writelines(f'{change_string}\n')
        raise ArithmeticError('ArithmeticError')
    if operand_1 == 0 and operation == '/':
        raise ZeroDivisionError('ZeroDivisionError')
    with open('calc.txt', 'a') as file:
        file.seek(count)
        file.write(f'{string}\n')
    return calc_file(operand_1, operand_2, operation)


summ_num_file = 0
count_line = 0
with open('calc.txt', 'r') as calc:
    for line in calc.readlines():
        count_line += 1
        try:
            num = check_calc_file(line, count_line)
            summ_num_file += num
        except (ValueError, ArithmeticError, ZeroDivisionError, ValueError) as err:
            print(f'{line.rstrip()} - {err}')
print('Сумма операций строк:', summ_num_file)
