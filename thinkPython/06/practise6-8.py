def gad(a, b):
    if b == 0:
        return a
    r = a % b
    return gad(b, r)

print gad(2,3)