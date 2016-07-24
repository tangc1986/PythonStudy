def avoids(word, avoid_string):
    for each_string in avoid_string:
        if each_string in word:
            return False
    return True

def avoid_number(character):
    all_no_chr = 0
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if avoids(word, character): all_no_chr = all_no_chr + 1
    fin.close()
    return all_no_chr

def has_no_e(word):
    return avoids(word, 'e')

#print avoid_number('e')

char_dict = {}
def init_dict():
    for i in range(26):
        char_dict[chr(i+ord('a'))] = 0
        char_dict[chr(i+ord('A'))] = 0

#TODO
init_dict()
fin = open('words.txt')
for char in char_dict.keys():
    char_dict[char] = avoid_number(char)
result_list = sorted(char_dict.iteritems(), key=lambda asd:asd[1], reverse=False)
for i in range(5):
    print result_list[i][0],result_list[i][1]
