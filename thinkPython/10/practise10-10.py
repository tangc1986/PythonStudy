import time

def fun(flag):
    fin = open('words.txt')
    lst = []
    start = time.time()
    if flag:
        for word in fin:
            lst.append(word.strip())
    else:
        for word in fin:
            lst = lst + [word.strip()]
    elapsed = (time.time() - start)
    fin.close()
    print elapsed
    
fun(True)
fun(False)
    
        