def checkio(words):
    return '111' in ''.join('1' if w.isalpha() else '0' for w in words.split())


# alt
from re import findall, I
def checkio(words):
    return bool(findall('([a-z]+ +){2,}[a-z]+', words, flags=I))
