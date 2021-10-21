def numbers(num):
    if num != 1:
        numbers(num - 1)
    print(num)


num_int = 5
numbers(num_int)

# зачёт!
