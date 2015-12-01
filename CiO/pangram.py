def check_pangram(text):
    alphabet = ''.join(map(chr, range(97, 123)))
    text = ''.join(c for c in sorted(list(set(text.lower()))) if c.isalpha())
    return text == alphabet
