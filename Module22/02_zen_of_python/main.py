zen = open('zen.txt', 'r')
text = zen.readlines()
text.reverse()
print(' '.join(text), end='\n')
zen.close()

# зачёт!
