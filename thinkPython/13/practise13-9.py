import string
import pprint
import math

words = []
fin = open('emma.txt')
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
    words_dict[word.lower()] = words_dict.get(word.lower(), 0) + 1
print 'This txt contain %d words' % len(words_dict)

sort_words_list = []
for k, v in words_dict.items():
    sort_words_list.append((v, k))
sort_words_list.sort(reverse=True)
index = 1
for freq, word in sort_words_list:
    print word, math.log(freq), math.log(index)
    index += 1
    
