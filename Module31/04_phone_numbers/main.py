import re

if __name__ == '__main__':

    phone_number = ['9999999999', '999999-999', '99999x9999']

    for i in range(len(phone_number)):
        result = re.match(r'^(\+8|9)\d{9}', phone_number[i])
        if result:
            print('номер: всё в порядке')
        else:
            print('номер: не подходит')
