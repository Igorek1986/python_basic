def my_len_min(string, data):
    return len(sorted((string, data), key=len)[0])


word_str = 'abcdaaa'
num = (10, 20, 30, 40)
min_len = my_len_min(word_str, num)

gen_obj = ((word_str[i], num[i]) for i in range(min_len))
print(gen_obj)

for item in gen_obj:
    print(item)

# sym_num = zip(word_str, num)
# print(sym_num)
#
#
# for i in sym_num:
#     print(i)

# зачёт!
