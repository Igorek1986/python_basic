import itertools

if __name__ == '__main__':
    digits = range(10)
    pincode_vars = itertools.product(digits, repeat=4)
    for var in pincode_vars:
        print(var)

# зачёт!
