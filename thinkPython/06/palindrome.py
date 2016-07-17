def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if not word:
        return True
    elif len(word) == 1:
        return True
    elif len(word) == 2:
        return first(word) == last(word)
    else:
        return first(word) == last(word) and is_palindrome(middle(word))

if __name__ == '__main__':
    word1 = 'noon'
    word2 = 'redivider'
    word3 = 'a'
    word4 = 'ab'
    word5 = 'bb'
    word6 = ''
    print is_palindrome(word1)
    print is_palindrome(word2)
    print is_palindrome(word3)
    print is_palindrome(word4)
    print is_palindrome(word5)
    print is_palindrome(word6)
    