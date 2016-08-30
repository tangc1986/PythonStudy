import string
import random

order = 1

def porcess_file(filename):
    hist = dict()
    fp = open(filename)
    for line in fp:
        process_line(line, hist)
    return hist

def process_line(line, hist):
    word_list = line.split()
    if order >= len(word_list): return
    offset = 0
    for i in range(order, len(word_list)):
        hist[tuple(word_list[offset:i])] =  hist.get(tuple(word_list[offset:i]), list()) + [word_list[i]]
        offset += 1

hist = porcess_file('emma.txt')

start = ('He',)
current = start
sentence = current
while hist.get(current, None) != None:
    tmp = (random.choice(hist[current]),)
    sentence = sentence + tmp
    current = current[1:] + tmp
    
for i in sentence:
    print i,

