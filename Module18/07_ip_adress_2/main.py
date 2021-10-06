def check_ip(address):
    parts = address.split(".")
    if len(parts) != 4:
        print('Адрес - это четыре числа, разделенные точками')
        return

    # TODO, Если переменную цикла используем в коде, её необходимо назвать так, чтобы название отражало суть содержания.
    #  "i" не отражает. В нашем случае, "i" это не Индекс.
    for i in parts:
        if not i.isdigit():
            print(i + '- не целое число')
            return
    # TODO, цикл ниже получился лишним, предлагаю реализовать вторую проверку блоком elif.
    for item in parts:
        if not 0 <= int(item) <= 255:
            print(item, 'превышает 255')
            return
    print('IP-адрес корректен')


ip_adress = '128.16.35.255'
check_ip(ip_adress)
