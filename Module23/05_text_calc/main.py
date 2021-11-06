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


def check_calc_file(string):
    my_list = string.split()
    if not my_list[0].isdigit() or not my_list[2].isdigit():
        raise ValueError('ValueError')
    operand_1 = int(my_list[0])
    operand_2 = int(my_list[2])
    operation = my_list[1]
    if operation not in ('+', '-', '/', '*', '//', '%'):
        raise ArithmeticError('ArithmeticError')
    if operand_1 == 0 and operation == '/':
        raise ZeroDivisionError('ZeroDivisionError')
    return calc_file(operand_1, operand_2, operation)


summ_num_file = 0
with open('calc.txt', 'r') as calc:
    for line in calc.readlines():
        try:
            num = check_calc_file(line)
            summ_num_file += num
        except (ValueError, ArithmeticError, ZeroDivisionError, ValueError) as err:
            print(f'{line.rstrip()} - {err}')
print('Сумма операций строк:', summ_num_file)
