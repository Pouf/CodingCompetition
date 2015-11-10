def count_words(text, words):
    return sum(1 for _ in words if _ in text.lower())
