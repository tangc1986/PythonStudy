import string
import pprint

words = []
fin = open('pg52892.txt')
for line in fin:
    pure_line = line.strip()
    if pure_line == '': continue
    for char in string.punctuation:
        pure_line.replace(char, ' ')
    for char in string.whitespace:
        pure_line.replace(char, ' ')
    for word in pure_line.split():
        if word.strip() != '': words.append(word)

pprint.pprint(words)