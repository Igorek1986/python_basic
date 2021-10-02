N_list = [1, 2, 2, 0, 4, 0, 1]

compressed_list = [i for i in N_list if i != 0]
compressed_list.extend([0] * N_list.count(0))

print(compressed_list)

compressed_list = [i for i in N_list if i != 0]
print(compressed_list)

# зачёт!
