nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

nice_list = [i for i3 in nice_list for i2 in i3 for i in i2]
print(nice_list)
