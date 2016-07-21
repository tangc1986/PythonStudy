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

print avoid_number('e')

#TODO