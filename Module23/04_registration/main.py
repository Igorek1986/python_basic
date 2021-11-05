def check_string_file(string):
    my_list = list(string.split())
    if len(my_list) < 3:
        raise IndexError('IndexError')
    if not my_list[0].isalpha():
        raise NameError('NameError')
    if not '@' in my_list[1] and not '.' in my_list[1]:
        raise SyntaxError('SyntaxError')
    if not 10 < int(my_list[2]) < 99:
        raise ValueError('ValueError')


with open('registrations.txt', 'r', encoding='utf-8') as file,\
        open('registrations_bad.log', 'a', encoding='utf-8') as bad, \
        open('registrations_good.log', 'a', encoding='utf-8') as good:

    for line in file.readlines():
        try:
            check_string_file(line)
            good.write(line)
        except (IndexError, NameError, SyntaxError, ValueError) as err:
            bad.write(f'{line.rstrip()} - {err}\n')
