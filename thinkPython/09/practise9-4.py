def uses_only(word, string):
    for i in word:
        if i not in string:
            return False
    return True

def func(words):    
    for word in words.split():
        if not uses_only(word.lower(), 'acefhlo'):
            return False
        return True
    
fin = open('words.txt')
for line in fin:
    if uses_only(line.lower(), 'acefhlo'):
        print line
    