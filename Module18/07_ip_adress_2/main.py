def check_ip(address):
    parts = address.split(".")
    if len(parts) != 4:
        print('Адрес - это четыре числа, разделенные точками')
        return
    for i in parts:
        if not i.isdigit():
            print(i + '- не целое число')
            return
    for item in parts:
        if not 0 <= int(item) <= 255:
            print(item, 'превышает 255')
            return
    print('IP-адрес корректен')


ip_adress = '128.16.35.255'
check_ip(ip_adress)
