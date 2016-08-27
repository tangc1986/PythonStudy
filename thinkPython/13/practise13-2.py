import string
import pprint

words = []
fin = open('pg52892.txt')
for line in fin:
    if 'START OF THIS PROJECT GUTENBERG EBOOK' in line:
        words = []
        continue
    pure_line = line.strip()
    if pure_line == '': continue
    line_list = [pure_line,]
    for char in string.punctuation+string.whitespace:
        new_list = []
        for tmp_word in line_list:
            new_list.extend(tmp_word.split(char))
        line_list = new_list
    for word in line_list:
        if word.strip() != '':
            words.append(word)

words_dict = {}
for word in words:
    if word.isdigit(): continue
    words_dict[word] = words_dict.get(word, 0) + 1
print 'This txt contain %d words' % len(words_dict)
pprint.pprint(words_dict)