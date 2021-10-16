def palindrome(string):
    count = 0
    for i_string in string:
        if i_string in string_dict:
            string_dict[i_string] += 1
        else:
            string_dict[i_string] = 1
    for i_count in string_dict.values():
        if i_count % 2 == 1:
            count += 1
    if count > 1:
        return False
    else:
        return True


while True:
    string_lst = list(input('Введите строку: '))
    string_dict = dict()
    if palindrome(string_lst):
        print('\nМожно сделать палиндромом\nДля выхода введите stop\n')
    elif string_lst == list('stop'):
        break
    else:
        print('\nНельзя сделать палиндромом\nДля выхода введите stop\n')

# зачёт!
