def encoder(text, key):
    new_lst_encoder = ''
    new_lst_encoder_2 = ''
    for i in text:
        if i != ' ' and i != '/' and i != '+' and i != '.':
            new_lst_encoder += alphabet[(alphabet.index(i) + shift) % 52]
        elif i == '/':
            new_lst_encoder += '/'
        else:
            new_lst_encoder += ' '
    i_shift = 3
    for word in new_lst_encoder.split(' '):
        new_word = ''
        for i in range(len(word)):
            new_word += (word[i - i_shift % len(word)])
        if new_word.endswith('/'):
            i_shift += 1
        new_lst_encoder_2 += new_word + ' '
        new_lst_encoder_2 = new_lst_encoder_2.replace('/', '\n')
    return new_lst_encoder_2


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
chiper = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj' \
         ' scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib' \
         ' oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo' \
         ' djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst' \
         ' tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj' \
         ' gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj' \
         ' xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj' \
         ' scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf' \
         ' tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b' \
         ' hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'
chiper = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm' \
         ' yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef' \
         ' uzSfbebcjmj vout/dp djbmTqf dbtft'
shift = -1


print(encoder(chiper, shift))
