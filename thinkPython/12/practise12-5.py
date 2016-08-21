def compare_word(word1, word2):
    if len(word1) != len(word2): return False
    diff1 = None
    diff2 = None
    for x, y in zip(word1, word2):
        if (x != y):
            if diff1 == None:
                diff1 = x, y
            elif diff2 == None:
                diff2 = x, y
            else:
                return False
    if diff1 == None or diff2 == None: return False
    if diff1[0] == diff2[1] and diff1[1] == diff2[0]:
        return True
    else:
        return False

words_dict = {}
fin = open('words.txt')
for word in fin:
    pure_word = word.strip()
    length = len(pure_word)
    words_dict[length] = words_dict.get(length, []) + [pure_word]

for key in words_dict:
    word_list = words_dict[key]
    for i in range(len(word_list)-1):
        for j in range(i+1, len(word_list)):
            if compare_word(word_list[i], word_list[j]):
                print word_list[i], word_list[j]
    
