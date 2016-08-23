words_dict = {}
fin = open('words.txt')
for word in fin:
    pure_word = word.strip()
    key = tuple(sorted(pure_word))
    words_dict[key] = words_dict.get(key, []) + [pure_word]

t = []
for word_tuple in words_dict:
    if len(words_dict[word_tuple]) > 1:
        t.append((len(words_dict[word_tuple]), word_tuple))
t.sort(reverse=True)
res = []
for _, word_tuple in t:
    print words_dict[word_tuple]

