def my_zip_min(string, data):
    len_zip = len(sorted((string, data), key=len)[0])
    zip_gen = ((string[i], data[i]) for i in range(len_zip))
    return zip_gen


word_str = 'abcdaaa'
num = (10, 20, 30, 40)
# num = {1: 10, 2: 20, 3: 30, 4: 40}
gen_obj = my_zip_min(word_str, num)

for i_tuple in gen_obj:
    print(i_tuple)
