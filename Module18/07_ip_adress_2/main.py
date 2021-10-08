def check_ip(address):
    parts = address.split(".")
    if len(parts) != 4:
        print('Адрес - это четыре числа, разделенные точками')
        return
    for item_ip in parts:
        if not item_ip.isdigit():
            print(item_ip + '- не целое число')
            return
        elif not 0 <= int(item_ip) <= 255:
            print(item_ip, 'превышает 255')
            return
    print('IP-адрес корректен')


ip_adress = '128.16.35.a4'
check_ip(ip_adress)

ip_adress = '240.127.56.340'
check_ip(ip_adress)

ip_adress = '34.56.42,5'
check_ip(ip_adress)

ip_adress = '128.0.0.255'
check_ip(ip_adress)

# зачёт!
