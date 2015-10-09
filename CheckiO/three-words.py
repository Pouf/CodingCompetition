def checkio(words):
    return '111' in ''.join('1' if w.isalpha() else '0' for w in words.split())
