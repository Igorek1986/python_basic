original_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
zipped_lst = [(original_lst[value], original_lst[value + 1]) for value in range(0, len(original_lst), 2)]
print(zipped_lst)

# зачёт!
