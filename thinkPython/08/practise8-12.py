def rot(char, step):
    assert(len(char) == 1)
    if not char.isalpha(): return char
    first_char = char.islower() and 'a' or 'A'
    #print 'first_char =', first_char
    offset = ord(char) - ord(first_char)
    new_offset = offset + step
    if new_offset < 0: new_offset = new_offset + 26
    if new_offset > 25: new_offset = new_offset - 26
    new_char = chr(ord(first_char) + new_offset)
    return new_char

def rotate_word(word, step):
    new_word = ''
    for a in word:
        new_word = new_word + rot(a, step)
    return new_word

assert(rotate_word('A', 3) == 'D')
assert(rotate_word('Z', 1) == 'A')
assert(rotate_word('cheer', 7) == 'jolly')
assert(rotate_word('melon', -10) == 'cubed')
assert(rotate_word(
    '''Ubj pna lbh gryy na rkgebireg sebz navagebireg ng AFN?In the elevators,the extrovert looks at the OTHER guy's shoes.''', 13) ==
       '''How can you tell an extrovert from anintrovert at NSA?Va gur ryringbef,gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.''')

print 'All Done!!!'