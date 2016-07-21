def is_palindrome(word):
    return word == word[::-1]

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
    