def compression_line(line):
    count = 1
    last_sym = line[0]
    result = ''
    for i in range(len(line) - 1):
        nex_sym = line[i + 1]
        if last_sym == nex_sym:
            count += 1
        else:
            result += last_sym + str(count)
            count = 1
        last_sym = nex_sym
    result += last_sym + str(count)
    return result


line_str = 'aaAAbbсaaaA'
print('Закодированная строка:', compression_line(line_str))

