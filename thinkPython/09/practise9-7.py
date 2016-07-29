def cartalk(word):
    if len(word) < 6: return False
    first_double = None
    second_double = None
    third_double = None
    pre_char = None
    for i in word:
        if pre_char == None:
            pre_char = i
            continue
        if pre_char == i:
            if first_double == None: 
                first_double = i
            elif second_double == None:
                second_double = i
            elif third_double == None:
                third_double = i
                return True
            else: pass
            pre_char = None
        else:
            if first_double != None: return False
            pre_char = i
    return False

fin = open('words.txt')
for i in fin:
    if cartalk(i.strip()):
        print i
        
            
            