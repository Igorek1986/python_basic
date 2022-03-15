import re

if __name__ == '__main__':

    phone_number = ['9999999999', '999999-999', '99999x9999']

    for count, value in enumerate(phone_number, start=1):
        result = re.match(r'^(\+8|9)\d{9}', value)
        if result:
            print(count, 'номер: всё в порядке')
        else:
            print(count, 'номер: не подходит')
