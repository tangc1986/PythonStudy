def has_no_e(word):
    return 'e' not in word

fin = open('words.txt')
all_word = 0
all_no_e_word = 0
for line in fin:
    word = line.strip()
    all_word = all_word + 1
    if has_no_e(word):
        all_no_e_word = all_no_e_word + 1
print '%.2f%%' % (float(all_no_e_word) / all_word * 100)
