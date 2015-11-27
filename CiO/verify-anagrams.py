def verify_anagrams(first_word, second_word):
    A = sorted(first_word.replace(' ','').lower())
    B = sorted(second_word.replace(' ','').lower())
    return A == B
