all_words = {}
fin = open('words.txt')
for word in fin:
    all_words[word.strip()] = 1

def is_word(word):
    if len(word) == 1 or word == '':
        return True
    if all_words.get(word, 0) == 1:
        return True
    else:
        return False
    
def magic_word(word):
    if word == '':
        return True
    for i in range(len(word)):
        new_word = word[:i]+word[i+1:]
        if is_word(new_word) and magic_word(new_word):
            continue
        else:
            return False
    return True

result = []
for i in all_words:
    if magic_word(i):
        result.append((len(i), i))
result.sort(reverse=True)
print result[0][1]